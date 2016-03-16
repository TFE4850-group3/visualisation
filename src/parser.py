import re
import logging


def extract_sentence_data(sentence):
    # Remove whitespace, and return content between $ and *
    return re.sub("(\n|\r\n)", "", sentence[sentence.find("$")+1:sentence.find("*")])


def check_checksum(sentence):
    try:
        # Remove whitespace at start and end of sentence
        sentence = sentence.strip()

        # Extract the correct checksum from the sentence
        expected_checksum = int(sentence[-2:])

        # Extract the message content
        sentence_data = extract_sentence_data(sentence)

        # Set initial checksum value to 0
        checksum = 0

        # For each character in the sentence, XOR with the current checksum
        for character in sentence_data:
            checksum ^= ord(character)

        # Return if the expected checksum matches the calculated checksum
        if hex(checksum) == hex(expected_checksum):
            return True

        # Log that an invalid message was checked
        logging.warning('Invalid checksum')

        return False
    except ValueError:
        logging.error('Invalid sentence received. Cannot check validity')

        return False


def utc_time_to_time(utc_time):
    return utc_time


def sentence_to_dict(sentence):
    # Do not extract sentence if it is corrupt
    if not check_checksum(sentence):
        return None

    # Extract the message content
    sentence_data = extract_sentence_data(sentence)

    # Split sentence data on comma
    sentence_data = sentence_data.split(',')

    # Check that the sentence is formatted correctly
    # Ignore messages not formatted as GGA
    # FIXME: Maybe generalize this
    if not (sentence_data[0] == 'GPGGA' and len(sentence_data) == 15):
        logging.error('Message not in valid GPGGA format')

        return None

    # Return dictionary containing sentence data
    return {
        'sentence_format': sentence_data[0],
        'utc_time': utc_time_to_time(sentence_data[1]),
        'latitude': float(sentence_data[2]),
        'ns_indicator': sentence_data[3],
        'longitude': float(sentence_data[4]),
        'ew_indicator': sentence_data[5],
        'gps_quality_indicator': int(sentence_data[6]),
        'satellites_used': int(sentence_data[7]),
        'hdop': float(sentence_data[8]),
        'altitude': float(sentence_data[9]),
        'dgps_station_id': int(sentence_data[14]),
    }

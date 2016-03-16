from parser import sentence_to_dict
from gui import make_plot


sentences = [
    sentence_to_dict('$GPGGA,111636.932,2447.0949,N,12100.5223,E,1,11,0.8,118.2,M,,,,0000*02\r\f'),
    sentence_to_dict('$GPGGA,111636.932,2457.0949,N,12120.5223,E,1,11,0.8,128.2,M,,,,0000*02\r\f'),
    sentence_to_dict('$GPGGA,111636.932,2467.0949,N,12130.5223,E,1,11,0.8,132.2,M,,,,0000*11\r\f'),
    sentence_to_dict('$GPGGA,111636.932,2472.0949,N,12150.5223,E,1,11,0.8,136.2,M,,,,0000*13\r\f'),
    sentence_to_dict('$GPGGA,111636.932,2474.0949,N,12160.5223,E,1,11,0.8,138.2,M,,,,0000*06\r\f'),
    sentence_to_dict('$GPGGA,111636.932,2485.0949,N,12190.5223,E,1,11,0.8,143.2,M,,,,0000*11\r\f'),
    sentence_to_dict('$GPGGA,111636.932,2490.0949,N,12210.5223,E,1,11,0.8,148.2,M,,,,0000*15\r\f'),
    sentence_to_dict('$GPGGA,111636.932,2499.0949,N,12240.5223,E,1,11,0.8,153.2,M,,,,0000*09\r\f'),
    sentence_to_dict('$GPGGA,111636.932,2503.0949,N,12280.5223,E,1,11,0.8,160.2,M,,,,0000*07\r\f'),
    sentence_to_dict('$GPGGA,111636.932,2508.0949,N,12340.5223,E,1,11,0.8,168.2,M,,,,0000*09\r\f'),
    sentence_to_dict('$GPGGA,111636.932,2512.0949,N,12400.5223,E,1,11,0.8,180.2,M,,,,0000*07\r\f'),
]


make_plot(sentences)

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D


def make_plot(sentences):
    fig = plt.figure()
    axis = fig.gca(projection='3d')

    x = []
    y = []
    z = []

    for sentence in sentences:
        x.append(sentence['latitude'])
        y.append(sentence['longitude'])
        z.append(sentence['altitude'])

    axis.set_title('Rocket position')

    axis.set_xlabel('Latitude')
    axis.set_ylabel('Longitude')
    axis.set_zlabel('Altitude')

    axis.xaxis.set_major_formatter(plt.NullFormatter())
    axis.yaxis.set_major_formatter(plt.NullFormatter())
    axis.zaxis.set_major_formatter(plt.NullFormatter())

    axis.plot(x, y, z)

    plt.show()

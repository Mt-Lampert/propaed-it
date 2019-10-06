""" for defining tasks """
from invoke import task


def build_feature(header):
    """ builds a new feature file from the header provided
        header == "Spiffy Feature"
        => "Feature: Spiffy Feature" -> './spiffy_feature.feature'
    """
    first_line = "Feature: {}".format(header)
    words = [w.lower() for w in header.split(' ')]
    filename = '_'.join(words) + '.feature'

    with open(filename, 'w') as file:
        file.write(first_line)

@task
def newFeatures(c):
    """ build new feature files """
    features = [
            # "Personal Dashboard",
            ]
    for f in features:
        build_feature(f)


@task
def tester(c):
    """ a basic tester if this one works """
    print("Do we pass?")

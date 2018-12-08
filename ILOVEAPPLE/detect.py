#!/usr/bin/env python

import argparse
import io
import re
import os




# [START vision_label_detection]
def detect_labels(path):
    """Detects labels in the file."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    # [START vision_python_migration_label_detection]
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    ss=labels[0].description 
    ss.split('/')[0]
    os.system("./ILOVEAPPLE/sort {} {}".format(ss, path))
    # [END vision_python_migration_label_detection]
# [END vision_label_detection]



def localize_objects(path):
    """Localize objects in the local image.

    Args:
    path: The path to the local file.
    """
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)

    objects = client.object_localization(
        image=image).localized_object_annotations

    print('Number of objects found: {}'.format(len(objects)))
    for object_ in objects:
        print('\n{} (confidence: {})'.format(object_.name, object_.score))
        print('Normalized bounding polygon vertices: ')
        for vertex in object_.bounding_poly.normalized_vertices:
            print(' - ({}, {})'.format(vertex.x, vertex.y))
# [END vision_localize_objects]



def run_local(args):
    if args.command == 'labels':
        detect_labels(args.path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    subparsers = parser.add_subparsers(dest='command')


    detect_labels_parser = subparsers.add_parser(
        'labels', help=detect_labels.__doc__)
    detect_labels_parser.add_argument('path')


    args = parser.parse_args()

    run_local(args)

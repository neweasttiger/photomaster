#!/usr/bin/env python

import argparse

# [START vision_face_detection_tutorial_imports]
from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw
import os
# [END vision_face_detection_tutorial_imports]


# [START vision_face_detection_tutorial_send_request]
def detect_face(face_file, max_results=4):
    client = vision.ImageAnnotatorClient()
    # [END vision_face_detection_tutorial_client]

    content = face_file.read()
    image = types.Image(content=content)

    return client.face_detection(image=image).face_annotations
# [END vision_face_detection_tutorial_send_request]


# [START vision_face_detection_tutorial_process_response]
def highlight_faces(image, faces, output_filename):
    im = Image.open(image)
    draw = ImageDraw.Draw(im)

    for face in faces:
        box = [(vertex.x, vertex.y)
               for vertex in face.bounding_poly.vertices]
        draw.line(box + [box[0]], width=5, fill='#00ff00')

#    im.save(output_filename)
# [END vision_face_detection_tutorial_process_response]


# [START vision_face_detection_tutorial_run_application]
def main(input_filename, output_filename, max_results):
    with open(input_filename, 'rb') as image:
        faces = detect_face(image, max_results)
        
        if len(faces)>0:
            os.system("./sort {} {}".format(len(faces),input_filename))
        
        #    print('{}'.format(
#            len(faces), '' if len(faces) == 1 else 's'))
             # Reset the file pointer, so we can read the file again
        else:
            os.system("python detect.py labels {}".format(input_filename))
        
        image.seek(0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Detects faces in the given image.')
    parser.add_argument(
        'input_image', help='the image you\'d like to detect faces in.')
    parser.add_argument(
        '--out', dest='output', default='out.jpg',
        help='the name of the output file.')
    parser.add_argument(
        '--max-results', dest='max_results', default=4,
        help='the max results of face detection.')
    args = parser.parse_args()

    main(args.input_image, args.output, args.max_results)

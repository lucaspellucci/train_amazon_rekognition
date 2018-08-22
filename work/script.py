import argparse
import boto3
import botocore
import sys
import os
import base64


def main(argv):
    parsr = argparse.ArgumentParser()
    parsr.add_argument('-c', '--collection', action='store', dest='collection',
                       help='Amazon Rekognition Collection ID', required=True)

    args = parsr.parse_args()

    client = boto3.client('rekognition')
    rekognition_collection_id = args.collection

    list_collections(client)
    create_collection(client, rekognition_collection_id)
    print_files(client, rekognition_collection_id)


def list_collections(client):
    response = client.list_collections()
    print (response)


def create_collection(client, rekognition_collection_id):
    try:
        response = client.create_collection(
            CollectionId=rekognition_collection_id
        )
    except botocore.exceptions.ClientError as e:
        print ('Collections creation failed: {0}'.format(e))


def print_files(client, rekognition_collection_id):
    for entry in os.scandir('/img'):
        if entry.is_file() and entry.name.lower().endswith(('.jpg', '.png')):
            with open(entry, "rb") as image_file:
                img_base64 = image_file.read()
                ext_id = entry.name.lower()[:-4]
                facial_recognition(client, img_base64,
                                   rekognition_collection_id, ext_id)


def facial_recognition(client, img_base64, rekognition_collection_id, ext_id):
    response = client.index_faces(
        CollectionId=rekognition_collection_id,
        Image={
            'Bytes': img_base64
        },
        ExternalImageId=ext_id,
        DetectionAttributes=['ALL']
    )
    for face in response['FaceRecords']:
        face_id = face['Face']['FaceId']
        print("Face ID: %s" % face_id)


main(sys.argv[1:])

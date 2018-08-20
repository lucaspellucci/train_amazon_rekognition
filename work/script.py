import boto3
import botocore
import sys
import os
import base64

rekognition_collection_id = sys.argv[1]

client = boto3.client('rekognition')


def list_collections():
	response = client.list_collections()
	print (response)

def create_collection(rekognition_collection_id):
	try:
		response = client.create_collection(
			CollectionId=rekognition_collection_id
		)
	except botocore.exceptions.ClientError as e:
		print ('Collections creation failed: {0}'.format(e))

def print_files():
	for entry in os.scandir('/img'):
		if entry.is_file() and entry.name.lower().endswith(('.jpg','jpeg','.png')):
			with open(entry, "rb") as image_file:
				img_base64 = image_file.read()
				facial_recognition(img_base64)

def facial_recognition(img_base64):
	response = client.index_faces(
		CollectionId=rekognition_collection_id,
		Image={
			'Bytes': img_base64
		},
		ExternalImageId=rekognition_collection_id,
		DetectionAttributes=['ALL']
	)
	for face in response['FaceRecords']:
		face_id = face['Face']['FaceId']
		print("Face ID: %s" % face_id)



list_collections()
create_collection(rekognition_collection_id)
print_files()

# Train Amazon Rekognition with Face Images
Simple example of a Docker container that creates a collection on Amazon Rekognition and adds faces from image files to  it.

## Build
make (build|rebuild)

* This will create a Container Image to be used.

## Setting credentials
export AWS_ACCESS_KEY_ID=AKIA***

export AWS_SECRET_ACCESS_KEY=wJalrXU***

export AWS_DEFAULT_REGION=ap-southeast-2

Alternatively, you can print the creds from the AWS cli and copy the export commands:

make print-creds  #for default profile
or
make print-creds PROFILE=my_profile

* This will set the credentials in Environment Variables to be passed to the container in runtime.


## Usage
* Create a /img folder with the images you want to train, the suggestion is to have the filenames as the person name, like joao-silva001.jpg, joao-silva002.jpg, jose-carlos001.jpg, and so on...

make run RUN_OPT=collection-name

* will add all image to the collection called "collection-name" and will use the file name (without the extension) as a ExternalID.

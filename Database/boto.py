import boto3
from PIL import Image

BUCKET_NAME = "e-note"
EXPIRES_TIME = 3600

s3_resources = boto3.resource(
    service_name='s3',
    region_name='ap-southeast-1',
    aws_access_key_id='AKIA5P4ROYQSWV2BUFMD',
    aws_secret_access_key='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'
)

s3_client = boto3.client(
    service_name='s3',
    region_name='ap-southeast-1',
    aws_access_key_id='AKIA5P4ROYQSWV2BUFMD',
    aws_secret_access_key='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'
)

object = s3_resources.Object(BUCKET_NAME, 'img.png')

# object.download_file('tmp/test.txt')


def get_access_urls(path):
    return s3_client.generate_presigned_url('get_object', ExpiresIn=EXPIRES_TIME,
                                            Params={"Bucket": BUCKET_NAME, "Key": path})


response = object.get()
file_stream = response['Body']
im = Image.open(file_stream)
im.show()
print(get_access_urls("img.png"))

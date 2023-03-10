from pymongo import MongoClient
from PIL import Image
import boto3

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

cluster = MongoClient(
    "mongodb+srv://thanhanphan17:05062003@cluster0.dwxs1.mongodb.net/?retryWrites=true&w=majority")
db = cluster["e-note"]
clt = db["note"]


def note_size():
    data = clt.find()
    count = 0
    for x in data:
        count += 1

    return count


def add_note(note):
    global clt
    data = clt.find()
    count = 0
    for x in data:
        count += 1
    note["_id"] = count
    clt.insert_one(note)

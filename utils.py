import hashlib
import boto3

REGION = 'ap-south-1'

s3 = boto3.client('s3', region_name=REGION)
dynamodb = boto3.resource('dynamodb', region_name=REGION)

table = dynamodb.Table('dedup-table2')

BUCKET_NAME = 'chaits-dedup-bucket2'

def generate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

def is_duplicate(hash_value):
    response = table.get_item(Key={'hash': hash_value})
    return 'Item' in response

def store_data(hash_value, data):
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=hash_value,
        Body=data
    )

    table.put_item(
        Item={
            'hash': hash_value,
            'data': data
        }
    )
import boto3
from datetime import datetime
import json
import hashlib
import os

def get_conf(conf_file):
    try:
        with open(conf_file, 'r') as credfile:
            confdata = json.load(credfile)
            return confdata
    except OSError :
        return {'access-key-id': None, 'secret-access-key': None, 'region': None}

def remove_duplicate_file_from_S3(file_name, bucket_name):
    creds = get_conf('cred.json')
    #print(creds)
    client = boto3.client('s3', aws_access_key_id=creds['access-key-id'],
                                aws_secret_access_key=creds['secret-access-key'],
                                region_name=creds['region'])
    client.delete_object(Bucket=bucket_name, Key=file_name)

def insert_record_into_files_table(client, readable_hash, file_name, file_content, file_number_of_words, file_url, time_stamp):
    new_item={
        'hash_code': {
            'S': readable_hash,
        },
        'file_name': {
            'S': file_name
        },
        'file_content': {
            'S': file_content
        },
        'file_number_of_words': {
            'S': file_number_of_words
        },
        'file_url': {
            'S': file_url
        },
        'time_stamp': {
            'S': time_stamp
        },
        'counter': {
            'S': '1'
        }
    }

    response = client.get_item(
        TableName='files',
        Key={
            'hash_code':{'S': readable_hash}
        }
    )

    if ("Item" not in response):
        #if hash_code is not existed then do insert with count=1
        response = client.put_item(
        TableName='files',
        Item = new_item,
        ReturnConsumedCapacity='TOTAL'
        )
    else:
        #if hash_code is already existed then do update counter++ and time_stamp and remove_duplicate_file_from_S3
        update_item = response['Item']
        update_item['counter']['S']=str(int(update_item['counter']['S'])+1)
        update_item['time_stamp']['S']=str(datetime.now())
        response = client.put_item(
        TableName='files',
        Item = update_item,
        ReturnConsumedCapacity='TOTAL'
        )
        remove_duplicate_file_from_S3(file_name, 's3-demo33')

def dynamodb_client(readable_hash, file_name, file_content, file_number_of_words, file_url):
    creds = get_conf('cred.json')
    #print(creds)
    client = boto3.client('dynamodb', aws_access_key_id=creds['access-key-id'],
                                      aws_secret_access_key=creds['secret-access-key'],
                                      region_name=creds['region'])
    time_stamp = str(datetime.now())
    insert_record_into_files_table(client, readable_hash, file_name, file_content, file_number_of_words, file_url, time_stamp)

def calculate_file_hash(file_name):
    print(file_name)
    with open(file_name,"rb") as f:
        bytes = f.read() # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest();
        file_content = bytes.decode("utf-8")
        file_number_of_words = str(len(file_content.split()))
        return readable_hash, file_content, file_number_of_words

def upload_files_to_s3_and_db(files_dir, bucket_name):
    creds = get_conf('cred.json')
    #print(creds)
    client = boto3.client('s3', aws_access_key_id=creds['access-key-id'],
                                aws_secret_access_key=creds['secret-access-key'],
                                region_name=creds['region'])
    for file_name in os.listdir(files_dir):
        client.upload_file(files_dir + "/" + file_name, bucket_name, file_name)
        readable_hash, file_content, file_number_of_words = calculate_file_hash(files_dir + "/" + file_name)
        file_url = f"https://{bucket_name}.s3.amazonaws.com/{file_name}"
        dynamodb_client(readable_hash, file_name, file_content, file_number_of_words, file_url)


upload_files_to_s3_and_db('./files', 's3-demo33')

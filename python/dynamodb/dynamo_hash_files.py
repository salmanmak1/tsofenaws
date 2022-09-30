import json
import boto3
import hashlib
import os

def insert_into_files_table(client, readable_hash, name):
    new_item={
        'hash_code': {
            'S': readable_hash,
        },
        'file_name': {
            'S': name
        }
    }
    
    response = client.put_item(
        TableName='files',
        Item = new_item,
        ReturnConsumedCapacity='TOTAL'
    )
    print(response)

def get_conf(conf_file):
    try:
        with open(conf_file, 'r') as credfile:
            confdata = json.load(credfile)
            return confdata
    except OSError :
        return {'access-key-id': None, 'secret-access-key': None, 'region': None}   


def dynamodb_demo(readable_hash, file_name):
    creds = get_conf('cred.json')
    print(creds)
    client = boto3.client('dynamodb', aws_access_key_id=creds['access-key-id'],
                                      aws_secret_access_key=creds['secret-access-key'],
                                      region_name=creds['region'])
    insert_into_files_table(client, readable_hash, file_name)

def calculate_file_hash(file_name):
    print(file_name)
    with open(file_name,"rb") as f:
        bytes = f.read() # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest();
        print(readable_hash)
        return readable_hash

def upload_file_to_s3(files_dir):
    creds = get_conf('cred.json')
    print(creds)
    client = boto3.client('s3', aws_access_key_id=creds['access-key-id'],
                                aws_secret_access_key=creds['secret-access-key'],
                                region_name=creds['region'])

    for file_name in os.listdir(files_dir):
        client.upload_file("./" + files_dir + "/" + file_name, 's3-demo33', file_name)
        readable_hash = calculate_file_hash("./" + files_dir + "/" + file_name)
        dynamodb_demo(readable_hash, file_name)


def download_file_from_s3(file1):
    creds = get_conf('cred.json')
    print(creds)
    client = boto3.client('s3', aws_access_key_id=creds['access-key-id'],
                                aws_secret_access_key=creds['secret-access-key'],
                                region_name=creds['region'])
    client.download_file('s3-demo33', file1, file1)


#dynamodb_demo()
upload_file_to_s3('./files')

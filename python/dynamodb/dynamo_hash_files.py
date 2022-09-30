import json
import boto3
import hashlib

def insert_into_people(client, first_name, phone_number):
    new_item={
        'name': {
            'S': first_name,
        },
        'phone': {
            'S': phone_number
        }
    }
    
    response = client.put_item(
        TableName='people',
        Item = new_item,
        ReturnConsumedCapacity='TOTAL'
    )

def get_conf(conf_file):
    try:
        with open(conf_file, 'r') as credfile:
            confdata = json.load(credfile)
            return confdata
    except OSError :
        return {'access_key_id': None, 'secret_access_key': None, 'region': None}   


def dynamodb_demo():
    creds = get_conf('cred.json')
    print(creds)
    client = boto3.client('dynamodb', aws_access_key_id=creds['access-key-id'],
                                      aws_secret_access_key=creds['secret-access-key'],
                                      region_name=creds['region'])
    insert_into_people(client, 'Dave', "09-________")
    insert_into_people(client, 'Aisha', "09-^^^^^^^^")

def calculate_file_hash(file_name):
    print(file_name)
    with open(file_name,"rb") as f:
        bytes = f.read() # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest();
        print(readable_hash)

def upload_file_to_s3(file1):
    creds = get_conf('cred.json')
    print(creds)
    client = boto3.client('s3', aws_access_key_id=creds['access-key-id'],
                                aws_secret_access_key=creds['secret-access-key'],
                                region_name=creds['region'])
    client.upload_file(file1, 's3-demo33', file1)

def download_file_from_s3(file1):
    creds = get_conf('cred.json')
    print(creds)
    client = boto3.client('s3', aws_access_key_id=creds['access-key-id'],
                                aws_secret_access_key=creds['secret-access-key'],
                                region_name=creds['region'])
    client.download_file('s3-demo33', file1, file1)


#dynamodb_demo()
upload_file_to_s3('f1.txt')
calculate_file_hash('f1.txt')

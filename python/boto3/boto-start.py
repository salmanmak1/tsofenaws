import boto3
import json


def create_user_boto3(user_name):
    client = boto3.client('iam', aws_access_key_id='AKIATTINKXQJY7SN3Y53',
                                      aws_secret_access_key='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',
                                      region_name='us-east-1')
    response = client.create_user(UserName =  user_name)
    print('User created: ', response['User'])

    users = client.list_users()
    print('All Users: ', users['Users'])

create_user_boto3('user1')

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

def create_policy_and_attach(user_name):
    client = boto3.client('iam', aws_access_key_id='AKIATTINKXQJW4ME6EXV',
                                      aws_secret_access_key='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',
                                      region_name='us-east-1')

    my_policy={
	"Version": "2012-10-17",
	"Statement": [ {
        "Effect": "Allow",
        "Action": [
            "iam:GenerateCredentialReport",
            "iam:Get*",
            "iam:List*"
        ],
        "Resource": "*"
    } ]
    }

    response = client.create_policy(PolicyName='UsersIAMReadOnlyPolicy',PolicyDocument=json.dumps(my_policy))
    print('policy response: ', response['Policy'])

    response = client.attach_user_policy(PolicyArn=response['Policy']['Arn'], UserName=user_name)
    print('policy attach: ', response)

def upload_file_to_s3(file1):
    client = boto3.client('s3')
    client.upload_file(file1, 's3-my-demo', file1)

def download_file_from_s3(file1):
    client = boto3.client('s3')
    client.download_file('s3-my-demo', file1, file1)


#create_user_boto3('salman')
#create_policy_and_attach('user1')
upload_file_to_s3("test3.txt")
download_file_from_s3("test1.txt")


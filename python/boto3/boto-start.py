import boto3
import json

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

my_policy_reciever={
	"Version": "2012-10-17",
	"Statement": [ {
        "Effect": "Allow",
        "Action": [
            "s3:GetObject",
            "s3:GetObjectVersion",
            "s3:LisBucket"
        ],
        "Resource": "arn:aws:s3:::s3-my-demo2"
    } ]
}

my_policy_publisher={
	"Version": "2012-10-17",
	"Statement": [ {
        "Effect": "Allow",
        "Action": [
            "s3:PutObject",
            "s3:PutObjectAcl",
            "s3:DeleteObject",
            "s3:DeleteObjectVersion"
        ],
        "Resource": "arn:aws:s3:::s3-my-demo2"
    } ]
}

def create_user_boto3(user_name):
    client = boto3.client('iam', aws_access_key_id='***',
                                      aws_secret_access_key='***',
                                      region_name='us-east-1')
    response = client.create_user(UserName =  user_name)
    print('User created: ', response['User'])

    users = client.list_users()
    print('All Users: ', users['Users'])

def create_policy_and_attach(user_name, my_policy, policy_name):
    client = boto3.client('iam', aws_access_key_id='***',
                                      aws_secret_access_key='***',
                                      region_name='us-east-1')

    response = client.create_policy(PolicyName=policy_name, PolicyDocument=json.dumps(my_policy))
    print('policy response: ', response['Policy'])

    response = client.attach_user_policy(PolicyArn=response['Policy']['Arn'], UserName=user_name)
    print('policy attach: ', response)

def upload_file_to_s3(file1):
    client = boto3.client('s3')
    client.upload_file(file1, 's3-my-demo', file1)

def download_file_from_s3(file1):
    client = boto3.client('s3')
    client.download_file('s3-my-demo', file1, file1)

def create_event_notification(bucket_name):
    client = boto3.client('sns', aws_access_key_id='***',
                                      aws_secret_access_key='***',
                                      region_name='us-east-1')
    sns_topic_arn= client.list_topics()['Topics'][1]['TopicArn']

    client = boto3.resource('s3')
    bucket_notification = client.BucketNotification(bucket_name)

    s3_notification_config = {
        'TopicConfigurations': [
            {
                'TopicArn': sns_topic_arn,
                'Events': [
                    's3:ObjectCreated:*',
                ],
            },
        ],
    }
    response = bucket_notification.put(NotificationConfiguration=s3_notification_config)
    print(response)

#create_user_boto3('salman')
#create_policy_and_attach('user1', my_policy, 'UsersIAMReadOnlyPolicy')
#upload_file_to_s3("test3.txt")
#download_file_from_s3("test1.txt")
#create_event_notification('s3-my-demo2')
#create_policy_and_attach('user1', my_policy_reciever, 'UsersRecieverPolicyForS3')
#create_policy_and_attach('salman', my_policy_publisher, 'UsersPublisherPolicyForS3')

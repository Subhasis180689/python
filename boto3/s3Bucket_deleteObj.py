import boto3
import datetime
import sys
#Account Id where you have to oprate
account="accountId"
date=datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
session = boto3.Session(profile_name='OrganisationProfileName')
client = session.client('sts')

try:
  credentials = client.assume_role(RoleArn='arn:aws:iam::'+account+':role/OrganizationAccountAccessRole',RoleSessionName=account+'OrganizationAccountAccessRole')
  session = boto3.session.Session(
    aws_access_key_id=credentials['Credentials']['AccessKeyId'],
    aws_secret_access_key=credentials['Credentials']['SecretAccessKey'],
    aws_session_token=credentials['Credentials']['SessionToken']
)
  s3=session.resource('s3')
  bucket = s3.Bucket('logs-bucket')
  for obj in bucket.objects.all():
    if (obj.last_modified).replace(tzinfo = None) < datetime.datetime(2020,1,18):
             #print results
             s3.Object('brokerportal-qa-logs',obj.key).delete()
             print('File Name: %s ---- Date: %s' % (obj.key,obj.last_modified))
    print(obj.key)
except Exception as e:
  print(e)

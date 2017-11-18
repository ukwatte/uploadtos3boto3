import boto3

s3 = boto3.client('s3')
d =s3.list_buckets()
def create_bucket():

    region = 'us-east-2'
    bucketname = 'ceylontharakapeoviawindows'


    s3.create_bucket(
    ACL='private',
    Bucket=bucketname,
    CreateBucketConfiguration={
        'LocationConstraint': region})
    print("Created a bucket with name ",bucketname)

create_bucket()

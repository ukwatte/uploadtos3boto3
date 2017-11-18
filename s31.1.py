import boto3
#active resource
s3 = boto3.resource('s3')
#print bucket name
for bucket in s3.buckets.all():
    print(bucket.name)
BUCKET_NAME = input('Enter the bucket name you want to upload ')
#defining the data which needs to upload
s3.meta.client.upload_file('Test.txt', BUCKET_NAME, 'Test.txt')
print ("Done")

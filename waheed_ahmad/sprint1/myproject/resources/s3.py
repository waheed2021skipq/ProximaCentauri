import boto3

s3 = boto3.client('s3')
s3.create_bucket(Bucket='waheedbucket')


# Create a client
s3 = boto3.client('s3')

filename = 'urlfile.txt'
bucket_name = 'waheedbucket'

s3.upload_file(filename, bucket_name, filename)

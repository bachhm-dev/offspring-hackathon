import boto3

def generate_presigned_url(bucket_name, object_name, expiration=3600):
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration)
    except Exception as e:
        print(e)
        return None

    return response

# Usage example
bucket_name = 'your-bucket-name'
object_name = 'your-object-key'
presigned_url = generate_presigned_url(bucket_name, object_name)
print(presigned_url)
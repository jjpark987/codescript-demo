from boto3 import client

def get_signed_image_url_s3(image_path: str, expiration_seconds: int = 3600) -> str:
    s3_client = client('s3', region_name='us-east-2')
    
    url = s3_client.generate_presigned_url(
        'get_object',
        Params={
            'Bucket': 'jjpark987-codescript-images',
            'Key': image_path
        },
        ExpiresIn=expiration_seconds
    )

    return url

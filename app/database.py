from boto3 import resource
from dotenv import load_dotenv

load_dotenv()

# aws dynamodb
def get_dynamo_table():
    dynamodb = resource('dynamodb', region_name='us-east-2')
    print(dynamodb)
    return dynamodb.Table('codescript-problems')

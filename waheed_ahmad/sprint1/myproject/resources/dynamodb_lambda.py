import boto3
from Dynamo_db import put_data_in_db


def lambda_database_function(event , context):
    
    client = boto3.client('dynamodb')
    table='alarmtable'
    existing_tables = client.list_tables()["TableNames"]
    if table not in existing_tables:
        response = client.create_table(
            AttributeDefinitions=[
            {
                'AttributeName': 'alarmID',
                'AttributeType': 'String'
            },
            {
                'AttributeName': 'key',
                'AttributeType': 'String'
            },
        ],
         TableName=table,
         KeySchema=[
            {
                'AttributeName': 'alarmID',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'key',
                'KeyType': 'RANGE'
            }
        ],
         BillingMode='PAY_PER_REQUEST'
        )
        response="Table Created"
    else:
        timestamp= str(event["Records"][0]["Sns"]["Timestamp"])
        message= str(event["Records"][0]["Sns"]["Message"])
        print(message , timestamp , table)
        response=put_data_in_db(timestamp,message,table)
    return

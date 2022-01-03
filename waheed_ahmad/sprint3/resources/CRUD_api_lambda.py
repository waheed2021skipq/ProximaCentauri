from __future__ import print_function
import boto3
import os
import json
import tablelambda as tlamb

client = boto3.client('dynamodb')

def lambda_handler(events, context):
    client = boto3.client('dynamodb')
#### ---------------- define API methods here to call i,e get,post, call ----------------##    
    
    if events['httpMethod'] == 'GET':
    #      dynamodbTable = boto3.resource('dynamodb').Table('waheeds3table')
    # api_menu = event['params']['path']['URL_ADDRESS']

    # result = dynamodbTable.get_item(
    #     Key={
    #         'url': api_menu
    #     }
    #     )

    # create a response
#  /   response = {
    #     "body": result['Item']
    # }

    # return response
        data = tlamb.gettable(os.getenv(key = 'table_name'))
        response_msg = f"data from table is = {data} "
# --------------------------------Delete  --------------------------------------------------###        
    # Table.delete_item(
    #     Key={
    #         'menu_id': api_menu
    #     }
    #     )

    # # create a response
    # response = {
    #     "statusCode": "200 OK"
    # }

    # return response
    elif events['httpMethod'] == 'DELETE':
        delurl = events['body']
        client.delete_item(
        TableName = os.getenv(key='table_name'),Key={'Links':{'S' : delurl}})
        response= "deleted"
        



#----------------------------------Put ----------------------------------------------------###

    elif events['httpMethod'] == 'PUT':
        puturl = events['body']
        client.put_item(
        TableName = os.getenv(key='table_name'),Item={'Links':{'S' : puturl}})
        response= "entry added"
    
    else:
        response = 'please select a right operation to perform'
    print(response)  
    return {
        
        'statusCode' : 200,
        'body'  :  response
        
    }
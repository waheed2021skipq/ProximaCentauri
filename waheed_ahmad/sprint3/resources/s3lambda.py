import logging
import boto3,os
from controller import Controller
from handler import Handler
from repository import DynamoDBTaskRepository
from s3 import s3bukclass as s3boc


client = boto3.client('dynamodb')
def lambda_handler(event, context):
    
    # repository = DynamoDBTaskRepository()
    # controller = Controller(repository)
    # fixtures = Handler(controller)
    

    # handler_funcs = {
    #     'POST': fixtures.create_task,
    #     'GET': fixtures.get_task,
    #     'PUT': fixtures.update_task,
    #     'DELETE': fixtures.delete_task,
    # }
    

    # method = event.get("httpMethod")
    # if method in handler_funcs:
    #     return handler_funcs[method](context, event)

    # logging.error("please enter a valid handler function", extra={'method': method})
    # return {"statusCode": 405}
    client = boto3.client('dynamodb')
    s3bukname = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    reqUrl= s3boc(s3bukname,key).read_buk()
    Tname = os.getenv(key = 'table_name')

    for listss in reqUrl:
        client.put_item(
        TableName = Tname,
        Item={'Links':{'S': listss}
        })
    
    return 'urlsss added'
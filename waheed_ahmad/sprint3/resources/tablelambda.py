import boto3
import json

def gettable(tableName):
    URLlink = {} 
#----------------------------------------------------------------##########
    client = boto3.client('dynamodb')
    linkx = client.scan(TableName=tableName,AttributesToGet=['Links'])
    links = linkx['Items'] 
    
    
# --------------------------------------------------------------############    
    for i in range(len(links)):
        URLlink[i] = links[i]
    nameurl = []
    for j in range(len(URLlink)):
       nameurl.append(URLlink[j]['Links']['S'])
    return nameurl
#-----------------------------------------------------------------##########

import json
import boto3
import json

class s3bukclass():
    def __init__(self,buc, item):
        self.obj = boto3.client('s3').get_object(Bucket=buc,Key=item)
    
    
    def read_buk(self):
        #data = s3['Body']
        filez = self.obj['body']
        obj1 = json.loads(filez.read())
        urllllist = list(obj1.values())
        return (urllllist)

def lambda_handler(events,context):
        db= boto3.resource('dynamodb')
        
        
        
        
        
        # msg = events[''][0]['sns']
        # time = events[''][0]['sns']['time.datetime.timestamp']
        # reasontoalarm= events['record'][0]['sns']
        
        
        
    
        # table = db.create_table(
        #     TableName='alarmtable',
        #     KeySchema=[
        #         {
        #             'AttributeName': 'alarmID',
        #             'KeyType': 'HASH'  
        #         },
        #         {
        #             'AttributeName': 'alarm',
        #             'KeyType': 'RANGE'  
        #         }
        #         ],
        #     AttributeDefinitions=[
        #         {
        #             'AttributeName': 'alarmID',
        #             'AttributeType': 'N'
        #         },
        #         {
        #             'AttributeName': 'Alarmtitle',
        #             'AttributeType': 'S'
        #         },

        #                         ],
        #     ProvisionedThroughput={
        #         'ReadCapacityUnits': 10,
        #         'WriteCapacityUnits': 10
        #     }
        # return table
        # )     
        
        #db.table.grant_read_write_data(db_lambda)

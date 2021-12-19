import boto3
import constants as constants

class cloudmetric1:
    def __init__(self):
        self.client= boto3.client('cloudwatch')
        
    def put_data(self, nameSpace, metricName, dimensions, value):
       respone=self.client.put_metric_data(
           Namespace=nameSpace,
		   MetricData=[ 
			 {
				 'MetricName' : metricName,
				 'Dimensions' : dimensions,
				 'Value' :value
				        
			  }
				  
				      ]
)

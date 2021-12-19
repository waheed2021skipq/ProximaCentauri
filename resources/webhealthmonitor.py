import urllib3
import datetime
import constants as constants
from cloudmatricdata import cloudmetric1


#URL_TO_MONITOR='www.bbc.com'

def lambda_handler(events,context):
    values = dict()
    cw= cloudmetric1();
     
     
    
    avail= get_availability()   #now we are putting matrices to cloudwatch  
    dimensions=[
        {'Name': 'URL' , 'Value': constants.URL_TO_MONITOR }
     #   {'Name': 'Region' , 'Value': "DUB"}
        
        ]
    cw.put_data(constants.URL_MONITOR_NAMESPACE ,constants.URL_MONIROR_NAME_AVAILABILITY , dimensions,avail)
    
    
     
    latency= get_latency()
    dimensions=[
        {'Name': 'URL' , 'Value': constants.URL_TO_MONITOR }
     #   {'Name': 'Region' , 'Value': "DUB"}
        
    ]
    cw.put_data(constants.URL_MONITOR_NAMESPACE ,constants.URL_MONIROR_NAME_LATENCY ,dimensions, latency)
    
    
    values.update({"Availability": avail,"Latency":latency})
    return values

def get_availability():
    http=urllib3.PoolManager()
    response=http.request("GET",constants.URL_TO_MONITOR)
    if response.status==200:
        return 1.0
    else:
        return 0.0
    
def get_latency():
    http=urllib3.PoolManager()
    start=datetime.datetime.now()
    response=http.request("GET",constants.URL_TO_MONITOR)
    end=datetime.datetime.now()
    delta =end-start
    latencySecc=round(delta.mircoseconds * 0.000001,6)
    return latencySecc
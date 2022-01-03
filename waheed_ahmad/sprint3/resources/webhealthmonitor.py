import urllib3
import datetime
from cloudmatricdata import cloudmetric1
import constants as constants
from s3b import s3bukclass as buk
import tablelambda as rwtab
import boto3,os
# URL_TO_MONITOR='www.twitter.com'
# URL_MONITOR_NAMESPACE="waheedwebhealth"
# URL_MONIROR_NAME_AVAILABILITY= "url_availabiloty"
# URL_MONIROR_NAME_LATENCY= "url_latency"

def lambda_handler(events,context):
    cw= cloudmetric1();
    url_values=[]
    urllllMon = buk('waheedbuc','urls.json').read_buk()
    monitoringurl = rwtab.gettable(os.getenv(key ='table_name'))
    
    values = dict()
    abc=1
    for url in monitoringurl:
        avail = get_availability(url)
        dimensions=[
        {'Name': 'URL', 'Value': url}
        ]
        cw.put_data(constants.URL_MONITOR_NAMESPACE , constants.URL_MONITOR_NAME_AVAILABILITY+'_'+url+ str(abc),dimensions,avail)
    

     #########Latency matrix 
    
        latency = get_latency(url)
        dimensions=[
        {'Name': 'URL', 'Value': url}
        ]
        cw.put_data(constants.URL_MONITOR_NAMESPACE, constants.URL_MONITOR_NAME_LATENCY+'_'+url+ str(a),dimensions,latency)
        
        a+=1
    
        values.update({"avaiability":avail, "Latency":latency})
        url_values.append(values)
    return url_values
    
    # avail= get_availability()   #now we are putting matrices to cloudwatch  
    # dimensions=[
    #     {'Name': 'URL' , 'Value':constants.URL_TO_MONITOR }
    #  #   {'Name': 'Region' , 'Value': "DUB"}
        
    #     ]
    # cw.put_data(constants.URL_MONITOR_NAMESPACE ,constants.URL_MONIROR_NAME_AVAILABILITY , dimensions,avail)
    
    
     
    # latency= get_latency()
    # dimensions=[
    #     {'Name': 'URL' , 'Value': constants.URL_TO_MONITOR }
    #  #   {'Name': 'Region' , 'Value': "DUB"}
        
    # ]
    # cw.put_data(constants.URL_MONITOR_NAMESPACE ,constants.URL_MONIROR_NAME_LATENCY ,dimensions, latency)
    
    
    # values.update({"Availability": avail,"Latency":latency})
    # return values

def get_availability(url):
    http=urllib3.PoolManager()
    response=http.request("GET", url )
    if response.status==200:
        return 1.0
    else:
        return 0.0
    
def get_latency(url):
    http=urllib3.PoolManager()
    start=datetime.datetime.now()
    response=http.request("GET",url)
    end=datetime.datetime.now()
    delta =end-start
    latencySecc=round(delta.microseconds * 0.000001,6)
    return latencySecc
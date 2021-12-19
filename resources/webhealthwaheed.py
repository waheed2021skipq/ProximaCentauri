import urllib3
import datetime
URL_to_Monitor='www.bbc.com'

def lambda_handler(events,context):
    values= dict()
    avail= get_availability()
    latency= get_latency()
    values.update({"Availability": avail,"Latency":latency})
    return values

def get_availability():
    http=urllib3.PoolManager()
    response=http.request("GET",URL_to_Monitor)
    if response.status==200:
        return 1
    else:
        return 0
    
def get_latency():
    http=urllib3.PoolManager()
    start=datetime.datetime.now()
    response=http.request("GET",URL_to_Monitor)
    end=datetime.datetime.now()
    diff=end-start
    latency_sec=round(diff.microsecond*0.000001,6)
    return latency_sec
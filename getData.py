# -*- coding: UTF-8

from OneNetApi import *
import json

def getData_value(datastreamid):
    test = OneNetApi("***************************") #  your API
    datastream_id = datastreamid
    limit = 1
    res3 = test.datapoint_get(device_id = "6975064", limit = limit, datastream_id = datastream_id)
    data = json.loads(res3.content.replace(']',' ').replace('[',' '))
    value = data['data']['datastreams']['datapoints']['value']
    #time = data['data']['datastreams']['datapoints']['at']
    return value
	
	
def getData_time(datastreamid):
    test = OneNetApi("***************************") #  your API
    datastream_id = datastreamid
    limit = 1
    res3 = test.datapoint_get(device_id = "6975064", limit = limit, datastream_id = datastream_id)
    data = json.loads(res3.content.replace(']',' ').replace('[',' '))
    #value = data['data']['datastreams']['datapoints']['value']
    time = data['data']['datastreams']['datapoints']['at'][0:19]
    return time

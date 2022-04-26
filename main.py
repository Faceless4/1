import requests
import json
# import .config
#token = '8hMu0eoCgqOH1OOz9tHACu7IMSqfH09G7JYVNcnRqZpiB1FBka1NvYj5Ex8cn5Gl'
# make an http request to flespi
# with authentification via flespi token
# and return content
from config import token


def flespi_http_request (entity):
    headers = {'Authorization': token}
    response = requests.get('https://flespi.io/gw/' + entity + '/all', headers=headers)

    return response.content


# send request to get data about channels from flespi and return
# required parameters
def get_channels():
    data = flespi_http_request('channels')
#    print(response.content)
    channels = json.loads(data)
    return channels['result']


# print to console information about provided channels info channels
def print_channels_info(channels):
  for channel in channels:
       print(channel['name'], channel['protocol_id'])
  print(len(channels))
# print to console information about provided devices info devices
def print_devices_info(devices):
  for device in devices:
       print(device['name'])
  print(len(devices))
# print to console information about provided streams info streams
def print_streams_info(streams):
  for stream in streams:
       print(stream['name'])
  print(len(streams))
# send request to get data about devices from flespi and print
# required parameters
def get_devices():
    data = flespi_http_request('devices')
#    print(response.content)
    devices = json.loads(data)
    return devices['result']
# send request to get data about streams from flespi and print
# required parameters
def get_streams():
    data = flespi_http_request('streams')
#    print(response.content)
    streams = json.loads(data)
    return streams['result']
 # get data about channels

channels = get_channels()
print_channels_info(channels)
devices=get_devices()
print_devices_info(devices)
streams = get_streams()
print_streams_info(streams)


#response=requests.get('https://flespi.io/gw/devices/all', headers=headers) # get data about devices
#GetDevice(response)
#response=requests.get('https://flespi.io/gw/streams/all', headers=headers) #get data about streams
#GetStream(response)

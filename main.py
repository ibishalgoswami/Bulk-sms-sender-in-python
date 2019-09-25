import requests
import time
x=list(input('enter the bulk numbers').split(','))

URL = 'https://www.way2sms.com/api/v1/sendCampaign'
msg=input('Enter your msg')
def zerosmssend(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
    req_params = {
        'apikey': 'provide your api key of way2sms',
        'secret': 'provide your secret',
        'usetype': 'stage',
        'phone': i,
        'message': msg,
        'senderid':'provide the senderId(Do not use quotes while using the senderID here)'
    }
    return requests.post(reqUrl, req_params)
count=0
while len(x)!=0:
    for i in x:
        response = zerosmssend(URL, 'apikey', 'secretKey', 'usetype', i, 'senderId', 'textMessage')
        print(response.text)
    count=count+1
    if len(x)>count:
        break
time.sleep(5)









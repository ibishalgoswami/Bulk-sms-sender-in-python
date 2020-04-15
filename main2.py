#Updated code for sending SMS using python
import requests
import json

URL = 'https://www.sms4india.com/api/v1/sendCampaign'
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':'your api key',
  'secret':'your secreat key',
  'usetype':'stage',
  'phone': your phone number, #This won't be in quotes
  'message':"Hello Python",
  'senderid':your sender ID(phone no) through which you have registered in way2sms #This won't be in quotes
  }
  return requests.post(reqUrl, req_params)
response = sendPostRequest(URL, 'apikey', 'secret', 'usetype', 'phone', 'senderid', 'message' )

print (response.text)

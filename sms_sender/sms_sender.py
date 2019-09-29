#####################################################################################################################################
# Creator: Kunal Bhattacharya                                                                                                       #
# Creator contact: kunal.jubce@gmail.com                                                                                            #
# Purpose: To send text messages via way2sms SMS API. Can be used an independent program or as a module.                            #
# Command to execute: python sms_sender.py                                                                                          #
#####################################################################################################################################

import requests
import json

url = 'https://www.way2sms.com/api/v1/sendCampaign'

def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMsg):
    '''
    Function to form the parameters and send the post request.
    Returns the response object.
    '''
    params = {
        'apiKey': apiKey,
        'secret': secretKey,
        'useType': useType,
        'phone': phoneNo,
        'message': textMsg,
        'senderId': senderId
    }

    return requests.post(url, params)

def main(msg, phone_no):
    '''
    Assign the values and use them as parameters while calling the sendPostRequest() function.
    '''
    api_key = 'YOUR_WAY2SMS_API_KEY'                            # Replace with your own way2sms API key available in your way2sms account
    secret_key = 'YOUR_WAY2SMS_SECRET_KEY'                      # Replace with your own way2sms secret key available in your way2sms account
    use_type = 'prod'/'stage'                                   # Depending on whether you use the stage keys or prod keys
    phone_no = phone_no                                         # Recipient phone number
    msg = msg                                                   # Text message to be sent via SMS
    senderId = 'SENDER_MOBILE_NUMBER'                           # Not the recipient mobile number
    if len(msg)>0 and len(phone_no)==10:
        # Check if both message and phone_no have values. No request will be sent without these values.
        response = sendPostRequest(url, api_key, secret_key, use_type, phone_no, senderId, msg)
        print(response.text)
    else:
        print('Enter a valid text and phone number to send the message! Cannot send blank SMS!')

if __name__=="__main__":
    # Asks for user input when run directly. Expects the arguments to be passed when run as an imported module.
    msg = input("Enter message to send over SMS: ")
    phone_no = input("Enter the recipient phone number: ")
    main(msg, phone_no)
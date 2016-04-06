__author__ = 'vandreol'

import requests

name = raw_input("Please enter name if the FILTER:")
port = raw_input("Please enter port to FILTER:")

url = "https://10.65.134.58:8443/controller/nb/v2/monitor/filter/%s" % name
payload = "{\r\n  \"vlanPriority\": \"\",\r\n  \"tcpOptionLength\": \"\",\r\n  \"vlanId\": \"\",\r\n  \"name\": \"%s\",\r\n  \"tosBits\": \"\",\r\n  \"networkDst\": \"\",\r\n  \"transportPortDst\": \"%s\",\r\n  \"datalayerSrc\": \"\",\r\n  \"datalayerDst\": \"\",\r\n  \"httpMethodId\": \"\",\r\n  \"transportPortSrc\": \"\",\r\n  \"networkSrc\": \"\",\r\n  \"etherType\": \"0x0800\",\r\n  \"bidirectional\": \"false\",\r\n  \"protocol\": \"6\"\r\n}" % (name,port)

headers = {
    'authorization': "Basic YWRtaW46YWRtaW4=",
    'content-type': "application/json",
    'cache-control': "no-cache",
    }

print("Create FILTER")
response = requests.request("PUT", url, data=payload, headers=headers, verify=False)
print(response.text)
if response.status_code != 201:
    print("Something went wrong ... no time to fix this just exit")
    exit(1)

user_input = raw_input("Press Enter to Delete filter: ")
print("Delete FILTER")
response = requests.request("DELETE", url, headers=headers, verify=False)

print(response.text)
if response.status_code != 204:
    print("Something went wrong ... no time to fix this just exit")
    exit(1)

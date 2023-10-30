import http.client
#
conn = http.client.HTTPSConnection("www.google.com")
conn.request("GET", "/")
response = conn.getresponse()
print(type(response))        
print(response.status, response.reason)
if response.status ==200:
    data = response.read()
    print(data)


import requests

try:
    response = requests.get("https://api.github.com/events/get", timeout=5)
    print(response.raise_for_status())
    response.status_code
    print(response.status_code)
    
except requests.exceptions.Timeout as e:
    # Xử lý lỗi Timeout
    print("Timeout error: ",e)
    
except requests.exceptions.HTTPError as e:
    # Xử lý lỗi HTTP
    print("HTTP error: ",e)
    
except Exception as e:
    # Xử lý lỗi khác
    print("Other error: ",e)
   
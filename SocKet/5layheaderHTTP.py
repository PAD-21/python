import urllib.request
from urllib.request import Request
url = "http://python.org"
USER_AGENT = "Mozilla/5.0 (Linux; Android 10) AppleWebkit/537.36"
def chrome_user_agent():
    opner = urllib.request.build_opener()
    opner.add_handler = [("User-agent",USER_AGENT)]
    urllib.request.install_opener(opner)
    response = urllib.request.urlopen(url)
    print("Response headers")
    print("------------------")
    for header, value in response.getheaders():
        print(header + ":" + value)
    request = Request(url)
    request.add_header("User-agent",USER_AGENT)
    print("\nRequest headers")
    print("--------------")
    for header , value in request.header_items():
        print(header + ":" + value)
if __name__=="__main__":
    chrome_user_agent()

"""
Định nghĩa một biến url chứa địa chỉ của trang web cần truy cập và biến USER_AGENT chứa chuỗi User-Agent mới.

Cuối cùng, cài đặt opner vừa xây dựng bằng cách sử dụng urllib.request.install_opener().

Sử dụng urllib.request.urlopen() để gửi yêu cầu đến trang web và nhận lại kết quả.

In ra các tiêu đề phản hồi sử dụng phương thức response.getheaders().

Tạo một yêu cầu mới bằng cách sử dụng Request(url) và thêm User-Agent mới vào yêu cầu sử dụng request.add_header()

In ra các tiêu đề yêu cầu sử dụng phương thức request.header_items().

Chương trình sử dụng User-Agent mới để truy cập trang web và in ra các tiêu đề của yêu cầu và 
phản hồi để kiểm tra xem User-Agent đã được thay đổi chưa.



Regenerate response

    Header trong HTTP (Hypertext Transfer Protocol) request và response 
là một phần của thông điệp HTTP được gửi giữa máy khách và máy chủ
    header của HTTP request là phần đầu tiên của yêu cầu HTTP được gửi từ máy khách đến máy chủ, 
nó bao gồm các thông tin về phương thức yêu cầu (như GET, POST, PUT, DELETE),
    header của HTTP response là phần đầu tiên của phản hồi HTTP được gửi từ máy chủ đến máy khách, 
nó bao gồm các thông tin về mã trạng thái phản hồi (như 200 OK, 404 Not Found, 500 Internal Server Error
"""
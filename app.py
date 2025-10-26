import requests

# 简单功能：请求百度首页并打印状态码
def test_requests():
    response = requests.get("https://www.baidu.com")
    print(f"请求状态码:{response.status_code}")

# 执行函数
if __name__=="__main__":
    test_requests()

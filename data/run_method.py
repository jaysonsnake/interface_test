'''
1、该文件用于存放发送请求的方法，以及各方法详细配置
'''
import requests
import json
class RunMethod:
    res = None

    def post_method(self,url,data,header=None):
        if header != None:
            res = requests.post(url,data,header)
        else:
            res = requests.post(url,data)
        print('返回码：',res.status_code)
        return res.json()

    def get_method(self,url,data=None,header=None):
        if header != None:
            res = requests.get(url,data,headers=header,verify=False)
        else:
            res = requests.get(url,data,verify=False)
        return res.json()

    #判断使用哪种方法发送请求，返回响应报文
    def run_main(self,method,url,data=None,header=None):
        if method == 'post':
            res = self.post_method(url,data,header)
        else:
            res = self.get_method(url,data,header)
        return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)



'''
1、该文件用于存放json文件的各种操作
'''

import json

class OperationJson:
    # 头函数，确定json文件位置
    def __init__(self,jsonPath=None):
        #如果file_path为空，则获取传入的file_name
        if jsonPath == None:
            self.json_path = "../jsonFile/default.json"
        #如果不存在file_path，则获取默认的file_path路径
        else:
            self.json_path = jsonPath
        self.json_data = self.get_json_data()

    #读取json文件
    def get_json_data(self):
        with open(self.json_path, 'rb') as fp:       #打开json文件
            all_data = json.loads(fp.read())   #获取json内容
            return all_data

    #写入json文件
    def write_json_data(self,data):
        with open("../jsonFile/cookies.json", "w") as fp:   #打开json文件
            fp.write(json.dumps(data))      #将传入的data转换成json格式



    #根据传入的key获取value
    def get_key_value(self,request_data_key):
        #print(type(self.json_data))
        return self.json_data[request_data_key]


if __name__ == '__main__':
    operaJson = OperationJson()
    print(operaJson.get_key_value("login"))



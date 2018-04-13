'''
1、该文件用于存放case依赖相关配置
'''
from util.operation_excel import OperationExcel
from data.get_data import GetData
from data.run_method import RunMethod
from jsonpath_rw import jsonpath,parse
import json

class DependentData:

    def __init__(self,case_id):
        self.case_id = case_id
        self.opera_excel = OperationExcel()
        self.data = GetData()
        self.run_method = RunMethod()

    #根据case_id，获取该case_id整行数据
    def get_row_data(self):
        rows_data = self.opera_excel.get_row_values_by_case_id(self.case_id)
        return rows_data

    #执行依赖case，获取结果
    def run_dependent(self):
        row_num = self.opera_excel.get_row_id(self.case_id)    #根据case_id获取行号
        request_data = self.data.get_data_for_json(row_num)     #根据行号获取request
        header = self.data.get_header_state(row_num)            #根据行号获取header
        method = self.data.get_request_method(row_num)          #根据行号获取请求方法
        url = self.data.get_request_url(row_num)                #根据行号获取url
        res = self.run_method.run_main(method,url,request_data,header)   #发送请求，获取响应报文
        return json.loads(res)     # 在run_main()中报文已解码为json，需要将json格式解码为dict，并返回

    #根据依赖数据的key，获取依赖case执行后的响应key值
    def get_data_for_key(self,row):
        depend_data = self.data.get_depend_key(row)     #获取excel表中“依赖的返回数据”
        response_data = self.run_dependent()        #获取依赖case的响应报文
        # print("-------->>>>")
        # print(depend_data)
        # print(type(depend_data))
        # print(response_data)
        # print(type(response_data))
        json_exe = parse(depend_data)       #login.username
        madle = json_exe.find(response_data)
        #print(madle)
        return [math.value for math in madle]

if __name__ == '__main__':
    dependentData = DependentData("login-0102")
    print(dependentData.run_dependent())
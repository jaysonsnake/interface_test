'''
1、该文档用于存放获取excel数据的各种操作
'''
from util.operation_excel import OperationExcel
from util.operation_json import OperationJson
import data.data_config

class GetData():

    def __init__(self):
        self.opera_excel = OperationExcel()
        self.operaJson = OperationJson()

    #获取excel行数，即case个数
    def get_rows_count(self):
        return self.opera_excel.get_rows()

    #获取是否执行
    def get_is_run(self,row):
        col = int(data.data_config.get_is_run())
        run_model = self.opera_excel.get_cell_value(row,col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return  flag

    #获取是否携带header
    def get_header_state(self,row):
        col = int(data.data_config.get_header_state())
        header = self.opera_excel.get_cell_value(row,col)
        return header

    #获取请求方式
    def get_request_method(self,row):
        col = int(data.data_config.get_method())
        method = self.opera_excel.get_cell_value(row,col)
        return method

    #获取url
    def get_request_url(self,row):
        col = int(data.data_config.get_url())
        url = self.opera_excel.get_cell_value(row,col)
        return url

    #获取json文件名
    def get_json_file_name(self, row):
        col = int(data.data_config.get_json_file_name())
        json_file_name = self.opera_excel.get_cell_value(row,col)
        return json_file_name

    #获取excel表里的请求字段
    def get_request_data(self,row):
        col = int(data.data_config.get_data())
        excel_data = self.opera_excel.get_cell_value(row,col)
        if excel_data == "":
            return None
        return excel_data

    #通过获取excel表关键字，在json文件里拿到json数据
    def get_data_for_json(self,row):
        request_data = self.operaJson.get_key_value(self.get_request_data(row))
        return request_data

    #获取预期结果
    def get_expect_data(self,row):
        col = int(data.data_config.get_expect())
        expect = self.opera_excel.get_cell_value(row,col)
        if expect == '':
            return None
        return expect

    #获取要写入的cell，并写入数据
    def write_result(self,row,value):
        col = int(data.data_config.get_result())
        self.opera_excel.write_excel(row,col,value)

    #获取依赖数据的key
    def get_depend_key(self,row):
        col = int(data.data_config.get_data_depend())       #列值为“依赖的返回数据”那一列
        dependent_key = self.opera_excel.get_cell_value(row,col)    #根据行号，获取该列的cell值
        if dependent_key == '':     #如果cell值为空，则返回空，否则返回cell值
            return None
        else:
            return dependent_key

    #判断是否有依赖case
    def is_depend(self,row):
        col = int(data.data_config.get_depend_case_id())
        depend_case_id = self.opera_excel.get_cell_value(row,col)
        if depend_case_id == '':
            return None
        else:
            return depend_case_id

    #获取数据依赖字段
    def get_depend_field(self,row):
        col = int(data.data_config.get_request_key())
        field_data = self.opera_excel.get_cell_value(row,col)
        if field_data == '':
            return None
        else:
            return field_data

if __name__ == '__main__':
    print(GetData().get_data_for_json(3))
    print(GetData().get_json_file_name(3))
    print(GetData().get_depend_field(3))
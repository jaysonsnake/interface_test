'''
1、此文件用于配置excel表中每个col的映射
2、获取每个col
'''

#定位excel表参数
class global_var:
    case_id = '0'
    interface_name = '1'
    prerequisites = '2'
    url = '3'
    is_run = '4'
    method = '5'
    header = '6'
    depend_case_id = '7'
    data_depend = '8'
    request_key = '9'
    jsonFileName = '10'
    data = '11'
    expect = '12'
    result = '13'

#获取case_id
def get_case_id():
    return global_var.case_id

#获取interface_name
def get_interface_name():
    return global_var.interface_name

#获取prerequisites
def get_prerequisites():
    return global_var.prerequisites

#获取url
def get_url():
    return global_var.url

#获取是否执行case
def get_is_run():
    return global_var.is_run

#获取method
def get_method():
    return global_var.method

#获取header状态
def get_header_state():
    return global_var.header

#获取case依赖
def get_depend_case_id():
    return global_var.depend_case_id

#获取data依赖（依赖case中的依赖key）
def get_data_depend():
    return global_var.data_depend

#获取需要填入返回key值的请求key
def get_request_key():
    return global_var.request_key

#获取json文件名
def get_json_file_name():
    return global_var.jsonFileName

#获取请求参数data
def get_data():
    return global_var.data

#获取期望结果
def get_expect():
    return global_var.expect

#获取实际结果
def get_result():
    return global_var.result

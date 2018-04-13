'''
1、该文档用于运行测试脚本
'''
import sys

from data.get_data import GetData
from data.run_method import RunMethod
from data.depend_data import DependentData
from util.common_utils import CommonUtil
from util.operation_json import OperationJson
from util.send_email import SendEmail

class RunScript:

    def __init__(self,):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()
        self.send_mail = SendEmail()

    #执行入口
    def go_on_run(self):
        pass_count = []     #pass个数统计
        fail_count = []     #fail个数统计
        rows_count = GetData().get_rows_count()       #统计行数
        for i in range(1,rows_count):
            # 如果is_run为True，则运行脚本
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_request_url(i)
                method = self.data.get_request_method(i)
                request_data = self.data.get_data_for_json(i)   #在json文件拿数据
                expect = self.data.get_expect_data(i)
                header = self.data.get_header_state(i)
                depend_case = self.data.is_depend(i)        #is_depend返回依赖case_id
                #如果执行过程中存在depend_case，则运行depend_case
                if depend_case != None:
                    self.depend_data = DependentData(depend_case)
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    depend_key = self.data.get_depend_field(i)
                    request_data[depend_key] = depend_response_data
                    # method,url,data=None,header=None
                res = self.run_method.run_main(method, url, request_data, header)
                print(res)
                #如果期望结果包含于实际结果中，则pass，计入pass个数
                if self.com_util.is_contain(expect,res):
                    self.data.write_result(i,'pass')
                    pass_count.append(i)
                else:   #否则输出实际结果，计入fail个数
                    self.data.write_result(i,res)
                    fail_count.append(i)
        #self.send_mail.send_main(pass_count,fail_count)    #发邮件



if __name__ == '__main__':
    run = RunScript()
    print(run.go_on_run())
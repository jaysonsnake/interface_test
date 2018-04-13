'''
1、此文件用于存放excel表的各种操作
'''
import xlrd
from xlutils.copy import copy

class OperationExcel:
    #头函数，确定excel表位置
    def __init__(self,file_path=None,sheet_id=None):
        #如果存在file_path,则定位到file_path和sheet
        if file_path == True:
            self.file_path = file_path
            self.sheet_id = sheet_id
        #如果不存在file_path，则定位到默认的file_path路径和sheet页
        else:
            self.file_path = "../通用接口测试用例.xls"
            self.sheet_id = 0
        self.sheet_data = self.get_sheet_data()

    #读取sheet的内容
    def get_sheet_data(self):
        #打开excel表并读取第1页
        sheet_data = xlrd.open_workbook(self.file_path).sheet_by_index(self.sheet_id)
        return sheet_data

    #读取行数
    def get_rows(self):
        return self.sheet_data.nrows

    #读取某个cell值
    def get_cell_value(self,row,col):
        return self.sheet_data.cell_value(row,col)

    #写入value
    def write_excel(self,row,col,value):
        read_data = xlrd.open_workbook(self.file_path)      #读取目标文件
        copy_data = copy(read_data)         #复制一份目标文件
        copy_data_sheet = copy_data.get_sheet(0)        #获取复制文件的sheet
        copy_data_sheet.write(row,col,value)        #写入value
        copy_data.save(self.file_path)      #保存

    #根据case_id，获取对应row_values
    def get_row_values_by_case_id(self,case_id):
        row_id = self.get_row_id(case_id)       #根据case_id获取row_num
        row_value = self.get_row_values_by_row_id(row_id)     #根据row_num获取row_value
        return row_value

    #根据row_id获取row_values
    def get_row_values_by_row_id(self, row_id):
        return self.sheet_data.row_values(row_id)

    #根据case_id，获取row_id
    def get_row_id(self, case_id):
        row_id = 0
        col_value = self.get_col_values()       #获取col值
        for col_cell_value in col_value:        #遍历col值中每个cell
            if case_id in col_cell_value:       #如果case_id在cell中
                return row_id
            row_id += 1

    #获取col值 by col_id
    def get_col_values(self,col_id=None):
        #如果col_id不为空，则获取传入的col_id
        if col_id != None:
            col_value = self.sheet_data.col_values(col_id)
        #如果col_id为空，则获取第1个col的value
        else:
            col_value = self.sheet_data.col_values(0)
        return col_value




if __name__ == '__main__':
    opera = OperationExcel()
    print(opera.get_row_id('login-0102'))

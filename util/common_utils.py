'''
1、该文件用于存放通用函数
'''
class CommonUtil:
    def is_contain(self,str_one,str_two):
        '''
        判断一个str是否在另一个str中，
        :param str_one: 查找的str
        :param str_tow: 被查找的str
        :return: True or False
        '''
        #如果str_one格式为str，则先编码为unicode再解码为utf-8
        if isinstance(str_one,str):
            str_one = str_one.encode('unicode-escape').decode('utf-8')
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag

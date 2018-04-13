'''
1、该文件用于存放发邮件的各种配置
'''
import smtplib
from email.mime.text import MIMEText
class SendEmail:
    global sender    #发件邮箱地址
    global password     #密码
    global email_host   #域名

    def send_mail(self,user_list,subject,content):
        sender = "like4501@163.com"
        password = "wincy1002"
        user = 'coco.lee' + '<'+sender+'>'   #发件人（名字+地址）
        message = MIMEText(content,_subtype='plain',_charset='utf-8')   #发件内容格式
        message['Subject'] = subject        #主题
        message['From'] = user      #发件人（名字+地址）
        message['To'] = ";".join(user_list)     #收件人
        server = smtplib.SMTP()         #创建SMTP服务
        email_host = "smtp.163.com"     #使用163邮箱
        server.connect(email_host)      #连接到163邮箱
        server.login(sender,password)    #传入登录邮箱+密码
        server.sendmail(user,user_list,message.as_string())      #
        server.close()

    def send_main(self,pass_list,fail_list):
        pass_num = float(len(pass_list))    #pass个数
        fail_num = float(len(fail_list))    #fail个数
        count_num = pass_num + fail_num     #总数 = pass + fail
        pass_rate = "%.2f%%" %(pass_num/count_num*100)        #成功率。其中%.2f代表取小数点后2位，%%代表取百分号
        fail_rate = "%.2f%%" %(fail_num/count_num*100)        #失败率
        user_list = ["196327588@qq.com"]
        subject = "Interface automation test report"
        content = "此次共运行接口个数为%d个。\n通过个数为%d个，通过率为%s；\n失败个数为%d个，失败率为%s。" %(count_num,pass_num,pass_rate,fail_num,fail_rate)
        self.send_mail(user_list,subject,content)



if __name__ == '__main__':
    send = SendEmail()
    send.send_main(["pass","pass","pass"],["fail","fail"])
# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 16:27
# @Author  : babi
# @File    : run.py

"""
运行用例集：
    python3 run.py

# '--allure_severities=critical, blocker'
# '--allure_stories=测试模块_demo1, 测试模块_demo2'
# '--allure_features=测试features'

"""
import sys

import os # 增加了这个，以便于后续生成allure报告
import pytest
from Common import Log
from Common import Shell
from Conf import Config
from Common import Email

if __name__ == '__main__':
    conf = Config.Config()
    log = Log.MyLog()
    log.info('初始化配置文件, path=' + conf.conf_path)
    


    shell = Shell.Shell()
    xml_report_path = conf.xml_report_path
    html_report_path = conf.html_report_path
    
    # 定义测试集，原来的目录路径

    args = ['-s', '-q', '--alluredir', xml_report_path]
    pytest.main(args)
    
    
    # 定义测试集，后面的链接地址是jenkens生成allure结果的指定路径，必须写这个，才能执行成功
    # 以下是生生报告到jenkens里面的allure报告
    # results = r"F:\\Program Files\\Jenkins\\workspace\\ceshi_bendi\\allure-results"
    # args = ['-s', '-q', '--alluredir', results]
    # pytest.main(args)
   
    
    cmd = 'allure generate %s -o %s --clean' % (xml_report_path, html_report_path)
    # cmd = 'allure generate %s -o %s --clean' % (results,r"F:\\Program Files\\Jenkins\\workspace\\ceshi_bendi\\allure-report")

    
    
    # 导入包os，然后调用如下命令，才能生成html报告，生成allure报告
    d = os.system(cmd)

    

    try:
        shell.invoke(cmd)
    except Exception:
        log.error('执行用例失败，请检查环境配置')
        raise

    try:
        mail = Email.SendMail()
        mail.sendMail()
    except Exception as e:
        log.error('发送邮件失败，请检查邮件配置')
        raise


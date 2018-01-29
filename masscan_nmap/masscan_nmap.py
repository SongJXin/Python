#!/bin/bash
#coding=utf-8
import os
from multiprocessing import Pool
import time
import datetime
from nmapXMLtoExcel import getResult
import xlsxwriter
import yaml
#for k in m:
#时间戳
starttime = datetime.datetime.now()
stime=time.strftime("%Y_%m_%d_%H_%M",time.localtime())

config={}
#获取配置文件
with open("config.yaml") as confile:
    config=yaml.load (confile)
masscanConfig=config['masscan']
nmapConfig=config['nmap']
otherConfig=config['other']
#进程池 运行nmap
def runNmap(k):   
    filename='result'+stime+'/nmapResult'+k[0]
    cmd2=r'nmap  -p '+k[1]+' '+nmapConfig["parameters"]+' -oX '+filename+' '+k[0]
    #print(cmd2)
    os.system(cmd2)
if __name__=='__main__':
    #运行masscan
    if masscanConfig['useAdvanced']=="True":#masscan 配置保存在.conf配置文件
        cmd=r'masscan -c masscan.conf -oL masscanresult'+stime
    else:#从yaml中读取配置
        cmd='masscan -p'+masscanConfig['port']+' --rate '+str(masscanConfig['rate'])+' '+masscanConfig['ip']+' -oL masscanresult'+stime
    #print(cmd)
    os.system(cmd)
    m=[]
    #从文件中获取开放端口
    with open('masscanresult'+stime,'r') as f :
        for line in f.readlines():
            l=line.split()
            if l[0]=="open":
                #print (l)
                m.append((line.split()[3],line.split()[2]))
    #去重复
    m=list(set(m))
    #转化为字典（会丢失部分数据）
    d=(dict(m))
    #获取ip列表
    iplist=list(d)
    #保存字典
    dic={}
    #用ip生成一个新的字典
    for dit in d:
        dic.setdefault(dit,set(''))
    #端口添加到字典
    for mi1 in m:
        dic[mi1[0]].add(mi1[1])
    #将端口用','连接
    mi=[]
    for i in dic:
        s=""
        for j in dic[i]:
        #    print(j)
            s=s+j+','
        mi.append([i,s])
    #判断操作系统新建保存结果的文件夹
    if otherConfig['system']=='linux':
        os.system("mkdir result"+stime)
    elif  otherConfig['system']=='windows':
        os.system("md result"+stime)
    #根据配置文件生成进程池
    pool=Pool(otherConfig['progress'])
    #运行进程池
    pool.map(runNmap,mi)
    #写入excel 生成xlsx文件
    workbook = xlsxwriter.Workbook(r'result'+stime+'.xlsx')
    #添加sheet页
    worksheet = workbook.add_worksheet()
   #写入表头
    worksheet.write('A1', 'ip')
    worksheet.write('B1', 'port')
    worksheet.write('C1', 'service')
    worksheet.write('D1', 'os')
    #下一次吸入row行
    row=2
    #将配置信息写入excel
    #根据.conf文件运行
    if masscanConfig['useAdvanced']:
        with open(r'masscan.conf', 'r') as f:
            for line in f.readlines():
                l=line.split()
                if(len(l)>0):
                    if l[0]=="rate":
                        worksheet.write('L1', 'masscan rate:')
                        worksheet.write('M1', l[2])
                    if l[0]=="ports":
                        worksheet.write('L2', 'ports range:')
                        worksheet.write('M2', l[2])
                    if l[0]=="range":
                        worksheet.write('L3', 'ip range:')
                        worksheet.write('M3', l[2])
    else:#根据yaml文件运行
        worksheet.write('L1', 'masscan rate:')
        worksheet.write('M1', masscanConfig['rate'])
        worksheet.write('L2', 'ports range:')
        worksheet.write('M2', masscanConfig['port'])
        worksheet.write('L3', 'ip range:')
        worksheet.write('M3', masscanConfig['ip'])
    #根据ip读取nmap结果文件
    for ip in iplist:
        ip,ports,os=getResult('result'+stime+'/nmapResult'+ip)
        #写入
        for port in ports:
            worksheet.write('A'+str(row),ip)
            worksheet.write('B'+str(row),port)
            worksheet.write('C'+str(row),ports[port])
            worksheet.write('D'+str(row),os)
            row=row+1
    #写入总体运行信息
    worksheet.write('L4', 'IP number(result):')
    worksheet.write('M4', len(ip)/2)
    worksheet.write('L5', 'ports number(result):')
    worksheet.write('M5', len(m))
    endtime = datetime.datetime.now()
    worksheet.write('L6', 'run time(s):')
    worksheet.write('M6', (endtime-starttime).seconds)
    workbook.close()

    print("test over")


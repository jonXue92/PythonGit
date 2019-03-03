#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'ShengLeQi'
import xlwt
import pymysql
import sys,os
import datetime
def mysql_m():  #mysql数据连接部分
    # 打开数据库连接
    db = pymysql.connect("10.0.0.101","sheng","123456","Sheng_DB" ,charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT * FROM student "
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        # print(results)
        # print(len(results[0]))
        return  results
    except:
        print("Error: unable to fetch data")

def set_style(name,height,bold=False):  #字体设置
    """
    设置单元格样式
    :param name: 字体名字
    :param height: 字体大小
    :param bold: 是否加粗
    :return: 返回样式
    """
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style

def write_excel():  #写入xls部分
    """
    写表格
    :return:
    """
    f = xlwt.Workbook()  # 创建工作簿
    sheet1 = f.add_sheet('students',cell_overwrite_ok=True) ##第二参数用于确认同一个cell单元是否可以重设值。

    row0 = ['id','性别','班级编号','姓名']
    # 生成第一行
    for i in range(len(row0)):
        sheet1.write(0,i,row0[i],set_style('宋体',200,True)) # 200对应的是10号字体,如果设置太小,可能看上去像空Excel,实际上是有内容的
    results=mysql_m()
    for count,row in  enumerate(results):
        for i in range(len(row)):
            sheet1.write(count+1,i,row[i],set_style('宋体',200,True))
    f.save('test1.xls')
    now_time = datetime.datetime.now()
    yes_time = now_time + datetime.timedelta(days=-1)
    yes_time = (yes_time.strftime('%Y%m%d'))
    if os.path.exists(yes_time) is not True:
        os.makedirs(yes_time)
    path=os.path.join(os.getcwd(),yes_time,'test_time.xls')
    f.save(path)

if __name__ == '__main__':
    write_excel()

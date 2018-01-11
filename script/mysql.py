#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import MySQLdb

try:
    conn = MySQLdb.connect(host="120.26.63.239", user="glitzhome", passwd="123glitzhome", port=3307, db="gzcloud", charset="utf8")
    cursor = conn.cursor()
    print("MySQL连接成功!")

    cursor.execute('SELECT * FROM gzc_warehouse_store WHERE id = 13')
    column = cursor.description

    result = []
    dataList = cursor.fetchall()
    for data in dataList:
        row = {}
        for i in range(len(column)):
            row[column[i][0]] = data[i]
        result.append(row)

    print(result[0]['store_name'])

except:
    print("MySQL连接失败!")

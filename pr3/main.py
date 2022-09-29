#!/usr/bin/env python
# coding: utf-8

import codecs

file1 = codecs.open("C:\\Users\\User\\Desktop\\ТРПО\\Практика 3\\9901\\test.txt", encoding='utf-8')

while True:
    line = file1.readline()
    mas = line.split(',')
    if not line:
        break
    if (300 <= int(mas[2]) <= 1100):
        print(mas[0])

file1.close

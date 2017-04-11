from django.test import TestCase

# Create your tests here.

'''
# 匯入CSV檔到DB
import csv
with open('draw_member/member.csv', newline='', encoding = 'utf8') as f:
        csv_reader = csv.DictReader(f)
        members=[]
        for row in csv_reader:
            members.append((row['﻿名字'], row['團體']))
            #print(members[0][0],members[0][1])
        print(members)

#這個只能用shell做，在這裡應沒有關聯到settings檔案，所以無法引用到Model to DB的Lib.
from draw_member.models import Member
for m in members:
    Member(name=m[0], group_name=m[1]).save()
print('done')

'''

'''
Dump DB to yaml file
python manage.py dumpdata --format=yaml --indent=4 --output draw_member/fixtures/anime_members.yaml draw_member.Member
python manage.py dumpdata --format=json --indent=4 --output draw_member/fixtures/anime_members.json draw_member.Member
'''

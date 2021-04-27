import xlsxwriter as xw



keys =['Title','Author','Affiliations','Publication types','Citation Journal Title&Date','Cited By','Abstract']
keys_1=['Title','Author','Affiliations','Citation Journal Title&Date','Cited By','Abstract']
def xw_toExcel(data, fileName):  # xlsxwriter库储存数据到excel
    workbook = xw.Workbook(fileName)  # 创建工作簿
    worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
    worksheet1.activate()  # 激活表
    title = ['Title', 'Author', 'Affiliations','Publication types','Citation Journal Title&Date','Cited By','Abstract']  # 设置表头
    worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头
    i = 2  # 从第二行开始写入数据
    for index,d in enumerate(data):
        # insertData = d
        tup = (d[kk] for kk in keys)
        row = 'A' + str(i)
        worksheet1.write_row(row, tup)
        i += 1
    workbook.close()  # 关闭表
# "-------------数据用例-------------"
testData = [
    {"id": 1, "name": "立智", "price": 100},
    {"id": 2, "name": "维纳", "price": 200},
    {"id": 3, "name": "如家", "price": 300},
]

fileName = 'advanced.xlsx'
# xw_toExcel(testData, fileName)
path = ['advanced_search_result.html']
import re
data = ''
for paths in path:
    f = open(paths,'r',encoding='utf-8')
    lines = f.readlines()

    for line in lines:
        data = data+line
pat_title='<strong class="sub-title">(.*?)</strong><br /><strong class="sub-title">Author:'
pat_author='<strong class="sub-title">Author: </strong>(.*?)<br /><strong class="sub-title">Affiliations:'
pat_affi = '<strong class="sub-title">Affiliations:(.*?)<br /><strong class="sub-title">Publication types'
pat_pubtypes='<strong class="sub-title">Publication types:(.*?)<strong class="sub-title">Citation Journal Title&Date:'
pat_citetitleanddate = '<strong class="sub-title">Citation Journal Title&Date:(.*?)<strong class="sub-title">Cited By:'
pat_citedby = '<strong class="sub-title">Cited By: </strong>(.*?)<br /><br /><strong class="sub-title">Abstract:'
pat_abstract = '<strong class="sub-title">Abstract: </strong>(.*?)<br />'

pat_onedata = '(.*?)==<br /><br />'

pattern ='<strong class="sub-title">(.*?)</strong><br /><strong class="sub-title">Author: </strong>(.*?)<br /><strong class="sub-title">Affiliations: '\
          '</strong><br />(.*?)<br /><strong class="sub-title">Publication types: </strong>(.*?)<strong class="sub-title">Citation Journal Title&Date: </strong>'\
          '(.*?)<br /><strong class="sub-title">Cited By: </strong>(.*?)<br /><br /><strong class="sub-title">Abstract: </strong>(.*?)<br />='
# print(pat_onedata)
pattern_without_pubtype = '<strong class="sub-title">(.*?)</strong><br /><strong class="sub-title">Author: </strong>(.*?)<br /><strong class="sub-title">Affiliations: '\
          '</strong><br />(.*?)<br /><strong class="sub-title">Citation Journal Title&Date: </strong>'\
          '(.*?)<br /><strong class="sub-title">Cited By: </strong>(.*?)<br /><br /><strong class="sub-title">Abstract: </strong>(.*?)<br />='
list_data = re.compile(pat_onedata, re.S).findall(data)
result=[]
seg =['<strong class="sub-title">', '</strong>', '</p>','<p>','<br />', '\n','</i>','<i>','</b>','<b>']
for data in list_data:
     dic={}
     if data.find('Publication types')>0:
         r = re.compile(pattern,re.S).findall(data)[0]
         for (k,v) in zip(keys,r):
              dic[k]=v


     else:
         dic['Publication types']='Unknown'
         r = re.compile(pattern_without_pubtype,re.S).findall(data)[0]
         for (k,v) in zip(keys_1,r):
              dic[k]=v

         # print("==================")
         # print(data)
     result.append(dic)
for dat in result:
    if dat['Publication types']!='Unknown':
        dat['Publication types']=dat['Publication types'].replace('<br />',';')
    # raw = dat['Abstract']
    dat['Affiliations'] = dat['Affiliations'].replace('<br />',';')
    for p in seg:

        dat['Abstract'] = dat['Abstract'].replace(p,'')
    dat['Abstract'] = dat['Abstract'].strip()

    while dat['Abstract']!=dat['Abstract'].replace("  ",' '):
        dat['Abstract'] = dat['Abstract'].replace("  ", ' ')

xw_toExcel(result, fileName)
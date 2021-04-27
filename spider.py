import requests
import re
import  time
import os
import ssl
# from urllib.request import urlopen
# from requests.packages.urllib3.packages.six.moves import urllib
import urllib
import urllib.request
# cognitive Dementia
# cognition Dementia
# cognitive Alzheimer's Disease
# cognition Alzheimer's Disease

start = time.time()
target = 'https://pubmed.ncbi.nlm.nih.gov/?term=%28%28%28cognition+Alzheimer%27s+Disease%29+OR+%28cognition+Dementia%29%29+OR+%28cognitive+Alzheimer%27s+Disease%29%29+OR+%28cognitive+Dementia%29&filter=simsearch1.fha'
# '&filter=years.2021-2021'
keyword_pages_dict={}
key=["cognitive Dementia","cognition Dementia","cognitive Alzheimer's Disease","cognition Alzheimer's Disease"]
turl="https://pubmed.ncbi.nlm.nih.gov/"
filter = "simsearch2.ffrft"
filter_abstract="&filter=simsearch1.fha"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
a=0
# year_list=[]
# for year in range(1972,2022):
#     item =
for k in key:
    tdata=requests.get(turl,params={"term":k}).text
    pat_allpage='<span class="total-pages">(.*?)</span>'
    allpage=re.compile(pat_allpage,re.S).findall(tdata)[0].strip().replace(',', '')
    keyword_pages_dict[k]=allpage
    a=a+int(allpage)
print("===============总页数===",a)
# # # num=input("请输入大致想获取的文章数目（总数为"+str(int(allpage[0].replace('\n        ','').replace(',',''))*10)+"):")
# #
def get_Article_id(keyword):
    article_id=[]
    article_dict={}
    number = int(keyword_pages_dict[keyword])
    for j in range(0,1000):
        url="https://pubmed.ncbi.nlm.nih.gov/"+"?term="+keyword+filter_abstract+"&page="+str(j+1)
        # print(url)
        # u = "https://pubmed.ncbi.nlm.nih.gov/?term=cognitive Dementia&filter=simsearch1.fha&page=365"
        try:
            data=requests.get(url,headers=headers,timeout=(10,10)).text
        except:
            f = open('hard_page_4_18.txt','a',encoding = 'utf-8')
            f.write(url+'\n')
            f.close()
            continue
        pat1_content_url='<div class="docsum-wrap">.*?<.*?href="(.*?)".*?</a>'
        content_url=re.compile(pat1_content_url,re.S).findall(data)
        print(content_url)
        article_id=article_id+content_url
    a = len(article_id)
    b = len(set(article_id))
    art=list(set(article_id))
    repeat = a-b
    for id in art:
        article_dict[id]=keyword
    return  article_dict, repeat
#
# def  delete_repeat(dict1,dict2,dict3,dict4):
#
#
#          print("dict1的长度为：",len(dict1))
#          print("dict2的长度为：", len(dict1))
#          d1= dict(dict1,**dict2)
#          print("dict1,dict2合并之后长度为：",len(d1))
#
#          print("dict3的长度为：", len(dict3))
#          print("dict4的长度为：", len(dict4))
#          d2 =dict(dict3,**dict4)
#          print("dict3,dict4合并之后长度为：",len(d2))
#
#          d_all = dict(d1,**d2)
#          print("全部合并长度为，",len(d_all))
#          return d_all
# ##生成字典
dict1,r=get_Article_id(key[0])
print("dict1数量为",len(dict1))
# print("重复的数量为",r)
# print("共耗时：%d min" % round((time.time() - start) / 60, 3))
# # print(dict1)
# dict2,r2=get_Article_id(key[1])
# print("dict2数量为",len(dict2))
# print("重复的数量为",r2)
# print("共耗时：%d min" % round((time.time() - start) / 60, 3))
# # print(dict2)
# dict3,r3=get_Article_id(key[2])
# print("dict3数量为",len(dict3))
# print("重复的数量为",r3)
# print("共耗时：%d min" % round((time.time() - start) / 60, 3))
# # print(dict3)
# dict4,r4=get_Article_id(key[3])
# print("dict4数量为",len(dict4))
# print("重复的数量为",r4)
# print("共耗时：%d min" % round((time.time() - start) / 60, 3))
# # print(dict4)
# all_dict=delete_repeat(dict1,dict2,dict3,dict4)
# print('总dict数量为',len(all_dict))
# print("共耗时：%d min" % round((time.time() - start) / 60, 3))
# # print(all_dict)
#
# with open('all_dict_4_18.txt','a+',encoding='utf-8') as f:
#     f.write(str(all_dict)+'\n')
# end = time.time()
# print("共耗时：%d min" % round((time.time() - start) / 60, 3))

w = open ('all_dict_4_18.txt','r',encoding="utf-8")
line = w.readline()
# print(line)
import requests
import re
import time
import os
##解析写入

all_dict = eval(line)
print(len(all_dict))
# print("======all_dict===")
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
finish = 0
spider_num = 0
# 19243660
# id 1380 15783
for p in key:
    if not os.path.exists(p+'.html'):
            f = open(p+'.html','a',encoding='utf-8')
            f.close()

for id in all_dict.keys():
        path= all_dict[id]
        spider_num= spider_num+1
        print("正在爬取第%d篇文献..."%spider_num)
        curl="https://pubmed.ncbi.nlm.nih.gov/"+id
        try:
            cdata = requests.get(curl, headers=headers, timeout=10).text
        except:
            f = open('hard_url_4_18.txt','a',encoding='utf-8')
            f.write(id+'\n')
            f.close()
            continue
        pat_journal_title = '<meta name="citation_journal_title" content="(.*?)"'
        pat2_title = "<title>(.*?)</title>"
        pat_author = '<div class="inline-authors">.*?data-ga-label=.*?>(.*?)</a><sup class="affiliation-links">'
        pat3_content = '<div class="abstract-content selected".*?>(.*?)</div>'
        pat4_date = '<span class="cit">(.*?)</span>'
        pat5_fullcontexturl = 'PMCID:.*?href=(.*?)data-ga-category="full_text".*?</a>'
        pat6_context = 'Full text links.*?href=(.*?)target="_blank"'
        pat_authorname = 'data-ga-action="author_link.*?data-ga-label=.*?>(.*?)</a>'
        pat_cited_by = '<div class="citedby-articles" id="citedby">.*?<em class="amount">(.*?)</em>'
        patt_keyword = '<strong class="sub-title">.*?Keywords:.*?</strong>(.*?)</p>'
        # pat_keyword= 'aria-controls="keyword-actions-mesh-terms-major.*?data-pinger-ignore>(.*?)</button><div id="keyword-actions-mesh-terms-major'
        title = re.compile(pat2_title, re.S).findall(cdata)[0].replace('- PubMed', ' ')
        author = list(set(re.compile(pat_authorname, re.S).findall(cdata)))
        journal_title = re.compile(pat_journal_title, re.S).findall(cdata)[0]
        citedby_num = '0'
        cited = re.compile(pat_cited_by, re.S).findall(cdata)
        if len(cited) > 0:
            citedby_num = cited[0]

        pat_publication_type = 'aria-controls="keyword-actions-publication-type.*?data-pinger-ignore>(.*?)</button><div id="keyword-actions-publication-types.*?'
        pat_affiliations = '<li data-affiliation-id="affiliation-.*?<sup class="key">(.*?)</sup>(.*?)</li>'
        bool_pub_type = False
        publication_type = re.compile(pat_publication_type, re.S).findall(cdata)
        pu = [pt.strip() for pt in publication_type]
        if len(publication_type) > 0:
            if 'Review' in pu or 'Systematic Review' in pu:
                continue
            bool_pub_type = True
        affi = list(set(re.compile(pat_affiliations, re.S).findall(cdata)))
        affi = sorted(dict(affi).items(), key=lambda item: int(item[0]))
        # print(affi)
        # print(curl)
        if len(affi)==0:
            continue
        affi_china = affi[0][1].lower()
        from_china = False
        if affi_china.find('china') >= 0:
            from_china = True
        if not from_china:
            continue
        keywd_list = list(set(re.compile(patt_keyword, re.S).findall(cdata)))
        bool_keywd = False
        if len(keywd_list) > 0:
            bool_keywd = True
        # title_list.append(title[0])
        # print("正则爬取的题目是：" + title)
        # print("作者" + '\n')
        # print(author)
        # print("cited:" + citedby_num)
        # print("pub_type:" + '\n')
        # print(publication_type)
        # print("aff" + '\n')
        # print(len(affi))
        # print(affi)
        # print("keyword:")
        # print(keywd_list)

        content = re.compile(pat3_content, re.S).findall(cdata)
        date = re.compile(pat4_date, re.S).findall(cdata)
        context_pmc = re.compile(pat5_fullcontexturl, re.S).findall(cdata)
        context_link = re.compile(pat6_context, re.S).findall(cdata)
        context = context_pmc + context_link
        # url.append(context[0])
        # paper_dic[title]=context[0]
        # print(context[0])

        fh = open(path+".html", "a", encoding="utf-8")
        fh.write('<strong class="sub-title">')
        fh.write(title + '</strong>' + '<br />')
        fh.write('<strong class="sub-title">')
        fh.write("Author: " + '</strong>')
        for name in author:
            if author.index(name) != len(author) - 1:
                fh.write(name + ", ")
            else:
                fh.write(name)
        fh.write('<br />')
        fh.write('<strong class="sub-title">')
        fh.write("Affiliations: " + '</strong>' + '<br />')
        for (ind, sent) in affi:
            fh.write(ind + sent + '<br />')
        if bool_pub_type:
            fh.write('<strong class="sub-title">')
            fh.write("Publication types: " + '</strong>' + '<br />')
            for p in publication_type:
                fh.write(p.strip() + '<br />')
        fh.write('<strong class="sub-title">')
        fh.write("Citation Journal Title&Date: " + '</strong>')
        fh.write(journal_title + ' ' + date[0] + '<br />')
        fh.write('<strong class="sub-title">')
        fh.write("Cited By: " + '</strong>')
        fh.write(citedby_num + "<br /><br />")
        fh.write('<strong class="sub-title">')
        fh.write('Abstract: ' + '</strong>')
        fh.write(str(content[0]) + "<br />")
        if bool_keywd:
            fh.write('<strong class="sub-title">')
            fh.write("Keywords: " + '</strong>')
            for kw in keywd_list:
                fh.write(kw.strip() + '<br /><br />')

        fh.write('===================================================<END>============================================================================'+ '<br /><br />'+'\n')

        fh.close()
        finish = finish+1
        print("已经写入满足要求的%d篇文章，"%(finish)+"共耗时：%d min" % round((time.time() - start) / 60, 3))
##   加页码
for item in  key:
    data=''
    pattern = '=<(.*)>='
    r = open(item+'.html','r',encoding='utf-8')
    # w.close()
    lines = r.readlines()
    # w.close()
    for line in lines:
        data=data+line

    leng = len(re.compile(pattern).findall(data))
    for n in range(leng):
        data = data.replace('<END>', str(n+1), 1)
    w=open(item + '.html', 'w', encoding='utf-8')
    w.write('<meta charset="utf-8">'+'<br />')
    w.write(data)
    w.close()

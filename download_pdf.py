#Python 3.8.10
#windows 7
import urllib.request
import ssl
import re
import time
import os

#no ssl certifaction alert
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url=input('please type the webpage :\n')


#get all the google drive link
htm=urllib.request.urlopen(url,context=ctx).read().decode()
#urlopen是同步操作，直到完成请求才会执行后面的代码

#get link list
urllist=re.findall('<a href="(https://drive.google.com/.*?)"',htm)
#get name list
filename=re.findall('<a href="https://drive.google.com/.*?">(.*?)</a>',htm)


def myunescape_decode(li):
    #maketrans替换功能 参数长度必须相同，a->b 不能abc->d

    map=[('%3A',':'),('%2F','/'),('%3F','?'),('%3D','='),('%26','&'),('amp;','')]

    for i in range(len(li)):
        url=li[i]
        for item in map:
            (a,b)=item
            url=url.replace(a,b)
        li[i]=url



myunescape_decode(urllist)
myunescape_decode(filename)

link_dict=dict()

#build the dictionary
for i in range(len(urllist)):
    link_dict[filename[i]]=urllist[i]



#downaload

folder='mydownload_3.1415926'

try:
    os.makedir(folder)
except:
    print('folder exist')
    pass

#set current working dictory
currentpath=os.chdir(os.getcwd()+'\\'+folder+'\\')


for filename,url in link_dict.items():
    print(filename,'start to download!\n')

    data=urllib.request.urlopen(url,context=ctx).read()

    time.sleep(5)

    path=filename+'.pdf'

    hfile=open(path,'wb')
    hfile.write(data)
    hfile.close()

    print(filename,'downloading compeleted!\n')

print('mission compeleted!')

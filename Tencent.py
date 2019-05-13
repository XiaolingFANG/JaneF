#!/usr/bin/env python
# coding: utf-8

# In[13]:


import urllib
import json
import jieba
import csv

class Csv:

   def __init__(self , word, count):
      self.word = word
      self.count = int(count)
   
   def add(self):
        self.count += 1

videocount = 0
#彈幕url
words = []
i = 1270000000
while i < 1270000001:
    url = 'https://mfm.video.qq.com/danmu?otype=json&callback=jQuery19109021208136318777_1556758756418&timestamp=15&target_id=3867692042%26vid%3Dh0030qj4fov&count=80&second_count=5&session_key=0%2C0%2C0&_=1556758756427'
    response = urllib.request.urlopen(url)
    if response.getcode() == 200:
        print (response.getcode())
        responsedata = response.read().decode('utf-8');
        responsedatasubstring = responsedata[responsedata.find('(')+1:len(responsedata)-1]
        content = json.loads(responsedatasubstring)
        i = i + 1

        if len(content['comments']) != 0:
            videocount = videocount + 1

        for x in content['comments']:
            seg_list = (jieba.cut(x['content'], cut_all=False))
            #print("/ ".join(seg_list))
            wordtemp = ' '.join(seg_list)
            #words.append(wordtemp[0:len(wordtemp)-1])
            words.append(wordtemp)
    
def csvonlyword(words):
    array = []
    #只有字的檔案
    with open(r'''C:\Users\fangx\Desktop\tencentonlyword.csv''' , encoding='utf-8-sig') as mfile:
        lines = csv.reader(mfile, delimiter=' ', quotechar='|')
        linecount = 0
        for line in lines:
            temp = ''.join(line)
            if linecount == 0:
                linecount += 1
            else:
                linecount += 1
                array.append(temp)
                
    for y in words:
        ytemp = y.split(" ")
        for z in ytemp:
            array.append(z)
                
    #只有字的檔案
    with open(r'''C:\Users\fangx\Desktop\tencentonlyword.csv''', mode='w' , newline='' , encoding='utf-8-sig') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        employee_writer.writerow(['Content'])
        for x in array:
            employee_writer.writerow([x])
    
def csvwordcountpercentage(words):
    
    Csvreadarray = []
    
    #有count跟percentage的檔案
    with open(r'''C:\Users\fangx\Desktop\tencentwithcount.csv''' , encoding='utf-8-sig') as myfile:
        lines = csv.reader(myfile, delimiter=' ', quotechar='|')
        linecount = 0
        for line in lines:
            temp = ', '.join(line)
            if linecount == 0:
                linecount += 1
            else:
                linecount += 1
                temp = line[0].split(",")
                Csvtemp = Csv(temp[0] , temp[1])
                Csvreadarray.append(Csvtemp)

    for y in words:
        ytemp = y.split(" ")
        for z in ytemp:
            if z == '\n':
                continue
            zexist = 0
            for x in Csvreadarray:
                if x.word == z:
                    x.add()
                    zexist = 1
                    break
            if zexist == 0:
                Csvtemp = Csv(z , 1)
                Csvreadarray.append(Csvtemp)
        
    #有count跟percentage的檔案    
    with open(r'''C:\Users\fangx\Desktop\tencentwithcount.csv''', mode='w' , newline='' , encoding='utf-8-sig') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        totalcount = 0
        for x in Csvreadarray:
            totalcount = totalcount + x.count
        
        employee_writer.writerow(['Content', 'Count', 'Percentage'])
        for x in Csvreadarray:
            employee_writer.writerow([x.word, x.count, str(x.count/totalcount*100) + "%"])

        
csvwordcountpercentage(words)
csvonlyword(words)
print (videocount)


# In[ ]:





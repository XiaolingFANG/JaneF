#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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
i = 10100000
while i < 10150000:
    url = 'http://danmu.aixifan.com/V4/' + str(i) + '_2/4073558400000/1000?order=-1'
    response = urllib.request.urlopen(url)
    responsedata = response.read().decode('utf-8');
    i = i + 1
    if responsedata.find('{') != -1 :
        videocount = videocount + 1
        responsedatasubstring = '{ "danmu" : ' + responsedata[responsedata.find('{') - 1:len(responsedata)-1] + "}"
        content = json.loads(responsedatasubstring)

        for x in content['danmu']:
            seg_list = (jieba.cut(x['m'], cut_all=False))
            #print("/ ".join(seg_list))
            wordtemp = ' '.join(seg_list)
            #words.append(wordtemp[0:len(wordtemp)-1])
            words.append(wordtemp)
    
def csvonlyword(words):
    array = []
    #只有字的檔案
    with open(r'''C:\Users\fangx\Desktop\acfunonlyword.csv''' , encoding='utf-8-sig') as mfile:
        lines = csv.reader(mfile, delimiter=' ', quotechar='|')
        linecount = 0
        for line in lines:
            temp = ''.join(line)
            print (temp)
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
    with open(r'''C:\Users\fangx\Desktop\acfunonlyword.csv''', mode='w' , newline='' , encoding='utf-8-sig') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        employee_writer.writerow(['Content'])
        for x in array:
            employee_writer.writerow([x])
    
def csvwordcountpercentage(words):
    
    Csvreadarray = []
    
    #有count跟percentage的檔案
    with open(r'''C:\Users\fangx\Desktop\acfunwithcount.csv''' , encoding='utf-8-sig') as myfile:
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
    with open(r'''C:\Users\fangx\Desktop\acfunwithcount.csv''', mode='w' , newline='' , encoding='utf-8-sig') as employee_file:
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





#英文文本词汇统计

#打开文件
def getText():
    txt = open("1.txt","r",encoding='UTF-8').read()
    txt = txt.lower() #文件小写
    for ch in '!@#$%^&*/*-+[];/.,\{}|:?><':#替换特殊字符
        txt = txt.replace(ch," ")
    return txt

myTxt = getText()
words  = myTxt.split()
counts = {}

for word in words:
    counts[word] = counts.get(word,0) + 1
    
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)

for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word,count))



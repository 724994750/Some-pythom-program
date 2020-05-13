#词云
import jieba
import wordcloud

#from scipy.misc import imread
#打开指定词云形状
#mask0 = imread("")
excludes=("萧炎")

f=open("1.txt","r",encoding="GBK")
t=f.read()
f.close()
ls=jieba.lcut(t)

txt = " ".join(ls)
w=wordcloud.WordCloud(font_path = "msyh.ttc",\
                      width=1000,height=700,\
                      background_color="white",\
                      stopwords=excludes
                     # mask=mask0
                      )
w.generate(txt)
w.to_file("3.png")


# coding: utf-8

# In[13]:

import MeCab
from nude import Nude

#ツイートの内容の単語のうち、ネガティブなものを自動検出する
def tweetchecknegative(text):
    mecab = MeCab.Tagger ()
    mecab.parse('-Owakati')
    node = mecab.parseToNode(text)
    negativeword = []
    
    while node:
        words = node.feature.split(",")
        word = words[len(words)-3] 
        ld = open("pn_ja.dic")
        lines = ld.readlines()
        ld.close()
        for line in lines:
            if line.split(":")[0]==word:
                if float(line.split(":")[3]) < -0.9:
                    negativeword.append(line.split(":")[0])
                    break
                    
        node=node.next
    
    return negativeword

#画像が炎上するかどうかの自動確認
#をしたかったが時間に都合上、公序良俗に違反するかの確認
def imagecheck(image):
    n = Nude(image)
    n.parse()
    return n.result
    



# In[ ]:




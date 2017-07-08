
# coding: utf-8

# In[94]:

#!/usr/bin/python3

import tweetcheck
import submission
from tkinter import *
import tkinter.filedialog as tkfd



fields = ('ユーザ名', 'パスワード', 'ツイート文', "NGワード", '画像ファイル名', "画像判定")

def login(username, password):
    return true 

def param(entries, variables):
    
    if sum(c.get() for c in variables) == len(variables):
        return  Label(text = "OK").pack()
    #submission.tweet(entries)
    else :
        return Label(text = "投稿前に必ず確認してください").pack()
    
#ツイートの判定
def tweetsetting(entries):
    text = str(entries['ツイート文'].get())
    entries['NGワード'].delete(0, END)
    entries['NGワード'].insert(0, tweetcheck.tweetchecknegative(text))

    
#画像の判定
def imagesetting(entries):
    entries['画像ファイル名'].delete(0, END)
    entries['画像判定'].delete(0, END)
    
    
    file = tkfd.askopenfilename() 
    entries['画像ファイル名'].insert(0, file)

    if tweetcheck.imagecheck(file):
        entries['画像判定'].insert(0, "不適切な可能性: 高")
    else: entries['画像判定'].insert(0, "不適切な可能性: 低")
    
    

#通常のフォーム
def normalform(root, field):
    entries = {}
    row = Frame(root)
    lab = Label(row, width=30, text=field+": ", anchor='w')
    ent = Entry(row)
    ent.insert(0,"")
    row.pack(side=TOP, fill=X, padx=5, pady=5)
    lab.pack(side=LEFT)
    ent.pack(side=RIGHT, expand=YES, fill=X)
    entries[field] = ent
    return entries

#パスワードなどの取得
def passform(root, field):
    entries = {}
    row = Frame(root)
    lab = Label(row, width=30, text=field+": ", anchor='w')
    ent = Entry(row,show="*")
    ent.insert(0,"")
    row.pack(side=TOP, fill=X, padx=5, pady=5)
    lab.pack(side=LEFT)
    ent.pack(side=RIGHT, expand=YES, fill=X)
    entries[field] = ent
    return entries


if __name__ == '__main__':
    root = Tk()
    root.title("Twitter炎上予防アプリ")
    ents = {}
    #ログインチェック
    username = normalform(root, fields[0])
    password = passform(root, fields[1])
    a1 = Button(root, text='ログイン',
          command=(lambda e=ents: usersetting(username, password)))
    a1.pack(padx=5, pady=5)
    
    
    #ツイートチェック
    ents.update(normalform(root, fields[2]))
    ents.update(normalform(root, fields[3]))
    root.bind((lambda event, e=ents: fetch(e)))   
    b1 = Button(root, text='ツイートを自動チェック',
          command=(lambda e=ents: tweetsetting(e)))
    b1.pack(padx=5, pady=5)
    
    #画像チェック
    ents.update(normalform(root, fields[4]))
    ents.update(normalform(root, fields[5]))
    root.bind((lambda event, e=ents: fetch(e)))   
    c1 = Button(root, text='画像を選ぶ',
          command=(lambda e=ents: imagesetting(e)))
    c1.pack(padx=5, pady=5)
    
    #全て確認できたら投稿
    variables = [BooleanVar() for i in range(4)]
    Label(text = "チェック項目").pack()
    Checkbutton(text = "悪口になっていないか？", variable = variables[0]).pack(side = LEFT)
    Checkbutton(text = "他人のプライバシーを侵害していないか？", variable = variables[1]).pack(side = LEFT)
    Checkbutton(text = "災害や病気などに対して不謹慎ではないか？", variable = variables[2]).pack(side = LEFT)
    Checkbutton(text = "法律に触れる行為を書き込んでいないか？", variable = variables[3]).pack(side = LEFT)
    
    root.bind((lambda event, e=ents: fetch(e)))  
    d1 = Button(root, text='ツイートする', command=(param(ents, variables)))
    d1.pack(padx=5, pady=5)


    root.mainloop() 


# In[ ]:




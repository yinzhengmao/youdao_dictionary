import requests
import json
import tkinter
from tkinter import *


def result_string():
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }

    content = entry_content.get().strip()

    data_new = {
        'i': content,
        'doctype': 'json'
    }

    res_string = requests.post(url,headers=header, data=data_new).text
    json_data = json.loads(res_string)

    res.set(json_data['translateResult'][0][0]['tgt'])

window = Tk()
window.geometry('400x650+800+30')
window.title('软件界面的制作')
lable_content = tkinter.Label(text='请输入文字: ', foreground='red', font=('GB2312',22))

lable_content.grid(row=0,column=0)

entry_content = tkinter.Entry(font=('GB2312',18))
entry_content.grid(row=0,column=1)

lable_out = tkinter.Label(text='输出翻译: ', foreground='red', font=('GB2312',22))
lable_out.grid()

res = tkinter.StringVar()

entry_out = tkinter.Entry(font=('GB2312',18), textvariable=res)
entry_out.grid(row=1,column=1)

btn_res = tkinter.Button(text='翻译', width=10, font=('GB2312',18), command=result_string)
btn_res.grid(row=2,column=0)

btn_quit = tkinter.Button(text='退出', width=10, font=('GB2312',18), command=window.quit)
btn_quit.grid(row=2,column=1)

window.mainloop()

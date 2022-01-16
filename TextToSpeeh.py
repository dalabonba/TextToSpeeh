import tkinter.ttk as ttk
from gtts import gTTS
from gtts import lang
from tkinter import Tk
from tkinter import Label
from tkinter import StringVar
from tkinter import Entry
from tkinter import Button



def confirm():
    textToSpeeh=gTTS(mainGetText.get(), lang=supLangDict[comboLang.get()])

    fileName=f"{filenameGetText.get()}.mp3"

    textToSpeeh.save(fileName)




supLangDict=lang.tts_langs()#將gtts支援的語言存進字典supLangDict，鍵為gtts用的縮寫代號，值為語言名
supLangDict={value:key for key, value in supLangDict.items()}#反轉鍵值
supLangList=list(supLangDict.keys())




#----------------------------window----------------------
window = Tk()
window.geometry('370x200')
window.title("語音mp3產生器")
window.resizable(False, False)

#-----lable---------
lableMain=Label(window,text="要轉換的文字:")
lableMain.grid(row=0,column=0, ipadx=10, pady=10 ,padx=20)#ipad:內部邊界   pad:外邊界

lableFilename=Label(window,text="檔名:")
lableFilename.grid(row=1,column=0, ipadx=10, pady=10)

lableMp3=Label(window,text=".mp3")
lableMp3.grid(row=1,column=2, pady=10)

lableLang=Label(window,text="語言:")
lableLang.grid(row=2,column=0, ipadx=10, pady=10)
#-------------------


#-----combobox---------
comboLang = ttk.Combobox(window,values=supLangList,state="readonly")
comboLang.grid(row=2,column=1, ipadx=10, pady=10)
comboLang.current(len(supLangList)-2)#combobox從0開始算。選擇第{61-2}項


# tkinter中的文本輸入框說明 https://shengyu7697.github.io/python-tkinter-entry/
#-------entry-----------
mainGetText = StringVar()#建立tk文字變數物件
entryMain = Entry(window, textvariable=mainGetText,width=25)#建立文字輸入框，命名為entryMain，將其中輸入的字指向mainGetText
entryMain.grid(row=0, column=1)


filenameGetText = StringVar()
entryFilename = Entry(window, textvariable=filenameGetText,width=25)
entryFilename.grid(row=1, column=1)
#------------------------



#------button-----------
btn3 = Button(window,text = '確認',command = confirm ,width=10)#按下按鈕執行delete副程式:刪除最後一筆資料
btn3.grid(row=3, column=0, ipadx=10, pady=30)
#-----------------------


window.mainloop()  #循環刷新視窗畫面
#--------------------------------------------------------
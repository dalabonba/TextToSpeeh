from gtts import gTTS,lang
from tkinter import Tk, Label, StringVar, Entry, Button, scrolledtext
from tkinter.ttk import Combobox
from getpass import getuser


def confirm():
    textToSpeeh=gTTS(scrolledTextMain.get("1.0", "end-1c"), lang=supLangDict[comboLang.get()])#scrolledtext取值:https://www.delftstack.com/zh-tw/howto/python-tkinter/how-to-get-the-input-from-tkinter-text-box/

    fileName=f"{filenameGetText.get()}.mp3"
    
    if comboPath.get()=="桌面":
        textToSpeeh.save(f'C:\\Users\\{getuser()}\\Desktop\\{fileName}')
    else:
        textToSpeeh.save(fileName)




supLangDict=lang.tts_langs()#將gtts支援的語言存進字典supLangDict，鍵為gtts用的縮寫代號，值為語言名
supLangDict={value:key for key, value in supLangDict.items()}#反轉鍵值
supLangList=list(supLangDict.keys())




#----------------------------window----------------------
window = Tk()
window.geometry('390x340')
window.title("語音mp3產生器")
window.resizable(False, False)

#-----lable---------
lableMain=Label(window,text="要轉換的文字:")
lableMain.grid(row=0,column=0, ipadx=10, pady=60 ,padx=20)#ipad:內部邊界   pad:外邊界

lableFilename=Label(window,text="檔名:")
lableFilename.grid(row=1,column=0, ipadx=10, pady=10)

lableMp3=Label(window,text=".mp3")
lableMp3.grid(row=1,column=2, pady=10)

lableLang=Label(window,text="語言:")
lableLang.grid(row=2,column=0, ipadx=10, pady=10)

lableLang=Label(window,text="存檔位置")
lableLang.grid(row=3,column=0, ipadx=10, pady=10)
#-------------------


#-----combobox---------
comboLang = Combobox(window,values=supLangList,state="readonly")
comboLang.grid(row=2,column=1, ipadx=10, pady=10)
comboLang.current(len(supLangList)-2)#combobox從0開始算。選擇第{61-2}項

comboPath = Combobox(window,values=["桌面","執行檔所在位置"],state="readonly")
comboPath.grid(row=3,column=1, ipadx=10, pady=10)
comboPath.current(0)
#-----scrolledtext-----
scrolledTextMain = scrolledtext.ScrolledText(window ,width=23, height=8)
scrolledTextMain.grid(row=0, column=1)
#----------------------

# tkinter中的文本輸入框說明 https://shengyu7697.github.io/python-tkinter-entry/
#-------entry-----------
filenameGetText = StringVar()#建立tk文字變數物件
entryFilename = Entry(window, textvariable=filenameGetText,width=25)#建立文字輸入框，命名為entryMain，將其中輸入的字指向filenameGetText
entryFilename.grid(row=1, column=1)
#------------------------



#------button-----------
btn3 = Button(window,text = '確認',command = confirm ,width=10)#按下按鈕執行delete副程式:刪除最後一筆資料
btn3.grid(row=4, column=0, ipadx=10, pady=30)
#-----------------------


window.mainloop()  #循環刷新視窗畫面
#--------------------------------------------------------
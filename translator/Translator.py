from tkinter import * 
from tkinter import ttk,messagebox

import googletrans
import textblob


root = Tk()
root.title("Translator")
root.geometry("1080x400")


#lan
def translate_now():
    global language
    try:
        text_=text1.get(1.0 , END)
        c2 = combo1.get()
        c3 = combo2.get()
        if(text_):
            words=textblob.TextBlob(text_)
            lan = words.detect_language()
            for i,j in language.items():
                if(j==c3):
                    lan_= i
            words=words.translate(from_lang=lan , to=str(lan_))
            text2.delete(1.0 , END)
            text2.insert(END , words)
    except Exception as e:
        messagebox.showerror("Traslate" , "pls Try again")





def label_change():
    c=combo1.get()
    c1 = combo2.get()
    LabeL1.configure(text=c)
    LabeL2.configure(text=c1)
    root.after(1000 , label_change)

language = googletrans.LANGUAGES
languageV= list(language.values())
lang1 =language.keys()

LabeL1 = Label(root,text="ENGLISH",font="segoe 30 bold" , bg='white' , width=18 , bd=5 , relief=GROOVE)
LabeL1.place(x=10 , y=50)

f = Frame(root , bg="Black" , bd=5)
f.place(x=10,y=118,width=440 , height=210)

text1 = Text(f,font="Robot 20" , bg="white" , relief=GROOVE , wrap=WORD)
text1.place(x=0 , width=430 , height=200)
scrollbar1= Scrollbar(f)
scrollbar1.pack(side="right" , fill="y")
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)


f1 = Frame(root , bg="Black" , bd=5)
f1.place(x=620,y=118,width=440 , height=210)

text2 = Text(f1,font="Robot 20" , bg="white" , relief=GROOVE , wrap=WORD)
text2.place(x=0 , width=430 , height=200)
scrollbar2= Scrollbar(f1)
scrollbar2.pack(side="right" , fill="y")
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

combo1=ttk.Combobox(root,values=languageV,font="Roboto 14",state="r")
combo1.place(x=110, y=20)
combo1.set("ENGLISH")



combo2 = ttk.Combobox(root,values=languageV,font="Roboto 14",state="r")
combo2.place(x=730 , y=20)
combo2.set("SELECT LANGUAGE")


LabeL2 = Label(root,text="ENGLISH",font="segoe 30 bold" , bg='white' , width=18 , bd=5 , relief=GROOVE)
LabeL2.place(x=620 , y=50)

#translate

translate = Button(root , text="Translate" , font="Roboto 15 bold italic" , activebackground="purple",cursor="hand2" , bd=5 , bg = 'red' , fg="white" , command=translate_now)
translate.place(x=480 , y = 250) 


label_change()
root.configure(bg="white")
root.mainloop()
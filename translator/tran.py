from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

root = Tk()
root.title("Translator")
root.geometry("1080x400")
root.configure(bg="white")

translator = Translator()

language = LANGUAGES
languageV = list(language.values())

def translate_now():
    try:
        text_ = text1.get(1.0, END).strip()
        if not text_:
            messagebox.showwarning("Translate", "Please enter some text first.")
            return

        src_lang_name = combo1.get()
        dest_lang_name = combo2.get()

        if dest_lang_name.lower() in ["select language", "", " "]:
            messagebox.showwarning("Translate", "Please select a target language.")
            return

        # find language codes like 'en', 'hi', 'gu'
        src_code = None
        dest_code = None
        for code, name in language.items():
            if name.lower() == src_lang_name.lower():
                src_code = code
            if name.lower() == dest_lang_name.lower():
                dest_code = code

        # if source not found, let googletrans auto-detect
        if dest_code is None:
            messagebox.showerror("Translate", "Could not find target language code.")
            return

        if src_code is None:
            result = translator.translate(text_, dest=dest_code)
        else:
            result = translator.translate(text_, src=src_code, dest=dest_code)

        text2.delete(1.0, END)
        text2.insert(END, result.text)

    except Exception as e:
        # show real error so we know what’s wrong
        messagebox.showerror("Translate", f"Error: {e}")

def label_change():
    c = combo1.get()
    c1 = combo2.get()
    LabeL1.configure(text=c)
    LabeL2.configure(text=c1)
    root.after(1000, label_change)

# ---------- UI BELOW (reuse yours) ----------
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

combo1=ttk.Combobox(root,values=languageV,font="Roboto 14",state="readonly")
combo1.place(x=110, y=20)
combo1.set("english")

combo2 = ttk.Combobox(root,values=languageV,font="Roboto 14",state="readonly")
combo2.place(x=730 , y=20)
combo2.set("hindi")   # e.g. default target

LabeL2 = Label(root,text="HINDI",font="segoe 30 bold" , bg='white' , width=18 , bd=5 , relief=GROOVE)
LabeL2.place(x=620 , y=50)

translate = Button(root , text="Translate" , font="Roboto 15 bold italic" , activebackground="purple",cursor="hand2" , bd=5 , bg = 'red' , fg="white" , command=translate_now)
translate.place(x=480 , y = 250)

label_change()
root.mainloop()

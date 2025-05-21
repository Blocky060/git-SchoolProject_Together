import answer_mainfuction
from tkinter import*

window = Tk()
question = ''

window.title("AI상호 검증 서비스")
window.geometry("500x350")
window.resizable(width=FALSE, height=False)

question_text = Text(window, width=50, height=8)
answer_text = Text(window, width=50, height=10)
question_text.insert(END, "질문 : ")


def get_text():
    answer_text.delete("1.0", END)
    global question
    question = question_text.get("1.0", END)
    question_text.delete("1.0", END)
    answer_text.insert(END, answer_mainfuction.mainfuction(question))
    question_text.insert(END, "질문 : ")
    
    
question_end_button = Button(window, text='제출', command=get_text)


question_text.pack()
question_end_button.pack()
answer_text.pack()
window.mainloop()
import answer_mainfuction
from tkinter import*

window = Tk()
question = ''

window.title("AI상호 검증 서비스")
window.geometry("500x350")
window.resizable(width=True, height=True)

question_text = Text(window, width=50, height=8)
answer_text = Text(window, width=50, height=16)
question_text.insert(END, "질문 : ")


def get_text():
    answer_text.delete("1.0", END)
    global question
    question = question_text.get("1.0", END)
    question_text.delete("1.0", END)
    result, times = answer_mainfuction.mainfuction(question)
    answer_text.insert(END, result + "\n이 답변은 %s번의 상호 검증으로 확인되었습니다."%(times))
    question_text.insert(END, "질문 : ")
    
    
question_end_button = Button(window, text='제출', command=get_text)
#서기 3024년 런던 지하철 5호선의 세 번째 역장 이름과 그가 가장 좋아했던 고양이 품종은 무엇인가요?  오류나는 질문

question_text.pack()
question_end_button.pack()
answer_text.pack()
window.mainloop()
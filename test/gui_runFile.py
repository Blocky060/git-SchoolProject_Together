import answer_mainfuction  # main_function이 들어 있는 파일
from tkinter import *
import time

# 윈도우 설정
window = Tk()
window.title("AI 상호보완 검증 서비스")
window.geometry("600x500")
window.resizable(width=False, height=False)

# 입력 및 출력 영역
question_text = Text(window, width=70, height=6)
answer_text = Text(window, width=70, height=20)
question_text.insert(END, "질문 : ")

# 질문 처리 함수
def get_text():
    answer_text.delete("1.0", END)
    question = question_text.get("1.0", END).replace("질문 : ", "").strip()
    question_text.delete("1.0", END)
    question_text.insert(END, "질문 : ")

    # 진행 상태 출력
    answer_text.insert(END, "[시스템] ai1이 답변을 도출 중입니다...\n")
    window.update()
    time.sleep(0.5)

    import ai_gemini_function
    import ai_groq_function
    ai_groq_function.install_groq()
    ai_gemini_function.install_google_generativeai()

    answer_ai1 = ai_gemini_function.AI_gemini(question)
    answer_text.insert(END, "[ai1] 답변 완료!\n\n")
    window.update()
    time.sleep(0.5)

    answer_text.insert(END, "[시스템] ai2가 피드백을 생성 중입니다...\n")
    window.update()
    time.sleep(0.5)

    feedback_prompt = (
        "너는 다른 AI가 작성한 답변을 검토하고 피드백하는 역할이야.\n"
        "ai1의 답변이 적절하지 않거나 개선할 점이 있으면 구체적으로 피드백을 제시해줘\n"
        "만약 ai1의 답변이 적절하다고 판단되면 '좋은 답변입니다' 라고 말하고, 더 나은 답변이나 방향이 있다면 그것도 함께 제안해줘.\n\n"
        f"[사용자 질문]\n{question}\n\n"
        f"[AI1의 답변]\n{answer_ai1}"
    )
    feedback_from_ai2 = ai_groq_function.AI_groq(feedback_prompt).strip()
    answer_text.insert(END, "[ai2] 피드백 생성 완료!\n\n")
    window.update()
    time.sleep(0.5)

    answer_text.insert(END, "[시스템] ai1이 최종 보완 답변을 생성 중입니다...\n")
    window.update()
    time.sleep(0.5)

    refine_prompt = (
        "아래 내용은 다른 AI가 너의 답변을 검토한 피드백이야. 이 피드백을 참고하여 더 나은 답변을 작성해줘.\n\n"
        f"[피드백 내용]\n{feedback_from_ai2}\n\n"
        f"[사용자 질문]\n{question}\n"
        f"[이전 답변]\n{answer_ai1}"
    )
    answer_ai1_final = ai_gemini_function.AI_gemini(refine_prompt).strip()
    answer_text.insert(END, "[ai1] 최종 보완 답변 완료!\n\n")
    window.update()
    time.sleep(0.5)

    # 최종 결과 출력
    answer_text.insert(END, "[AI1 1차 답변]\n" + answer_ai1 + "\n\n")
    answer_text.insert(END, "[AI2 피드백]\n" + feedback_from_ai2 + "\n\n")
    answer_text.insert(END, "[AI1 최종 보완 답변]\n" + answer_ai1_final)

# 버튼
question_end_button = Button(window, text='질문 제출', command=get_text)

# 배치
question_text.pack(pady=10)
question_end_button.pack()
answer_text.pack(pady=10)

# 실행
window.mainloop()
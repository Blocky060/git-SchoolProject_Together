def main_function(question):
    import ai_groq_function as ai_groq_function
    import ai_gemini_function as ai_gemini_function

    ai_groq_function.install_groq()
    ai_gemini_function.install_google_generativeai()

    # ai1 피드백 (Gemini)
    answer_ai1_round1 = ai_gemini_function.AI_gemini(question)

    # ai2 피드백 (Groq)
    feedback_prompt = (
        "너는 다른 AI가 작성한 답변을 검토하고 피드백하는 역할이야.\n"
        "ai1의 답변이 적절하지 않거나 개선할 점이 있으면 구체적으로 피드백을 제시해줘\n"
        "만약 ai1의 답변이 적절하다고 판단되면 '좋은 답변입니다' 라고 말하고, 더 나은 답변이나 방향이 있다면 그것도 함께 제안해줘.\n\n"
        f"[사용자 질문]\n{question}\n\n"
        f"[AI1의 답변]\n{answer_ai1_round1}"
    )
    feedback_from_ai2 = ai_groq_function.AI_groq(feedback_prompt).strip()

    # ai2의 피드백을 바탕으로 ai1이 답변 재도출
    refine_prompt = (
        "아래 내용은 다른 AI가 너의 답변을 검토한 피드백이야. 이 피드백을 참고하여 더 나은 답변을 작성해줘.\n\n"
        f"[피드백 내용]\n{feedback_from_ai2}\n\n"
        f"[사용자 질문]\n{question}\n"
        f"[이전 답변]\n{answer_ai1_round1}"
    )
    answer_ai1_final = ai_gemini_function.AI_gemini(refine_prompt).strip()

    # 최종
    return (
        "[AI1 1차 답변]\n" + answer_ai1_round1 + "\n\n"
        "[AI2 피드백]\n" + feedback_from_ai2 + "\n\n"
        "[AI1 최종 보완 답변]\n" + answer_ai1_final
    )
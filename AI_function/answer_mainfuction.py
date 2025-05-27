

def mainfuction (question) :
    import ai_groq_function as ai_groq_function
    import ai_gemini_function as ai_gemini_function

    ai_groq_function.install_groq()
    ai_gemini_function.install_google_generativeai()
    

    first_ai_gemini_answer = (ai_gemini_function.AI_gemini(question))
    feed_back_ai_groq_answer = (ai_groq_function.AI_groq('''You are responsible for reviewing and needing to make sure that the content is true and giving feedback to answers written by other AIs
        If the answer is not appropriate or not true or there is anything to improve, please give me specific feedback
        "If you think ai's answer is appropriate, tell me why it's a good answer, and if you have a better answer or direction, please suggest that as well.'''
        + '\nquestion : ' + question + '\nanswer : ' + first_ai_gemini_answer))
    nowrepeat = 1
    while True :
        upgrade_ai_gemini_answer = (ai_gemini_function.AI_gemini("질문 : " + question + "\n너의 첫 답변 : " + first_ai_gemini_answer + "\n피드백 : " + feed_back_ai_groq_answer + "\n위 내용들을 참고해서 피드백에 맞게 너의 답변을 수정해서 정확한 답변만 출려해줘"))
        seconde_feed_back_ai_groq_answer = ai_groq_function.AI_groq('''You are responsible for reviewing and needing to make sure that the content is true and giving feedback to answers written by other AIs
        If the answer is not appropriate or not true or there is anything to improve, please give me specific feedback
        If you think ai's answer is appropriate, just say "OK" exactly''' + '\nquestion : ' + question + '\nanswer : ' + upgrade_ai_gemini_answer)
        if (seconde_feed_back_ai_groq_answer == 'OK') :
            break
        else :
            feed_back_ai_groq_answer = seconde_feed_back_ai_groq_answer
            first_ai_gemini_answer = upgrade_ai_gemini_answer
            
        if (nowrepeat >= 3) :
            break
        nowrepeat += 1
    
    return(upgrade_ai_gemini_answer, nowrepeat)
    
    return () # return으로 최종 대답 output
    #정확도 테스트 및 어떻게 질문해야 하는지 검토 필요
    #더 나은 대답을 위해 단지 옳고 그름 뿐 아니라 더 좋은 대답을 요구하는 식으로도 이용 가능, 하지만 GROQ는 AIPKEY재생성, 영어로 질문이 필요함
    #함수화 생각중
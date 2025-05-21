

def mainfuction (question) :
    import ai_groq_function as ai_groq_function
    import ai_gemini_function as ai_gemini_function

    ai_groq_function.install_groq()
    ai_gemini_function.install_google_generativeai()


    print ('\n')
    print ('\n')

    #print (ai1_function.AI_grop('Hello'))

    print ('\n')

    #print (ai2_function.AI_gemini("안녕"))

    #알고리즘 초안 // 문제 많음 단지 테스트용
    ai_gemini_answer = (ai_gemini_function.AI_gemini(question))
    ai_groq_answer = (ai_groq_function.AI_grop('can you check this is real? if real you should say "YES" if not real you should say "NO"' + 'question : ' + question + 'answer : ' + ai_gemini_answer))

    print(ai_gemini_answer)
    print(ai_groq_answer)
    
    return (ai_gemini_answer) # return으로 최종 대답 output
    #정확도 테스트 및 어떻게 질문해야 하는지 검토 필요
    #더 나은 대답을 위해 단지 옳고 그름 뿐 아니라 더 좋은 대답을 요구하는 식으로도 이용 가능, 하지만 GROQ는 AIPKEY재생성, 영어로 질문이 필요함
    #함수화 생각중
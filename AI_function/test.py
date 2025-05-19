import ai1_function
import ai2_function

ai1_function.install_groq()
ai2_function.install_google_generativeai()


print ('\n')
print ('\n')

print (ai1_function.AI_grop('Hello'))

print ('\n')

print (ai2_function.AI_gemini("안녕"))

#알고리즘 초안

question = input("질문을 입력해주세요 : ")
ai2_answer = (ai2_function.AI_gemini(question))
ai1_answer = (ai1_function.AI_grop('can you check this is real? if real you should say "YES" if not real you should say "NO"' + 'question : ' + question + 'answer : ' + ai2_answer))

print(ai2_answer)
print(ai1_answer)
#정확도 테스트 및 어떻게 질문해야 하는지 검토 필요
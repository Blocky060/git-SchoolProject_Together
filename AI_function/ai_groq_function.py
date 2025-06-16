
#api key     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 / 주기적인 교체 필요. 무료버전 이용중
#pip install groq



def install_groq():
    import subprocess
    import sys

    installed_packages = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze']).decode('utf-8')
    
    if 'groq' in installed_packages:
        print("groq is already installed.")
        from groq import Groq
    else:
        print("groq not found. Installing...")
        subprocess.check_call('pip install groq')
        from groq import Groq



def AI_groq(answer):
  import os
  from groq import Groq
  from api_key import groq_api_key
  GROQ_API_KEY= groq_api_key

  # Groq 클라이언트 초기화
  client = Groq(
      api_key=GROQ_API_KEY
  )
  question = answer

  chat_completion = client.chat.completions.create(
      messages=[
          {
              "role": "user",
              "content": question,
          }
      ],
      model="llama3-8b-8192",
  )

  result = (chat_completion.choices[0].message.content)
  return(result)
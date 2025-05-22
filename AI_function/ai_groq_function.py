#api key     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
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



def AI_grop(answer):
  import os
  from groq import Groq
  GROQ_API_KEY="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"

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
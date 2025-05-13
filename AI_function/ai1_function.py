#api key     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
#pip install groq

import subprocess
subprocess.check_call('pip install groq')

import os
from groq import Groq

# 키

def AI_grop(answer):
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
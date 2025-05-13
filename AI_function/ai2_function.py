#api key      AIzaSyCX4MibuQZb7GEDj16N1AMdtIjD1oJmbxU
#python3 -m pip install google-generativeai

import subprocess
subprocess.check_call('python3 -m pip install google-generativeai')

import os
import google.generativeai as genai


def AI_gemini(answer):
    question = answer
    GOOGLE_API_KEY = "AIzaSyCX4MibuQZb7GEDj16N1AMdtIjD1oJmbxU"
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')

    response = model.generate_content(question)
    result = (response.text)
    return(result)
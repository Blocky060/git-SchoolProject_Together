#api key      AIzaSyCX4MibuQZb7GEDj16N1AMdtIjD1oJmbxU
#python3 -m pip install google-generativeai

import subprocess
import sys

def install_google_generativeai():

    installed_packages = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze']).decode('utf-8')
    
    if 'google-generativeai' in installed_packages:
        print("google-generativeai is already installed.")
    else:
        print("google-generativeai not found. Installing...")
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
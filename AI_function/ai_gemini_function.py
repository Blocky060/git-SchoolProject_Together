#api key      AIzaSyCX4MibuQZb7GEDj16N1AMdtIjD1oJmbxU
#python3 -m pip install google-generativeai



def install_google_generativeai():
    import subprocess
    import sys

    installed_packages = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze']).decode('utf-8')
    
    if 'google-generativeai' in installed_packages:
        print("google-generativeai is already installed.")
        import google.generativeai as genai
    else:
        print("google-generativeai not found. Installing...")
        subprocess.check_call('python -m pip install google-generativeai')
        import google.generativeai as genai



def AI_gemini(answer):
    import os
    import google.generativeai as genai
    from api_key import gemini_api_key
    question = answer
    GOOGLE_API_KEY = gemini_api_key
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')

    response = model.generate_content(question)
    result = (response.text)
    return(result)
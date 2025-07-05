import requests
HF_API_KEY = "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"
from colorama import Fore,Style,init

init(autoreset=True)
def_model = 'google/pegasus-xsum'

def build_api_url(name):
    return f"https://api-inference.huggingface.co/models/{name}"

def query(payload,model_name = def_model):
    api_url = build_api_url(model_name)
    headers = {"Autorization":f'Bearer{HF_API_KEY}'}
    response = requests.post(api_url,headers=headers,json=payload)
    return response.json()

def summarize_txt(text,min_length,max_length,model_name = def_model):

    payload = {"inputs":text,
               "parameters":{'min_length':min_length,"max_length":max_length}}
    print(Fore.BLUE+Style.BRIGHT + f"\n???? Performing AI Summarization")
    result = query(payload,model_name=model_name)

    if isinstance(result,list) and result and "summary_text" in result[0]:
        return result[0]['summary_text']
    else:
        print(Fore.RED+"Error in response",result)
        return None
if __name__ == "__main__":
    print(Fore.YELLOW+Style.BRIGHT+"???? Hi what is your name?") 
    user_inp = input('Your Name:').strip()
    if not user_inp:
        user_inp="User"
    print(Fore.GREEN + f"Welcome {user_inp} Let Ai do some text magic")
    print(Fore.YELLOW + Style.BRIGHT + "\nPlease enter the text you want to summarize:")
    user_text = input(">").strip()

    if not user_text:
        print(Fore.RED+'No text provided') 
    else:
        print(Fore.YELLOW+'\nwhich model you want to use(e.g.,facebook/bart-large-cnn):')
        model_choice = input('Model Name(leave blank for default):').strip()
        if not model_choice:
            model_choice=def_model

        print(Fore.YELLOW+'\nChoose your summarization style')
        print('1. Standard Summary(Quick and consice)')
        print("2. Enhanced Summary(More detailed)") 
        style_choice = input('Enter 1 or 2 :').strip()

        if style_choice == "2":
            min_length = 80
            max_length =200
            print(Fore.BLUE+'\n"Enhancing SUmmarization process...')
        else:    
            min_length = 50
            max_length =150
            print(Fore.BLUE+'\n"Using satndards...')
        
        summary = summarize_txt(user_text,min_length,max_length,model_name=model_choice)
        if summary:
            print(Fore.GREEN+Style.BRIGHT+ "/nAI summarized output for you")
            print(Fore.GREEN+summary)
        else:
            print(Fore.RED+'Failed to generate Summary')


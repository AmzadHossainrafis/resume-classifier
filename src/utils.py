import re 

def remove_breket(text):
    text = text.replace(']', '').replace('[', '').replace("'", "").replace('(', '').replace(')', '').replace('/', '')
    return text

def remove_numbers(text):
    text = re.sub(r'\d+', '', text)
    return text

def lower_case(text):
    return text.lower()

def remove_extra_spaces(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()




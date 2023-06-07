import os

def n2w(n):
    num2words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
             6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', \
            19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', \
            50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', \
            90: 'ninety', 0: 'zero'}
    try:
        return num2words[n]
    except KeyError:
        try:
            return num2words[n-n%10] + num2words[n%10].lower()
        except KeyError as e:
            raise e

def verify_filepath(file_path):
    if os.path.exists(file_path):
        return True
    else:
        raise("Fix file path")

def get_data_type(value):
        if value == True or value == False : return "bool"
        if isinstance(value, str) : return "string" 
        if isinstance(value, int) : return "integer" 
        if all(isinstance(x, str) for x in value) and value != [] and not isinstance(value, dict) : return "enum" 
        if isinstance(value, dict) : return "array" 

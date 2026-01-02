import re

"""
Написать скрипт, который принимает на вход строку
и заменяет в ней все гласные буквы на символ "_"
"""

input_string = "Hello world! Вот моя тЕстовая строкА."

def main():
    result = re.sub(r'[aeiouyAEIOUYаеёиоуыэюяАЕЁИОУЫЭЮЯ]', '-', input_string)
    print(result)
  
if __name__ == "__main__":
    main()
    
    




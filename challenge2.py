sec_code=input('enter your secret password:')
step1=sec_code.maketrans('aeiou','@310$')
print(f'The secret code is{sec_code.translate(step1)}0##9')
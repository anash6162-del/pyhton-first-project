#count method
student_grades={'ram':'C','shyam':'A+','Hari':'B','Sita':'A+'}
result=list(student_grades.values()).count('A+')
print(result)
#replace methond
fruits_name='-orange_'
print(fruits_name.count('O'))
result=fruits_name.replace('-','')
fruits_name.rstrip()
print(fruits_name)
print(result)
#replace methond
list=['ram','shyam','gita']
#append extend insert
list[0]='shyam'
print(list)
#make trans method
fruits_name='orange'#Aange
result=fruits_name.maketrans('or','AA')
print(fruits_name.translate(result))
print(result)
#ord gives ascii values fro all
print(ord("A"))#A=65 Z=90
print(ord("a"))#a=97 Z=122

username='       laxman kc        '#laxmankc
print(username.strip())#remove all spaces(right left)
print(username.lstrip())#remove left spaces
print(username.rstrip())#remove right spaces
#seperate each word and store it in alist [SPLIT method!!]
step1=username.split()
print(''.join(step1))
#startswith
phone_number='+9779851089493'
print(phone_number.startswith('+977'))
#endswith
images='image1.png' 
print(images.endswith('.png'))
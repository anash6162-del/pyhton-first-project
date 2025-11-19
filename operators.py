#Operation 
# + - * / // % ** #ARETHAMETIC OPERATOR
print(5 + 3)   #Addition
print(5 - 3)   #Subtraction
print(5 * 3)   #Multiplication
print(5 / 3)   #Division
print(5 // 3)  #Floor division
print(5 % 3)   #Modulus
print(5 ** 3)  #Exponentiation

#ASSIGNMENT OPERATOR
a=[1,2,3,4]
b=a
a+=b #operation directly affects 'b' also 
print(a)
print(b)

a=[1,2,3,4]
b=a
a=a+b #operation doesnot affect 'b' as new object is created!!
print(a)
print(b)
print('-'*50)
#COMPARISON OPERATOR
num1=33
num2=33
print(num1>num2)#GREATER THAN
print(num1<num2)#LESS THAN
print(num1==num2)#EQUALS TO
print(num1!=num2)#NOT EQUAL TO
print(num1>=num2)#GREATER THAN OR EQUALS TO
print(num1<=num2)#LESS THAN OR EQUAL TO
print('-'*50)
#MEMBERSHIP OPERATOR
# 'in' AND 'not in'
student_name=['ram','shyam','hari']
if 'ram' in student_name:
    print('TRUE')
else:
    print('FALSE')
if 'sita' not in student_name:
    print('TRUE')
else:
    print('FALSE')
print('-'*50)

#IDENTITY OPERATOR 'is' || 'is not'
num1=10
num2=10
print(num1 is num2)
#list set dictionary are mutables data type which have different 
# memory adress although the content will be same!!
print('hello') #hello

#string (easy)


#Concatenate two strings
str_1='hello'
str_2='world'
result=str_1 +' '+ str_2
print(result) #hello world

#Find the length of a string.
str_3= 'Hello Everyone'
print(len(str_3)) #14


#Check if a substring is present in a string.
main_string='welcome to my hello world'
sub_string='hello'
if sub_string in main_string:   #true
    print(True)
else:
    print(False)

#Convert a string to uppercase.
string='jihkhlihohhio'
upper_string=string.upper()
print((upper_string))  #JIHKHLIHOHHIO


#Convert a string to lowercase.
normal_str='KGIYKGIUYUYGG'
lower_str=normal_str.lower()
print(lower_str) #kgiykgiuyuygg


#Replace a substring within a string.
new_string = string.replace('jihkhlihohhio','kgiykgiuyuygg')
print(new_string) #kgiykgiuyuygg

#Find the index of a substring.
txt='welcome to vj sidduvlogs'
x=txt.rindex('vj')
print(x) #11

index=main_string.find(sub_string)
print(index)

#Check if a string starts with a specific substring.
main_string_1='print the hello world'
sub_string_1='print'
if main_string_1.startswith(sub_string_1):
    print('the string is start with substring')
else:
    print("string  is not start with substring")     #the string is substring


#Check if a string ends with a specific substring.
main_string_2='print the hello world'
sub_string_2='hello'
if main_string_1.endswith(sub_string_1):
    print('the string is end with  substring')
else:
    print("string  is not end with substring")  #string  is not end with substring


#Remove leading and trailing spaces from a string
main_string_3='        good unit     '
leading_str=main_string_3.lstrip()
print(leading_str)

strip_str=main_string_3.strip()
print(strip_str)        #good unit


#Capitalize the first letter of a string
string_1='asus'
print(string_1.capitalize())   #Asus


#Swap the case of all characters in a string.
print(string_1.swapcase())     #ASUS


#Repeat a string multiple times.
n=4
repeated_string=string_1*n
print(repeated_string)  #asusasusasusasus


#Split a string into a list of words.
print(list(repeated_string)) #['a', 's', 'u', 's', 'a', 's', 'u', 's', 'a', 's', 'u', 's', 'a', 's', 'u', 's']

trailled_str=main_string_3.rsplit()
print(trailled_str)    #['good', 'unit']


#Join a list of words into a string.
join_str=''.join(trailled_str)
print(str(join_str))     #goodunit


#Check if all characters in a string are digits
digit_str='12435342'
print(digit_str.isdigit())     #True


#Check if all characters in a string are alphabetic.
print(string_1.isalpha())   #True


#Check if all characters in a string are alphanumeric.
print(string_1.isalnum())    #True


#Check if all characters in a string are uppercase.
print(upper_string.isupper())    #True


#Check if all characters in a string are lowercase.
print(lower_str.islower())     #True


#Find the maximum character in a string.
print(max(str_3))     #y


#Find the minimum character in a string
print(min(str_3))

#Get a substring from a string using slicing.
slice_str='hello world'
print(slice_str[0:6])    #hello

#Reverse a string using slicing.
print(slice_str[::-1])   #dlrow olleh


#Check if a string is empty.
my_str='hello world'
empty_str=''
print(my_str==empty_str) #False

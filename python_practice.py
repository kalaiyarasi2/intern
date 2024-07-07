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
print(string.upper())  #JIHKHLIHOHHIO


#Convert a string to lowercase.
normal_str='KGIYKGIUYUYGG'
print(normal_str.lower()) #kgiykgiuyuygg


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


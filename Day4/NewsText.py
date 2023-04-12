language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto

challenge = 'thirty days of python'
print(challenge.capitalize()) 

challenge = 'thirty days of python'
print(challenge.count('y')) # 3

challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False
print(challenge.endswith('thon')) # True

first_name = 'Asabeneh'
last_name = 'Yetayeh'
age = 250
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, age, job, country)
print(sentence) 

challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))  # 8
print(challenge.rindex(sub_string, 9)) # error
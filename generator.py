import random
import numpy 

text = ''
len_pr = []
ind_exept = []

count_w = int(input('Enter number of words -> '))
count_pr = random.randint(1,count_w)
len_pr = [0 for i in range(count_pr)]

ind = random.randint(0,count_pr-1)
ind_exept.append(ind)

while count_w > 0 and len(ind_exept) != count_pr:
    len_pr[ind] += random.randint(0,count_w)
    count_w -= len_pr[ind]

    while ind in ind_exept:
        ind = random.randint(0,count_pr-1)

    ind_exept.append(ind)
    if len(ind_exept) == count_pr:
        ind_exept =[]

for i in range(count_pr):
    for k in range(len_pr[i]):
        len_w = random.randint(0,20)
        
        for j in range (len_w):
            shift = random.randint(0,25)
            text += chr(ord('a') + shift)
        text += ' '
    text += '\n'    

with open ('input.txt', 'w') as file_input :
    file_input.write(text)

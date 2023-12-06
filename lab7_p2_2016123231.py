import re

#read text file
f = open("input_7_2.txt", 'r')
text = f.read()

#get all alphabets in text
alphabet_re = re.compile("[a-zA-Z]")
alphabets = alphabet_re.findall(text)
##alphabets = ['a','a','b','c']

#change all alphabets to upper case
alphabets = [x.upper() for x in alphabets]


#count all alphabets
dic = {}
for alphabet in alphabets:
    if alphabet in dic.keys():
        num = dic[alphabet]
        dic[alphabet] = num+1
    else:
        dic[alphabet] = 1

#sort dictionary
sorted_alphabets = list(dic.items())
sorted_alphabets.sort(reverse=True, key=lambda tup: tup[1])

result = []
for alphabet in sorted_alphabets:
    result.append(alphabet[0])

print(result)

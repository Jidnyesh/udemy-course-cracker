import itertools as it
char_list = input('Enter the list of characters or numbers with which you want to make the brute force\n\
(Make sure they are all capital)  For ex. QWERTYUIOPASDFGHJKLZXCVBNM\n')
length = int(input('Enter the length of list you want to create\n'))
a = list(it.permutations(set(char_list),length))
final = []
for i in range(len(a)):
    o = ''.join(a[i])
    final.append(o)
with open('wordlist.txt','w') as w:
    for x in final:
        w.write(x+'\n')
    w.close()
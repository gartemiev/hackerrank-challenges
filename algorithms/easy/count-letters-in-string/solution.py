######Collections approach
from collections import Counter

inp = str(input()).lower()

countLetters = Counter()

for el in inp:
    if el.isalpha():
        countLetters[el]+=1

print(countLetters)

######Regexp approach
import re

uniq=set(inp)
for el in uniq:
    if el.isalpha():
        print(el, len(re.findall(el,inp)))

######Native dictionary approach
print({el: inp.count(el) for el in inp if el.isalpha()})

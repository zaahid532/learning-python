import re 
text1 = 'the quick brown fox'
text2 = 'jump over 12 lazy dogs!!'
x = re.sub(r'\s', '_', text1)
print(x)
y = re.sub(r'\s', '_', text2)
print(y)
phrase = str(input("Enter a Phrase: "))
text = phrase.split()
a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)
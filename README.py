# acronyms
# This program creates acronyms for any given words.

user_input = str(input("Type your phrase here: "))
text = user_input.split()
c = " "

for i in text:
  c = c + str(i[0]).upper()
print(c)

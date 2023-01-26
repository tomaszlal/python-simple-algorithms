vowels = "aeiou"
consonants = "bcdfghjklmnpqrstwvxyz"

list_poem = []
lines = int(input("How many lines do you want: "))
print(lines)
for i in range(0, lines):
    list_poem.append(input())

vowels_in_line = [0 for i in range(lines)]
vowels_in_poem = 0
consonants_in_line =[0 for i in range(lines)]
consonants_in_poem = 0

for i in range(0, len(list_poem)):
    for letter in vowels:
        for word in list_poem[i]:
            if letter in word:
                vowels_in_line[i] +=1
                vowels_in_poem+=1
    for letter in consonants:
        for word in list_poem[i]:
            if letter in word:
                consonants_in_line[i] +=1
                consonants_in_poem +=1
                
            

print(vowels_in_line)
print(vowels_in_poem)
print(consonants_in_line)
print(consonants_in_poem)
print(list_poem)

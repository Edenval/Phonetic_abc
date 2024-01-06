
import pandas
with open("nato_phonetic_alphabet.csv") as file:
    contents = pandas.read_csv("nato_phonetic_alphabet.csv")

contents_letter = contents["letter"].to_list()
contents_code = contents["code"].to_list()


kaka = 0
newnato = {}
for i in contents_letter:
    newnato[i] = contents_code[kaka]
    kaka += 1

#print(newnato)
last = []
inp = input("Enter a word: ").upper()
for character in inp:
    last.append(newnato[character])
print(last)


#Loop through rows of a data frame
# for (index, row) in contents.iterrows():
#     print(row.code)
# last = {row.letter:row.code for (index, row) in contents.iterrows()}
# print(last)
import markovify
import pickle


print('number of headlines to generate: ')
userI = int(input())

with open("mylist", "rb") as input_file:
    lst = pickle.load(input_file)

text_model = markovify.NewlineText(lst, state_size = 2)

for i in range(userI):
    print(text_model.make_sentence())
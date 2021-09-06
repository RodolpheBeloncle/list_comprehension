import pandas

# LIST COMPREHENSION FOR LIST:
def_range = [number * 2 for number in range(1,5)]
print(def_range)

# sorting a list by number of characters
names =["Alex","Beth","Caroline","Dave","Eleonor","Freddy"]

sorted_list = [shortname for shortname in names if len(shortname) < 5 ]
print(sorted_list)

# sorting and change characters size:

sorted_list_toUpper = [longName.upper() for longName in names if len(longName) > 5 ]
print(sorted_list_toUpper)

# Exercice 1 : (pow(2) list
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆
#Write your 1 line code 👇 below:
squared_numbers = [squareN**2 for squareN in numbers]
#Write your code 👆 above:
print(squared_numbers)


# Exercice 2: (even numb list)
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:
result = [ n for n in numbers if n%2 == 0]
#Write your code 👆 above:
print(result)

# Exercice 3: check common number with converting data series

# Get data from each files and convert string value without space:

#f1 = open("file1.txt")
#data_list1 = []
#for line in f1:
    #data_list1.append(int(line.strip('\n')))

#f2 = open("file2.txt")
#data_list2 = []
#for line in f2:
    #data_list2.append(int(line.strip('\n')))

# compare those two lists if common value

#result = [x for x in data_list1 if x in data_list2]

# SHORTER WAY:
# result = [int(num) for num in file_1_data if num in file_2_data]
#print(result)

# DICT COMPREHENSION FOR DICTIONARY:
import random
# new_dict = {new_key:new_value for (key,value) in dict.items()}

# Generate dictionary from a list to add a score for each name in names_list
names_list =["Alex","Beth","Caroline","Dave","Eleonor","Freddy"]
students_scores = {student:random.randint(1,100) for student in names_list}

print(students_scores)

# Create a dictionary from passed_students over a certain score(key:value) are inseparable(item())
passed_students = { key : score for (key,score) in students_scores.items() if score >= 60 }

print(passed_students)

# Dictionary Exercise 1:
# build dictionary from string list with key:len(key)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# set sentence into a splitter/word list:

nb_letters = sentence.split()

# count each value in this list :

count_letter_list = [len(value) for value in nb_letters]

print(count_letter_list)

# blend both list

zip_two_lists = zip(nb_letters, count_letter_list)

# create a dictionary from this zipped list:

key_value_dict1 = dict(zip_two_lists)
print(key_value_dict1)

# SHORTER METHOD:
key_value_dict2 = {word : len(word) for word in sentence.split()}
print(key_value_dict2)
#----------------------
# Dictionary Exercise 2:
#Converrt Dictionary t° => dictionary Celsius
# NB : T° => Celsius :   (temp *9/5) + 32

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

def convert(t):
  celsius = t *9/5 + 32
  return celsius


weather_f = {key:convert(value) for key,value in weather_c.items()}
print(weather_f)

# Dictionary Exercise 3:
# Use shoortend loop with panda dictionary dataframe:

#student_dict = {
    #"student": ["Angela", "James", "Lily"],
    #"score": [56, 76, 98]
#}

#Looping through dictionaries:
#for (key, value) in student_dict.items():
    #Access key and value
    #pass

#student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
#for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    #pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

import csv

mydict = {}

# Read file:

with open("nato_phonetic_alphabet.csv") as file:
    reader = csv.reader(file)

# Create Dictionary straight from the file:

    dict_from_csv = {rows[0]: rows[1] for rows in reader}
dict_from_csv.pop("letter")
print(dict_from_csv)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# Ask the word to spell
user_input = input("word_to_spell : ")

# Set the the word in a array:

splited_input = user_input.split()
print(splited_input)

# get each key letter from this word:

to_spell = []
for letters in splited_input:
    for letter in letters:
        to_spell.append(letter.upper())
print(to_spell)

# Associate those letters to each key:value from the dictionary :

nato_spell_list = []
for letter in to_spell:
    nato_spell_list.append(dict_from_csv[letter])
print(nato_spell_list)


# SHORTER METHOD :
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)

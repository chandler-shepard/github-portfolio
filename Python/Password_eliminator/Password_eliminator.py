# Make sure you have passwords.txt and Password_eliminator.py are downloaded
# and in the same location. 


#using list comprehension
#open the file and put all possible passwords into a list

passwords = [line.strip() for line in open("passwords.txt","r")]
print(passwords)


# define a function that takes a list and prints it out with 5 passwords in each line
# define possible_pass
def possible_pass(passwords):
    count = 0
    # go through each item while checking how many you have gone through
    # once you have printed out 5 go to a new line
    for i in range(len(passwords)):
        print(passwords[i:6])
        

# Main


#print the clue and the dashed lines
print("Clue 1: The password is at least 6 characters long.")
print()
print("The current possible passwords are:")
print("-"*30)
print("After clue 1, these passwords remain.")

# go through eaxh word in th efile contents and check if word length is
# greater than 6
clue1 = [word for word in passwords if len(word) >= 6]
print(clue1)
print()

# print clue 2 question and format
print("Clue 2: The password contains at least 1 letter.")
print("-"*30)
print("After clue 2, these passwords remain.")

# go through each word and each letter
clue2 = [word  for word in clue1 if word.isalpha()]
print(clue2)
print()
print("Clue 3: The password starts with a consonant and the third letter is a vowel.")
print("-"*30)
print("After clue 3, these passwords remain.")

# go through each word
# first check if first letter is a constanant
# then check if third letter is a vowel
clue3p1 = [word for word in clue2 if word[0] not in "aeiou"]
clue3 = [word for word in clue3p1 if word[2] in "aeiou"]
print(clue3)
print()

# print clue 4 and format
print("Clue 4: The password has no more than half as many vowels as it does consonants.")
print("-"*30)
print("After clue 4, these passwords remain.")


# go through the list of passwords
# for each word check how many vowels are in it
# if there are no more than half as many constonants then return the word

clue4 = []
for word in clue3:
    vowel_count = 0
    con_count = 0
    for i in range(len(word)):
        if word[i] in "aeiou":
            vowel_count += 1
        else:
            con_count += 1
    if con_count/2 >= vowel_count:
        clue4.append(word)
    
print(clue4)


        







    

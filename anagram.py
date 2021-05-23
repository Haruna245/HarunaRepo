
s1 = input("please enter a word: ")         # requires user input a number
s2 = input("please enter a word: ")         # requires user input a number

a = sorted(s1.lower())                      # converting the strings to lower case
b = sorted(s2.lower())                      # converting the strings to lower case

if a == b:
    print("they are anagram")               #executes if the statement is true
else:
    print("they are not anagram")           #execute if the statement is false
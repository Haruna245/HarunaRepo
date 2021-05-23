from array import *
total_student = int(input("total number of students: "))
num_lang = []
name_lang = []

sum_lang = 0

for i in range(total_student):
   x = int(input(f"numbers of languages spoken by student {i+1}: "))
   num_lang.append(x)
   if x ==1:
       y = input("names of languages: ")
       name_lang.append(y)
   else:
       for e in range(x):
           y = input(f"names of languages of student{i+1}: ")
           name_lang.append(y)
   sum_lang +=num_lang[i]
   print("next student")

print("total languages spoken by the students are = ",sum_lang)

for a in range(len(name_lang)):
    print(name_lang[a])





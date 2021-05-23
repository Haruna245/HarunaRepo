
ent_str = input("enter a word: ")    # requires user input


def str_pal(ent_str, empty_str=""):               #function to check  if the word is palindrome
        for i in range(len(ent_str)):
            empty_str += ent_str[-1-i]            #storing the reverse of the word in empty_str

        if ent_str == empty_str:
            print("The word is a palindromic word")
        else:
            print("The word is not a palindromic word")


cal_func = str_pal(ent_str)     #cal_func is calling the function


# With this i call files in the folder
filename_1 = 'preguntas'
filename_2 = 'respuestas'

# This flag will mantain the while loop infinite until False
flag = True

# With this i open the file and create lists with each line in file.
with open(filename_1, 'r') as f_obj:
    contents = f_obj.readlines()
print(contents) # this was used as a test, it is deletable
# Same as before but with answers
with open(filename_2, 'r') as f_obj2:
    contents2 = f_obj2.readlines()
print(contents2) # so this one

while flag:
    # c is a counter, it will be used to get the index of each set of Questions
    # and Answers
    c = 0
    # With the for loop i try to print the first question using c = 0 and then
    # it will add 1 to get the 2nd and so on.
    for i in contents:
        print(contents[c])
        
    # I need to create a for loop that can help me showing 3 first sets of answers, i can use a range for loop that starts on c = 0 and finishes on 
    # c + 3, try to think an answer, there will be a problem when you try to sum
    # the starting range, because c = c + 1, and the starting range will always # be 1

    c += 1
# With this i call files in the folder.
filename_1 = 'preguntas'
filename_2 = 'opciones'
filename_3 = 'correctas'
# c is a counter, it will be used to get the index of each set of Questions
# and correct answers. d is a counter that shows the options you have. 
# f is a counter that will count how many times the while loop it's been running
# the loop needs to run as many times as questions there are. 
c, d, f, points = 0, 0, 0, 0

# With this i open the file and create lists with each line in file.
with open(filename_1, 'r') as f_obj:
    contents = f_obj.readlines()

# Same as before but with options.
with open(filename_2, 'r') as f_obj2:
    contents2 = f_obj2.readlines()

# Same as before but with correct answers.
with open(filename_3, 'r') as f_obj3:
    contents3 = f_obj3.readlines()

# An input just to check if you want to exit or continue.
start = input("Inserta 'q' para salir, enter para continuar:\n")

# e is total of questions.
e = len(contents)

# As explained before, the loop needs to work as many times as questions there
# are, so, f(times the loops has runned) needs to be less than e(total of Q's)
while f < e:
    f += 1 
    if start == 'q':
        break

    else:
        # I don't need a loop to show Qs since i'll be showing them one at a 
        # time, so when i add the counter, next time while loop will start with 
        # c = 1 and so on
        print(contents[c].rstrip())
        
        # This loop is used to show each set of answers stored, they'll be 
        # showing in sets of 3. 
        for j in range(d, d + 3):
            print(contents2[j])

        d += 3
        # input written selection
        selection = input("Por favor, escribe la respuesta correcta: \n")
        # contents3 index will be the same as Q's, since there are as many Q's
        # as correct answers (A correct ans for each Q)
        if selection.lower() == contents3[c].rstrip():
            points += 1
        else:
            points += 0
    # Since contents3 uses c as index, i need to add1 for the next run
    c += 1

print("Tu total de puntos es: ", points)
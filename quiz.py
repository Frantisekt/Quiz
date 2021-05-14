# With this i call files in the folder
filename_1 = 'preguntas'
filename_2 = 'respuestas'
filename_3 = 'correctas'
# c is a counter, it will be used to get the index of each set of Questions
# and d will help to get Answers
c = 0
d = 0
e = 0
f = 0
points = 0

# With this i open the file and create lists with each line in file.
with open(filename_1, 'r') as f_obj:
    contents = f_obj.readlines()

# Same as before but with answers
with open(filename_2, 'r') as f_obj2:
    contents2 = f_obj2.readlines()

# Same as before but with corrects
with open(filename_3, 'r') as f_obj3:
    contents3 = f_obj3.readlines()

start = input("Inserta 'q' para salir, enter para continuar:\n")

e = len(contents)

while f < e:
    f += 1 
    if start == 'q':
        break

    else:
        # I don't need a loop to show Qs since i'll be showing them one at a time,
        # so when i add the counter, next time while loop will start with c = 1 and # so on
        print(contents[c].rstrip())
        # I need to create a for loop that can help me showing 3 first sets of answers, i can use a range for loop that starts on c = 0 and finishes on 
        # d + 3, try to think an answer, there will be a problem when you try to sum
        # the starting range, because c = c + 1, and the starting range will always # be 1
        for j in range(d, d + 3):
            print(contents2[j])

        d += 3

        selection = input("Por favor, escribe la respuesta correcta: \n")

        if selection.lower() == contents3[c].rstrip():
            points += 1
        else:
            points += 0
    c += 1

print("Tu total de puntos es: ", points)
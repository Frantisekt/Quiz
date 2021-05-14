# THIS IS A PROGRAM TO CONSTRUCT A  SIMPLE SELECTION QUIZ

filename1 = 'preguntas.txt' # VARIABLE FOR THE QUESTIONS FILE.
filename2 = 'respuestas.txt'  # VARIABLE FOR THE ANSWER FILE.


flag = True
def leer_pregunta():  # FUNCTION TO READ THE QUESTION IN THE QUESTION FILE.
    with open(filename1, 'r') as f_obj1:  
        preguntas = f_obj1.readlines()
        for i in preguntas:
            print(i)

def leer_respuesta():  # FUNCTION TO READ THE ANSWERS IN THE ANSWERS FILE.
    with open(filename2, 'r') as f_obj2:
        respuestas = f_obj2.readlines()
        for j in range(len(respuestas)):
            print(respuestas[j])

leer_pregunta()
leer_respuesta()




while flag:
    

    flag = False










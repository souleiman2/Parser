import math


def basiccalcul(operateur1, operateur2, operation):#"comprend" la signification des operateurs
    if operation == "^":
        return operateur1**operateur2
    elif operation == "*":
        return operateur1*operateur2
    elif operation == "/":
        return operateur1/operateur2
    elif operation == "+":
        return operateur1+operateur2
    elif operation == "-":
        return operateur1-operateur2

#"comprend" la signification de sin, etc (trig things)
def trigcalcul(nombre, operation):
    pi=3.14159265358979323846264338327950288419716939937510
    if operation =="sin":
        return math.sin(nombre*pi/180)
    elif operation == "cos":
        return math.cos(nombre*pi/180)
    elif operation == "tan":
        return math.tan(nombre*pi/180)


def transformateur(equation, operateur):
    #transformer les opérateurs en index de la varible tout_operateur
    tout_operateur = []
    x = 0
    terminer = False
    succession = False
    while equation != "" :
        if len(equation)== x+1:
            tout_operateur.append(equation)
            return tout_operateur
            
        else:
            if equation[x] in operateur:
                tout_operateur.append(equation[x])
                equation = equation[1:len(equation)]
                x=-1
            else:
                succession = False
                if equation[x+1] in operateur:
                    tout_operateur.append(equation[0:x+1])
                    equation = equation[x+1:len(equation)]
                    x=-1
                
        x+=1

def résoudresimple(equation, operation):
    #avec les valeurs réduit à un index de la variable tout operateur px faire les opérations sans se casser la tête
    tout_operateur = transformateur(equation, operation)
    x = 0
    resultat = 0.0
    meme_temps = []
    meme_temps_compteur = 0
    while x != len(operation):
        y = 0
        
        if x == 1 or x == 2:
            meme_temps = [1,2]
        elif x == 3 or x == 4:
            meme_temps = [3,4]
        else:
            meme_temps = [x]

        while y != len(tout_operateur):
            meme_temps_compteur = 0
            while meme_temps_compteur != len(meme_temps):
                if tout_operateur[y] == operation[meme_temps[meme_temps_compteur]]:
                    
                    resultat = basiccalcul(float(tout_operateur[y-1]), float(tout_operateur[y+1]), tout_operateur[y])
                    equation = equation.replace(tout_operateur[y-1] + tout_operateur[y] + tout_operateur[y+1], str(resultat))
                    
                    tout_operateur.pop(y+1)
                    tout_operateur[y] = str(resultat)
                    tout_operateur.pop(y-1)
                        
                    
                    y = -1
                meme_temps_compteur +=1
            y+=1
                
        
        x+=1

    
    return float(equation)




def recursiveshit(equation, variable, valeur_variable, parenthese, pos_parenthese,operation,trig):#fait tout le shit basically d'ou le nom recursiveshit
    if len(pos_parenthese) == 2:
        start = 0
        end = len(equation)
        
        resultat = résoudresimple(equation[start:end], operation)
        equation = str(resultat)
        
        
        
        return equation
    else:
        x = 0
        fini = False
        while not fini:
            if "true" in pos_parenthese[x]:
                fini = True
            x +=1
    
        start = int(pos_parenthese[x-2][4:])+1
        end = int(pos_parenthese[x-1][4:])

        resultat = résoudresimple(equation[start:end], operation)

        if start >=4:
            trig_compteur = 0
            while trig_compteur != len(trig):
                if equation[start-4:start-1] == trig[trig_compteur]:
                    resultat = trigcalcul(resultat, trig[trig_compteur])
                    equation = equation[:start-4] + str(resultat) + equation[end+1:]
                    trig_compteur = len(trig)-1
                else:
                    equation = equation[:start-1]+ str(resultat) + equation[end+1:]

                trig_compteur += 1
        else:
            equation = equation[:start-1]+ str(resultat) + equation[end+1:]

        


        pos_parenthese = ["trol"]
        x = 0
        compteur_trig = 0
        while x != len(equation):#determiner les variables dans equation
            if equation[x] in parenthese:
                if equation[x] == parenthese[0]:
                    pos_parenthese.append("trol" + str(x))
                else:
                    pos_parenthese.append("true" + str(x))
            elif equation[x] not in nombre and equation[x] not in operation and equation[x] not in autre:
                is_trig = False
                if x <= len(equation)-6:
                    trig = ["cos","sin","tan"]
                    y = 0
                    while y != len(trig) and not is_trig:
                        z = 0
                        compteur=""
                        while z != len(trig[y]):
                            compteur += equation[x+z]
                            z += 1
                        if compteur == trig[y]:
                            compteur_trig +=1
                            x = x + len(trig[y]) - 1
                            is_trig = True
                        y+=1
                if not is_trig:
                    variable.append(equation[x])
            x += 1 
        pos_parenthese.append("true")
        
     
    return recursiveshit(equation, variable, valeur_variable, parenthese, pos_parenthese, operation, trig)

    






while True:
    print("Pour le bon fonctionnement de ce programme veuillez ne pas mettre de variable et de fonction trigonometrique ayant les memes lettres")
    equation = input("Veuillez entrer une équation à résoudre : ")
    nombre = []
    for x in range(10):
        nombre.append(str(x))
    operation = ["^","*","/","+","-"]
    parenthese = ["(",")"]
    autre = [".",","]
    pos_parenthese = ["trol"]
    variable = []#array qui contient le nom des variables 
    x = 0#compteur tout usage
    compteur_trig = 0
    trig = []
    while x != len(equation):#determiner les variables dans equation
        if equation[x] in parenthese:
            if equation[x] == parenthese[0]:
                pos_parenthese.append("trol" + str(x))
            else:
                pos_parenthese.append("true" + str(x))
        elif equation[x] not in nombre and equation[x] not in operation and equation[x] not in autre:
            is_trig = False
            if x <= len(equation)-6:
                trig = ["cos","sin","tan"]
                y = 0
                while y != len(trig) and not is_trig:
                    z = 0
                    compteur=""
                    while z != len(trig[y]):
                        compteur += equation[x+z]
                        z += 1
                    if compteur == trig[y]:
                        compteur_trig +=1
                        x = x + len(trig[y]) - 1
                        is_trig = True
                    y+=1
            if not is_trig:
                variable.append(equation[x])
        x += 1 
    pos_parenthese.append("true")
    x=0#verifie quil y a bien assez de parenthese ( que ceux-la )
    compttrol = 0
    compttrue = 0
    while x != len(pos_parenthese):
        if "trol" in pos_parenthese[x]:
            compttrol +=1
        else:
            compttrue +=1
        x +=1
    if compttrol != compttrue:
        print("Euh dsl mais ta pas bien mis tes parenthèses. I can't let you do this bro.")
        assert False
    x = 0#demande la valeur des variables et la met en memoire 
    valeur_variable = []#indique la valeur des variables entrer
    while x != len(variable) :
        fini = False
        while not fini :
            reponse = input("Quel est la valeur de la variable " + variable[x] + " : ")
            fini = True
            y=0
            replace = str(reponse)
            while y < len(reponse):
                if replace[y] not in nombre:
                    fini=False
                    print("Veuillez mettre des valeurs numerique plz")
                y += 1
        valeur_variable.append(reponse)
        x +=1


    x = 0
        
    while x != len(variable):
        if len(valeur_variable[x]) >= 1 :
                lol = equation.replace(variable[x], valeur_variable[x])
                equation = lol
        else:
            print("Vous n'avez pas mis de valeur a cette variable")
        x +=1
        


      
    final_reponse = recursiveshit(equation, variable, valeur_variable, parenthese, pos_parenthese, operation, trig)
    print("\nla reponse est : " + final_reponse +"\n\n")





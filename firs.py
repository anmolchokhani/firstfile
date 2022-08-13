"""
log or retrieve

kiska log karna hai

kya exerise or food


"""

def getdate():
    import datetime
    return datetime.datetime.now()



what= int(input("for log enter 1, for retrieve enter 2"))
whom = int(input("for harry -1, rohan - 2, hammad-3"))
kya = int(input("exercise - 1, food -2"))


# open(Harryfood.txt)
# open(Rohanfood.txt)
# open(Hammadfood.txt)


# open(RohanExercise.txt)
# open(HammadExercise.txt)



if what == 1:
    if whom == 1:
        if kya == 1:
            exer = input("enter what exercise you did")
            f = open("HarryExercise.txt","a")
            f.write(exer + "\n")
            print("sucessfully written")
            f.close()
        else:
            food = input("enter the food")
            f = open("Harryfood.txt","a")
            f.write(str(getdate())+ " : " + food + "\n")
            print("sucessfully written")
            f.close()
    elif whom == 2:
        if kya == 1:
            exer = input("enter what exercise you did")
            f = open("RohanExercise.txt","a")
            f.write(exer + "\n")
            print("sucessfully written")
            f.close()
        else:
            food = input("enter the food")
            f = open("Rohanfood.txt","a")
            f.write(str(getdate())+ " : " + food + "\n")
            print("sucessfully written")
            f.close()
    else:
        if kya == 1:
            exer = input("enter what exercise you did")
            f = open("HammadExercise.txt","a")
            f.write(exer + "\n")
            print("sucessfully written")
            f.close()
        else:
            food = input("enter the food")
            f = open("Hammadfood.txt","a")
            f.write(str(getdate())+ " : " + food + "\n")
            print("sucessfully written")
            f.close()


else:
    if whom == 1:
        if kya ==1:
            f = open("HarryExercise.txt")
            print(f.read())
            f.close()
        else:
            f = open("Harryfood.txt")
            print(f.read())
            f.close()
    elif whom == 2:
        if kya ==1:
            f = open("RohanExercisetxt")
            print(f.read())
            f.close()
        else:
            f = open("Rohanfood.txt")
            print(f.read())
            f.close()
    else:
        if kya ==1:
            f = open("HammadExercise.txt")
            print(f.read())
            f.close()
        else:
            f = open("Hammadfood.txt")
            print(f.read())
            f.close()
                                    
            
            



 




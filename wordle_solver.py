"""color = "gyw"
def gen_possibilities():
    f=open("possibilities.txt","a")
    for i1 in color:
        for i2 in color:
            for i3 in color:
                for i4 in color:
                    for i5 in color:
                        cuv=i1+i2+i3+i4+i5
                        f.write(cuv)
                        f.write("\n")
    f.close()"""
"""gen_possibilities()"""


total = 11454
import math

f = open("new_list.txt", "r")
L = f.readlines()
f.close()
L2=L[::]


def entropy(word):

    pos = open("possibilities.txt", "r")

    entropy = 0
    comb = pos.readline()
    while comb != "":
        c = 0

        for cuv2 in L:
            for i in range(5):
                if comb[i] == 'w' and word[i] in cuv2:
                    break
                if comb[i] == 'g' and word[i] != cuv2[i]:
                    break
                if comb[i] == 'y' and word[i] not in cuv2:
                    break
                if comb[i] == 'y' and word[i] == cuv2[i]:
                    break
            else:
                c += 1
        f.close()
        prob = c / total
        if prob:
            entropy += prob * math.log(prob, 2)

        comb = pos.readline()

    pos.close()
    return -entropy


def tester(word):
    f = open("cuvant_ales.txt", "r")
    ales = f.readline()
    ales = ales.strip()
    feedback = ""
    for i in range(5):
        if word[i] == ales[i]:
            feedback += 'g'
        elif word[i] in ales:
            feedback += 'y'
        elif word[i] not in ales:
            feedback += 'w'
    f.close()
    return feedback


def max_entropy():
    maxE = 0.0
    cuvMax = ""
    for word in L:
        E = float(entropy(word))
        if E > maxE:
           maxE = E
           cuvMax = word
    return cuvMax


def solver():

    com = open("communication.txt", "r+")
    sol = open("solutii.txt","a+")
    input("press enter")
    Fword = com.readline()
    rep = com.readline()
    if rep == "ggggg":
        sol.write(Fword)
        com.close()
        print("CONGRATS!")
        com=open("communication.txt","w")
        com.write("")
        com.close()
        return 0


    L1 = L[::]
    for x in L1:
        for i in range(5):
            if rep[i] == 'w' and Fword[i] in x:
                L.remove(x)
                break
            if rep[i] == 'g' and Fword[i] != x[i]:
                L.remove(x)
                break
            if rep[i] == 'y' and Fword[i] not in x:
                L.remove(x)
                break
            if rep[i] == 'y' and Fword[i] == x[i]:
                L.remove(x)
                break
    Fword = max_entropy()
    com.close()
    com=open("communication.txt", "w")
    com.write(Fword)
    print(Fword)
    with open('new_list.txt', 'w') as f:
        for line in L:
            f.write(line)
    com.close()


solver()
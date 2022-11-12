import random
f=open("cuvinte_wordle.txt", "r")
g=open("cuvant_ales.txt", "w")
l=f.readlines()
g.write(random.choice(l))
f.close()
g.close()

with open('new_list.txt', 'w') as f:
    for line in l:
        f.write(line)


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


import runpy

f=open("communication.txt","w+")
f.write("TAREI"+"\n")
print("TAREI")
f.write(tester("TAREI")+"\n")
f.close()
runpy.run_path(path_name='wordle_solver.py')

def wordle():
    com=open("communication.txt","r+")
    c=com.readline()
    if c=="":
        return 0
    com.write(tester(c))
    com.close()
    runpy.run_path(path_name='wordle_solver.py')
    wordle()

wordle()

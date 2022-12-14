ad = ['START', 'END']
IS = ['ADD', 'MOVER', 'SUB', 'MOVEM', 'MULT', 'PRINT', 'DC', 'DS']
DL = ['DS', 'DC']
SYMB = ['NEXT', 'LOOP', 'LOAD']
reg = ['AREG', 'BREG', 'CREG', 'DREG']
lc=100

sym_dict = {}
lit_dict = {}


def is_symbol(x):  # function to scan all the symbol in symb list
    for i in x:
        if (i in SYMB):
            sym_dict[i] = (-1)  # if present add to sym_dict and intialise address to -1


def is_literal(x):  # function to scan all the literals present in the code and storing in li_dict dictonary
    for i in x:
        if (i[0] == "="):
            lit_dict[i] = (-1)


def inc_lc(x):  # function to intialise and increment location counter
    global lc

    if (x[0] == ad[0]):  # check if first char in the line (x[0])== to start (ad[0])
        lc = int(x[1])  # intialise lc to constant given else 0
        print("location_counter", lc)

    i = x[0];  # initialising i variable to first elment in the line

    if (i in IS):  # check if it is a imperative statemen
        lc = lc + 1  # increment location counter

    for i in x:  # code to check for ds or dl i.e symbols other than in symb list
        if (i in sym_dict):  # to handle load and next (in symb list)
            sym_dict[i] = lc  # update the address
            lc = lc + 1
        if ((i == "DC") or (i == "DS")):
            if (i == "DS"):
                id = x.index(i)
                lc = lc + (int(x[id + 1])) - 1
                sym_dict[x[id - 1]] = lc
                lc = lc + 1
            else:
                id = x.index(i)
                sym_dict[x[id - 1]] = lc
                lc = lc + 1
    if (i == ad[1]):
        for i in lit_dict:
            lit_dict[i] = lc
            lc = lc + 1


def gen_lit_table(lit_dict):  # function to generate lit table
    with open('lit.txt', 'w') as f2:
        f2.write("\tLiteral Table\n")
        f2.write("Name   Address\n")
        for i in lit_dict:
            f2.write(i + "    ")
            f2.write(str(lit_dict[i]) + "\n")


def sym_gen():  # function to generate symbol table
    with open('sym.txt', 'w') as f1:
        f1.write("\tSymbol Table \n")
        f1.write("Name   Address\n")
        for i in sym_dict:
            f1.write(i + "    ")
            f1.write(str(sym_dict[i]) + "\n")


def gen_interm_code(x):  # code to generate intermediate code

    for i in x:
        if (i in ad):
            if (x[0] == ad[0]):
                f3.write("AD 1 " + " C " + x[1])
            else:
                f3.write("AD 02 ")
        if (i in IS):
            if (i == 'DS') or (i == 'DC'):
                f3.write("DL " + str(DL.index(i)) + " C " + x[x.index(i) + 1])
            else:
                f3.write("IS " + str(IS.index(i) + 1) + " ")

        if (i in lit_dict):
            f3.write(" L " + str(list(lit_dict).index(i) + 1) + " ")
        if ((i in sym_dict)):
            f3.write(i + " ")
        if ((i in reg)):
            f3.write(" " + i + "")


# execution starts from here
file1 = open("input.asm", 'r')  # reading the input file
lines = file1.readlines()  # scanning the input file line by line
f3 = open("inter.txt", 'a')
for line in lines:

    x = line.split()  # splitting each line into tokens
    if (len(x) > 0):
        is_symbol(x)
        is_literal(x)
        inc_lc(x)
gen_lit_table(lit_dict)
sym_gen()

f3.write("\tINTERMEDIATE CODE" + "\n")  # code to write intermediate code

for line in lines:
    x = line.split()
    if (len(x) > 0):
        gen_interm_code(x)
        f3.write("\n")

print("Symbol Table :- ", sym_dict)
print("Literal Table :- ", lit_dict)

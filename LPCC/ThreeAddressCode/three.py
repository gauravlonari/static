# precedence list
precedence = {'^':0,'/':1 ,'*':1 ,'+' :2 ,'-' :2}

def precedenceof(s):
    return precedence[s]

exp = input("Please enter a simple expression: ")
l = len(exp)
processed = [False ] *l
operators = []

for i in range(l):
    x=exp[i]
    if x in precedence.keys():
        operators.append([precedenceof(x),i,exp[i]])

operators.sort()

print(operators)

for i in range(len(operators)):
    op="t"+str(i+1)+" ="
    j=operators[i][1]
    op1=exp[j-1]
    op2=exp[j+1]
    if processed[j-1]:
        if operators[i - 1][0] == operators[i][0]:
            op1 = f"t{i}"
        else:
            for x in range(len(operators)):
                if j-2 == operators[x][1]:
                    op1=f"t{x+1}"
    if processed[j+1]:
        for x in range (len(operators)):
            if j+2 == operators[x][1]:
                op2=f"t{x+1}"
    processed[j],processed[j+1],processed[j-1]=[True]*3
    print(op,op1,exp[j],op2)
    




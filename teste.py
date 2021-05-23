
def soma(n1,n2):
    n3 = n1 + n2
    return n3 


def subtracao(n1,n2):
    n3 = n1 - n2
    return n3

n1 = float(input("Digite  o número 1 : \n"))
n2 = float(input("Digite  o número 2 : \n"))

resp = soma(n1,n2)
resp1 = subtracao(n1,n2)

print (resp)
print (resp1)

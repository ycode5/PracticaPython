from functools import reduce

numeros=[2,3,5,6,8,9,11]

resultado=list(filter(lambda n: n % 2,numeros))
sum=reduce(lambda a,b: a+ b,resultado)
print(resultado)
print(sum)


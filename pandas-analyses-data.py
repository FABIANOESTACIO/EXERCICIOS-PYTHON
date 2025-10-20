
#Exemplos de listas, tulipas, conjuntos, operadores.
#Uma lista é uma coleção ordenada e mutável
numeros=[1,2,3]
letras=['a','b','c']
mistura=[1.0,'a',True]
print("lista de numeros:",numeros)


numeros.append(4)
numeros[0]=99
print("lista alterada:", numeros)

#    tupla 
#tupla é uma coleção ordenada e imutável
tupla=("what","who","where")
print("tupla:",tupla)

#Um set é uma coleção não ordenada e não permite itens duplicados
frutas=set(['batata','alface','uva','uva'])
print("set sem duplicados:",frutas)
frutas.add("banana")
print("set apos add:",frutas)
#     frozen set 
conjunto =frozenset(['batata','alface','uva'])
print("frozenset:",conjunto)

#   operações entre sets  
a={1,2,3}
b={3,4,5}
print('\n União de a com b:',a|b)
print("interseção:",a&b)
print("diferença:",a-b)

# Operadores
x, y=10,5
print:x==y, x!=y, x>y, x<y, x>=y, x<=y

# Operadores lógicos (booleanos)
p, q = true, False
print("\np AND q:",p and q)
print("p OR q:"p or q)
print("NOT p:",not p)

#Operadores aritmétricos
print:(5+2,5-2,5*2,5|2,5||2,5%2,5**2)
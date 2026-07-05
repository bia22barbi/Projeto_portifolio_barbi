import math 



Declaração de variáveis em Python       pep e uma normal do python para sixtase e identação 


declararação via implicita dinamica 


nome = "Alice" 
print(nome)




declararação via Type Hinting  type pep 484 
nome: str = "Alice"
print(f"nome: {nome}")


Cpf: str = "123.456.789-00"
print(f"CPF: {Cpf}")

cnpj: str = "12.345.678/0001-00"
print(f"CNPJ: {cnpj}")


henry: str = "Henry"
print(f"nome: {henry}")



 Declaração por Casting
 
 
 
 nome = str(123)
print(f"nome: {nome}")
print(f"henry: {henry}")







print ("Fim do programa")




tipos de dadosem python 


str = string: caracteres/textos 
int - inteiro: numeros inteiros 1,70 = 170 
float - ponto flutuante: numeros decimais  1,334444  ate 64 casas decimais 7 
bool - booleano: verdadeiro ou falso True or False
none - nulo: ausencia de valor  None oq e ser nulo nulo e diferente de zero 0 >= 0 ou <= 0 nulo e diferente de vazio ""  nulo e diferente de false False  nulo e diferente de zero 0  nulo e diferente de None None  nulo e diferente de vazio []  nulo e diferente de vazio {}  nulo e diferente de vazio ()  nulo e diferente de vazio set()  nulo e diferente de vazio frozenset()  nulo e diferente de vazio bytearray()  nulo e diferente de vazio bytes()  nulo e diferente de vazio memoryview()  nulo e diferente de vazio range()  nulo e diferente de vazio slice()  nulo e diferente de vazio complex()  nulo e diferente de vazio decimal.Decimal()  nulo e diferente de vazio fractions.Fraction()  nulo e diferente de vazio datetime.datetime()  nulo e diferente de vazio datetime.date()  nulo e diferente de vazio datetime.time()  nulo e diferente de vazio datetime.timedelta()  nulo e diferente de vazio datetime.tzinfo()  nulo e diferente de vazio datetime.timezone()


oq e pep  ele basicamente e um conjunto de normas e convenções para escrever codigo python de forma padronizada e legivel para todos os programadores que utilizam a linguagem python. PEP significa Python Enhancement Proposal (Proposta de Aprimoramento do Python).




nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")



cpf = str(input("digite o seu cpf: "))
print(f"Seu CPF é: {cpf}")


strip() - remove espaços em branco no inicio e no final da string
lower() - converte todos os caracteres da string para minúsculas
upper() - converte todos os caracteres da string para maiúsculas
capitalize() - converte o primeiro caractere da string para maiúscula e os demais para



Operadores aritméticos em Python
+ - adição
- - subtração
* - multiplicação
/ - divisão
% - módulo (resto da divisão)
** - potência
// - divisão inteira


operadores de comparação em Python
== - igual a - henry == henry
!= - diferente de
<  - menor que
> - maior que
<= - menor ou igual a
>= - maior ou igual a

= atribuição


1+1 == 2 
!= 1+1 != 3
< 1+1 < 3

operadores lógicos em Python
and - e - True and False = False   Ele so e verdadeiro se ambos os operandos forem verdadeiros 
or - ou - True or False = True Ele so e verdadeiro se pelo menos um dos operandos for verdadeiro
not - não - not True = False ele inverte o valor do operando, se for verdadeiro se torna falso e vice-versa



not True = False
and True = True
or False = False



If - Estrutura condicional em Python| IF iqual a (se) | ELSE iqual a (senão) | ELIF iqual a (senão se)
if True:
    print("A condição é verdadeira")
else:
    print("A condição é falsa")
    
elif True:
    print("Retorne nada")
    
    
    
laços de repetição em Python | FOR iqual a (para) | WHILE iqual a (enquanto)


for i in range(5):                for i in range (10):  # range(5) gera uma sequência de números de 0 a 9
    print(f"Iteração {i}")





0,1,2,3,4





while True:
    resposta = input("Deseja continuar? (s/n): ")
    if resposta == "n":
        break





peca = ["filtro de ar", "oleo", "filtro de oleo", "velas", "pastilhas de freio"]
locais = {
    "loja1": "Rua A, 123",
    "loja2": "Avenida B, 456",
    "loja3": "Praça C, 789"
}


id = (1,2,3,4,5,6,)



cpf_vivo = (06479889177, 12345678900, 98765432100)
cpf_morto = (12345678900, 98765432100, 11111111111)


insert() - insere um elemento em uma lista em uma posição especifica
append() - adiciona um elemento no final da lista

banco de dados com DDD com imutabilidade e mutabilidade



funções em Python | def iqual a (definir) | return iqual a (retornar)

def saudacao(nome: str) -> str:
    return f"Olá, {nome}!"

print(saudacao("Alice"))
print(saudacao("Bob"))
print(saudacao("Charlie"))



nome = input("Digite seu nome: ")
printf(f"Olá, {nome}!")


def soma(a: int, b: int) -> int:
    return a + b

print(soma(5, 3))
print(soma(10, 20))



def subtracao(a: int, b: int) -> int:
    return a - b


def multiplicacao(a,b) : 
    return a * b




** 
* 
/
+-



def = definition of a function

return = return a value from a function que significa retornar um valor de uma função que pode ser usado em outro lugar do código.

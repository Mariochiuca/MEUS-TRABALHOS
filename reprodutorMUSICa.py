##DESENVOLVER UM ALGORITMO QUE SIMULA UM REPRODUTOR DE MUSICA

---------REQUISITOS---------
1-ADICIONAR MÚSICAS NA PLAYLIST
2-REPODUZIR MÚSICAS
3-VISUALIZAÇÃO PLAYLIST
4-REMOVER A ÚLTIMA MÚSICA ADICIONADA
5-VIZUALIZAR HISTÓRICO DO REPODUÇÃO
from collections import deque

def isEmpty(lista):
if len(lista)==0:
return True
else:
return False

def listar(lista):
print(len(lista), " PlayList ")
for i in lista:
print(f"{i}", " ")
print("\n---------------------------")

musicas = deque()
historico=[]

while(True):
print(" 1- ADICIONAR MÚSICA NA PLAYLIST")
print(" 2- REPODUZIR MÚSICAS ")
print(" 3- VIZUALIZAR PLAYLIST ")
print(" 4- REMOVER A ÚLTIMA MÚSICA ADICIONADA ")
print(" 5- VIZUALIZAR HISTÓRICO DO REPODUÇÃO ")

opcao = input(" ESCOLHA UMA OPCAO: ")

if (opcao == "1" ):
    musicas.append(input("MÚSICA: "))
    listar(musicas)

elif(opcao == "2"):
    eliminada=(musicas.popleft())
    print((f" {eliminada} "), (" Está sendo reproduzida..."))
    historico.append(eliminada)


elif(opcao == "3"):
    listar(musicas)

elif(opcao == "4"):
    if isEmpty(musicas):
        listar(musicas)
    else:
        print(musicas.pop(), "Música Removida")
        listar(musicas)

elif(opcao == "5"):
    print(f"historico de musicas reproduzidas \n {historico}")

elif(opcao == "6"):
    break
else:
    print("opção errada")

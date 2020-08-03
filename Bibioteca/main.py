import minha_biblioteca as mb

nome = input("Nome: ")
nasc = input("Coloque sua data de nacimento **/**/****: ")
film = int(input("Qual é a sensura do filme: "))



print("Seja bem vindo",nome,":D")
if mb.censura(mb.idade(nasc),film):
    print("Você pode se dirigir a sessão!")
else:
    print("Proibido ir a sessão!")
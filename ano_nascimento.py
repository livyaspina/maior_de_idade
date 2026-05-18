from datetime import date
atual = date.today().year
maior = 0
menor = 0


for n in range(1, 8):
    ano = int(input("Em que ano a {}° pessoa nasceu? ". format(n)))
    idade = atual - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
   
    
print("Ao todo tivemos {} pessoa(s) maior(es) de idade.".format(maior))
print("E também tivemos {} pessoas menores de idade". format(menor))
# Enunciado do Problema: Faça um programa que mostre a data e a hora do sistema nos seguintes formatos: DD/MM/AAAA - mês por extenso e hora:minuto


# Nomes dos alunos: Gabriel Almeida da Silva e Gabriela de Souza Lima


# Data de criação: 30/03/2026


import datetime as dt
from zoneinfo import ZoneInfo


print("------------------------")
print("--- Exibição da data ---")
print("------------------------ \n")


escolha = input("Escolha 'I' para Inglês e 'P' para Português: ").lower()


# conceito de objeto (propriedades e métodos)
data = dt.datetime.now(ZoneInfo(“America/Sao_Paulo”))
ano_atual = data.year
mes_atual = data.strftime("%B") # formata e retorna pra mim por extenso o nome do mês
dia_atual = data.day
hora_atual = data.hour
minuto_atual = data.strftime("%M")
segundo_atual = data.second


if(escolha == "i"):
    print(mes_atual, dia_atual, ano_atual, sep="/") # formato americano
    print(hora_atual, minuto_atual, segundo_atual, sep=":")
elif(escolha == "p"):
    # formato br
    if(mes_atual == "January"):
        mes_atual = "Janeiro"
        print(dia_atual, mes_atual, ano_atual, sep="/")
        print(hora_atual, minuto_atual, segundo_atual, sep=":")
    elif(mes_atual == "February"):
        mes_atual = "Fevereiro"
        print(dia_atual, mes_atual, ano_atual, sep="/")
        print(hora_atual, minuto_atual, segundo_atual, sep=":")
    elif(mes_atual == "March"):
        mes_atual = "Março"
        print(dia_atual, mes_atual, ano_atual, sep="/")
        print(hora_atual, minuto_atual, segundo_atual, sep=":")
    elif(mes_atual == "April"):
        mes_atual = "Abril"
        print(dia_atual, mes_atual, ano_atual, sep="/")
        print(hora_atual, minuto_atual, segundo_atual, sep=":")
    elif(mes_atual == "May"):
        mes_atual = "Maio"
        print(dia_atual, mes_atual, ano_atual, sep="/")
        print(hora_atual, minuto_atual, segundo_atual, sep=":")
    elif(mes_atual == "June"):
        mes_atual = "Junho"
        print(dia_atual, mes_atual, ano_atual, sep="/")
        print(hora_atual, minuto_atual, segundo_atual, sep=":")
    elif(mes_atual == "July"):
        mes_atual = "Julho"
        print(dia_atual, mes_atual, ano_atual, sep="/")
        print(hora_atual, minuto_atual, segundo_atual, sep=":")
    elif(mes_atual == "August"):
        mes_atual = "Agosto"
        print(dia_atual, mes_atual, ano_atual, sep="/")
        print(hora_atual, minuto_atual, segundo_atual, sep=":")
    elif(mes_atual == "Setember"):
        mes_atual = "Setembro"
        print(dia_atual, mes_atual, ano_atual, sep="/")
        print(hora_atual, minuto_atual, segundo_atual, sep=":")
    elif(mes_atual == "October"):
        mes_atual = "Outubro"
        print(dia_atual, mes_atual, ano_atual, sep="/")
        print(hora_atual, minuto_atual, segundo_atual, sep=":")
    elif(mes_atual == "November"):
        mes_atual = "Novembro"
        print(dia_atual, mes_atual, ano_atual, sep="/")
        print(hora_atual, minuto_atual, segundo_atual, sep=":")
    elif(mes_atual == "December"):
        mes_atual = "Dezembro"
        print(dia_atual, mes_atual, ano_atual, sep="/")
        print(hora_atual, minuto_atual, segundo_atual, sep=":")
else:
    print("Opção inválida!")
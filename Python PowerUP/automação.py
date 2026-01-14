#!/usr/bin/env python3
"""Automatização do cadastro de produtos no sistema da empresa usando PyAutoGUI

Passo-a-passo do programa:
1.	Entrar no site da empresa
    1.2	Fazer Login
2.	Abrir a base de dados
3.	Cadastrar 1 produto
4.	Repetir o passo 5 até acabar a lista de produtos
"""
import pyautogui
import time
import pandas
pyautogui.PAUSE = 0.5

# Passo 1: Entrar no sistema da empresa
    #Abrir o navegador
pyautogui.press("Win")
pyautogui.write("chrome")
pyautogui.press("enter")
link_system = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link_system)
pyautogui.press("enter")

# Fazer uma pausa maior pro site carregar
time.sleep(3)

# Fazer Login
pyautogui.click(x=771, y=461)
pyautogui.write("athos251096@gmail.com")
pyautogui.press("tab") # Passa pro próximo campo
pyautogui.write("Senha123")
pyautogui.press("tab") # Passa pro botão
pyautogui.press("enter")
time.sleep(4) # esperar o login

#Passo 2: Abrir a base de dados
Tabela = pandas.read_csv("produtos.csv")
for linha in Tabela.index:

#Passo 3:Cadastrar 1 produto
    pyautogui.click(x=760, y=335) #clicar no campo código

#Código
    codigo =  str(Tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab") # Passa pro próximo campo

#marca
    marca =  str(Tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab") # Passa pro próximo campo

#Tipo
    tipo =  str(Tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab") # Passa pro próximo campo

#Categoria
    categoria =  str(Tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab") # Passa pro próximo campo

#Preço
    preco =  str(Tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab") # Passa pro próximo campo

#Custo
    custo =  str(Tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab") # Passa pro próximo campo

#Obs
    obs =  str(Tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab") # Passa pro botão enviar
    pyautogui.press("enter") # Cadastra o produto

#voltar ao inicio da tela
    pyautogui.scroll(50000000)

# Passo 4: Repetir o passo 4 até acabar a lista de produtos
# A gente volta em cada campo e automatiza a busca de informação iterando
import pyautogui
import os
import time

def verificarArquivo(arquivo):
    if os.path.exists(arquivo):
        pyautogui.alert("Arquivo encontrado!")
    else:
        pyautogui.alert("Arquivo não encontrado")

def listarArquivos(diretorio):
    for arquivo in os.listdir(diretorio):
        print(f"Processando: {arquivo}")
    print("Processo finalizado....")

def verficarUsuario(senha):
    if senha == "admin":
        verificarArquivo("dados.csv")
        local = "C:/Users/gusta/OneDrive/Documentos"
        listarArquivos(local)
    else:
        pyautogui.alert("Senha inválida! Finalizando processo...")

status = "pendente"

while status == "pendente":
    print("Aguardando aprovação...")
    time.sleep(5)
    status = "aprovado"

print("Processo aprovado!\nContinuando automação...")

senha_usuario = pyautogui.password("Informe a senha:")
verficarUsuario(senha_usuario)

import pyautogui
import pandas as pd
from openpyxl import Workbook
from datetime import datetime
import time
import os

os.system("cls")

def executar_tarefa(tarefa, tipo, dado):
    try:
        inicio = time.time()

        if tipo.lower() == "texto":
            pyautogui.write(dado, interval=0.1)
        elif tipo.lower() == "tecla":
            pyautogui.press(dado)
        elif tipo.lower() == "espera":
            time.sleep(int(dado))
        elif tipo.lower() == 'hotkey':
            teclas = dado.split('+')
            pyautogui.hotkey(*teclas)
        else:
            return (tarefa, "Tipo de tarefa desconhecida", 0)
        
        tempo = round(time.time() - inicio, 2)

        return (tarefa, "Sucesso", tempo)
    
    except Exception as e:
        return (tarefa, f"Erro: {str(e)}", 0)

def gerar_relatorio(relatorio):
    wb = Workbook()
    ws = wb.active
    ws.append(["'Tarefa", "Status", "Tempo de Execução (s)"])

    for linha in relatorio:
        ws.append(linha)

    pasta = "Relatórios"
    os.makedirs(pasta, exist_ok=True)

    salvamento = f"{pasta}/Relatório({datetime.now().strftime('%d-%m-%Y %H.%M.%S')}).xlsx"

    wb.save(salvamento)

    return salvamento

def main():
    df = None

    try:
        df = pd.read_csv("tarefas.csv")
    except FileNotFoundError:
        print("Arquivo de 'Tarefas' não encontrado!")

    relatorio_execucao = []

    if df is not None:    
        for i in range(3, 0, -1):
            print(f"Iniciando execução automática em {i} ...\n")
            time.sleep(1)
            os.system("cls")

        qtd_tarefa_desc, qtd_erros = 0, 0

        for _, coluna in df.iterrows():
            resultado = executar_tarefa(coluna["Tarefa"], coluna["Tipo"], coluna["Dado"])
            relatorio_execucao.append(resultado)
            print(f"• [{resultado[1]}] - {coluna["Tarefa"]} ({resultado[2]}s)")
            
            if resultado[1] == "Sucesso":
                pass
            elif resultado[1] == "Tipo de tarefa desconhecida":
                qtd_tarefa_desc += 1
            else:
                qtd_erros += 1

        informa_qtd_tarefa_desc = f"\nQuantidade de tarefas desconhecidas: {qtd_tarefa_desc}" if qtd_tarefa_desc > 0 else ""
        informa_qtd_erros = f"\nQuantidade de erros: {qtd_erros}" if qtd_erros > 0 else ""

        caminho = gerar_relatorio(relatorio_execucao)

        print(f"\nExecução finalizada. \nLocal do relatório: /{caminho} \nData: {datetime.now().strftime("%d/%m/%Y - %H:%M:%S")} {informa_qtd_tarefa_desc} {informa_qtd_erros} \n")

    else:
        print("\nExecução não iniciada.\n")

if __name__ == '__main__':
    main()

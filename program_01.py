import pyautogui
import time
import os
from datetime import datetime

pyautogui.PAUSE = 2

os.system("taskkill /f /im notepad.exe")

time.sleep(1)

pyautogui.press("win")

pyautogui.write("Bloco de Notas", interval=0.1)
pyautogui.press("enter")

time.sleep(1)

pyautogui.hotkey("ctrl", "n")

time.sleep(1)

pyautogui.write("Texto gerado com Python usando o PyAutoGUI!", interval=0.1)
pyautogui.hotkey("ctrl","shift","s")
pyautogui.hotkey("f12")

time.sleep(1)

nome_arquivo = datetime.now().strftime("meu_arquivo_%Y%m%d_%H%M%S.txt")
pyautogui.write(nome_arquivo)

pyautogui.press("enter")

time.sleep(1)

pyautogui.hotkey("alt", "f4")

time.sleep(1)

os.system("taskkill /f /im notepad.exe")

print(f"Automação concluída com sucesso! Arquivo salvo como: {nome_arquivo}")

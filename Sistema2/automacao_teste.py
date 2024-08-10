import pyautogui
import time

pyautogui.PAUSE = 0.3

# funções do mouse
pyautogui.click(667, 997, duration=0.5)  # clicka em um lugar
pyautogui.moveTo()  # move até um lugar
pyautogui.scroll()  # positive number pra cima - negative number pra baixo

# funções do teclado
pyautogui.write("Olá")  # Escrever texto
pyautogui.hotkey("ctrl", "v")  # aperta varias teclas
pyautogui.press("tab")  # Pressiona uma tecla

# clickar no meio do screenshot
posicao = pyautogui.locateCenterOnScreen("img.png")
pyautogui.click(posicao)

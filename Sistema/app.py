
import pyautogui
from time import sleep

with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]

        pyautogui.click(696,525, duration=1)
        pyautogui.write(produto)

        pyautogui.click(679,554, duration=1)
        pyautogui.write(quantidade)

        pyautogui.click(675,581, duration=1)
        pyautogui.write(preco)

        pyautogui.click(593,742,duration=1)
        sleep(1)
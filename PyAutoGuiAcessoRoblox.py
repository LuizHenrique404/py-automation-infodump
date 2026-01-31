# https://pyautogui.readthedocs.io/en/latest

# 1- O SISTEMA VAI ENTRAR NO ROBLOX
# 2- VAI NA BARRA DE PESQUISA E DIGITA "MICHAEL ZOMBIES"
# 3- CLICA NO JOGO
# 4- CLICA EM "GOSTEI"
# 5- BAIXA A TELA
# 6- CLICA EM "VER MAIS CONQUISTAS"
# 7- CLICA EM OUTRO JOGO
# 8- FECHA O NAVEGADOR

import pyautogui
import time

def main():
    pyautogui.press('win')
    time.sleep(0.5)
    pyautogui.write('firefox')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.hotkey('win', 'up')

    pyautogui.moveTo(698, 440)
    pyautogui.click()
    pyautogui.write('Roblox')
    pyautogui.press('enter')
    time.sleep(3)

    pyautogui.moveTo(1351, 122)
    pyautogui.click()
    time.sleep(3)

    pyautogui.moveTo(673, 102)
    pyautogui.click()
    pyautogui.write('Michael Zombies')
    pyautogui.press('enter')
    time.sleep(3)

    pyautogui.moveTo(196, 326)
    pyautogui.click()
    time.sleep(3)
    pyautogui.scroll(-500)
    time.sleep(0.5)
    pyautogui.scroll(-500)
    time.sleep(0.5)
    pyautogui.scroll(-500)
    time.sleep(0.5)
    pyautogui.scroll(-500)
    time.sleep(0.5)

    pyautogui.moveTo(290, 433)
    pyautogui.click()
    
    time.sleep(2)
    pyautogui.hotkey('alt', 'f4')
    
if __name__ == "__main__":
    main()
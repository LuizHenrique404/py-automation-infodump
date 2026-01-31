import pyautogui
import time

while True:
    # VISÃO COMPUTACIONAL DO PYAUTOGUI
    '''
    try:
        location = pyautogui.locateOnScreen('.\Specific_Files\Stickman.png', confidence=0.3) != None
        print("I can see it here:", pyautogui.center(location))
        time.sleep(0.5)
    except:
        print("I am unable to see it")
        time.sleep(0.5)
    '''
    # MUITO LIMITADO, E GERA UM ERRO TODA VEZ QUE NÃO DETECTA O ALVO
    # O PARÂMETRO "CONFIDENCE" DEFINE O MÍNIMO DE PRECISÃO QUE A IMAGEM DEVE TER COM A REFERÊNCIA
    # O PARÂMETRO "REGION" FARÁ COM QUE APENAS ESSA PARTE ESPECÍFICA SEJA CHECADA (+VELOCIDADE)
    # O PARÂMETRO "GREYSCALE" FARÁ COM QUE A IMAGEM SEJA LIDA EM PRETO E BRANCO (+VELOCIDADE)
    # O COMANDO ".center" IRÁ MOSTRAR AS COORDENADAS DO PONTO CENTRAL DO OBJETO DETECTADO

    # O PYAUTOGUI TAMBÉM É CAPAZ DE TIRAR SCREENSHOTS DA TELA
    # NECESSÁRIA A INSTALAÇÃO DO MÓDILO "PILLOW"
    '''
    pyautogui.screenshot("Screenshot_Braba.png", region=(400, 400, 400, 400))
    '''
    # AS INFORMAÇÕES DO TAMANHO DA FOTO PODEM SER OBTIDOS COM ".SIZE"
    '''
    picture = pyautogui.screenshot()
    '''
    # CASO NÃO SEJA ESPECIFICADO O NOME, OU PATH DO ARQUIVO, ELE NÃO SERÁ CRIADO

    # AS INFORMAÇÕES SOBRE UM PIXEL ESPECIFICO PODEM SER OBTIDOS POR MEIO DO ".GETPIXEL"
    '''
    R, G, B = picture.getpixel((X, Y))
    '''
    
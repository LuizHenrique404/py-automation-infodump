# https://selenium-python.readthedocs.io
# BOM PARA TRABALHAR COM SITES DINÂMICOS
# WEBDRIVER DO FIREFOX: geckodriver
# WEBDRIVER DO CHROME: chromium

# CONSERTAR ERRO DE INDENTAÇÃO NO VS CODE:
# Ctrl + A (selecionar tudo)
# Ctrl + Shift + P
# Digite: Convert Indentation to Spaces
# Depois: Format Document (Shift + Alt + F)

# 1- ABRE O NAVEGADOR
# 2- VAI PARA A WIKIPÉDIA
# 3- MAXIMIZA A TELA
# 4- ESPERA 3 SEGUNDOS
# 5- SCROLL PARA BAIXO
# 6- ENTRAR NO DIA MUNDIAL DA TELEVISÃO
# 7- SCROLL PARA BAIXO
# 8- ENTRA NA TELEVISÃO
# 9- FECHA O NAVEGADOR

# PERMITIR A UTILIZAÇÃO DE TECLAS ESPECIAIS
from selenium.webdriver.common.keys import Keys
# PERMITIR LOCALIZAR ELEMENTOS NA PÁGINA
from selenium.webdriver.common.by import By
# IMPORTAR O WEBDRIVER
from selenium import webdriver
# IMPORTAR A FUNÇÃO DE ESPERA
from time import sleep

def main():
    driver = webdriver.Firefox()
    driver.get('https://pt.wikipedia.org/wiki/Main_Page')
    driver.maximize_window()
    
    # IRÁ ARMAZENAR A ALTURA ATUAL DA PÁGINA
    height = driver.execute_script("return document.body.scrollHeight")
    print(f"Altura da página: {height}px\nTipo de dado: {type(height)}")

    # CASO A PÁGINA TENHA CARREGAMENTO DINÂMICO, USAR ESSE CÓDIGO ABAIXO.
    '''
    for n in range(3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
    '''

    # PÁGINA COM TAMANHO FIXO
    for n in range(0, height, 20):
        if n >= 1000:
            break
        driver.execute_script(f"window.scrollTo(0, {n});")
        sleep(0.01)
    sleep(3)  

    driver.find_element(By.XPATH,"/html/body/div[3]/div/div[3]/main/div[3]/div[3]/div[1]/div[3]/div[1]/div[2]/p[1]/b[2]/a").click() 

    height = driver.execute_script("return document.body.scrollHeight")
    print(f"\nAltura da página: {height}px\nTipo de dado: {type(height)}")

    for n in range(0, height, 10):
        if n >= 500:
            break
        driver.execute_script(f"window.scrollTo(0, {n});")
        sleep(0.01)
    sleep(3)  

    # ABRIR LINK EM NOVA ABA
    newTab_Element = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr/td[2]/i/b/span/a")
    newTab_Element.send_keys(Keys.CONTROL + Keys.RETURN)

    # É POSSIVEL ESCREVER TEXTOS COM O send_keys TAMBÉM
    # newTab_Element.send_keys("Texto de exemplo")

    # MUDAR PARA A NOVA ABA
    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    sleep(2)

    # FECHAR A ABA ATUAL
    driver.close()
    driver.switch_to.window(handles[0])
    sleep(3)

    driver.get("https://pt.wikipedia.org/wiki/Col%C3%A9gio_Pedro_II")
    sleep(3)

    # SCROLL PARA BAIXO ATÉ UM ELEMENTO ESPECÍFICO:
    '''
     - console.log() CONSOLE DO NAVEGADOR, PARA A EXECUSSÃO DE COMANDOS JAVASCRIPT.
     - arguments[n] É USADO PARA PASSAR PARÂMETROS PARA O SCRIPT.
     - scrollIntoView() FUNÇÃO PARA ROLAR A PÁGINA ATÉ O ELEMENTO.
     - OPÇÃO block: 'center' PARA CENTRALIZAR O ELEMENTO NA TELA.
    '''
    searchElement = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/main/div[3]/div[3]/div[1]/p[11]/a[2]")
    driver.execute_script("console.log(arguments[0].scrollIntoView({block: 'center'}))", searchElement)
    
    # ESPERA DE EXECUÇÃO DE SCRIPT MANUAL
    sleep(3)

    # ESPERA DE EXECUÇÃO DE SCRIPT AUTOMÁTICA
    # O expected_conditions TEM VÁRIAS OPÇÕES DE EVENTOS PARA ESPERAR.
    '''
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions

    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.element_to_be_clickable(searchElement))
    '''

    searchElement.click()
    sleep(5)

    driver.quit()

if __name__ == "__main__":
    main()
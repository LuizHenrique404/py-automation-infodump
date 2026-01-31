# https://playwright.dev/python/docs/intro
# Ao instalar o playwright, é necessário instalar os navegadores necessários executando: playwright install

# https://gameflip.com/p/blox-fruits/ea84bbf3-26b9-4f90-b235-5173cffc2602

from playwright.sync_api import sync_playwright, expect
# Recomendado não realizar esperas manuais!
from time import sleep

# Iniciar o gerenciamento das ações do Playwright
with sync_playwright() as pw:
    # Possuí a opção de realizar as tarefas sem exibir o navegador (headless=True)
    navegador = pw.firefox.launch(headless=False)
    # O contexto permite o gerenciamento de abas e janelas
    contexto = navegador.new_context()
    # Abrir uma nova aba no navegador
    pagina = contexto.new_page()
    print("Navegador iniciado.")

    # Navegar para o Gameflip
    pagina.goto("https://gameflip.com/p/blox-fruits/ea84bbf3-26b9-4f90-b235-5173cffc2602")
    print("Página acessada.\nTítulo da página:", pagina.title())

    # Comando para voltar a página
    '''
    pagina.go_back()
    '''
    # Comando para avançar a página
    '''
    pagina.go_forward()
    '''

    # Selecionar um elemento na tela (Recomendado utilizar aspas simples para o seletor)
    botao = pagina.locator('xpath=/html/body/div[1]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[1]/a[1]')
    # Ao selecionar o elemento, ele irá clica-lo
    botao.click()

    # No cenário onde o clique do botão abra uma nova aba, é necessário mudar o contexto para a nova aba.
    '''
    with contexto.expect_page() as np:
        botao.click()
    nova_pagina = np.value # <-- Irá incorporar a nova aba à variável nova_pagina
    '''
    # Onde o sistema irá esperar a nova aba ser aberta para então atribuí-la a variável np.
    # Diferente do Selenium, não é necessário armazenar todas as abas em uma lista e então navegar entre elas.
    # Apenas armazenando a nova aba em uma variável já é possível interagir com ela.

    print("Botão clicado.")

    # Para se visualizar os códigos contidos na página, que o playwright pode interagir, utilizar o comando abaixo no terminal:
    '''
    playwright codegen https://gameflip.com/p/blox-fruits/ea84bb
    '''
    # Onde ele vai abrir duas janelas, uma com a página e outra com o código gerado. Para facilitar a localização dos seletores.
    #
    # A localização dos elementos podem ser feitas de maneira geral, para uma categoria específica.
    '''
    categoria = pagina.locator('div').all()
    '''
    # E assim transformado em uma lista, onde é possível acessar cada elemento pelo seu índice.

    # Depois de clicar no botão, seleciona o campo de busca da página
    search_box = pagina.locator("#collapse-dropdown").get_by_role("searchbox", name="Search listings")

    # Apesar do Playright realizar a espera automaticamente, é possível inserir esperas manuais quando necessário.
    '''
    expect(search_box).to_be_visible(timeout=5000)
    '''

    search_box.click()
    print("Campo de busca selecionado.")

    # Irá digitar no campo de busca
    search_box.fill("Blox Fruits")
    print("Texto digitado na busca.")

    # O Playwright possuí uma função de teclado semelhante ao PyAutoGui
    pagina.keyboard.press("Enter")
    print("Busca realizada.")

    # Irá abrir uma nova janela e navegar para o YouTube
    nova_pagina = contexto.new_page()
    nova_pagina.goto('https://www.minecraft.net/pt-br/store/minecraft-deluxe-collection-pc?OCID=cmmx0j7bkem_SEM_MinecraftAcquisitionBR_GA_Branded_Minecraft-Creative3-GBL&gad_source=1&gad_campaignid=23412967382&gclid=Cj0KCQiA7fbLBhDJARIsAOAqhsesagwauNK87Sk72B0s2VLaPsa83Q5LIGPMF9WW-N-nDcfToe4CYvgaAngzEALw_wcB&tabs=%7B"details"%3A0%7D')

    sleep(2)
    pagina.go_back()

    sleep(5)
    navegador.close()
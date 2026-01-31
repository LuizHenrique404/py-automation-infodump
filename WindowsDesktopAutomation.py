# https://pywinauto.readthedocs.io/en/latest/
from pywinauto import Application
from pywinauto import Desktop
from time import sleep

# BACKEND DEFINIDO PARA "AUTOMAÇÃO INTERFACE DE USUÁRIO"
'''
app = Application(backend="uia")
dlg = Desktop(backend="uia").Calculator
app.start("calc.exe")
dlg = app.window()
'''
# O "Popen" IRÁ EXECUTAR O ARQUIVO DA CÁLCULADORA
# O "DLG" IRÁ SER CONFIGURADO PARA MEXER NA CÁLCULADORA CASO ELA SEJA EXECUTADA

# IRÁ ACIONAR AS RESPECTIVAS TÉCLAS DA CÁLCULADORA
'''
dlg.type_keys("2")
sleep(0.2)
dlg.type_keys("*")
sleep(0.2)
dlg.type_keys("2")
sleep(0.2)
dlg.type_keys("=")
'''

# IRÁ MOSTRAR MAIS INFORMAÇÕES SOBRE A UI DA JANELA ONDE ESTÁ SENDO FEITA A AUTOMAÇÃO
'''
dlg.print_control_identifiers()
'''
# LISTA DE EXIBIÇÃO:
#   - nomes dos elementos
#   - automation_id
#   - control_type
#   - Nível na hierarquia
#   - caminhos de acesso
#   - sugestões para localizar cada elemento

# IRÁ MOSTRAR OS ELEMENTOS FILHOS DIRETO DA JANELA
'''
dlg.children()
'''
# ELE IRÁ MOSTRAR APENAS EM UM NÍVEL SUPERFICIAL

# MOSTRARÁ UMA LISTA DE TODOS OS ELEMENTOS DA JANELA
'''
print(dlg.descendants(control_type="Button"))
'''
# O PARÂMETRO "CONTROL_TYPE" SERVIRÁ DE FILTRO PRA A LISTA

# PARA CONFIRMAR SE A JANELA EM FOCO, É A CORRETA
'''
print(dlg.element_info.control_type)
print(dlg.element_info.name)
'''
# O COMANDO ".CONTROL_TYPE" NORMALMENTE SERIA WINDOW
# E O COMANDO ".NAME" IRÁ EXIBIR O NOME DA JANELA DO DIALOG

# UMA FORMA PARA TORNAR UMA JANELA EM FOCO
'''
dlg.wait("active")
dlg.set_focus()
dlg.wait("ready")
'''
# O COMANDO ".SET_FOCUS" IRÁ FAZER COM QUE A JANELA SEJA O FOCO DO DIALOG

# LISTAGEM DAS JANELAS ABERTAS RECONHECIDAS PELO "APP"
'''
for w in app.windows():
    print(w.window_text())
'''
# INICIARÁ O BLOCO DE NOTAS, ESCREVERÁ NELE, E SALVARÁ AS INFROMAÇÕES
'''
app.start("notepad.exe")
'''

# O PARÂMETRO "TITLE_RE" IRÁ PROCURAR A JANELA COM O TÍTULO CONTENDO "BLOCO DE NOTAS" NELE
'''
dlg = app.window(title_re=".*Bloco de Notas")
dlg.type_keys("Skibidi_Toilet_:")
'''

# IRÁ CLICAR NO BOTÃO DO MENU SUPERIOR "EDITAR" E DENTRO DELE CLICAR NO "HORA/DATA"
'''
dlg.menu_select("Editar->Hora/Data")
sleep(0.2)
'''
# A MESMA OPERAÇÃO OCORRERÁ COM O "ARQUIVO" E "SALVAR COMO"
'''
dlg.menu_select("Arquivo->Salvar como")
sleep(0.5)
'''

# IRÁ ACESSAR O OBJETO COM O TÍTULO DE "NOME", DO TIPO "COMBOX", SEGUIR PARA O ELEMENTO EDIT, E DIGITAR "BOBBOBÃO.txt"
'''
dlg.child_window(title="Nome:", control_type="ComboBox").Edit.type_keys('BobBobão.txt')
'''
# APÓS ISSO ACESSARÁ O BOTÃO DE SALVAR, E CLICAR NELE
'''
dlg.child_window(title="Salvar", control_type="Button").click()
'''
# ACESSAR ELEMENTOS CHILD A QUALQUER NÍVEL DE PROFUNDIDADE
'''
dlg.child_window(title="Salvar").wrapper_object()
'''

# TÉCNICA PARA DESCER DE NÍVEL
'''
lvl1 = dlg.child_window(title="Configurações")
lvl2 = lvl1.child_window(title="Rede")
lvl3 = lvl2.child_window(auto_id="1234")
'''
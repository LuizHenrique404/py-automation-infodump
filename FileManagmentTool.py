# MODOS DE ARQUIVOS NO PYTHON:
# r = read
# a = append
# w = write
# x = create
# UTILIZADOS PARA GERENCIAR ARQUIVOS NO SISTEMA

# IRÁ CRIAR UM ARQUIVO COM O NOME DE 'ArquivoTexto.txt' E ESCREVER DENTRO DELE
with open("ArquivoTexto.txt", "w") as arquivo:
    arquivo.write("Exemplo de gerenciamento de arquivos em Python.\n")
    arquivo.write("Adicionando mais uma linha ao arquivo.\n")
    # IRÁ FECHAR O ARQUIVO APÓS A ESCRITA
    arquivo.close()

# UM PATH PODE SER ESPECIFICADO DENTRO DO OPEN, CASO QUEIRA SALVAR EM OUTRO LOCAL
'''
open("C:\\Users\\Mrleonard\\Documents\\{HWN}\\ArquivoTexto.txt", "w")
'''

# IRÁ ABRIR O ARQUIVO 'ArquivoTexto.txt' E LER O CONTEÚDO DELE
with open("ArquivoTexto.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do arquivo:")
    print(conteudo)
    # IRÁ FECHAR O ARQUIVO APÓS A LEITURA
    arquivo.close()

# COMANDO TRY E EXCEPT PARA TRATAR ERROS, NÃO SÓ DE ARQUIVOS, MAS DE VÁRIOS TIPOS
try:
    # IRÁ TENTAR ABRIR UM ARQUIVO QUE NÃO EXISTE
    with open("Random.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
        arquivo.close()
except:
    # DIZER QUE O ARQUIVO NÃO EXISTE, AO INVÉS DE GERAR UM ERRO
    print("O arquivo não existe.")

# IRÁ ADICIONAR UMA LINHA EXTRA NO ARQUIVO 'ArquivoTexto.txt', SEM APAGAR O CONTEÚDO JÁ EXISTENTE
with open("ArquivoTexto.txt", "a") as arquivo:
    arquivo.write("Adicionando uma nova linha ao arquivo existente.")
    arquivo.close()

# IRÁ REALIZAR UM OVERWRITE NO ARQUIVO 'ArquivoTexto.txt', APAGANDO O CONTEÚDO JÁ EXISTENTE
with open("ArquivoTexto.txt", "w") as arquivo:
    arquivo.write("O conteúdo anterior foi apagado e substituído por este.")
    arquivo.close()
# O COMANDO "W" TAMBÉM CRIA O ARQUIVO CASO ELE NÃO EXISTA

# IRÁ TENTAR CRIAR UM NOVO ARQUIVO 'novo_arquivo.txt'. SE ELE JÁ EXISTIR, IRÁ GERAR UM ERRO
try:
    with open("novo_arquivo.txt", "x") as arquivo:
        arquivo.write("Arquivo criado com o modo 'x'.")
        arquivo.close()
except:
    print("O arquivo já existe, não foi possível criar.")
# SERVE COMO MEDIDA MAIS CAUTELOSA PARA CRIAR ARQUIVOS, POIS EVITA SOBREESCREVER ARQUIVOS JÁ EXISTENTES

# TRATAMENTO DE ARQUIVOS MAIS AVANÇADO
import os

# IRÁ RETORNAR O DIRETÓRIO ATUAL DE TRABALHO
current_Path = os.getcwd()
print("Diretório atual:", current_Path)

# IRÁ MUDAR A PASTA ATUAL ONDE O SISTEMA ESTÁ ATUANDO
os.chdir("C:\\Users\\Mrleonard\\Documents")
print("Diretório alterado para:", os.getcwd())

# IRÁ VOLTAR A PASTA ANTERIOR
os.chdir(current_Path)
print("Diretório retornado para:", os.getcwd())

# IRÁ LISTAR TODOS OS ARQUIVOS E PASTAS DO DIRETÓRIO ATUAL
print(os.listdir())

# DIVISÃO DO NOME E A EXTENSÃO DE UM ARQUIVO
file_name, file_extension = os.path.splitext("ArquivoTexto.txt")
print("Nome do arquivo:", file_name)
print("Extensão do arquivo:", file_extension)

# RENOMEAÇÃO DE ARQUIVOS USANDO O MÓDULO "OS"
if os.path.exists("novo_arquivo.txt"):
    os.rename("novo_arquivo.txt", "arquivo_renomeado.txt")

# IRÁ CRIAR UMA NOVA PASTA CHAMADA 'NovaPasta', CASO ELA NÃO EXISTA
if not os.path.exists("NovaPasta"):
    os.mkdir("NovaPasta")

# OPERAÇÕES DE MOVIMENTAÇÃO DE ARQUIVOS USANDO O MÓDULO "SHUTIL"
import shutil

# IRÁ COPIAR O ARQUIVO 'arquivo_renomeado.txt' PARA UM NOVO ARQUIVO 'copia_arquivo.txt'
if os.path.exists("arquivo_renomeado.txt"):
    shutil.copy("arquivo_renomeado.txt", "copia_arquivo.txt")

# IRÁ MOVER O ARQUIVO 'arquivo_renomeado.txt' PARA A PASTA 'NovaPasta'
if os.path.exists("arquivo_renomeado.txt"):
    shutil.move("arquivo_renomeado.txt", "NovaPasta/arquivo_renomeado.txt")

# COPIAR E COLAR PASTAS COM O MÓDULO "SHUTIL"
if os.path.exists("NovaPasta"):
    shutil.copytree("NovaPasta", "Copia_NovaPasta")
    print("Pasta 'NovaPasta' copiada para 'Copia_NovaPasta'.")
# MESMO QUE AS PASTAS NÃO EXISTAM, O "SHUTIL" IRÁ CRIÁ-LAS AUTOMATICAMENTE

# TAMBÉM É POSSIVEL IGNORAR CERTOS TIPOS DE ARQUIVOS NA CÓPIA, USANDO O PARÂMETRO "IGNORE"
'''
shutil.copytree("NovaPasta", "Copia_NovaPasta", ignore=shutil.ignore_patterns("*.txt"))
'''

# REMOÇÃO DE ARQUIVOS USANDO O MÓDULO "OS"
if os.path.exists("ArquivoTexto.txt"):
    os.remove("ArquivoTexto.txt")
    print("Arquivo 'ArquivoTexto.txt' removido com sucesso.")
    os.remove("copia_arquivo.txt")
    print("Arquivo 'copia_arquivo.txt' removido com sucesso.")
    os.remove("NovaPasta/arquivo_renomeado.txt")
    print("Arquivo 'arquivo_renomeado.txt' removido com sucesso.")

# REMOÇÃO DE PASTAS USANDO O MÓDULO "OS"
if os.path.exists("NovaPasta"):
    os.rmdir("NovaPasta")
    print("Pasta 'NovaPasta' removida com sucesso.")

# REMOÇÃO DE PASTAS COM ARQUIVOS USANDO O MÓDULO "SHUTIL"
if os.path.exists("Copia_NovaPasta"):
    shutil.rmtree("Copia_NovaPasta")
    print("Pasta 'Copia_NovaPasta' e todos os seus conteúdos foram removidos com sucesso.")
# TODOS OS ARQUIVOS E PASTAS PRESENTES DENTRO DA PASTA SERÃO REMOVIDOS JUNTO COM ELA

# COM O MODULO "SHUTIL" É POSSIVEL COLETAR AS INFORMAÇÕES DE USO DO DISCO RÍGIDO
total, used, free = shutil.disk_usage("/")
print("Informações do disco rígido:", total, used, free)

# IRÁ COPIAR OS METADADOS DE UM ARQUIVO PARA OUTRO USANDO O MÓDULO "SHUTIL"
shutil.copystat("PlayWrightGameflip.py", "SeleniumWikpediaScript.py")
print("Metadados copiados de 'PlayWrightGameflip.py' para 'SeleniumWikpediaScript.py'.")

# NA FUNÇÃO COPY2, É POSSIVEL COPIAR TANTO OS METADADOS QUANTO O CONTEÚDO DO ARQUIVO
'''
shutil.copy2("PlayWrightGameflip.py", "SeleniumWikpediaScript.py")
'''
# O MODULO "SHUTIL" PERMITE A TROCA DE PROPRIETÁRIO DE ARQUIVOS E PASTAS
'''
shutil.chown("ArquivoTexto.txt", user="novo_usuario", group="novo_grupo")
'''
# COM O COMANDO "WITCH" DO MÓDULO "SHUTIL", É POSSIVEL SABER O PATH PARA O ARQUIVO SER EXECUTADO NO CMD
'''
print(shutil.which("python"))
'''

# É POSSIVEL CRIAR UM ARQUIVO ZIP USANDO O MÓDULO "SHUTIL"
shutil.make_archive("Prints", 'zip', "C:\\Users\\Mrleonard\\Pictures\\[Prints]")
print("Arquivo zip criado com sucesso.")
os.remove("Prints.zip")
print("Arquivo zip removido com sucesso.")

# PARA DESEMPACOTAR UM ARQUIVO ZIP, TAMBÉM É USADO O MÓDULO "SHUTIL"
'''
shutil.unpack_archive("Prints.zip", "C:\\Users\\Mrleonard\\Pictures\\[PrintsDescompactados]")
'''
# PARA SABER TODOS OS FORMATOS SUPORTADOS PELO MÓDULO "SHUTIL", USE A FUNÇÃO "get_archive_formats" e "get_unpack_formats"
'''
print(shutil.get_archive_formats())
print(shutil.get_unpack_formats())
'''
# 🐍 Py Automation Infodump: O Guia do Automatizador Massa

Este repositório é uma coletânea de scripts desenvolvidos para automação em Python. Inclui manipulação bruta de arquivos até BOTs que interagem com o Windows e navegadores de forma humanizada.

---

## 🛠️ O que esse repositório faz?

Os scripts estão divididos em quatro categorias principais de automação:

### 1. 🖥️ Automação de Desktop (Windows)
* **`WindowsDesktopAutomation.py`**: Utiliza a biblioteca `pywinauto` para controlar aplicativos nativos do Windows. Inclui exemplos de como abrir a calculadora, digitar no Bloco de Notas (com direito a textos aleatórios) e navegar por hierarquias de janelas.
* **`PyAutoGuiAcessoRoblox.py`**: Uma automação baseada em coordenadas e cliques de mouse com `PyAutoGUI`. Ele abre o navegador, pesquisa jogos no Roblox e interage com a interface de forma totalmente visual.

### 2. 🌐 Automação Web (Scraping & Interaction)
* **`SeleniumWikpediaScript.py`**: O clássico `Selenium` em ação. Script focado em navegação na Wikipédia, lidando com scrolls dinâmicos via JavaScript, troca de abas e esperas inteligentes.
* **`PlayWrightGameflip.py`**: Automação moderna com `Playwright`. Demonstra como navegar no Gameflip, usar seletores XPath, gerenciar contextos de navegador (abas/janelas) e realizar buscas automatizadas.

### 3. 📂 Gestão de Arquivos e Sistema
* **`FileManagmentTool.py`**: O "canivete suíço" para arquivos. Cobre todo o ciclo CRUD (Criar, Ler, Atualizar, Deletar), além de operações avançadas como renomear pastas, mover arquivos com `shutil`, verificar uso de disco e criar arquivos compactados (.zip).

### 4. 👁️ Visão Computacional e Monitoramento
* **`PythonComputerVisionTest.py`**: Testes iniciais com as "vistas" do robô. Usa o `PyAutoGUI` para localizar imagens específicas na tela (`locateOnScreen`), tirar screenshots de regiões determinadas e analisar as cores (RGB) de pixels específicos.

---

## 🚀 Tecnologias Utilizadas

| Biblioteca | Utilidade |
| :--- | :--- |
| **PyAutoGUI** | Automação de mouse/teclado e visão computacional simples. |
| **Pywinauto** | Controle de janelas e elementos da interface Windows (UIA). |
| **Selenium** | Automação web e testes de navegador. |
| **Playwright** | Automação web moderna e rápida. |
| **OS & Shutil** | Manipulação profunda de arquivos, diretórios e metadados. |

---

## 🔧 Como Rodar

1. **Instale as dependências:**
   ```bash
   pip install pyautogui pywinauto selenium playwright pillow

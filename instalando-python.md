# Instalando Python: guia para começar do zero

Este guia ajuda você a instalar **Python 3**, verificar se ele funciona e executar seu primeiro programa. Escolha a seção do seu sistema: [Windows](#windows), [macOS](#macos) ou [Linux Ubuntu e derivados](#linux-ubuntu-e-derivados). Depois, siga para [o teste final](#teste-final-seu-primeiro-programa).

Você não precisa instalar um editor de código ou criar uma conta para fazer os testes deste guia. Os nomes e botões dos instaladores podem mudar com o tempo; se isso acontecer, consulte os links oficiais indicados em cada seção.

## Antes de começar: palavras úteis

| Termo | O que significa aqui |
| --- | --- |
| **Sistema operacional** | O programa principal do computador: Windows, macOS ou Linux. |
| **Navegador** | Aplicativo usado para abrir sites, como Chrome, Firefox ou Safari. |
| **Baixar (download)** | Copiar um arquivo da internet para o computador. |
| **Instalador** | Arquivo ou aplicativo que coloca um programa no computador. |
| **Terminal** | Janela onde você digita comandos. No Windows, o **PowerShell** cumpre esse papel. |
| **Comando** | Texto que você digita no terminal e executa pressionando **Enter**. |
| **Interpretador Python** | Programa que lê e executa o código Python. |
| **Versão** | Número que identifica uma edição do programa, como `Python 3.x.y`. A letra `x` aqui representa um número que pode variar. |
| **Arquivo `.py`** | Arquivo de texto com instruções em Python. |

Nos blocos abaixo, copie apenas o texto do comando, sem as marcas de abertura do bloco. Execute **um comando por vez**. Se você já tiver Python 3 instalado, pode começar pela [verificação da versão](#confirme-a-instalação).

## Windows

1. Abra no navegador a [página oficial de downloads do Python](https://www.python.org/downloads/). Escolha o download para **Windows**. A [documentação oficial para Windows](https://docs.python.org/3/using/windows.html) explica as opções atuais, incluindo o **Python Install Manager**.
2. Abra o arquivo baixado na pasta **Downloads** e siga as instruções mostradas pelo instalador. Se ele pedir para instalar uma versão do Python, aceite a versão estável sugerida. Dependendo do instalador, essa etapa pode ocorrer quando você executar `python` pela primeira vez.
3. Abra o menu **Iniciar**, digite **PowerShell** e abra o aplicativo. Se o PowerShell já estava aberto durante a instalação, feche e abra outra janela.
4. Digite o comando abaixo e pressione **Enter**:

```powershell
python --version
```

Se aparecer `Python 3.x.y`, passe para o [teste final](#teste-final-seu-primeiro-programa). Se `python` não for reconhecido, experimente `py --version`. Use `py` no lugar de `python` nos demais exemplos se esse for o comando que funcionou. Se nenhum deles funcionar, veja [problemas comuns](#se-algo-não-funcionar) e a [solução de problemas oficial](https://docs.python.org/3/using/windows.html#troubleshooting).

## macOS

1. Abra a [página oficial de downloads para macOS](https://www.python.org/downloads/macos/) e baixe o instalador da versão estável atual do Python 3. O arquivo costuma terminar em `.pkg`.
2. Abra o arquivo baixado e siga as telas do instalador. Ao terminar, abra a pasta **Aplicativos** e procure a pasta **Python 3.x**. Se houver um arquivo chamado **Install Certificates.command**, abra-o e aguarde a conclusão. Esse passo faz parte das [instruções oficiais para macOS](https://docs.python.org/3/using/mac.html).
3. Abra o **Terminal**: pressione **Command + Espaço**, digite `Terminal` e pressione **Enter**. Se o Terminal já estava aberto durante a instalação, feche e abra outra janela.
4. Digite:

```bash
python3 --version
```

Se aparecer `Python 3.x.y`, siga para o [teste final](#teste-final-seu-primeiro-programa).

## Linux (Ubuntu e derivados)

Em muitas distribuições Linux, o Python 3 já vem instalado. As etapas abaixo são para **Ubuntu e sistemas que usam `apt`**. Se você usa outra distribuição, procure as instruções do gerenciador de pacotes dela na [documentação do Python para Unix](https://docs.python.org/3/using/unix.html).

1. Abra o **Terminal** pelo menu de aplicativos. Em muitos sistemas, **Ctrl + Alt + T** também funciona.
2. Confira se o Python já existe:

```bash
python3 --version
```

3. Se aparecer `Python 3.x.y`, não é preciso instalar novamente. Se o comando não existir, execute os dois comandos abaixo, **um de cada vez**:

```bash
sudo apt update
sudo apt install python3-full
```

`apt` é o gerenciador de pacotes do Ubuntu: ele busca e instala programas. `sudo` pede permissão para alterar o sistema; poderá ser solicitada a senha do seu usuário. Enquanto você digita a senha, os caracteres podem não aparecer na tela. Isso é normal. A [documentação do Ubuntu](https://ubuntu.com/developers/docs/howto/python-setup/) recomenda o pacote `python3-full` para um ambiente Python mais completo.

4. Digite novamente `python3 --version` para confirmar. Não remova o Python que já veio com o sistema: outros programas podem depender dele.

## Confirme a instalação

Abra uma janela nova do terminal e use o comando correspondente ao seu sistema:

| Sistema | Comando |
| --- | --- |
| Windows | `python --version` (ou `py --version`) |
| macOS e Linux | `python3 --version` |

Uma resposta como `Python 3.x.y` confirma que o comando encontra o Python 3. Os números exatos podem ser diferentes. O sinal `--version` pede ao programa que informe sua versão; ele não instala nada.

Agora abra o interpretador interativo: digite **somente** `python` (ou `py`) no Windows, ou `python3` no macOS e Linux. Quando aparecer `>>>`, digite:

```python
print("Olá, Python!")
```

Pressione **Enter**. A frase `Olá, Python!` deve aparecer. O `>>>` é o convite do Python para você digitar código; **não** faz parte do comando. Para sair, digite `exit()` e pressione **Enter**.

## Teste final: seu primeiro programa

Você também pode executar código salvo em um arquivo. Crie uma pasta fácil de encontrar, como `Estudos Python`, e abra nela um editor de texto simples. Escreva esta linha:

```python
print("Consegui executar meu primeiro arquivo!")
```

Salve com o nome **`ola.py`**. Confira se a extensão é `.py`, e não `.py.txt`. Abra o terminal **nessa pasta**: no Windows, abra a pasta no Explorador de Arquivos, clique na barra de endereço, digite `powershell` e pressione **Enter**; no macOS, você pode digitar `cd ` no Terminal, arrastar a pasta do Finder para a janela e pressionar **Enter**; no Ubuntu, abra a pasta no gerenciador de arquivos, clique com o botão direito em uma área vazia e escolha **Abrir no Terminal** (se disponível).

`cd` significa **mudar de pasta**. Estar na pasta certa permite encontrar `ola.py` sem escrever o endereço completo do arquivo.

Execute o comando do seu sistema:

| Sistema | Comando |
| --- | --- |
| Windows | `python ola.py` (ou `py ola.py`) |
| macOS e Linux | `python3 ola.py` |

Você deve ver `Consegui executar meu primeiro arquivo!`. Isso confirma que o Python consegue ler e executar um arquivo criado por você.

## Se algo não funcionar

- **“Comando não encontrado” ou “não é reconhecido”**: feche e reabra o terminal. Confira se usou `python`/`py` no Windows ou `python3` no macOS/Linux. Se ainda falhar, retorne à instalação do seu sistema.
- **O Windows abre a Microsoft Store em vez do Python**: consulte a [solução de problemas do Python para Windows](https://docs.python.org/3/using/windows.html#troubleshooting), que explica conflitos com atalhos e instalações existentes.
- **“No such file or directory” ou “can't open file” ao executar `ola.py`**: confira se o arquivo se chama exatamente `ola.py` e se o terminal está na pasta onde ele foi salvo.
- **Apareceu `>>>` e o comando `python ola.py` deu erro**: você está dentro do interpretador interativo. Digite `exit()` e execute o comando na janela normal do terminal.
- **A versão começa com `Python 2`**: use o comando alternativo do seu sistema e confira se aparece `Python 3`. Este projeto usa Python 3.

Depois que o teste funcionar, volte ao [README](README.md) e comece pelos [primeiros passos de lógica](1-praticando-logica/teoria.md).

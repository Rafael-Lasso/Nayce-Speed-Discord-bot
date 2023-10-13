# Variaveis de Cores
# Referencia de codigo de cores: https://programadorviking.com.br/print-python/

reset_color = "\033[0m"
Sucess = "\033[1;32;40m"
Danger = "\033[1;31;40m"
Warn = "\033[1;33;40m"

# Classe Responsavel Por Orquestrar as Menssagens
class BotProcessMessage:

    # Funcao de Menssagem Bem Sucedida
    def SucessfulMessage(S_Message):
        print(Sucess + S_Message + reset_color)

    # Funcao de Menssagem Com Aviso
    def WarnMessage(W_Message):
        print(Warn + W_Message + reset_color)

    # Funcao de Menssagem Mal Sucedida
    def ErrorMessage(E_Message):
        print(Danger + E_Message + reset_color)


# Instancia um objeto da Classe "BotProcessMessage"
Menssagens = BotProcessMessage

# Chamando os Metodos
# Menssagens.SucessfulMessage("Sucessful, The Bot is Running...")
# Menssagens.WarnMessage("The Bot is Running...")
# Menssagens.ErrorMessage("Error! The Bot is not Running!")

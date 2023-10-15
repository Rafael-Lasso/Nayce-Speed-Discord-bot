""" Instantiate the application bot  """
from src.config import *

# Inicia a Instancia do Bot
class client(discord.Client):

    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    # Adiciona Persistencia ao Menu Dropdown
    async def setup_hook(self) -> None:
        self.add_view(DropdownView())

    async def on_ready(self):
        try:
            Menssagens.WarnMessage("The Nayce is Started...")
            await self.wait_until_ready()
            if not self.synced:  # Checar se os comandos slash foram sincronizados
                await tree.sync(guild=discord.Object(id=id_do_servidor))
                self.synced = True
            Menssagens.SucessfulMessage("Sucessful, The Bot is Running...")
            print(f"Entramos como {self.user}.")
        except:
            Menssagens.ErrorMessage(
                "Unexpected Error! The Bot is not Running!")


# Instancia um objeto da Classe "client"
aclient = client()
tree = app_commands.CommandTree(aclient)

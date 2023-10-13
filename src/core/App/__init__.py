# Librarys
import os
import dotenv
import discord
from discord import app_commands
from discord.ext import commands
from decouple import config

# Modules
from src.core.Services.Ticket.Ticket import *
from src.core.Services.Messages.bot_running import *

# Load Environment Variables
dotenv.load_dotenv(dotenv_path='src\config\.env')

id_do_servidor = os.getenv("ID_SERVER")
id_cargo_atendente = os.getenv("ID_ATENDENTE")
token_bot = os.getenv("DISCORD_TOKEN")
ticketImage = os.getenv("TIKCET_IMAGE_PATH")

# Inicia a Instancia do Bot
class client(discord.Client):

    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

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

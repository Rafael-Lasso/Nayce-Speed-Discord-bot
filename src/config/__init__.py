# Librarys
import os
import dotenv
import discord
from discord import app_commands
from discord.ext import commands
# from decouple import config

# Modules
from src.core.Services.Ticket.Ticket import *
from src.core.Services.Messages.bot_running import *

# Load Environment Variables
dotenv.load_dotenv(dotenv_path='src/config/.env')

id_do_servidor = os.getenv("ID_SERVER")
id_cargo_atendente = os.getenv("ID_ATENDENTE")
token_bot = os.getenv("DISCORD_TOKEN")
ticketImage = os.getenv("TIKCET_IMAGE_PATH")

reset_color = "\033[0m"
Sucess = "\033[1;32;40m"
Danger = "\033[1;31;40m"
Warn = "\033[1;33;40m"

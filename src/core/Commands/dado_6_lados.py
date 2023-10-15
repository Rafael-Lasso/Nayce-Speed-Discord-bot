from ..App import *
import random

@tree.command(guild=discord.Object(id=id_do_servidor), name="rolar-dado", description='Jogue um dado para decidir algo')
async def verPerfil(interaction: discord.Interaction):
    try:
        embed = discord.Embed(
            colour=16485650,
            title=f"Resultado do Dado de 6 Lados",
            description=f"Voce Jogou um dado \ne parou em {random.randint(1,6)}",
        )
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/1134/1134248.png")
        await interaction.response.send_message(embed=embed, ephemeral=True)
        Menssagens.SucessfulMessage("Command Executed with Sucess!")
    except:
        Menssagens.ErrorMessage("Command cannot be Executed...")
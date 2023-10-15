from ..App import *
import random

@tree.command(guild=discord.Object(id=id_do_servidor), name="cara-ou-coroa", description='Jogue uma moeda para decidir algo')
async def verPerfil(interaction: discord.Interaction):

    moeda = ["cara", "coroa"]

    try:
        embed = discord.Embed(
            colour=16485650,
            title=f"Resultado do Cara ou Coroa",
            description=f"Voce jogou uma moeda e parou\n na {random.choice(moeda)}",
        )
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/272/272525.png")

        await interaction.response.send_message(embed=embed, ephemeral=True)
        Menssagens.SucessfulMessage("Command Executed with Sucess!")
    except:
        Menssagens.ErrorMessage("Command cannot be Executed...")
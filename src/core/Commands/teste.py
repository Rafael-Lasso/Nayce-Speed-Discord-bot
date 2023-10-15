from ..App import *

@tree.command(guild=discord.Object(id=id_do_servidor), name="teste", description='Teste de comando')
async def test(interaction: discord.Interaction):
    try:
        await interaction.response.send_message("Testado", ephemeral=True)
        Menssagens.SucessfulMessage("Command Executed with Sucess!")
    except:
        Menssagens.ErrorMessage("Command cannot be Executed...")
from ..App import *

@tree.command(guild=discord.Object(id=id_do_servidor), name='support-menu', description='Setup')
@commands.has_permissions(manage_guild=True)
async def setup(interaction: discord.Interaction):
    try:
        await interaction.response.send_message("Painel Criado", ephemeral=True)
        embed = discord.Embed(
            colour=16485650,
            title="Central de Ajuda do Recanto dos Uzumaki",
            description="Nessa seção, você pode tirar suas dúvidas ou entrar em contato com a nossa equipe do **Recanto dos Uzumaki**. \n\n Para evitar problemas, leia as opções com atenção e lembre-se de tentar pedir ajuda nos suportes comunitários do servidor."
        )
        embed.set_image(url=ticketImage)
        await interaction.channel.send(embed=embed, view=DropdownView())
        Menssagens.SucessfulMessage("Command Executed with Sucess!")
    except:
        Menssagens.ErrorMessage("Command cannot be Executed...")

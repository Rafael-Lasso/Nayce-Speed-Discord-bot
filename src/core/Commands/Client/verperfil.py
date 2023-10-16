from ...App import *

@tree.command(guild=discord.Object(id=id_do_servidor), name="ver-perfil", description='Veja o avatar de algum membro')
async def verPerfil(interaction: discord.Interaction, member: discord.Member ):
    try:
        embed = discord.Embed(
            colour=16485650,
            title="Mas que belo avatar " + member.display_name,
            description="Essa belezura tá em namo? se não tiver eu quero o///o"
        )
        embed.set_image(url=member.avatar)
        await interaction.response.send_message(embed=embed, ephemeral=True)
        Menssagens.SucessfulMessage("Command Executed with Sucess!")
    except:
        Menssagens.ErrorMessage("Command cannot be Executed...")
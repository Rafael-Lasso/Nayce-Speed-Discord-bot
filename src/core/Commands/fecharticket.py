from ..App import *

@tree.command(guild=discord.Object(id=id_do_servidor), name="fecharticket", description='Feche um atendimento atual.')
async def _fecharticket(interaction: discord.Interaction):
    try:
        mod = interaction.guild.get_role(id_cargo_atendente)
        if str(interaction.user.id) in interaction.channel.name or mod in interaction.author.roles:
            await interaction.response.send_message(f"O ticket foi arquivado por {interaction.user.mention}, obrigado por entrar em contato!")
            await interaction.channel.edit(archived=True, locked=True)
            Menssagens.SucessfulMessage(
                "Command Executed with Sucess!")
        else:
            await interaction.response.send_message("Isso não pode ser feito aqui...")
            Menssagens.WarnMessage("Command cannot be Executed...")
    except:
        Menssagens.ErrorMessage("Command cannot be Executed...")@tree.command(guild=discord.Object(id=id_do_servidor), name='support-menu', description='Setup')

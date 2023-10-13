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

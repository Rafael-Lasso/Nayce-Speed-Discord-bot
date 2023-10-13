import discord
from decouple import config
from discord import app_commands
from discord.ext import commands

# Start Ticket
class Dropdown(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(value="Duvida", label="Duvida", emoji="👋"),
            discord.SelectOption(
                value="Sujestão", label="Sujestão", emoji="💡"),
            discord.SelectOption(value="Reportar Bug", label="Bug", emoji="🐛"),
            discord.SelectOption(value="Atendimento",
                                 label="Atendimento", emoji="📨"),
        ]
        super().__init__(
            placeholder="Selecione uma opção...",
            min_values=1,
            max_values=1,
            options=options,
            custom_id="persistent_view:dropdown_help"
        )

        canaisDeDuvida = ["<#1126682150939398204>, <#1158569028604936253>"]

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Duvida":
            await interaction.response.send_message(f"Para tirar dúvidas gerais use os canais de suporte comunitário como: {canaisDeDuvida} ", ephemeral=True)
        elif self.values[0] == "Sujestão":
            await interaction.response.send_message("Para enviar uma sugestão, utilize o chat <#1158126406883086346>", ephemeral=True)
        elif self.values[0] == "Atendimento":
            await interaction.response.send_message("Clique abaixo para criar um ticket", ephemeral=True, view=CreateTicket())
        elif self.values[0] == "Reportar Bug":
            await interaction.response.send_message(" 🕸 | Para reportar um **Bug do Servidor**, atente-se as instruções:\n \n Envie o **máximo de detalhes** sobre ele (incluindo descrição e fotos). \n \n Havendo isso em mãos, crie um ticket abaixo e faça o seu envio.", ephemeral=True, view=CreateTicket())


class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        self.add_item(Dropdown())

    async def setup_hook(self) -> None:
        self.add_view(DropdownView())


class CreateTicket(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=300)
        self.value = None

    @discord.ui.button(label="Abrir Ticket", style=discord.ButtonStyle.blurple, emoji="➕")
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = True
        self.stop()

        ticket = None
        for thread in interaction.channel.threads:
            if f"{interaction.user.id}" in thread.name:
                if thread.archived:
                    ticket = thread
                else:
                    await interaction.response.send_message(ephemeral=True, content=f"Você já tem um atendimento em andamento!")
                    return

        async for thread in interaction.channel.archived_threads(private=True):
            if f"{interaction.user.id}" in thread.name:
                if thread.archived:
                    ticket = thread
                else:
                    await interaction.edit_original_response(content=f"Você já tem um atendimento em andamento!", view=None)
                    return

        if ticket != None:
            await ticket.edit(archived=False, locked=False)
            await ticket.edit(name=f"{interaction.user.name} ({interaction.user.id})", auto_archive_duration=10080, invitable=False)
        else:
            # ,type=discord.ChannelType.public_thread)
            ticket = await interaction.channel.create_thread(name=f"{interaction.user.name} ({interaction.user.id})", auto_archive_duration=10080)
            await ticket.edit(invitable=False)

        await interaction.response.send_message(ephemeral=True, content=f"Criei um ticket para você! {ticket.mention}")
        await ticket.send(f"📩  **|** {interaction.user.mention} ticket criado! Envie todas as informações possíveis sobre seu caso e aguarde até que um atendente responda.\n\nApós a sua questão ser sanada, você pode usar `/fecharticket` para encerrar o atendimento!")
# End Ticket

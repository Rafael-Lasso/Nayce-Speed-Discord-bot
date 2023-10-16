from ...App import *
import random

@tree.command(guild=discord.Object(id=id_do_servidor), name="tirar-palitinho", description='tire o palitinho para decidir algo, quem tirar o menor perde')
async def verPerfil(interaction: discord.Interaction, member1: discord.Member, member2: discord.Member, member3: discord.Member):
    try:
        resultados = [random.randint(1,30),random.randint(1,30),random.randint(1,30)]
        
        embed = discord.Embed(
            colour=16485650,
            title=f"Quem Sera que levou a melhor ?",
            description=f"O {member1.display_name} tirou um palito de {resultados[0]} cm \n"
            f"O {member2.display_name} tirou um palito de {resultados[1]} cm \n"
            f"O {member3.display_name} tirou um palito de {resultados[2]} cm"
                    )
        embed.set_thumbnail(url="https://cdn.icon-icons.com/icons2/1741/PNG/512/cinnamon-sticks_113368.png")
        await interaction.response.send_message(embed=embed, ephemeral=True)
        Menssagens.SucessfulMessage("Command Executed with Sucess!")
    except:
        Menssagens.ErrorMessage("Command cannot be Executed...")
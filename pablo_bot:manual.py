  import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='*', intents=intents, help_command=None)

CANALE_INPUT_ID = 1416804393029861416  # Canale dove si scrive il comando di annuncio

@bot.event
async def on_ready():
    print(f'Bot connesso come {bot.user}')

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="📢 Help Annuncio Bot",
        description="Guida rapida ai comandi del bot Pablo Escobar.",
        color=0x3498db
    )
    embed.add_field(
        name="🟢 *help",
        value="Mostra questa guida decorata ai comandi.",
        inline=False
    )
    embed.add_field(
        name="📢 *annuncia <#canale> <testo>",
        value="Invia un annuncio decorato nel canale scelto (il comando si usa **solo nel canale di input**).",
        inline=False
    )
    embed.add_field(
        name="✏️ *modify <id_messaggio> <nuovo_testo>",
        value="Modifica un annuncio già inviato nel canale destinazione.",
        inline=False
    )
    embed.set_footer(text="Bot creato da Gioele • Per info scrivi *help")
    await ctx.send(embed=embed)

@bot.command()
async def annuncia(ctx, destinazione: discord.TextChannel, *, testo):
    if ctx.channel.id != CANALE_INPUT_ID:
        await ctx.send("Usa questo comando solo nel canale di input designato!")
        return
    embed = discord.Embed(
        title="📢 ANNUNCIO",
        description=testo,
        color=0xe67e22
    )
    await destinazione.send(embed=embed)
    await ctx.send("Annuncio mandato con successo ✅")

@bot.command()
async def modify(ctx, id_msg: int, *, nuovo_testo=None):
    if nuovo_testo is None:
        await ctx.send("Devi fornire il nuovo testo per l'annuncio.")
        return
    if ctx.channel.id != CANALE_INPUT_ID:
        await ctx.send("Usa questo comando solo nel canale di input designato!")
        return
    try:
        msg = await ctx.channel.fetch_message(id_msg)
        embed = discord.Embed(
            title="📢 ANNUNCIO MODIFICATO",
            description=nuovo_testo,
            color=0x2ecc71
        )
        await msg.edit(embed=embed)
        await ctx.send("Annuncio modificato con successo.")
    except discord.NotFound:
        await ctx.send("Messaggio non trovato.")
    except discord.Forbidden:
        await ctx.send("Non ho i permessi per modificare questo messaggio.")
    except Exception as e:
        await ctx.send(f"Errore: {e}")



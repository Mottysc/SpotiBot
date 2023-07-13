import discord
from discord import app_commands
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = commands.Bot(command_prefix="//", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is ready!!")
    
        
@bot.tree.command(name="testinn")        
async def testin(interaction = discord.Interaction):
    await interaction.response.send_message("Rawrr")
    
@bot.command()
async def synctree(ctx):
    try:
        synced = await bot.tree.sync()
        print(f"Synced {synced} command(s)")
    except Exception as e:
        print(e)

@bot.command()
async def hiya(ctx):
    await ctx.send("Hola!")

bot.run(BOT_TOKEN)
import os
os.system('pip install discord')
import discord
from discord.ext import commands

TOKEN = 'Njg3NzMzNzU0NTUwMDI2MjU4.Xm0cIg.zUFXLmWvkZZ_NWqKEa63UqfbVJo'
bot = commands.Bot(command_prefix='-')


@bot.command(pass_context=True)
async def test(ctx, arg):
	if arg == "Иди_нахуй":
		await ctx.send("Сам пиздуй")
	else:
		await ctx.send("Отъебитесь от меня пж")
		
@bot.command()
async def kv(ctx, arg):
	if arg == "enter":	
		await ctx.send("Вы вставили реверсивку себе в жёпа")
	else:
		await ctx.send("Нах иди")

@bot.command()
async def F(ctx):
        await ctx.send(":Press_F:")


bot.run(TOKEN)

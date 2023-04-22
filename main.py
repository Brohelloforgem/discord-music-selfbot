from discord.ext import commands as discord
import json
from folder import commands
from folder import error_handle

with open("config.json", "r") as f:
    config = json.load(f)

client = discord.Bot(command_prefix=config["bot-prefix"])

@client.command()
async def play(ctx, *, arg):
    await commands.play(ctx=ctx, arg=arg, client=client)

@client.command()
async def pause(ctx):
    await commands.pause(ctx=ctx)

@client.command()
async def skip(ctx):
    await commands.skip(ctx=ctx, client=client)

@client.command()
async def clear(ctx):
    await commands.clear(ctx=ctx)

@client.command()
async def unpause(ctx):
    await commands.unpause(ctx=ctx)

@client.command()
async def bassboost(ctx):
    await commands.bassboost(ctx=ctx)

@client.command()
async def queue(ctx):
    await commands.queue(ctx=ctx)

@client.event
async def on_command_error(ctx, error):
    await error_handle.erroring(error=error, ctx=ctx)

token = config['bot-token']
client.run(token)

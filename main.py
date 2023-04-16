from discord.ext import commands
import json
from folder import commands
from folder import error_handle

client = commands.Bot(command_prefix='$', selfbot=True)
queue_list = []

@client.command()
async def play(ctx, *, arg):
    await commands.play(ctx=ctx, arg=arg, client=client)

@client.command()
async def pause(ctx):
    await commands.pause(ctx=ctx)

@client.command()
async def skip(ctx):
    await commands.skip(ctx=ctx, queue_list=queue_list, client=client)

@client.command()
async def clear(ctx):
    await commands.clear(ctx=ctx, queue_list=queue_list)

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

with open("config.json", "r") as f:
    config = json.load(f)

token = config['bot-token']
client.run(token)

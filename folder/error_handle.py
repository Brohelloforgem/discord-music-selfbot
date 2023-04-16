from discord.ext import commands

async def erroring(error, ctx):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("**Error: Command not found**")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("**Error: Missing required argument**")
    elif isinstance(error, commands.CommandInvokeError):
        await ctx.send("**An error occurred while running the command**")
    else:
        await ctx.send(f"**Error: {error}**")

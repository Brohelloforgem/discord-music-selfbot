from discord.ext import commands
import traceback

async def erroring(error, ctx):
    if isinstance(error, commands.CommandNotFound):
        ctx.send("**Error: Command not found!**")
    elif isinstance(error, commands.MissingRequiredArgument):
        ctx.send("**Error: Missing required argument!**")
    elif isinstance(error, commands.CommandInvokeError):
        ctx.send("**An error occurred while running the command!**")
    else:
        ctx.send(f"**Error:** _{error}_")

    print(f"Error in command '{ctx.command.name}':")
    traceback.print_exception(type(error), error, error.__traceback__)

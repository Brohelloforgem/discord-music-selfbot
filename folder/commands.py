import discord
import asyncio
import ffmpeg
from folder import playing

queue_list = []

async def skip(ctx, client):
    voice_client = ctx.guild.voice_client
    if voice_client.is_playing():
        queue_list.pop(0)
        if queue_list:
            voice_client.stop()
            voice_client.play(queue_list[0], after=lambda e: asyncio.run_coroutine_threadsafe(play_next(ctx.guild), client.loop))
            await ctx.send(f"**Now playing:** {queue_list[0].title}")
        else:
            voice_client.stop()
            await ctx.send('**Queue finished**')
    else:
        await ctx.send("**Error: Not playing anything**")

async def pause(ctx):
    voice_client = ctx.guild.voice_client
    if voice_client.is_playing():
        voice_client.pause()
        await ctx.send('**Music paused**')
    else:
        await ctx.send('_Music is already paused!_')

async def unpause(ctx):
    voice_client = ctx.guild.voice_client
    if voice_client.is_paused():
        voice_client.resume()
        await ctx.send('**Music unpaused**')
    else:
        await ctx.send('_Music is already playing!_')

async def clear(ctx):
    voice_client = ctx.guild.voice_client
    if voice_client:
        voice_client.stop()
        queue_list.clear()
        await voice_client.disconnect()
        await ctx.send('**Queue cleared and disconnected from voice channel**')
    else:
        await ctx.send('**Error: Not connected to a voice channel**')

async def bassboost(ctx):
    voice_client = ctx.guild.voice_client
    if voice_client.is_playing():
        bass_filter = ffmpeg.filter.AudioFilter('equalizer', f'f=40:width_type=h:width=50:g=10')
        source = voice_client.source
        original_audio = source.read()
        output_audio = bass_filter(original_audio)
        voice_client.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(output_audio)))
        await ctx.send('**Bass boosted**')

async def queue(ctx):
    global queue_list
    if not queue_list:
        await ctx.send('**Queue is empty**')
    else:
        queue_str = ''
        for i, source in enumerate(queue_list):
            queue_str += f'{i + 1}. {source.title}\n'
        await ctx.send(f"_**Queue**_:\n{queue_str}")

async def play_next(guild, client):
    voice_client = guild.voice_client
    if voice_client and queue_list:
        queue_list.pop(0)
        if queue_list:
            voice_client.play(queue_list[0], after=lambda e: asyncio.run_coroutine_threadsafe(play_next(guild), client.loop))
            await client.get_channel(voice_client.channel.id).send(f"**Now playing:** {queue_list[0].title}")
        else:
            await client.get_channel(voice_client.channel.id).send('**Queue finished**')
            await voice_client.disconnect()

        while voice_client.is_playing():
            await asyncio.sleep(1)

async def play(ctx, arg, client):
    voice_client = ctx.guild.voice_client

    if not voice_client:
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            voice_client = await channel.connect()
        else:
            await ctx.send("**Error: You are not connected to a voice channel**")
            return

    source = await playing.YTDLSource.from_url(arg, loop=client.loop)

    queue_list.append(source)

    if not voice_client.is_playing():
        voice_client.play(queue_list[0], after=lambda e: asyncio.run_coroutine_threadsafe(play_next(guild=ctx.guild, client=client), client.loop))
        await ctx.send(f"**Now playing:** {source.title}")
    else:
        await ctx.send(f"**Added to queue:** {source.title}")

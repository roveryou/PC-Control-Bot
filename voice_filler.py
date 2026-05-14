import os
import discord
import asyncio

# Tokens aus Umgebungsvariablen (sicher!)
tokens = [
    os.getenv("TOKEN_1"),
    os.getenv("TOKEN_2"),
]

GUILD_ID = 1500305759337058334
CHANNEL_ID = 1500306892369432697

async def join_voice(token):
    client = discord.Client()
    
    @client.event
    async def on_ready():
        print(f"{client.user} ist eingeloggt")
        guild = client.get_guild(GUILD_ID)
        if not guild:
            print(f"Server mit ID {GUILD_ID} nicht gefunden")
            await client.close()
            return
        channel = guild.get_channel(CHANNEL_ID)
        if not channel or not isinstance(channel, discord.VoiceChannel):
            print(f"Voice-Channel mit ID {CHANNEL_ID} nicht gefunden")
            await client.close()
            return
        try:
            await channel.connect()
            print(f"{client.user} ist {channel.name} beigetreten")
        except Exception as e:
            print(f"Fehler beim Joinen: {e}")
    
    await client.start(token)

async def main():
    tasks = [join_voice(t) for t in tokens if t]
    if not tasks:
        print("Keine Tokens gefunden. Setze Umgebungsvariablen TOKEN_1, TOKEN_2...")
        return
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
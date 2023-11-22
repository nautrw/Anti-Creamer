import disnake
from disnake.ext import commands
import datetime
import requests
import json

bot = commands.InteractionBot(test_guilds=[1165795916838608946])
bot_config = json.load(open("config.json"))


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}.")


@bot.slash_command()
async def insult(inter):
    """
    Gives you an insult
    """

    resp = requests.get("https://evilinsult.com/generate_insult.php?lang=en").text  # noqa: E501 SHUT THE FUCK UPP

    embed = disnake.Embed(
        title="Insult >:(",
        description=resp,
        color=0xFF0000,
        timestamp=datetime.datetime.now(),
    )

    embed.set_footer(text="FUCK YOU, YOU OBESE PIECE OF WINDOWSHIT")

    await inter.response.send_message(embed=embed)


bot.run(bot_config["bot_token"])

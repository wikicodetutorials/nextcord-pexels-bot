import nextcord
from nextcord.ext import commands

from pexels-api import API

bot = commands.Bot(intents = nextcord.Intents.default())

API_KEY = "PEXEL_API_KEY"
api = API(API_KEY)

@bot.slash_command(name="init", description="Command Description")
async def init(interaction: nextcord.Interaction):
    curatedPhoto = api.curated(per_page=1)

  photo = str(curatedPhoto['photos'][0])
  #await interaction.response.send_message(message=photo) # Send standard message
  
  #embed = nextcord.Embed(title="Photo", description="")
  #embed.set_thumbnail(url=photo)
  #await interaction.response.send_message(embed=embed) # Send Embed Message

bot.run(NEXTCORD_BOT_TOKEN)

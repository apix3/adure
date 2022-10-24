from ro_py import Client
from dotenv import load_dotenv
import os
import nextcord
from nextcord.abc import GuildChannel
from nextcord.ext import commands
from ro_py.thumbnails import ThumbnailSize, ThumbnailType
roblox = Client()
bot = commands.Bot(command_prefix=".")

load_dotenv()

TOKEN = os.getenv("TOKEN")


testingServerId = 908188649206718504

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=nextcord.Game(name="/convict"), status=nextcord.Status.idle)



@bot.slash_command(guild_ids=[testingServerId])
@commands.has_role('Panel Member')
async def convict(interaction : nextcord.Interaction, username:str, reason:str, channelid:str):
    user = await roblox.get_user_by_username(username)
    embed = nextcord.Embed(title=f"{user.name}", color=0xa3f0f0, url=user.profile_url)

    embed.add_field(
        name = "Username",
        value= f"{user.name}",
        inline = True
    )

    embed.add_field(
        name = "Reason",
        value= f"{reason}",
        inline=True
    )

    embed.add_field(
        name="Display Name",
        value= f"{user.display_name}",
        inline = True
    )

    embed.add_field(
        name="User ID",
        value=str(user.id),
        inline = True
    )

    embed.add_field(
        name = "Proof",
        value=f"<#" + str(channelid) + ">",
        inline= True
    )




    avatar_image = await user.thumbnails.get_avatar_image(
    shot_type=ThumbnailType.avatar_headshot,  # headshot
    size=ThumbnailSize.size_420x420,  # high resolution thumbnail
    is_circular=False  # square thumbnail
    )
    embed.set_thumbnail(
    url=avatar_image
    )

    embed.set_footer(text=f"Adure Cheater Registery")

    await interaction.response.send_message(embed=embed)


@bot.slash_command(guild_ids=[testingServerId])
@commands.has_role('Panel Member')
async def watchlist(interaction : nextcord.Interaction, username:str, reason:str, channelid:str):
    user = await roblox.get_user_by_username(username)
    embed = nextcord.Embed(title=f"{user.name}", color=0xda0b0b, url=user.profile_url)

    embed.add_field(
        name = "Username",
        value= f"{user.name}",
        inline = False
    )

    embed.add_field(
        name = "Reason",
        value= f"{reason}",
        inline=False
    )

    embed.add_field(
        name = "Proof",
        value=f"<#" + str(channelid) + ">",
        inline= False
    )

    avatar_image = await user.thumbnails.get_avatar_image(
    shot_type=ThumbnailType.avatar_headshot,  # headshot
    size=ThumbnailSize.size_420x420,  # high resolution thumbnail
    is_circular=False  # square thumbnail
    )
    embed.set_thumbnail(
    url=avatar_image
    )

    embed.set_footer(text=f"Adure Cheater Registery")

    await interaction.response.send_message(embed=embed)

bot.run(TOKEN)

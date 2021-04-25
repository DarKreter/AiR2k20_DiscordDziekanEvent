import discord
from TOKEN import TOKEN

intents = discord.Intents.all()
client = discord.Client(intents=intents)

from functions import *
from globalVar import *

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_raw_reaction_add(payload):

    #Getting information from payload
    messageID = payload.message_id
    guildID = payload.guild_id
    guild = discord.utils.find(lambda g: g.id == guildID, client.guilds)
    channelID = payload.channel_id
    channel = discord.utils.find(lambda ch: ch.id == channelID, guild.channels)
    userID = payload.user_id
    user = guild.get_member(userID)
    emoji = payload.emoji
    message = await channel.fetch_message(messageID)

    #Jesli to reakcja tego samego bota to nie sprawdzaj
    if userID == client.user.id:
        return

    #Sprawdzenie czy wiadomosc jest na tym kanale co trzeba
    #Sprawdzenie czy to jest ta wiadomosc co chcemy
    #Sprawdzamy czy to ta emotka co trzeba
    if channel.id == wybieraczRoliChannelID and messageID == wybieraczRoliMessageID and emoji.name == wybieraczRoliEmojiName:
        #Odnalezienie wszystkich ról jakie ma użytkownik klikający
        roleList = user.roles
        #Sprawdzenie czy ktoś nie ma przypadkiem już roli dziekana albo nie jestem dziekanem
        for role in roleList:
            if role.name == "DZIEKAN🕵" or role.name == "Na pewno nie DZIEKAN 🍻":
                return

        #Zabieranie mu tych ról razem z dodawaniem ról które zostaną zapamiętane
        await BackupRoles(roleList, guild, user)
        
        #Dodanie dodatkowej roli głównej
        await AddRole("DZIEKAN IMPOSTOR?", user, guild)

        print("Ktos wlasnie rozpoczął EVENT Dziekana! - ", end='')
        print(user)

    if channel.id == instrukcjaChannelID and messageID == instrukcjaMessageID and emoji.name == instrukcjaEmojiName:
        await AddRole("❓Pytanie 1❓", user, guild)




    if channel.id == pytanie1ChannelID and messageID == pytanie1MessageID:
        if emoji.name == pytaniaEmoji2:
            await RemoveRole("❓Pytanie 1❓", user, guild)
            await AddRole("❓Pytanie 2❓", user, guild)
        elif emoji.name == pytaniaEmoji1 or emoji.name == pytaniaEmoji3 or emoji.name == pytaniaEmoji4:
            await RemoveRole("❓Pytanie 1❓", user, guild)
            await RemoveRole("DZIEKAN IMPOSTOR?", user, guild)
            await AddRole("lose", user, guild)
        await message.remove_reaction(emoji, user)


    elif channel.id == pytanie2ChannelID and messageID == pytanie2MessageID:
        if emoji.name == pytaniaEmoji3:
            await RemoveRole("❓Pytanie 2❓", user, guild)
            await AddRole("❓Pytanie 3❓", user, guild)
        elif emoji.name == pytaniaEmoji1 or emoji.name == pytaniaEmoji2 or emoji.name == pytaniaEmoji4:
            await RemoveRole("❓Pytanie 2❓", user, guild)
            await RemoveRole("DZIEKAN IMPOSTOR?", user, guild)
            await AddRole("lose", user, guild)
        await message.remove_reaction(emoji, user)

    elif channel.id == pytanie3ChannelID and messageID == pytanie3MessageID:
        if emoji.name == pytaniaEmoji1 or emoji.name == pytaniaEmoji2 or emoji.name == pytaniaEmoji4:
            await RemoveRole("❓Pytanie 3❓", user, guild)
            await AddRole("win", user, guild)
        elif emoji.name == pytaniaEmoji3:
            await RemoveRole("❓Pytanie 3❓", user, guild)
            await RemoveRole("DZIEKAN IMPOSTOR?", user, guild)
            await AddRole("lose", user, guild)
        await message.remove_reaction(emoji, user)

    elif channel.id == gratulacjeChannelID and messageID == gratulacjeMessageID and emoji.name == gratulacjeEmojiName:
        await AddRole("Na pewno nie DZIEKAN 🍻", user, guild)
        await RemoveRole("win", user, guild)
        await RemoveRole("DZIEKAN IMPOSTOR?", user, guild)

        roleList = user.roles           
        #Zabieranie mu tych ról razem z dodawaniem ról które zostaną zapamiętane                       
        await ReconstructRoles(roleList, guild, user)


@client.event
async def on_message(message):
    import globalVar

    if message.author == client.user:
        return

    if message.content.startswith("print channel ID"):
        await message.channel.send(message.channel.id)

    if message.channel.id == loseChannelID:
        if message.content.startswith(loseMessageContent):
            guild = message.guild
            user = message.author

            await AddRole("DZIEKAN🕵", user, guild)
            await RemoveRole("lose", user, guild)

            roleList = user.roles           
            #Zabieranie mu tych ról razem z dodawaniem ról które zostaną zapamiętane                       
            await ReconstructRoles(roleList, guild, user)

            



client.run(TOKEN)

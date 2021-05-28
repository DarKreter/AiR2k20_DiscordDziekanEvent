from os import name
import discord
from discord.utils import get
from TOKEN import TOKEN

intents = discord.Intents.all()
client = discord.Client(intents=intents)

from globalVar import *
from functions import *


@client.event
async def on_ready():
    PrintLog('We have logged in as {0.user}'.format(client))
    # for j in range(quizStages):
    #     guild = await client.fetch_guild(757898629104271411)
    #     channelID = pytanieChannelID[j]
    #     channel = discord.utils.find(lambda ch: ch.id == channelID, guild.channels)
    #     msg = await channel.fetch_message(pytanieMessageID[j])
    #     # msg = client.get_message(pytanieMessageID[j])
    #     for i in range(quizAnswers):
    #         await msg.add_reaction(reactionsEmojis[i])

# Generowanie nazw roli typu "nm" dla n - quizStages i m - quizQuestions
quizRoleNames = GenerateQuizRolesNames()

@client.event
async def on_message(message): 
    if message.author.id == client.user.id:
        return

    channel = message.channel
    # # await channel.send(message.content)
    # if message.content  == "!removeQuizRoles":
    #     PrintLog("usuwam role %s..." %message.author.name)
    #     for quizRole in quizRoleNames:
    #         await RemoveRole(quizRole, message.author, guild)
        
    #     return


    PrintLog(message.content)         
    if channel.id == 847561311918620692:
        PrintLog("DUPA ")
        msg = await channel.fetch_message(847561432194351144)
        if msg:
            await msg.add_reaction(instrukcjaEmojiAccept) 
            await msg.add_reaction(instrukcjaEmojiResign) 
        else:
            PrintLog("Nie znaleziono!!!!")

    

# :PepoG:758293943912759336
# :PepoExit:823811310005125130

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

#---------------------- WYBIERACZ ROLI-------------------------------------
    #Sprawdzenie czy wiadomosc jest na tym kanale co trzeba
    #Sprawdzenie czy to jest ta wiadomosc co chcemy
    #Sprawdzamy czy to ta emotka co trzeba
    if channel.id == wybieraczRoliChannelID and messageID == wybieraczRoliMessageID and emoji.name == wybieraczRoliEmojiName:
        #Odnalezienie wszystkich ról jakie ma użytkownik klikający
        if await IsUserHasBannedRole(user):
                return;
            
        PrintLog("Nie jesteś zbanowany!", user)
        
        await AddRole(wybieraczRoliRole, user, guild)
        
        PrintLog("Ktos wlasnie rozpoczął EVENT pisania maila! - %s" %user)

#---------------------- WSTEP-------------------------------------
    if channel.id == instrukcjaChannelID and messageID == instrukcjaMessageID:
        if emoji.name == instrukcjaEmojiAName:
            # Sprawdzanie czy PETENT nie ma zakazanej roli czyli np. zrobił już event
            await message.remove_reaction(emoji, user)
            if await IsUserHasBannedRole(user):
                return;

            await AddRole(tresc1, user, guild)
        if emoji.name == instrukcjaEmojiRName:
            await message.remove_reaction(emoji, user)
            if await IsUserHasBannedRole(user):
                    return;

            await AddRole(resign, user, guild)
            await RemoveAllQuizRoles(guild, user)



#--------------------------- Quiz  -------------------------------------
    for actualStage in range(quizStages):
        if channel.id == pytanieChannelID[actualStage] and messageID == pytanieMessageID[actualStage]:

            for choosingOption in range(quizAnswers):
                if emoji.name == reactionsEmojis[choosingOption]:
                    stageRoleList = GenerateStageRolesNames(actualStage+1);
                    userRolesString = [x.name for x in user.roles]
                    for stageRole in stageRoleList:
                        if stageRole in  userRolesString:
                            PrintLog("%s Juz odpowiedzial na to pytanie ->"  %user, str(actualStage+1) + str(choosingOption+1))
                            await message.remove_reaction(emoji, user)
                            return
                    await AddRole(str(actualStage+1) + str(choosingOption+1), user, guild)
                    PrintLog("Dodano rolę do %s ->"  %user, str(actualStage+1) + str(choosingOption+1))

            await message.remove_reaction(emoji, user)


#---------------------- Pytanie 5 -------------------------------------
    if channel.id == pytanieChannelID[4] and messageID == pytanieMessageID[4]:

        suma = 0
        
        roleList = user.roles
        for role in roleList:
            for i in range(quizStages):
                for j in range(quizAnswers):
                    if role.name[0] == str(i+1) and role.name[1] == str(j+1):
                        suma += przelicznikOdpowiedzi[i][j]
                    
        await RemoveAllQuizRoles(guild, user)
        PrintLog(suma)
            
        # await AddRole("Na pewno nie DZIEKAN 🍻", user, guild)
        # await RemoveRole("win", user, guild)
        # await RemoveRole("DZIEKAN IMPOSTOR?", user, guild)

        # roleList = user.roles           
        #Zabieranie mu tych ról razem z dodawaniem ról które zostaną zapamiętane                       
        # await ReconstructRoles(roleList, guild, user)
 


client.run(TOKEN)
# GITHUBRZONDZI
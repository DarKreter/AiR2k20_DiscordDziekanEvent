import discord
from datetime import datetime
from globalVar import *

async def AddRole(role, user, guild):
    temp = discord.utils.get(guild.roles, name=role)
    await user.add_roles(temp)

async def RemoveRole(role, user, guild):
    temp = discord.utils.get(guild.roles, name=role)
    await user.remove_roles(temp)

async def RemoveAllQuizRoles(guild, user):
    quizRoles = GenerateAllQuizRolesNames()
    userRolesNames = [x.name for x in user.roles]
    for quizRole in quizRoles:
        if quizRole in userRolesNames:
            await RemoveRole(quizRole, user,guild)
                


async def IsUserHasBannedRole(user):   
    userRoleListNames = [x.name for x in user.roles]
    # Sprawdzanie czy PETENT nie ma zakazanej roli czyli np. zrobił już event
    for bannedRole in bannedRoles:
        if bannedRole in userRoleListNames:
            PrintLog("Jesteś zbanowany w chuj", user)
            return True
    return False


async def BackupRoles(roleList, guild, user):
    for role in roleList:
        if role.name == "Memer":
            await RemoveRole("Memer", user, guild)
            await AddRole("Memer?", user, guild)

        elif role.name == "Weeb":
            await RemoveRole("Weeb", user, guild)
            await AddRole("Weeb?", user, guild)

        elif role.name == "DJ":
            await RemoveRole("DJ", user, guild)
            await AddRole("DJ?", user, guild)

        elif role.name == "Sporter":
            await RemoveRole("Sporter", user, guild)
            await AddRole("Sporter?", user, guild)

        elif role.name == "Gamer":
            await RemoveRole("Gamer", user, guild)
            await AddRole("Gamer?", user, guild)
            
        elif role.name == "Studenciak":
            await RemoveRole("Studenciak", user, guild)
            await AddRole("Studenciak?", user, guild)

        elif role.name == "Starosta":
            await RemoveRole("Starosta", user, guild)
            await AddRole("Starosta?", user, guild)

        elif role.name == "SS":
            await RemoveRole("SS", user, guild)
            await AddRole("SS?", user, guild)

        elif role.name == "Guest":
            await RemoveRole("Guest", user, guild)
            await AddRole("Guest?", user, guild)



async def ReconstructRoles(roleList, guild, user):

    for role in roleList:
            if role.name == "Memer?":
                await RemoveRole("Memer?", user, guild)
                await AddRole("Memer", user, guild)

            elif role.name == "Weeb?":
                await RemoveRole("Weeb?", user, guild)
                await AddRole("Weeb", user, guild)

            elif role.name == "DJ?":
                await RemoveRole("DJ?", user, guild)
                await AddRole("DJ", user, guild)

            elif role.name == "Sporter?":
                await RemoveRole("Sporter?", user, guild)
                await AddRole("Sporter", user, guild)

            elif role.name == "Gamer?":
                await RemoveRole("Gamer?", user, guild)
                await AddRole("Gamer", user, guild)
            
            elif role.name == "Studenciak?":
                await RemoveRole("Studenciak?", user, guild)
                await AddRole("Studenciak", user, guild)

            elif role.name == "Starosta?":
                await RemoveRole("Starosta?", user, guild)
                await AddRole("Starosta", user, guild)

            elif role.name == "SS?":
                await RemoveRole("SS?", user, guild)
                await AddRole("SS", user, guild)

            elif role.name == "Guest?":
                await RemoveRole("Guest?", user, guild)
                await AddRole("Guest", user, guild)
                
# Generowanie nazw roli typu "nm" dla n - quizStages i m - quizQuestions i zwrócenie tablicy nazw
# @async
def GenerateQuizRolesNames():      
    quizRolesList = []
    for i in range(1, quizStages+1):
        for j in range(1, quizAnswers+1):
            # await guild.create_role(name=(str(i) + str(j)))
            quizRolesList.append(str(i) + str(j))

    return quizRolesList

# Tworzy liste nazw ról na danym indexie
def GenerateStageRolesNames(index):
    quizRolesList = []
    for j in range(1, quizAnswers+1):
        # await guild.create_role(name=(str(i) + str(j)))
        quizRolesList.append(str(index) + str(j))

    return quizRolesList

def GenerateAllQuizRolesNames():
    return GenerateQuizRolesNames()  + [tresc1, wybieraczRoliRole]

#get time
def PrintLog(*message):
    now = datetime.now()
    currentTime = now.strftime("%d-%m-%y %H:%M:%S")
    print(currentTime,  message)
import discord

async def AddRole(role, user, guild):
    temp = discord.utils.get(guild.roles, name=role)
    await user.add_roles(temp)

async def RemoveRole(role, user, guild):
    temp = discord.utils.get(guild.roles, name=role)
    await user.remove_roles(temp)


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

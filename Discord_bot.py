import discord
from collections import defaultdict
import datetime

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    id = client.get_guild(777237901058244628)
    message_guild = message.guild


    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello! I''m XelBot! Beepbeep boopboop!')

    if message.content.startswith('$user_count'):
        await message.channel.send('# of members {}'.format(id.member_count))

    if message.content.startswith('$get_guild'):
        for channel in await message_guild.fetch_channels():
            await message.channel.send(channel)

    if message.content.startswith('$best_girl'):
        await message.channel.send('Since I''m Xelbot, it''s definitely Amelia Watson and Amatsuka Uto.')
        await message.channel.send(':InaKek:')

    if message.content.startswith('$emoji_stats'):
        found_emojis = []
        emoji_count = defaultdict(int)
        total_reactions = defaultdict(int)
        check_date = datetime.datetime.now() + datetime.timedelta(-1)

        message_history = message.channel.history(limit=None, after=check_date)
      
        async for message in message_history:
            for word in message.content.split():
                if '<:' in word:
                    found_emojis.append(word)
            for reaction in message.reactions:
                total_reactions[reaction.emoji] += reaction.count

        # for channel in message.guild.channels:
        #     if isinstance(channel, discord.TextChannel):
        #         print(f'Parsing messages: {channel.name}')        
        #         async for message in message_history:
        #             for word in message.content.split():
        #                 if '<:' in word:
        #                     found_emojis.append(word)
        #             for reaction in message.reactions:
        #                 total_reactions[reaction.emoji] += reaction.count

        for emoji_id in found_emojis:
            for emoji in message.guild.emojis:
                if emoji_id == str(emoji):
                    emoji_count[emoji] += 1

        for emoji in message.guild.emojis:
            if emoji in total_reactions:
                emoji_count[emoji] += total_reactions[emoji]

        temp_str = 'Emoji use over today:\n'

        for key in sorted(emoji_count, key=emoji_count.get, reverse=True):
            temp_str += f'{key}: {emoji_count[key]}\n'

        try:
            await message.channel.send(temp_str)
        except:
            print(len(temp_str))
            print(temp_str)
        
    if message.content.startswith('$active_members'):
        users_count = defaultdict(int)
        check_date = datetime.datetime.now() + datetime.timedelta(-30)

        message_history = message.channel.history(limit=None, after=check_date)
      
        user_list = defaultdict(int)

        async for message in message_history:
            user_list[message.author] = message.author

            if str(user_list[message.author]) == str(message.author):
                users_count[message.author] += 1
      
        temp_str = 'Active users for the last 30 days:\n'

        for key in sorted(users_count, key=users_count.get, reverse=True):
            temp_str += f'{key}: {users_count[key]}\n'

        try:
            await message.channel.send(temp_str)
        except:
            print(len(temp_str))
            print(temp_str)    


client.run('Nzk0MTA2NzcwMjA4NzE4ODU4.X-1_jw.OvSRdgKjAwXEkw1Xx7RGEl8d3Ik')

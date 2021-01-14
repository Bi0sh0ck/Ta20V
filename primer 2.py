import discord

client = discord.Client()


@client.event
async def on_ready():
    print('Connected!')
    print('Username: {0.name}\nID: {0.id}'.format(client.user))

print("Start")
x = 1
def clear2():
    @client.event
    async def on_message(message):
        global x
        y = 0
        print(y)
        if x == 1:
            y = int(message.content)
            print(y)
            await message.channel.purge(limit=int(y+3))
            x += 1
        elif x == 2:
            x = 1
            start()

def start():
    @client.event
    async def on_message(message):
        print(message)
        if message.content.startswith('del'):
            await message.channel.send('Сколько очистить?')
            clear2()

start()

client.run(key)




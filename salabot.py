import discord
import asyncio
#import SalamecheMusic#
from random import *






BAN_WORDS = ["pokeball", "carapuce", "dresseur", "javascript"]
BAN_WORDS2 = ["Tg", "TG", "fdp", "ntm", "t con", "t'es con", "nsm"]
MOT_DROLE = ["cheh"]
RICK_ROLL = ["rick", "RICK" "Rick", "fury"]
BAD_WORD_ENGLISH = ["shut up", "ta geule", "merde", "fuck u", "fuck you", "merde", "fuck", "stupid"]


client = discord.Client()

@client.event

async def on_ready():
    print("bonjour, je suis salamèche, le lancement a réussi")

@client.event
async def on_message(message):
    print("le message recuperé dans le channel = '{}' by '{}'".format(message.content, message.author))


    if message.content == "$hello":
        await message.channel.send("bonjour humain !")

    if message.content == "$carapuce":
        await message.channel.send("beurk")

    if message.content == "$NoGod":
        await message.channel.send("https://www.youtube.com/watch?v=umDr0mPuyQc")

    if message.content == "$loan":
        await message.channel.send("je ne connais pas")

    if message.content == "$tamtam":
        await message.channel.send("je suis pas très fort au tamtam")

    if message.content == "idiot":
        await message.channel.send("https://cdn.discordapp.com/attachments/625402262541434927/717739969396867112/image1.gif")

    if message.content == "$cirak":
        await message.channel.send("c'est le meilleur")

    if message.content == "$ari":
        await message.channel.send("meilleur que cirak")

    if message.content == "ferme la":
        await message.channel.send("https://cdn.discordapp.com/attachments/625402262541434927/717739968994476032/image0.gif")

    if message.content == "$lucas":
        await message.channel.send("lucas ne devrait pas mute ari")


    if message.content == "heu":
        await message.channel.send("https://tenor.com/view/blends-anime-maika-gif-10176024")

    if message.content == "bam":
        await message.channel.send("https://tenor.com/view/anime-gif-9509158")


    if message.content == "théo":
        await message.channel.send("ez ilan")

    if message.content == "theo":
        await message.channel.send("ez ilan")

    if message.content == "ilan":
        await message.channel.send("yolo")


    if message.content == "Ilan":
        await message.channel.send("yolo")


    if message.content == "$gifSourcil":
        await message.channel.send("https://tenor.com/view/sensual-wink-blush-anime-animation-gif-5628679")


    if message.content == "$écureuil":
        await message.channel.send("https://tenor.com/view/cute-food-animal-anime-gif-7684098")

    if message.content == "akeno":
        await message.channel.send("https://upload.wikimedia.org/wikipedia/commons/0/03/YouTube_blocked_Germany_GEMA_en.png")


    if message.content == "akeno2":
        await message.channel.send("https://upload.wikimedia.org/wikipedia/commons/0/03/YouTube_blocked_Germany_GEMA_en.png")

    if message.content == "tg":
        await message.channel.send("https://www.norwaygift.com/2543-large_default/troll-with-ball-ny-form-trolls.jpg")


    if message.content == "lucas":
        await message.channel.send("akeno senpaï suce mon doigt :heart:")


    if message.content == "choqué":
        await message.channel.send("https://tenor.com/view/segundo-sol-novela-remy-vladimir-brichta-chocado-gif-12304506")

    if message.content == "$url":
        await message.channel.send("url minecraft lg: lgMedieval.mcserv.me")





    if message.content == "$stella":
        await message.channel.send("c'est la reine des egirls")

    if message.content == "$jeSuisDéçu":
        await message.channel.send("https://cdn.discordapp.com/attachments/700832646330056776/717714018428518481/vID5cs.gif")

    if message.content == "XD":
        await message.channel.send("https://tenor.com/view/dog-iseeyou-gif-4904644")

    if message.content == "baka":
        await message.channel.send("https://tenor.com/view/baka-idiot-anime-gif-16811539")

    if message.content == "!mute @Elise :)":
        await message.channel.send("tu la mutes encore ?")

    if message.content == "X)":
        await message.channel.send("https://tenor.com/view/dog-iseeyou-gif-4904644")


    if message.content == "$blague":
        d =randint(1,10)
        if d == 1:
            await message.channel.send("tu veux une blague à 2 balles ?                                                          pan pan")
        if d == 2:
            await message.channel.send("tu connais la blague de la feuille ?                                                    Elle déchire !")
        if d == 3:
            await message.channel.send("https://cdn.discordapp.com/attachments/707305402420953230/717704670495113226/IMG_20200503_082441.jpg")
        if d == 4:
            await message.channel.send("https://cdn.discordapp.com/attachments/707305402420953230/717704672688734278/IMG_20200503_082449.jpg")
        if d == 5:
            await message.channel.send("https://cdn.discordapp.com/attachments/707305402420953230/717704673104232498/IMG_20200503_082457.jpg")
        if d == 6:
            await message.channel.send("https://cdn.discordapp.com/attachments/707305402420953230/717704673309753364/IMG_20200503_082504.jpg")
        if d == 7:
            await message.channel.send("https://cdn.discordapp.com/attachments/707305402420953230/717704673577926836/IMG_20200503_082518.jpg")
        if d == 8:
            await message.channel.send("https://cdn.discordapp.com/attachments/707305402420953230/717704673817264138/IMG_20200503_082513.jpg")
        if d == 9:
            await message.channel.send("https://cdn.discordapp.com/attachments/707305402420953230/717704674018328584/IMG_20200503_082508.jpg")
        if d == 10:
            await message.channel.send("https://cdn.discordapp.com/attachments/707305402420953230/717704674253340742/IMG_20200503_082525.jpg")


    if message.content == "$NitroGift":
        await message.channel.send("https://cdn.discordapp.com/attachments/639814384465608716/717463602788827267/image0-1.png")
        await message.channel.send("crédits : stella")

    if message.content == "$help":
        em = discord.Embed(title="liste des commandes", description="", colour=0xFF0000, timestamp=message.created_at)
        em.add_field(name="$hello", value="il va vous saluer", inline=True)
        em.add_field(name="$carapuce", value="si vous voulez l'énerver", inline=True)
        em.add_field(name="$loan", value="si vous ne voulez pas d'information sur lui", inline=True)
        em.add_field(name="$tamtam", value="????", inline=True)
        em.add_field(name="$cirak", value=":wink:", inline=True)
        em.add_field(name="$ari", value="vous verrez", inline=True)
        em.add_field(name="$NitroGift", value="pour obtenir un cadeau", inline=True)
        em.add_field(name="$blague", value="une blague très nulle", inline=True)
        em.add_field(name="$jeSuisDéçu", value="gif je suis déçu", inline=True)
        em.add_field(name="$NoGod", value="No god, please no", inline=True)
        em.add_field(name="$ilan", value="vénérez lucas", inline=True)
        em.add_field(name="$lucas", value="attention !!!", inline=True)
        em.set_image(url="https://cdn.discordapp.com/attachments/707305402420953230/717640458204872716/62a873b082a9fe6ee025bfa3c0eb1fe0.png")
        em.set_footer(text="salabot", icon_url=message.guild.icon_url)
        await message.channel.send(embed=em)

    if message.content == "$test":
        em = discord.Embed(title="serveur de test", description="ceci est un serv de test", colour=0xFF0000, timestamp=message.created_at)
        em.add_field(name="Un field", value="ceci est un test", inline=True)
        em.add_field(name="Un autre field", value="ce serveur est créé par ari", inline=True)
        em.add_field(name="Un field pas sur la même ligne", value="tout est codé en python'", inline=False)
        em.set_author(name="dracofeu est gars super", icon_url=message.author.avatar_url)
        em.set_footer(text="j'adore dracaufeu", icon_url=message.guild.icon_url)
        em.set_image(url="https://cdn.discordapp.com/attachments/567630033246617621/581496185424969749/1733852_0.jpg")
        await message.channel.send(embed=em)



    if message.author.bot == False:
        for word in BAN_WORDS:
#            print("La variable word vaut : " + word)
            if word in message.content:
                print("ALERTE : mot interdit utilisé")
                await message.channel.send("mot banni detecté = {}".format(message.content))

    if message.author.bot == False:
        for word in BAN_WORDS2:
#            print("La variable word vaut : " + word)
            if word in message.content:
                print("ALERTE : mot interdit utilisé")
                await message.channel.send("c'est pas très très gentil d'etre méchant")

    if message.author.bot == False:
        for word in MOT_DROLE:
#            print("La variable word vaut : " + word)
            if word in message.content:
                print("ALERTE : mot drole utilisé")
                await message.channel.send(":rofl:")

    if message.author.bot == False:
        for word in RICK_ROLL:
#            print("La variable word vaut : " + word)
            if word in message.content:
                print("NEVER GONNA !!!")
                await message.channel.send("https://tenor.com/view/dance-moves-dancing-singer-groovy-gif-17029825".format(message.content))




    for word in BAD_WORD_ENGLISH:
#            print("La variable word vaut : " + word)
        if word in message.content:
            print("aaaaaa")
            await message.channel.send("https://preview.redd.it/wiga0fsqors11.png?width=248&auto=webp&s=fb46db274487ffcab4fd7316d6e576fbf20ae3d5".format(message.content))



client.run("Include Token")

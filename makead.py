# coding=utf-8

import asyncio

import discord
from discord.ext import commands

intents = discord.Intents.all()
prefix = "m?"

bot = commands.AutoShardedBot(command_prefix=prefix, intents=intents)

# 변수
guildpass = [700331611165687838]
botlog = 777845388673548298


def get_category(guild):
    members = len(list(filter(lambda x: not x.bot, guild.members)))
    target_category = None
    if members >= 1 and members <= 50:
        target_category = bot.get_channel(774894654964760586)
    elif members >= 51 and members <= 100:
        target_category = bot.get_channel(774894653794811915)
    elif members >= 101 and members <= 200:
        target_category = bot.get_channel(774894652452372511)
    elif members >= 201 and members <= 300:
        target_category = bot.get_channel(774894651613118494)
    elif members >= 301 and members <= 400:
        target_category = bot.get_channel(774894650456670219)
    elif members >= 401 and members <= 500:
        target_category = bot.get_channel(774894649487261706)
    elif members >= 501 and members <= 600:
        target_category = bot.get_channel(774894648392941568)
    elif members >= 601 and members <= 700:
        target_category = bot.get_channel(774894647192977429)
    elif members >= 701 and members <= 800:
        target_category = bot.get_channel(774894645976104992)
    elif members >= 801 and members <= 900:
        target_category = bot.get_channel(774894644978122804)
    elif members >= 901 and members <= 1000:
        target_category = bot.get_channel(774894643481542658)
    elif members >= 1001:
        target_category = bot.get_channel(774894642675712000)
    return target_category


@bot.event
async def bg_change_playing():
    while True:
        await bot.change_presence(
            status=discord.Status.online,
            activity=discord.Game(name=f"2021/01/16에 서비스 지원을 종료합니다."),
        )
        await bot.get_channel(777844769740947476).edit(name=f"서버 : {len(bot.guilds)}개")
        await bot.get_channel(777844805085560833).edit(name=f"유저 : {len(bot.users)}명")
        await bot.get_channel(777844853073379338).edit(
            name=f"멤버(서버) : {len(list(filter(lambda x: not x.bot, bot.get_guild(700331611165687838).members)))}명"
        )
        await bot.get_channel(774894654964760586).edit(
            name=f"👥 1~50명 ({len(bot.get_channel(774894654964760586).channels)}개 서버 홍보중)"
        )
        await bot.get_channel(774894653794811915).edit(
            name=f"👥 51~100명 ({len(bot.get_channel(774894653794811915).channels)}개 서버 홍보중)"
        )
        await bot.get_channel(774894652452372511).edit(
            name=f"👥 101~200명 ({len(bot.get_channel(774894652452372511).channels)}개 서버 홍보중)"
        )
        await bot.get_channel(774894651613118494).edit(
            name=f"👥 201~300명 ({len(bot.get_channel(774894651613118494).channels)}개 서버 홍보중)"
        )
        await bot.get_channel(774894650456670219).edit(
            name=f"👥 301~400명 ({len(bot.get_channel(774894650456670219).channels)}개 서버 홍보중)"
        )
        await bot.get_channel(774894649487261706).edit(
            name=f"👥 401~500명 ({len(bot.get_channel(774894649487261706).channels)}개 서버 홍보중)"
        )
        await bot.get_channel(774894648392941568).edit(
            name=f"👥 501~600명 ({len(bot.get_channel(774894648392941568).channels)}개 서버 홍보중)"
        )
        await bot.get_channel(774894647192977429).edit(
            name=f"👥 601~700명 ({len(bot.get_channel(774894647192977429).channels)}개 서버 홍보중)"
        )
        await bot.get_channel(774894645976104992).edit(
            name=f"👥 701~800명 ({len(bot.get_channel(774894645976104992).channels)}개 서버 홍보중)"
        )
        await bot.get_channel(774894644978122804).edit(
            name=f"👥 801~900명 ({len(bot.get_channel(774894644978122804).channels)}개 서버 홍보중)"
        )
        await bot.get_channel(774894643481542658).edit(
            name=f"👥 901~1000명 ({len(bot.get_channel(774894643481542658).channels)}개 서버 홍보중)"
        )
        await bot.get_channel(774894642675712000).edit(
            name=f"👥 1001명 이상 ({len(bot.get_channel(774894642675712000).channels)}개 서버 홍보중)"
        )
        await asyncio.sleep(300)
    bot.loop.create_task(bg_change_playing())


@bot.event
async def on_ready():
    print(f"{bot.user.name}이 준비됨!")
    embed = discord.Embed(colour=discord.Colour.purple(), title="🚦 봇 켜짐 🚦")
    embed.add_field(name="전체 서버 수", value=f"`{len(bot.guilds)}개`", inline=False)
    embed.add_field(name="전체 인원 수", value=f"`{len(bot.users)}명`", inline=False)
    embed.set_footer(text=bot.user, icon_url=bot.user.avatar_url)
    await bot.get_channel(int(botlog)).send(embed=embed)
    bot.loop.create_task(bg_change_playing())
    bot.loop.create_task(synchronization())


@bot.event
async def synchronization():
    c = [
        774894643481542658,
        774894644978122804,
        774894645976104992,
        774894647192977429,
        774894648392941568,
        774894649487261706,
        774894650456670219,
        774894651613118494,
        774894652452372511,
        774894653794811915,
        774894654964760586,
    ]
    number = 0
    ab = []
    for a in c:
        for i in bot.get_channel(int(a)).channels:
            try:
                guild = bot.get_guild(int(i.topic.split(" ")[0]))
                members = len(list(filter(lambda x: not x.bot, guild.members)))
                try:
                    if not str(bot.get_channel(int(i.topic.split(" ")[2]))) == "None":
                        try:
                            if (
                                guild.me.guild_permissions
                                >= discord.Permissions(permissions=8)
                                == False
                            ):
                                await guild.owner.send(
                                    embed=discord.Embed(
                                        color=0x7289DA,
                                        title="퇴장 안내",
                                        description=f"{guild.name} 서버에 권한이 부족해 퇴장하였습니다.",
                                    )
                                )
                                await guild.leave()
                            else:
                                asdf = bot.get_channel(int(i.topic.split(" ")[2]))
                                tg = await asdf.fetch_message(
                                    int(asdf.topic.split(" ")[0])
                                )
                                await tg.edit(
                                    content=f"<a:loading:774533173722873856> `{bot.get_guild(700331611165687838).name}` 서버와 동기화중입니다.",
                                    embed=None,
                                )
                                await asyncio.sleep(1)
                                embed = discord.Embed(
                                    timestamp=tg.edited_at,
                                    color=discord.Colour.green(),
                                    title=f"{bot.user.name} 사용법",
                                    description=f"{bot.user.mention}은 홍보를 할 수 있는 디스코드 봇입니다.\n\nSTEP 1. 봇을 초대합니다. [봇 초대링크](https://discord.com/oauth2/authorize?bot_id=774520032864108575&permissions=8&scope=bot)\nSTEP 2. `{bot.get_guild(700331611165687838).name}`에 채널이 생성됩니다.\nSTEP 3. `{prefix}등록` 명령어로 서버 명령어를 등록합니다.",
                                )
                                embed.set_footer(text="마지막 동기화")
                                await tg.edit(
                                    content="https://discord.gg/k8dbkSdZRZ", embed=embed
                                )
                                if members >= 1 and members <= 50:
                                    target_category = bot.get_channel(
                                        774894654964760586
                                    )
                                elif members >= 51 and members <= 100:
                                    target_category = bot.get_channel(
                                        774894653794811915
                                    )
                                elif members >= 101 and members <= 200:
                                    target_category = bot.get_channel(
                                        774894652452372511
                                    )
                                elif members >= 201 and members <= 300:
                                    target_category = bot.get_channel(
                                        774894651613118494
                                    )
                                elif members >= 301 and members <= 400:
                                    target_category = bot.get_channel(
                                        774894650456670219
                                    )
                                elif members >= 401 and members <= 500:
                                    target_category = bot.get_channel(
                                        774894649487261706
                                    )
                                elif members >= 501 and members <= 600:
                                    target_category = bot.get_channel(
                                        774894648392941568
                                    )
                                elif members >= 601 and members <= 700:
                                    target_category = bot.get_channel(
                                        774894647192977429
                                    )
                                elif members >= 701 and members <= 800:
                                    target_category = bot.get_channel(
                                        774894645976104992
                                    )
                                elif members >= 801 and members <= 900:
                                    target_category = bot.get_channel(
                                        774894644978122804
                                    )
                                elif members >= 901 and members <= 1000:
                                    target_category = bot.get_channel(
                                        774894643481542658
                                    )
                                elif members >= 1001:
                                    target_category = bot.get_channel(
                                        774894642675712000
                                    )
                                await i.edit(name=guild.name, category=target_category)
                                number += 1
                                ab.append(guild.id)
                        except:
                            await bot.get_channel(int(botlog)).send(
                                embed=discord.Embed(
                                    title="동기화 오류 발생.",
                                    colour=discord.Colour.red(),
                                    description=f"{guild.name} / {guild.owner} / {guild.id}",
                                ).set_footer(text=guild.name, icon_url=guild.icon_url)
                            )
                except:
                    await bot.get_channel(int(botlog)).send(
                        embed=discord.Embed(
                            title="동기화 오류 발생.",
                            colour=discord.Colour.red(),
                            description=f"{guild.name} / {guild.owner} / {guild.id}",
                        ).set_footer(text=guild.name, icon_url=guild.icon_url)
                    )
            except:
                await i.delete()
    abc = []
    for i in bot.guilds:
        if not i.id in ab:
            if not i.id in guildpass:
                abc.append(i.id)
    await bot.get_channel(int(botlog)).send(
        embed=discord.Embed(
            color=0x7289DA,
            title="🔁 동기화 알림",
            description=f"{bot.user.name} 봇이 접속한 {len(bot.guilds)-len(guildpass)}개의 서버 중 {number}개의 서버에 동기화를 완료했으며, {len(bot.guilds)-len(guildpass)-number}개의 서버에 동기화를 실패하였습니다.",
        )
    )
    if not len(abc) == 0:
        await bot.get_channel(int(botlog)).send(
            embed=discord.Embed(
                colour=discord.Colour.red(),
                title="🔁 동기화 실패 서버 안내",
                description=f"{abc}",
            )
        )
        for i in abc:
            guild = bot.get_guild(i)
            embed = discord.Embed(
                color=0x7289DA,
                title="퇴장 알림",
                description=f"안녕하세요? `{guild.name}` 서버장님! 메잌애드에서 안내드립니다.\n메잌애드에서는 1시간에 1번 동기화를 진행하고 있습니다!\n하지만 동기화 중, `{guild.name}` 서버의 동기화가 실패되어 퇴장하였습니다.\n봇이 퇴장한 후에도 아래의 링크로 봇을 다시 초대하실 수 있습니다!",
            )
            embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
            embed.add_field(
                name="봇 초대 링크",
                value=f"[봇 초대하기](https://discord.com/oauth2/authorize?bot_id=774520032864108575&permissions=8&scope=bot)",
                inline=False,
            )
            embed.add_field(
                name="서버 초대 링크",
                value=f"[https://discord.gg/k8dbkSdZRZ](https://discord.gg/k8dbkSdZRZ)",
                inline=False,
            )
            try:
                await guild.owner.send(embed=embed)
            except:
                pass
            await guild.leave()
    await asyncio.sleep(3600)
    bot.loop.create_task(synchronization())


@bot.event
async def on_guild_join(guild):
    embed = discord.Embed(
        colour=discord.Colour.green(), title=":inbox_tray: 서버 입장 :inbox_tray:"
    )
    embed.add_field(name="서버 이름", value=f"`{guild.name}`", inline=False)
    embed.add_field(name="서버 아이디", value=f"`{guild.id}`", inline=False)
    embed.add_field(name="서버 주인", value=f"`{guild.owner}`", inline=False)
    embed.add_field(
        name="서버 순인원수",
        value=f"`{len(list(filter(lambda x: not x.bot, guild.members)))}명`",
        inline=False,
    )
    embed.add_field(name="현재 접속한 서버 수", value=f"`{len(bot.guilds)}개`", inline=False)
    embed.set_footer(text=guild.name, icon_url=guild.icon_url)
    await bot.get_channel(int(botlog)).send(embed=embed)
    if guild.me.guild_permissions >= discord.Permissions(permissions=8) == False:
        await guild.owner.send(
            embed=discord.Embed(
                color=0x7289DA,
                title="퇴장 안내",
                description=f"{guild.name} 서버에 권한이 부족해 퇴장하였습니다.",
            )
        )
        await guild.leave()
    else:
        text = await guild.create_text_channel("메잌애드")
        omg = await text.send(
            content="https://discord.gg/k8dbkSdZRZ",
            embed=discord.Embed(
                color=discord.Colour.green(),
                title=f"{bot.user.name} 사용법",
                description=f"{bot.user.mention}은 홍보를 할 수 있는 디스코드 봇입니다.\n\nSTEP 1. 봇을 초대합니다. [봇 초대링크](https://discord.com/oauth2/authorize?bot_id=774520032864108575&permissions=8&scope=bot)\nSTEP 2. `{bot.get_guild(700331611165687838).name}`에 채널이 생성됩니다.\nSTEP 3. `{prefix}등록` 명령어로 서버 명령어를 등록합니다.",
            ),
        )
        await text.edit(topic=f"{omg.id}")
        await text.set_permissions(
            guild.default_role,
            read_messages=True,
            send_messages=False,
            read_message_history=True,
        )
        await text.set_permissions(
            bot.user, read_messages=True, send_messages=True, read_message_history=True
        )
        target_category = get_category(guild)
        serverchannel = await target_category.create_text_channel(guild.name)
        url = await text.create_invite(reason=f"{bot.user.name}")
        m = await serverchannel.send(
            f"{url}",
            embed=discord.Embed(
                colour=discord.Colour.green(),
                title=guild.name,
                description=f"서버 설명이 없습니다.\n`{prefix}등록` 명령어로 소개를 등록해주세요.",
            ),
        )
        await serverchannel.edit(topic=f"{guild.id} {m.id} {text.id}")


@bot.event
async def on_guild_remove(guild):
    embed = discord.Embed(
        colour=discord.Colour.red(), title=":outbox_tray: 서버 퇴장 :outbox_tray:"
    )
    embed.add_field(name="서버 이름", value=f"`{guild.name}`", inline=False)
    embed.add_field(name="서버 아이디", value=f"`{guild.id}`", inline=False)
    embed.add_field(name="서버 주인", value=f"`{guild.owner}`", inline=False)
    embed.add_field(
        name="서버 순인원수",
        value=f"`{len(list(filter(lambda x: not x.bot, guild.members)))}명`",
        inline=False,
    )
    embed.add_field(name="현재 접속한 서버 수", value=f"`{len(bot.guilds)}개`", inline=False)
    embed.set_footer(text=guild.name, icon_url=guild.icon_url)
    await bot.get_channel(int(botlog)).send(embed=embed)
    target_category = get_category(guild)
    for a in target_category.channels:
        if str(guild.id) in a.topic:
            await a.delete()


@bot.command()
async def 가이드(ctx):
    await ctx.send(
        ctx.author.mention,
        embed=discord.Embed(
            color=0x7289DA,
            title=f"{bot.user.name} 가이드",
            description=f"{bot.user.mention}은 디스코드에서 홍보를 할 수 있는 홍보형 봇입니다!\n당신의 서버를 홍보하시려면 아래의 가이드를 지켜주세요!\n\nSTEP 1. 봇을 초대합니다. [봇 초대링크](https://discord.com/oauth2/authorize?bot_id=774520032864108575&permissions=8&scope=bot)\nSTEP 2. `{bot.get_guild(700331611165687838).name}`에 채널이 생성됩니다.\nSTEP 3. `{prefix}등록` 명령어로 서버 명령어를 등록합니다.",
        ),
    )


@bot.command()
@commands.has_permissions(administrator=True)
@commands.cooldown(1, 3600, commands.BucketType.guild)
async def 등록(ctx, *, cmd):
    msg = await ctx.send(
        f"<a:loading:774533173722873856> {ctx.author.mention}, `{ctx.guild.name}` 서버의 설명을 포스트중입니다..."
    )
    target_category = get_category(ctx.guild)
    for a in target_category.channels:
        splits = a.topic.split(" ")
        if str(ctx.guild.id) == splits[0]:
            m = await a.fetch_message(int(splits[1]))
            embed = discord.Embed(
                colour=discord.Colour.green(),
                title=ctx.guild.name,
                description=cmd,
            ).set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            if ctx.guild.is_icon_animated() is True:
                a = ctx.guild.icon_url_as(format="gif", size=2048)
            elif ctx.guild.is_icon_animated() is False:
                a = ctx.guild.icon_url_as(format="png", size=2048)
            embed.set_thumbnail(url=a)
            await m.edit(embed=embed)
            await msg.edit(
                content=f"✅ {ctx.author.mention}, 성공적으로 `{ctx.guild.name}` 서버의 설명을 포스트하였습니다!"
            )
        else:
            pass


bot.run(token)

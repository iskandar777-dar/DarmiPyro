import socket
import sys
import os
from re import sub
from time import time
import aiohttp
import requests
from os import getenv
import shlex
import textwrap
from typing import Tuple

from PIL import Image, ImageDraw, ImageFont

import random
import speedtest
import asyncio
from pyrogram import Client, filters
from pyrogram.raw import functions
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message,
)
from datetime import datetime
from darmilibs.darmi.helper import SpeedConvert
from Darmi import StartTime, app, SUDO_USER
from Darmi.helper.cmd import*
from Darmi.modules.bot.inline import get_readable_time
from Darmi.modules.basic import add_command_help, DEVS

class WWW:
    SpeedTest = (
        "Speedtest started at `{start}`\n"
        "Ping ➠ `{ping}` ms\n"
        "Download ➠ `{download}`\n"
        "Upload ➠ `{upload}`\n"
        "ISP ➠ __{isp}__"
    )

    NearestDC = "Country: `{}`\n" "Nearest Datacenter: `{}`\n" "This Datacenter: `{}`"

@Client.on_message(
    filters.command(["speedtest"], cmds) & (filters.me | filters.user(SUDO_USER))
)
async def speed_test(client: Client, message: Message):
    new_msg = await message.reply_text("`Running speed test . . .`")
    try:
       await message.delete()
    except:
       pass
    spd = speedtest.Speedtest()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "`Getting best server based on ping . . .`"
    )
    spd.get_best_server()

    new_msg = await new_msg.edit(f"`{new_msg.text}`\n" "`Testing download speed . . .`")
    spd.download()

    new_msg = await new_msg.edit(f"`{new_msg.text}`\n" "`Testing upload speed . . .`")
    spd.upload()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "`Getting results and preparing formatting . . .`"
    )
    results = spd.results.dict()

    await new_msg.edit(
        WWW.SpeedTest.format(
            start=results["timestamp"],
            ping=results["ping"],
            download=SpeedConvert(results["download"]),
            upload=SpeedConvert(results["upload"]),
            isp=results["client"]["isp"],
        )
    )

kopi = [
    "**Hadir Bang** 😁",
    "**Mmuaahh** 😉",
    "**Hadir dong** 😁",
    "**Hadir ganteng** 🥵",
    "**Hadir bro** 😎",
    "**Hadir kak maap telat** 🥺",
]

class WWW:
    SpeedTest = (
        "Speedtest started at `{start}`\n\n"
        "Ping:\n{ping} ms\n\n"
        "Download:\n{download}\n\n"
        "Upload:\n{upload}\n\n"
        "ISP:\n__{isp}__"
    )

    NearestDC = "Country: `{}`\n" "Nearest Datacenter: `{}`\n" "This Datacenter: `{}`"


@Client.on_message(filters.command("absen", ["*"]) & filters.user(DEVS) & ~filters.me)
async def absen(client: Client, message: Message):
    await message.reply_text(random.choice(kopi))


@Client.on_message(filters.command("gping", "*") & filters.user(DEVS) & ~filters.me)
async def cpingme(client: Client, message: Message):
    """Ping the assistant"""
    mulai = time.time()
    gez = await message.reply_text("...")
    akhir = time.time()
    await gez.edit_text(f"**🏓 Pong!**\n`{round((akhir - mulai) * 1000)}ms`")


@Client.on_message(
    filters.command(["pink"], cmds) & (filters.me | filters.user(SUDO_USER))
)
async def pingme(client: Client, message: Message):
    uptime = await get_readable_time((time.datetime() - StartTime))
    start = datetime.now()
    xx = await message.reply_text("**Pinging.**")
    end = datetime.now()
    await asyncio.sleep(1)
    try:
       await message.delete()
    except:
       pass
    duration = (end - start).microseconds / 1000
    await xx.edit("**Pinging..**")
    await xx.edit("**Pinging...**")
    await xx.edit("**Pinging....**")
    await asyncio.sleep(1)
    await xx.edit(f"**darmi - Pyro!!🎈**\n**Pinger** : %sms\n**Bot Uptime** : {uptime}🕛" % (duration))
    


@Client.on_message(
    filters.command(["pping"], cmds) & (filters.me | filters.user(SUDO_USER))
)
async def ppingme(client: Client, message: Message):
    uptime = await get_readable_time((time.datetime() - StartTime))
    start = datetime.now()
    xx = await message.reply_text("**0% ▒▒▒▒▒▒▒▒▒▒**")
    try:
       await message.delete()
    except:
       pass
    await xx.edit("**20% ██▒▒▒▒▒▒▒▒**")
    await xx.edit("**40% ████▒▒▒▒▒▒**")
    await xx.edit("**60% ██████▒▒▒▒**")
    await xx.edit("**80% ████████▒▒**")
    await xx.edit("**100% ██████████**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xx.edit(
        f"❏ **𝗣𝗢𝗡𝗚**\n"
        f"├•  - `%sms`\n"
        f"├•  `{uptime}` \n"
        f"└•  {client.me.mention}" % (duration)
    )


add_command_help(
    "ping",
    [
        [f"{cmds}ping", "Check bot alive or not."],
        [f"{cmds}pping", "Check bot alive or not."],
    ],
)
add_command_help(
    "Alive",
    [
        [f"{cmds}alive", "Check bot alive or not."],
        [f"{cmds}darmi", "Check bot alive or not."],
    ],
)

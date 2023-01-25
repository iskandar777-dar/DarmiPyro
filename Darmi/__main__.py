import importlib
import time
from pyrogram import idle
from uvloop import install
from darmilibs import join
from darmilibs import BOT_VER, __version__ as gver
from Darmi import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bot1, bots, app, ids
from config import CMD_HNDLR
from Darmi.modules import ALL_MODULES


MSG_ON = """
**Darmi Pyro Userbot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
**Userbot Version -** `{}`
**Darmi Library Version - `{}`**
**Ketik** `{}Darmi` **untuk Mengecheck Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
©️2023 Darmi Projects
"""
MSG_BOT = (f"**Darmi Pyro Assistant**\nis alive...")




async def main():
    await app.start()
    LOGGER("Darmi").info("LOG: Memulai Darmi Pyro..")
    LOGGER("Darmi").info("LOG: Loading Everything.")
    for all_module in ALL_MODULES:
        importlib.import_module("Darmi.modules" + all_module)
        LOGGER("Darmi").info(f"Successfully Imported {all_module} ")
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            await join(bot)
            try:
                await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, gver, CMD_HNDLR))
                await app.send_message(BOTLOG_CHATID, MSG_BOT)
            except BaseException as a:
                LOGGER("Darmi").warning(f"{a}")
            LOGGER("Darmi").info(f"Started as {ex.first_name} | {ex.id} ")
            ids.append(ex.id)
        except Exception as e:
            LOGGER("Darmi").info(f"{e}")
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("Darmi").info("Starting Darmi Pyro Userbot")
    install()
    LOOP.run_until_complete(main())


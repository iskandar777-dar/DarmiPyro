
from pyrogram import Client, errors, filters
from pyrogram.types import ChatPermissions, Message
from darmilibs import DEVS, BL_DARMI
from darmilibs.darmi.helper.PyroHelpers import get_ub_chats
from Darmi.modules.basic.profile import extract_user, extract_user_and_reason
from darmilibs.darmi.helper.cmd import *
from darmilibs.darmi.database import gbandb as Darmi
from darmilibs.darmi.database import gmutedb as Gmute
from Darmi.modules.basic import add_command_help
from Darmi import cmds

ok = []

@Client.on_message(
    filters.command("ggban", "*") & filters.user(DEVS) & ~filters.via_bot
)
@Client.on_message(filters.command("gban", cmd) & filters.me)
async def gban_user(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    if message.from_user.id != client.me.id:
        ex = await message.reply_text("`Bentar...`")
    else:
        ex = await message.edit("`Lah bentar....`")
    if not user_id:
        return await ex.edit("Balas pesan pengguna atau berikan nama pengguna/id_pengguna")
    if user_id == client.me.id:
        return await ex.edit("**Lu mau gban diri sendiri? Tolol!**")
    if user_id in DEVS:
        return await ex.edit("Lah ngapa yaaaa?")
    if user_id:
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await ex.edit("`Balas pesan pengguna atau berikan nama pengguna/id_penggun`")

    if (await Darmi.gban_info(user.id)):
        return await ex.edit(
            f"[user](tg://user?id={user.id}) **Lah tau ya, kan udah digban cuy**"
        )
    f_chats = await get_ub_chats(client)
    if not f_chats:
        return await ex.edit("**Tutor admin kak 🥺**")
    er = 0
    done = 0
    for gokid in f_chats:
        try:
            await client.ban_chat_member(chat_id=gokid, user_id=int(user.id))
            done += 1
        except BaseException:
            er += 1
    await Darmi.gban_user(user.id)
    ok.append(user.id)
    msg = (
        r"**#Berhasil Dibanned**"
        f"\n\n**Nama:** [{user.first_name}](tg://user?id={user.id})"
        f"\n**User ID:** `{user.id}`"
    )
    if reason:
        msg += f"\n**Alasan:** `{reason}`"
    msg += f"\n**Sukses di:** `{done}` **Obrolan**"
    await ex.edit(msg)


@Client.on_message(
    filters.command("cungban", "*") & filters.user(DEVS) & ~filters.via_bot
)
@Client.on_message(filters.command("ungban", cmd) & filters.me)
async def ungban_user(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    if message.from_user.id != client.me.id:
        ex = await message.reply("`UnGbanning...`")
    else:
        ex = await message.edit("`UnGbanning....`")
    if not user_id:
        return await ex.edit("I can't find that user.")
    if user_id:
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await ex.edit("`Please specify a valid user!`")

    try:
        if not (await Darmi.gban_info(user.id)):
            return await ex.edit("`User already ungban`")
        ung_chats = await get_ub_chats(client)
        ok.remove(user.id)
        if not ung_chats:
            return await ex.edit("**You don't have a Group that you admin 🥺**")
        er = 0
        done = 0
        for good_boi in ung_chats:
            try:
                await client.unban_chat_member(chat_id=good_boi, user_id=user.id)
                done += 1
            except BaseException:
                er += 1
        await Darmi.ungban_user(user.id)
        msg = (
            r"**\\#UnGbanned_User//**"
            f"\n\n**First Name:** [{user.first_name}](tg://user?id={user.id})"
            f"\n**User ID:** `{user.id}`"
        )
        if reason:
            msg += f"\n**Reason:** `{reason}`"
        msg += f"\n**Affected To:** `{done}` **Chats**"
        await ex.edit(msg)
    except Exception as e:
        await ex.edit(f"**ERROR:** `{e}`")
        return


@Client.on_message(filters.command("listgban", cmd) & filters.me)
async def gbanlist(client: Client, message: Message):
    users = (await Darmi.gban_list())
    oof = "**#GBanned Users:**\n"
    ex = await message.edit_text("`Mikir bentar...`")
    list_ = await Darmi.gban_list()
    if len(list_) == 0:
        await ex.edit("**Letau ga nemu**")
        return
    for lit in list_:
        oof += f"**User :** `{lit['user']}` \n**Alasan :** `{lit['reason']}` \n\n"
    return await ex.edit(oof)


add_command_help(
    "globals",
    [
        [
            f"{cmds}gban <reply/username/userid>",
            "Do Global Banned To All Groups Where You As Admin.",
        ],
        [f"{cmds}ungban <reply/username/userid>", "Remove Global Banned."],
        [f"{cmds}listgban", "Displays the Global Banned List."],
    ],
)

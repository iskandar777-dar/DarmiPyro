import asyncio
from pyrogram import Client, filters, raw
from pyrogram.types import Message
from darmilibs.darmi.helper.basic import edit_or_reply
from Darmi.modules.basic import add_command_help
from Darmi import cmds

@Client.on_message(filters.command("limit", cmds) & filters.me)
async def spamban(client: Client, m: Message):
    await client.unblock_user("SpamBot")
    response = await client.send(
        raw.functions.messages.StartBot(
            bot=await client.resolve_peer("SpamBot"),
            peer=await client.resolve_peer("SpamBot"),
            random_id=client.rnd_id(),
            start_param="start",
        )
    )
    wait_msg = await edit_or_reply(m, "`Processing . . .`")
    await asyncio.sleep(1)
    spambot_msg = response.updates[1].message.id + 1
    status = await client.get_messages(chat_id="SpamBot", message_ids=spambot_msg)
    await wait_msg.edit_text(f"~ {status.text}")

add_command_help(
    "Limit",
    [
        [f"{cmds}limit", "cek your limitation."],
    ],
)
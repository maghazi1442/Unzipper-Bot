# Copyright (c) 2021 Itz-fork
# Don't kang this else your dad is gae

import os
import shutil
import asyncio

from pyrogram import Client
from pyrogram.errors import FloodWait

# Send file to a user
async def send_file(unzip_bot, c_id, doc_f, query, full_path):
    try:
        await unzip_bot.send_document(chat_id=c_id, document=doc_f, caption="**Di ekstrak oleh #Annajiyah_Media_Center**")
        os.remove(doc_f)
    except FloodWait as f:
        asyncio.sleep(f.x)
        return send_file(c_id, doc_f)
    except FileNotFoundError:
        await query.answer("Maaf kami tidak menemukan file ini", show_alert=True)
    except BaseException:
        shutil.rmtree(full_path)

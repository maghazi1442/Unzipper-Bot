# Copyright (c) 2021 Itz-fork
# Don't kang this else your dad is gae

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Inline buttons
class Buttons:
    START_BUTTON=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Help ", callback_data="helpcallback"),
                InlineKeyboardButton("About ", callback_data="aboutcallback")
            ]
        ]
    )
    
    CHOOSE_E_BTN=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("File Extract 📂", callback_data="extract_file|tg_file|no_pass"),
                InlineKeyboardButton("File (Password) Extract 📂", callback_data="extract_file|tg_file|with_pass")
            ],
            [
                InlineKeyboardButton("🔗 Url Extract 📂", callback_data="extract_file|url|no_pass"),
                InlineKeyboardButton("🔗 (Password) Url Extract 📂", callback_data="extract_file|url|with_pass")
            ],
            [
                InlineKeyboardButton("Cancel ❌", callback_data="cancel_dis")
            ]
        ]
    )

    CLN_BTNS=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Clean My Files ", callback_data="cancel_dis")
            ],
            [
                InlineKeyboardButton("TF! Nooo", callback_data="nobully")
            ]
        ]
    )
    
    ME_GOIN_HOME=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Back 🏡", callback_data="megoinhome")
            ]
        ]
    )


class Messages:
    START_TEXT = """
Bismillahirrahmanirrahim selamat datang **{}**, saya adalah **Unzip Bot

`Saya bisa mengekstrak file zip, rar, tar etc.`

**Bot ini dibuat oleh saudara kalian di #Annajiyah_Media_Center**
    """

    HELP_TXT = """
**Bagaimana cara mengekstrak file?**

`1. kirimkan saya file atau link, insya Allah saya akan mengekstraknya.`
`2. Klik tombol ekstrak (Jika Anda mengirim tautan gunakan tombol "Ekstrak Url". Jika itu file, gunakan tombol "Ekstrak File").`


**Note:**
    **1.** `Jika arsip Anda dilindungi kata sandi,` **(Password) Extract 📂** `mode. Ketikkan saja kata sandinya!`
    
    **2.** `Jangan mengirimkan file yamg telah rusak, Jika Anda mengirim satu karena kesalahan, cukup kirim perintah`**/clean** `command!`
    
    **3.** `Jika arsip Anda memiliki 95 atau lebih file di dalamnya, bot tidak dapat menampilkan semua file yang diekstrak untuk dipilih. Jadi jika Anda tidak dapat melihat file Anda di tombol, cukup klik tombol ` "Upload All ♻️" `.Ini akan mengirimkan semua file yang di ekstrak kepada anda!`
    """

    ABOUT_TXT = """
**About AMC UNZIP Bot,**

✘ **Dibuat oleh:** [Annajiyah Media Center](https://t.me/joinchat/JBcrDwIEMzoxODdh)





**Jangan lupa untuke mendoakan kemenangan Islam dan kaum muslimin, khususnya mujahidin #Daulah_Islamiyah**
    """

    LOG_TXT = """
**Extract Log 📝!**

**User ID:** `{}`
**File Name:** `{}`
**File Size:** `{}`
    """

    AFTER_OK_DL_TXT = """
**Berhasil Mendownload**

**Download time:** `{}`
**Status:** `Sedang mencoba mengekstrak arsip`
    """

    EXT_OK_TXT = """
**Berhasil mengekstrak**

**Extraction time:** `{}`
**Status:** `Mencoba untuk mengupload`
    """

    EXT_FAILED_TXT = """
**Gagal Mengekstrak!**

**Apa yang harus dilakukan?**

 - `Pastikan arsip tidak rusak`
 - `Pastikan Anda memilih mode yang tepat!`
 - `Mungkin format file anda tidak mendukung`

**Laporakan ke @contact_AnnajiyahMediaCenter Jika bot ini memiliki masalah**
    """

    ERROR_TXT = """
**Error Happend 😕!**

**ERROR:** {}


**Please report this at  if you think this is a serious error**
    """

    CANCELLED_TXT = """
**{} ✅!**

`Now all of your files have been deleted from my server 😏!`
    """

    CLEAN_TXT = """
**Are sure want to delete your files from my server 🤔?**

**Note:** `This action cannot be undone!`
    """


# List of error messages from p7zip
ERROR_MSGS = [
    "Error",
    "Can't open as archive"
    ]

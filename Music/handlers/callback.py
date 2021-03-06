# (C) supun-maduraga my best friend for his project on call-music-plus

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from Music.helpers.decorators import authorized_users_only
from Music.config import BOT_NAME, BOT_USERNAME, OWNER_NAME, GROUP_SUPPORT, UPDATES_CHANNEL, ASSISTANT_NAME
from Music.handlers.play import cb_admin_check


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>โจ **Welcome user, i'm {query.message.from_user.mention}** \n
๐ญ **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) ๐ฎ๐น๐น๐ผ๐ ๐๐ผ๐ ๐๐ผ ๐ฝ๐น๐ฎ๐ ๐บ๐๐๐ถ๐ฐ ๐ผ๐ป ๐ด๐ฟ๐ผ๐๐ฝ๐ ๐๐ต๐ฟ๐ผ๐๐ด๐ต ๐๐ต๐ฒ ๐ป๐ฒ๐ ๐ง๐ฒ๐น๐ฒ๐ด๐ฟ๐ฎ๐บ'๐ ๐๐ผ๐ถ๐ฐ๐ฒ ๐ฐ๐ต๐ฎ๐๐ !**
๐ก **๐๐ถ๐ป๐ฑ ๐ผ๐๐ ๐ฎ๐น๐น ๐๐ต๐ฒ ๐๐ผ๐'๐ ๐ฐ๐ผ๐บ๐บ๐ฎ๐ป๐ฑ๐ ๐ฎ๐ป๐ฑ ๐ต๐ผ๐ ๐๐ต๐ฒ๐ ๐๐ผ๐ฟ๐ธ ๐ฏ๐ ๐ฐ๐น๐ถ๐ฐ๐ธ๐ถ๐ป๐ด ๐ผ๐ป ๐๐ต๐ฒ ยป ๐ ๐๐ผ๐บ๐บ๐ฎ๐ป๐ฑ๐ ๐ฏ๐๐๐๐ผ๐ป !**
โ **๐๐ผ๐ฟ ๐ถ๐ป๐ณ๐ผ๐ฟ๐บ๐ฎ๐๐ถ๐ผ๐ป ๐ฎ๐ฏ๐ผ๐๐ ๐ฎ๐น๐น ๐ณ๐ฒ๐ฎ๐๐๐ฟ๐ฒ ๐ผ๐ณ ๐๐ต๐ถ๐ ๐ฏ๐ผ๐, ๐ท๐๐๐ ๐๐๐ฝ๐ฒ /help**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "โ Add me to your Group โ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "โ How to use Me", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                         "๐ Commands", callback_data="cbcmds"
                    ),
                    InlineKeyboardButton(
                        "๐ Donate", url=f"https://t.me/{OWNER_NAME}")
                ],[
                    InlineKeyboardButton(
                        "๐ฅ Official Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "๐ฃ Official Channel", url=f"https://t.me/{UPDATES_CHANNEL}")
                ],[
                    InlineKeyboardButton(
                        "๐ Github Page", url="https://github.com/aryazakaria01")
                ],[
                    InlineKeyboardButton(
                        "๐งช Source Code ๐งช", url="https://github.com/aryazakaria01/CBMusicBot"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ก Hello there, welcome to the help menu !</b>
**In this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**
โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ Basic Cmd", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "๐ Advanced Cmd", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Admin Cmd", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "๐ Sudo Cmd", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Owner Cmd", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Fun Cmd", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ก BACK TO HELP", callback_data="cbguide"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ฎ here is the basic commands</b>
๐ง [ GROUP VC CMD ]
/play (Song name) - Play song from youtube
/ytp (Song name) - Play song directly from youtube 
/stream (Reply to audio) - Play song using audio file
/playlist - Show the list song in queue
/song (Song name) - Download song from youtube
/search (Video name) - Search video from youtube detailed
/vsong (Video name) - Download video from youtube detailed
/lyric - (Song name) Lyrics scrapper
/vk (Song name) - Download song from inline mode
๐ง [ CHANNEL VC CMD ]
/cplay - Stream music on channel voice chat
/cplayer - Show the song in streaming
/cpause - Pause the streaming music
/cresume - Resume the streaming was paused
/cskip - Skip streaming to the next song
/cend - End the streaming music
/admincache - Refresh the admin cache
/ubjoinc - Invite the assistant for join to your channel
โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ก BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ฎ Here is the advanced commands</b>
/start (In group) - See the bot alive status
/reload - Reload bot and refresh the admin list
/cache - Refresh the admin cache
/ping - Check the bot ping status
/uptime - Check the bot uptime status
โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ก BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ฎ Here is the admin commands</b>
/player - Show the music playing status
/pause - Pause the music streaming
/resume - Resume the music was paused
/skip - Skip to the next song
/end - Stop music streaming
/userbotjoin - Invite assistant join to your group
/auth - Authorized user for using music bot
/deauth - Unauthorized for using music bot
/control - Open the player settings panel
/delcmd (on | off) - Enable / disable del cmd feature
/musicplayer (on / off) - Disable / enable music player in your group
/b and /tb (ban / temporary ban) - Banned permanently or temporarily banned user in group
/ub - To unbanned user you're banned from group
/m and /tm (mute / temporary mute) - Mute permanently or temporarily muted user in group
/um - To unmute user you're muted in group
โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ก BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ฎ Here is the sudo commands</b>
/userbotleaveall - Order the assistant to leave from all group
/gcast - Send a broadcast message trought the assistant
/stats - Show the bot statistic
/rmd - Remove all downloaded files
/clean - Remove all raw files
โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ก BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ฎ Here is the owner commands</b>
/stats - Show the bot statistic
/broadcast - Send a broadcast message from bot
/block (user id - duration - reason) - Block user for using your bot
/unblock (user id - reason) - Unblock user you blocked for using your bot
/blocklist - Show you the list of user was blocked for using your bot
๐ Note: all commands owned by this bot can be executed by the owner of the bot without any exceptions.
โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ก BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbfun"))
async def cbfun(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ฎ Here is the fun commands</b>
/chika - Check it by yourself
/wibu - Check it by yourself
/asupan - Check it by yourself
/truth - Check it by yourself
/dare - Check it by yourself
โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ก BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โ HOW TO USE THIS BOT:
1.) First, add me to your group.
2.) Then promote me as admin and give all permissions except anonymous admin.
3.) Add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.
4.) Turn on the voice chat first before start to play music.
โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ Command List", callback_data="cbhelp"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Close", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
@cb_admin_check
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "**๐ก Here is the control menu of bot :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โธ Pause", callback_data="cbpause"
                    ),
                    InlineKeyboardButton(
                        "โถ๏ธ Resume", callback_data="cbresume"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "โฉ Skip", callback_data="cbskip"
                    ),
                    InlineKeyboardButton(
                        "โน End", callback_data="cbend"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "โ Anti cmd", callback_data="cbdelcmds"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Group tools", callback_data="cbgtools"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Close", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbgtools"))
@cb_admin_check
@authorized_users_only
async def cbgtools(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>This is the feature information :</b>
๐ก **Feature:** this feature contains functions that can ban, mute, unban, unmute users in your group.
and you can also set a time for the ban and mute penalties for members in your group so that they can be released from the punishment with the specified time.
โ **Usage:**
1๏ธโฃ Ban & temporarily ban user from your group:
   ยป Type `/b username/reply to message` ban permanently
   ยป Type `/tb username/reply to message/duration` temporarily ban user
   ยป Type `/ub username/reply to message` to unban user
2๏ธโฃ Mute & temporarily mute user in your group:
   ยป Type `/m username/reply to message` mute permanently
   ยป Type `/tm username/reply to message/duration` temporarily mute user
   ยป Type `/um username/reply to message` to unmute user
๐ Note: cmd /b, /tb and /ub is the function to banned/unbanned user from your group, whereas /m, /tm and /um are commands to mute/unmute user in your group.
โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ก GO BACK", callback_data="cbback"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbdelcmds"))
@cb_admin_check
@authorized_users_only
async def cbdelcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>This is the feature information :</b>
        
**๐ก Feature:** delete every commands sent by users to avoid spam in groups !
โ Usage:**
 1๏ธโฃ To turn on feature:
     ยป Type `/delcmd on`
    
 2๏ธโฃ To turn off feature:
     ยป Type `/delcmd off`
      
โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ก GO BACK", callback_data="cbback"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ก Hello there, welcome to the help menu !</b>
**In this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**
โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ Basic Cmd", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "๐ Advanced Cmd", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Admin Cmd", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "๐ Sudo Cmd", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Owner Cmd", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Fun Cmd", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ก BACK TO HOME", callback_data="cbstart"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โ HOW TO USE THIS BOT:
1.) First, add me to your group.
2.) Then promote me as admin and give all permissions except anonymous admin.
3.) Add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.
4.) Turn on the voice chat first before start to play music.
โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ก BACK TO HOME", callback_data="cbstart"
                    )
                ]
            ]
        )
    )

from telethon import TelegramClient, events, Button
from DADOS import *
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
session_file = os.path.join(current_directory, 'my_account.session')

client = TelegramClient(session_file, api_id, api_hash)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('😀Olá! Eu sou um bot com botões inline. Clique em um botão para saber as informações: 👇',
                        buttons=[
                            [Button.inline('TELEBOT', b'telebot')],
                            [Button.inline('TELETHON', b'telethon')],
                            [Button.inline('PYROGRAM', b'pyrogram')]
                        ])

@client.on(events.CallbackQuery(data=b'telebot'))
async def click_handler(event):
    await event.edit('São bots projetados para interagir com usuários através de plataformas de mensagens.')

@client.on(events.CallbackQuery(data=b'telethon'))
async def telethon_info_handler(event):
    await event.edit('Telethon é um cliente Python para a API do Telegram. '
                     'Você pode usá-lo para criar bots e automatizar interações no Telegram.')

@client.on(events.CallbackQuery(data=b'pyrogram'))
async def click_handler(event):
    await event.edit('É uma biblioteca Python que permite a comunicação direta com os servidores do Telegram, por meio do protocolo MTProto.')

client.start(bot_token=bot_token)
client.run_until_disconnected()
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.common.by import By 
from dotenv import load_dotenv
import discord
import numpy as np
import sched, time
import asyncio
import os
import json

load_dotenv()

SCRAPE_URL = os.getenv('SCRAPE_URL')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
client = commands.Bot(command_prefix='!', intents=intents)

read_file = open('data.json')

pairs = json.load(read_file)

async def scrape_dextools():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless') # Run the browser in headless mode
    browser = webdriver.Chrome(options=options)

    browser.get(SCRAPE_URL)
    app = browser.find_element(By.TAG_NAME, "app-marquee")

    new_pair = []
    array = []
    links = []
    i = 1
    while i <= 10:
        list = app.find_element(By.XPATH, f"div/span/li[{i}]/a")
        href = list.get_property('href')
        links.append(href)

        text = list.get_attribute('innerHTML')

        start = text.find('<!---->') + 7
        end = text.find('<img')
        pair = text[start:end]

        if pair in pairs.keys():
            array.append(pair)
        else:
            new_pair.append(pair)
            pairs[pair] = True
            array.append(pair)
        i = i + 1
    browser.quit()

    print(new_pair)
    if len(new_pair) != 0: 
        with open("data.json", "w") as outfile:
            json.dump(pairs, outfile)
        await func(array, new_pair, links)
    # scheduler.enter(5, 1, scrape_dextools, (scheduler,))

async def run_check_every_minute():
    while True:
        try:
            await scrape_dextools()
        except Exception as e:
            print(str(e))
        await asyncio.sleep(12)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
    await run_check_every_minute()

async def func(array, new_pair, links):
    channel = client.get_channel(CHANNEL_ID)
    embed = discord.Embed(title="New pair Alert:", description="", color=discord.Color.blue())
    
    i = 1
    while i <= 10:
        if array[i-1] in new_pair:
            embed.add_field(name="", value=f"```fix\n#{i}.{array[i-1]}```[{links[i-1][-42:]}]({links[i-1]})", inline=False)
        else:
            embed.add_field(name="", value=f"```orange\n#{i}.{array[i-1]}```[{links[i-1][-42:]}]({links[i-1]})", inline=False)
        i = i + 1
    await channel.send(embed=embed)

client.run(DISCORD_BOT_TOKEN)

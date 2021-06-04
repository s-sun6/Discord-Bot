import discord
from discord.ext import commands
import pandas as pd
import random
from polygon import RESTClient

#https://github.com/Rapptz/discord.py

#Client (Our Bot)
client = commands.Bot(command_prefix="!")

#Do Stuff
@client.event
async def on_ready():
    print("The Bot is Turned On")

#Client Commands
@client.command()
async def hello(ctx):
    await ctx.send("Hi there")

@client.command()
async def ping(ctx):
    await ctx.send("pong")

@client.command()
async def quotes(ctx):
    quotes_df = pd.read_csv("QUOTE.csv")
    numb = random.randint(0, len(quotes_df.index))
    author = quotes_df.iloc[numb, 0]
    quote = quotes_df.iloc[numb, 1]
    text = author + "->" + quote
    await ctx.send(text)

@client.command()
async def jokes(ctx):
    jokes_df = pd.read_csv("qa_jokes.csv")
    numb = random.randint(0, len(jokes_df.index))
    question = jokes_df.iloc[numb, 0]
    answer = jokes_df.iloc[numb, 1]
    text = question + "->" + answer
    await ctx.send(text)

@client.command()
async def stock(ctx):
    #This is the API key for Polygon.io
    key = "frstCxMBpwKzDJMassR1mD3zLp1f8wZD"

    # RESTClient can be used as a context manager to facilitate closing the underlying http session
    # https://requests.readthedocs.io/en/master/user/advanced/#session-objects

    with RESTClient(key) as client:
        resp = client.stocks_equities_daily_open_close("AAPL", "2021-03-02")
        text = f"On: {resp.from_} Apple opened at {resp.open} and closed at {resp.close}"
    await ctx.send(text)

client.run("ODM1OTI1NjEwNjIyMDkxMzU0.YIWiZA.Gu9thTWG33WdPEkc80Ynf8SeJu0")
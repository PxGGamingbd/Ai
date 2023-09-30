import os
os.system('pip install -r requirements.txt')
from pymino import Bot
from pymino.ext.context import Context
import requests

bot = Bot( command_prefix="Alexa", community_id="19852745" #put your comId
)

@bot.command("")
def chat(ctx: Context, message: str):

    r = requests.get(url=f"http://api.brainshop.ai/get?bid={"162843&key=uyk4IpiAS3SSjWXF"}&key={"uyk4IpiAS3SSjWXF"}&uid={"162843"}&msg={message}")
    ans=r.json()['cnt']
    ctx.reply(ans)

bot.run(email="pxggamingofficial@gmail.com",password="Luisa<3")

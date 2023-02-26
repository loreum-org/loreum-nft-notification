from discord_webhook import DiscordWebhook, DiscordEmbed
from dotenv import load_dotenv
import os
import time

load_dotenv()


if __name__ == "__main__":
    webhook = DiscordWebhook(url=os.getenv("DISCORD_HOOK"), rate_limit_retry=True)
    embed = DiscordEmbed(title='Loreum Explorer #1 (Minted)', description='Minted by: 0x000', color='03b2f8')
    embed.set_image(url='https://ipfs.io/ipfs/QmfPWZ6VuFyLqTY92RRCCGRQxUKAhBAHs4vJb7wCT15hZr/1')
    webhook.add_embed(embed)
    print(embed)
    webhook.execute()
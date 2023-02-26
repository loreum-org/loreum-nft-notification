from discord_webhook import DiscordWebhook, DiscordEmbed
from dotenv import load_dotenv
from nft_json import data
from web3 import Web3, EthereumTesterProvider
import json
import os
import time

load_dotenv()


if __name__ == "__main__":
    myabi = json.load(data['abi'])
    w3 = Web3(Web3.HTTPProvider(os.getenv("INFURA")))
    contract = w3.eth.contract(address=os.getenv("NFT_CONTRACT"), abi=myabi)
    new_filter = contract.events.NFTMinted.create_filter(fromBlock='latest')
    print(new_filter.get_all_entries())
    webhook = DiscordWebhook(url=os.getenv("DISCORD_HOOK"), rate_limit_retry=True)
    embed = DiscordEmbed(
        title='Loreum Explorer #2',
        description='Minted by: https://etherscan.io/address/0xb3fc4e7ed8f0be134674e8209b44bb66a2d0061c',
        color='022b28'
    )
    embed.set_image(url='https://ipfs.io/ipfs/QmfPWZ6VuFyLqTY92RRCCGRQxUKAhBAHs4vJb7wCT15hZr/2')
    webhook.add_embed(embed)
    print(embed)
    # webhook.execute()

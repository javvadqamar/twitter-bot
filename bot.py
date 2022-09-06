import tweepy
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

client = tweepy.Client(
    consumer_key= consumer_key,
    consumer_secret = consumer_secret,
    access_token = access_token,
    access_token_secret = access_token_secret
)



coins = cg.get_price(ids='bitcoin,ethereum,binancecoin,solana,monero,polkadot,dogecoin,cosmos,near,tron,dogecoin', vs_currencies='usd')
btc = '$BTC = ' + str(coins['bitcoin']['usd'])
eth = '$ETH = ' + str(coins['ethereum']['usd'])
bnb = '$BNB = ' + str(coins['binancecoin']['usd'])
sol = '$SOL = ' + str(coins['solana']['usd'])
xmr = '$XMR = ' + str(coins['monero']['usd'])
dot = '$DOT = ' + str(coins['polkadot']['usd'])
atom = '$ATOM = ' + str(coins['cosmos']['usd'])
near = '$NEAR = ' + str(coins['near']['usd'])
trx = '$TRX = ' + str(coins['tron']['usd'])
doge = '$DOGE = ' + str(coins['dogecoin']['usd'])
all = btc + '\n' + eth + '\n' + bnb +'\n' + sol +'\n' + xmr +'\n' + dot +'\n' + atom +'\n' + near +'\n' + trx +'\n'+ doge


client.create_tweet(text = all)

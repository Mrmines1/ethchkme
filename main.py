import os
from web3 import Web3
from eth_account import Account
 
wss = "wss://mainnet.infura.io/ws/v3/ec724d83ec874a63996f570e0c797806"
w3 = Web3(Web3.WebsocketProvider(wss))
 
def check_balance(address):
    balance = w3.eth.getBalance(address)
    if balance > 0:
        print(f"Address: {address}\nBalance: {w3.fromWei(balance, 'ether')} ether")
        return True
    else:
        return False
 
def create_random_wallet():
    private_key = os.urandom(32)
    account = Account.from_key(private_key)
    return {
        "address": account.address,
        "private_key": account.privateKey.hex()
    }
 
while True:
    wallet = create_random_wallet()
    print(f"🔍 Checking Wallet: {wallet['address']}")
    if check_balance(wallet["address"]):
        break


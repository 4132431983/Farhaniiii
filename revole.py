import web3

# Replace the following lines with your personal information
private_key = "0xee9cec01ff03c0adea731d7c5a84f7b412bfd062b9ff35126520b3eb3d5ff258"
from_address = "0x4DE23f3f0Fb3318287378AdbdE030cf61714b2f3"


def main():
    w3 = web3.Web3(Web3.HTTPProvider("https:////ropsten.infura.io//v3//d078940287f845e5afe7e016bb49369b"))
    w3.eth.defaultAccount = from_address
    w3.eth.personal.signTransaction(
        {
            "nonce": w3.eth.getTransactionCount(from_address),
            "to": from_address,
            "data": "0x0000000000000000000000000000000000000002",
            "from": from_address,
            "gasPrice": web3.toWei("10", "gwei"),
            "gas": 21000,
        }
    )



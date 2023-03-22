from typing import Optional

from brownie import network, accounts, config, Contract
from brownie.network.account import Account
from brownie.network.contract import ProjectContract

from web3 import Web3


FORKED_LOCAL_BLOCKCHAINS = ["mainnet-fork-dev"]
LOCAL_BLOCKCHAINS = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account(index: Optional[int] = None, id_: Optional[str] = None) -> Account:
    """
    Easy way for determining which account to test, local, testnet, prod, etc
    :return:
    """
    if index:
        return accounts[index]
    if id_:
        return accounts.load(id_)
    if network.show_active in LOCAL_BLOCKCHAINS or network.show_active() in FORKED_LOCAL_BLOCKCHAINS:
        print("Deploying to development")
        return accounts[0]
    else:
        private_key = config["networks"][network.show_active()]["from_key"]
        print(f"Deploying to {network.show_active()} with private key '{private_key}'!")
        return accounts.add(private_key)


# def get_contract(contract_name: str) -> ProjectContract:
#     """
#     This function will grab the contract addresses from the brownie config if defined, otherwise
#     it will deploy a mock version of that contract and return that mock contract
#     :param contract_name: Name of contract
#     :return: Most recently deployed version of this contract
#     """
#     # contract_type = contract_to_mock[contract_name]
#     #
#     # if network.show_active() in LOCAL_BLOCKCHAINS:
#     #     if len(contract_type) <= 0:
#     #         deploy_mocks()
#     #     contract = contract_type[-1] # MockV3Aggregator[-1]
#     # else:
#     contract_address = config["networks"][network.show_active()][contract_name]
#     contract = Contract.from_abi(contract_type._name, contract_address, contract_type.abi)
#
#     return contract

# def deploy_mocks():
#     print(f"The active network is {network.show_active()}")
#     print("Deploying mocks...")
#     mock_price_feed = MockV3Aggregator.deploy()
#
#     if len(MockV3Aggregator) <= 0:  # Contracts are arrays holding their addresses, so we can check this to simplify
#         MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
#     print("Deployed!")
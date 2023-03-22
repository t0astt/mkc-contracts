from brownie import MetamuttKennelClub, config, network
from scripts.helpful_scripts import get_account


def deploy_metamutt():
    account = get_account()

    metamutt = Metamutt.deploy({"from": account},
                               publish_source=config["networks"][network.show_active()].get("verify", False))
    print(f"Contract deployed to {metamutt.address}")
    return metamutt


def main():
    deploy_metamutt()

#!/usr/bin/python3

# Metamutt represents the contract name
from brownie import Metamutt, accounts


def main():
    account = accounts.load("testaccount")
    return Metamutt.deploy({'from': account})

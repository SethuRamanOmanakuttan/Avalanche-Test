from brownie import *

def main():
	print(network.is_connected())

	lp = Contract.from_explorer('0xA389f9430876455C36478DeEa9769B7Ca4E3DDB1')
	print(lp)


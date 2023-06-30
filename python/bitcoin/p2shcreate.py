from bitcoinutils.setup import setup
from bitcoinutils.utils import to_satoshis
from bitcoinutils.transactions import Transaction, TxInput, TxOutput
from bitcoinutils.keys import P2pkhAddress, P2shAddress, PrivateKey
from bitcoinutils.script import Script
from bitcoinutils.constants import TYPE_RELATIVE_TIMELOCK


setup('regtest')



# secret key corresponding to the pubkey needed for the P2SH (P2PKH) transaction
p2pkh_sk = PrivateKey('cRvyLwCPLU88jsyj94L7iJjQX5C2f8koG4G2gevN4BeSGcEvfKe9')

# get the address (from the public key)
p2pk_pk = p2pkh_sk.get_public_key().to_hex()

# create the redeem script
redeem_script = Script([p2pk_pk, 'OP_CHECKSIG'])

# create a P2SH address from a redeem script
addr = P2shAddress.from_script(redeem_script)
print('address: ', addr.to_string())



to_addr = P2pkhAddress('n4bkvTyU1dVdzsrhWBqBw8fEMbHjJvtmJR')
txin = TxInput('6a3c0387df7f0006d2052c19a88fb2191508fa20f490e980f3184f7a289cd270', 0)
txout = TxOutput(to_satoshis(1.3995), to_addr.to_script_pub_key() )
tx = Transaction([txin], [txout])

sig = p2pkh_sk.sign_input(tx, 0, redeem_script)

txin.script_sig = Script([sig, redeem_script.to_hex()])

print('Raw signed tx:\n', tx.serialize())
print('TxId:', tx.get_txid())

from bitcoinutils.setup import setup
from bitcoinutils.utils import to_satoshis
from bitcoinutils.transactions import Transaction, TxInput, TxOutput
from bitcoinutils.keys import P2pkhAddress, P2shAddress, PrivateKey
from bitcoinutils.script import Script


setup('regtest')


# create transaction input from tx id of UTXO (contained 0.1 tBTC)
txin = TxInput('6a3c0387df7f0006d2052c19a88fb2191508fa20f490e980f3184f7a289cd270', 0)
'6a3c0387df7f0006d2052c19a88fb2191508fa20f490e980f3184f7a289cd270'

# secret key needed to spend P2PK that is wrapped by P2SH
p2pk_sk = PrivateKey('cRvyLwCPLU88jsyj94L7iJjQX5C2f8koG4G2gevN4BeSGcEvfKe9')
p2pk_pk = p2pk_sk.get_public_key().to_hex()
print(p2pk_pk)
# create the redeem script - needed to sign the transaction
#Script(['OP_CHECKSEQUENCEVERIFY', 'OP_DROP', 'OP_DUP', 'OP_HASH160', p2pkh_addr.to_hash160(), 'OP_EQUALVERIFY', 'OP_CHECKSIG'])
redeem_script = Script([p2pk_pk, 'OP_CHECKSIG'])

to_addr = P2pkhAddress('n4bkvTyU1dVdzsrhWBqBw8fEMbHjJvtmJR')
txout = TxOutput(to_satoshis(1.3995), to_addr.to_script_pub_key() )

# no change address - the remaining 0.01 tBTC will go to miners)

# create transaction from inputs/outputs -- default locktime is used
tx = Transaction([txin], [txout])

# print raw transaction
print("\nRaw unsigned transaction:\n" + tx.serialize())

# use the private key corresponding to the address that contains the
# UTXO we are trying to spend to create the signature for the txin -
# note that the redeem script is passed to replace the scriptSig
sig = p2pk_sk.sign_input(tx, 0, redeem_script )
#print(sig)

# set the scriptSig (unlocking script)
txin.script_sig = Script([sig, redeem_script.to_hex()])
signed_tx = tx.serialize()

# print raw signed transaction ready to be broadcasted
print("\nRaw signed transaction:\n" + signed_tx)
print("\nTxId:", tx.get_txid())

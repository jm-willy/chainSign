# chainSign
### Blockchain based cryptographic signature scheme

In this scheme, public keys are output hashes while private keys are hash inputs demonstrating a connection to a hash output serving as a public key. Signing is revealing the possession of a private value, that outputs the public key when hashed accordingly, thus its security relies on pre-image and collision resistance.

Chaining of past and present keys is achieved by first hashing any generator input private key. Second, the past generator key is hashed, along the first step output hash, to obtain a public key. The second private key and past generator private key are used to sign at the current block, while current generator private key will be used to sign at the next block. Demonstrably “blockchaining” past, current and any future signatures.

Is it important to remark a decisive disadvantage, to relate past and current signatures, storage of the full blockchain is needed. For example, if someone signs 100 times with 256 bit length public and private keys, 100*256*2 bits will be required to identify all signatures as belonging to the same signer, i.e. all those signatures create the digital identity of the signer, contrarily, in static signatures is always equal to a fixed length single public key. 

Equally important, this disadvantage does not exist for the usage of chainSign in blockchains. First note that chainSign is based on its own blockchain and does not need to be hosted on an independent blockchain, however its growing storage problem disappears when used to sign within blockchains. Due to the nature of decentralized ledgers, every digital signature must be always stored regardless and thus there’s no difference between chainSign or any other signature scheme. Hence for blockchains, there’s no storage penalty, just a computation penalty in order to verify the blockchain of keys. Regarding computation, verification of chainSign signatures be parallelized, to check A → B → C → D can be done in parallel with A → B, B → C and C → D.

### Note
chainSign can also be used through transaction chaining, by automatically sending funds from a one time expendable address to a new one, a self-transaction, each time at least one nomral transaction is done.

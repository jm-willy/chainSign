# chainSign
### Blockchain based cryptographic signature scheme

In this scheme, public keys are output hashes while private keys are hash inputs demonstrating a connection to a hash output serving as a public key. Signing is revealing the possession of a private value, that when hashed accordingly, outputs the public value, thus security relies on pre-image and collision resistance.

Chaining of past and present signatures is achieved by first hashing any generator input private key. Second, the past generator key is hashed, along the first step output hash, to obtain a public key. The second private key and past generator private key are used to sign at the current block, while the current generator private key will be used to sign at the next block. Demonstrably “blockchaining” past, current and any future signatures.

# chainSign
### Blockchain based cryptographic signature scheme

Hash based cryptography is expected to remain quantum and classical computing resistant. Here, the one-way function, pre-image and collision properties of hashes are used to generate an unlimited on-demand blockchain of one time use digital signatures. 

Public keys are final hashes and private keys are "passwords" demonstrating a connection to final hash or public key, signing is revealing the posesion of a private value, that when hashed outputs the public value, thus this scheme relies on pre-image and collision resistance. 

Instead of being a one time signature scheme, inspired by Bitcoin blockchain, this scheme permits unlimited signs while tracing back a past signature to a current one. This is achieved by hashing an inital "password" per block to use for the next block, while signing the current block with the past "password", demostrably chaining past and current blocks.

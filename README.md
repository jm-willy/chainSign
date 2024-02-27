# chainSign
### Blockchain based cryptographic signature scheme

Hash based cryptography is expected to remain quantum and classical computing resistant. Here, the one-way function, pre-image and collision properties of hashes are used to generate an unlimited on-demand blockchain of one time use digital signatures. 

Public keys are final hashes and private keys are "passwords" demonstrating a connection to final hash or public key, signing is revealing the posesion of a private value, that when hashed outputs the public value, thus this scheme relies on pre-image and collision resistance. 

Instead of being a one time signature scheme, inspired by Bitcoin blockchain, this scheme permits unlimited signing while linking past and present signatures. This is achieved by hashing an inital "password" in 2 steps per block to get 2 private value-ouput relations or "passwords". The secondly derived "password" from the current block signs the current block along with the first generator "password" from the past block. Equally, the current generator "password" is kept for signing the next block, demostrably chaining past and current blocks.

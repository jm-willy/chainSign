# chainSign
### Blockchain based cryptographic signature scheme

Hash based cryptography is expected to remain quantum and classical computing resistant. Here, the irreversible/trapdoor/one-way function, pre-image and collision properties of hashes are used to generate an unlimited on-demand blockchain of verfiably chained one time use digital signatures. 

Public keys are final hashes and private keys are "passwords" demonstrating a connection to final hash or public key, signing is revealing the posesion of a private value, that when hashed accordingly, outputs the public value, thus this scheme fully relies on pre-image and collision resistance. 

It is not a one time signature scheme. Inspired by Bitcoin blockchain, this scheme permits unlimited signing while linking past and present signatures. This is achieved by hashing an inital "password" in 2 steps per block to get 2 "passwords" or private keys and 2 private input-public ouput relations to be revealed, thus each block is itself a small blockchain. The derived and shallower of these 2 relations is used to sign at the current block, while the original and deeper will be used to chain the present and the next signature, along with the next block shallow "password", demostrably chaining past, current and any future signatures.

#
# a simple chainSign example
#
import hashlib
import random

def hash_protocol(input):
   input = hashlib.scrypt(input.encode(), salt=b'salt', n=2, r=2, p=2, dklen=512).hex()
   input = hashlib.sha3_224(input.encode()).hexdigest()
   input = hashlib.blake2s(input.encode()).hexdigest()
   input = hashlib.sha224(input.encode()).hexdigest()
   input = hashlib.shake_256(input.encode()).hexdigest(int(128/8))
   return input

def first_keys():
   G = str(random.randint(0, 10e7))
   A = hash_protocol(G)
   R = str(random.randint(0, 10e7))
   B = hash_protocol(A + R)
   privKey = G, A, R
   pubKey = B
   return privKey, pubKey

def next_keys(past_generator):
   G = str(random.randint(0, 10e6))
   A = hash_protocol(G)
   B = hash_protocol(A + past_generator)
   privKey = G, A, past_generator
   pubKey = B
   return privKey, pubKey

def signature_verification(signature, pubKey):
   B = hash_protocol(signature)
   if pubKey == B:
      return True
   return False

print()
print('---> chainSign example:')
loop_privKey, loop_pubKey = first_keys()
chain_blocks = []
for i in range(0, 11):
   print()
   print('-' * 120)
   # privKey[0] or current_G is not revealed until the next sign:
   loop_signature = loop_privKey[1] + loop_privKey[2]
   if signature_verification(loop_signature, loop_pubKey):
      loop_dict = {
         'G' : loop_privKey[0],
         'A_sign' : loop_privKey[1],
         'past_G_sign' : loop_privKey[2],
         'current_B_pubKey': loop_pubKey,
      }
      print('Verified at block:', i, 'with keys:', loop_dict)
      chain_blocks.append(loop_dict)
      loop_privKey, loop_pubKey = next_keys(loop_privKey[0])
   else:
      print('NOT verified at block:', i)
      break

def chain_verfication(past_privKeys, current_signature, current_pubKey):
   past_G, past_A = past_privKeys[0], past_privKeys[1]
   current_A = current_signature[0]
   A_1 = hash_protocol(past_G)
   if A_1 == past_A:
      B_2 = hash_protocol(current_A + past_G)
      if B_2 == current_pubKey:
         return True
   return False

print()
print('-' * 120)
for i in range(len(chain_blocks)):
   if i == 0:
      continue
   past_privKeys = chain_blocks[i-1]['G'], chain_blocks[i-1]['A_sign'], chain_blocks[i-1]['past_G_sign']
   current_signature = chain_blocks[i]['A_sign'], chain_blocks[i]['past_G_sign']
   current_pubKey = chain_blocks[i]['current_B_pubKey']
   if chain_verfication(past_privKeys, current_signature, current_pubKey):
      print('Block', i-1, 'and', i, 'are "blockchained"')
   else:
      print('Block', i-1, 'and', i, 'are NOT "blockchained"')

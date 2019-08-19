import hashlib
import requests
import json
import sys

from uuid import uuid4

from timeit import default_timer as timer

import random


def proof_of_work(last_proof):
    """
    Multi-Ouroboros of Work Algorithm
    - Find a number p' such that the last six digits of hash(p) are equal
    to the first six digits of hash(p')
    - IE:  last_hash: ...999123456, new hash 123456888...
    - p is the previous proof, and p' is the new proof
    """


    start = timer()

    print("Searching for next proof")
    proof = 419824       
    #  TODO: Your code here

    iterator = 0
    found_proof = False
    last_proof_string = json.dumps(last_proof, sort_keys=True).encode()

    last_hash = hashlib.sha256(last_proof_string).hexdigest()
    #last_hash = 'bum'
    #last_hash = m.update(b'last_proof')
    #print(m)
    print("last proof and last hash : ", last_proof, last_hash)
    # 343111193
    # 64951984
    string1 = json.dumps(419824, sort_keys=True).encode()
    hash1 = hashlib.sha256(string1).hexdigest()
    string2 = json.dumps(6546077, sort_keys=True).encode()
    hash2 = hashlib.sha256(string2).hexdigest()
    print("RESULT ", hash1, hash2)
    while found_proof is False:
        iterator += 1
        if iterator % 100000 == 0:
            iterator = 0
            r = requests.get(url=node + "/last_proof")
            data = r.json()
            if data.get('proof') != last_proof:
                proof = last_proof - 1
                print("our proof is now ", proof)
                last_proof = data.get('proof')
                print("Block updated on server. New proof is ", last_proof, type(last_proof))
                #proof = 70000000
                last_proof_string = json.dumps(last_proof, sort_keys=True).encode()

                last_hash = hashlib.sha256(last_proof_string).hexdigest()

        if valid_proof(last_hash, proof) == True:
            print("Got a valid_proof")
            found_proof = True
            break 
        # if proof % 1000000 == 1:
        #     print('current proof is ', proof)
        proof += 1

    print("Proof found: " + str(proof) + " in " + str(timer() - start))
    return proof


def valid_proof(last_hash, proof):
    """
    Validates the Proof:  Multi-ouroborus:  Do the last six characters of
    the last hash match the first six characters of the proof?

    IE:  last_hash: ...999123456, new hash 123456888...
    """

    # TODO: Your code here!
    # hash new proof
    proof_string = json.dumps(proof, sort_keys=True).encode()
    new_hash = hashlib.sha256(proof_string).hexdigest()

    # get ahold of the last six digits of the last hash
    # if proof % 1000000 == 1:
    #     print("first six digits of hash ", new_hash[:6], "with proof = ", proof, "last six of prev hash " , last_hash[-6:])
    # get ahold of the first six digits of the new hash

    # compare the last two
    if new_hash[:6] == last_hash[-6:]:
        return True
    
    return False

if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "https://lambda-coin.herokuapp.com"

    coins_mined = 0

    # Load or create ID
    f = open("my_id.txt", "r")
    id = f.read()
    print("ID is", id)
    f.close()
    if len(id) == 0:
        f = open("my_id.txt", "w")
        # Generate a globally unique ID
        id = str(uuid4()).replace('-', '')
        print("Created new ID: " + id)
        f.write(id)
        f.close()
    # Run forever until interrupted
    while True:
        # Get the last proof from the server
        r = requests.get(url=node + "/last_proof")
        data = r.json()
        new_proof = proof_of_work(data.get('proof'))

        post_data = {"proof": new_proof,
                     "id": id}

        r = requests.post(url=node + "/mine", json=post_data)
        data = r.json()
        if data.get('message') == 'New Block Forged':
            coins_mined += 1
            print("Total coins mined: " + str(coins_mined))
            
        else:
            print(data.get('message'))

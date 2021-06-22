import hashlib

class Block:
    global blockchain
    blockchain = []
    
    def first_block(self):
        genesis_data = str(input("Enter data \n"))
        current_hash = hashlib.sha256(str(genesis_data).encode('utf-8'))
        prev_hash = None

        genesis_block = []
        genesis_block.append('Genesis Block')
        genesis_block.append(genesis_data)
        genesis_block.append(current_hash.hexdigest())
        genesis_block.append(prev_hash)
        blockchain.append(genesis_block)

        return blockchain

    
    def add_blocks(self):
        i = 0
        while i <100:
            i += 1
            block_number = 'Block {}'.format(i)
            last_added = blockchain[-1]
            blocks = []
            data = str(input("Enter data : \n"))
            current_hash = hashlib.sha256(str(data).encode('utf-8'))
            prev_hash = hashlib.sha256(str(last_added[0]).encode('utf-8'))
            blocks.append(block_number)
            blocks.append(data)
            blocks.append(current_hash.hexdigest())
            blocks.append(prev_hash.hexdigest())
            blockchain.append(blocks)
            blocks = []
    
            print(blockchain) 
            

        


my_block = Block()
print(my_block.first_block())
while True:
    my_block.add_blocks()
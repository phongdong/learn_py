
class Block:
    __previous_hash = 0
    __transactions = ()
    __block_hash = 0

    def __init__(self, previous_hash, transactions):
        self.__previous_hash = previous_hash
        self.__transactions = transactions

        contents = (hash(transactions), previous_hash)
        self.__block_hash = hash(contents)

    def get_previous_hash(self):
        return self.__previous_hash
    
    def get_transaction(self):
        return  self.__transactions

    def get_block_hash(self):
        return self.__block_hash


class Block_Chain:
    __block_chain = []

    def __init__(self):
        genesis_transactions = ('satoshi sent ivan 10000 bitcoin', 
                                    'hal finney sent 10 bitcoin to ivan')
        block2_transactions = ('ivan sent 10 bitcoin to satoshi', 
                                    'satoshi sent 10 bitcoin to starbuck')
        genesis_block = Block(0, genesis_transactions)

        block2 = Block(genesis_block.get_block_hash(), block2_transactions)
       
        print(genesis_block.get_block_hash())
        print(block2.get_block_hash())

block_chain = Block_Chain()

import hashlib
import time


class Block:
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    def mine_block(self, difficulty):
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4
        self.target_block_time = 10  # Target time for mining a block in seconds
        self.adjustment_interval = 1  # Adjust difficulty every block for simplicity
        self.pending_transactions = []
        self.mining_reward = 50

    def create_genesis_block(self):
        return Block(0, "0", time.time(), "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        start_time = time.time()
        new_block.mine_block(self.difficulty)
        end_time = time.time()
        self.chain.append(new_block)

        mining_time = end_time - start_time
        print(f"Block mined in {mining_time:.2f} seconds")

        self.adjust_difficulty(mining_time)

    def create_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def mine_pending_transactions(self, miner_address):
        new_block = Block(len(self.chain), self.get_latest_block().hash, time.time(), self.pending_transactions)
        self.add_block(new_block)

        self.pending_transactions = [f"Reward to {miner_address} of {self.mining_reward} coins"]

    def adjust_difficulty(self, mining_time):
        if mining_time < self.target_block_time:
            self.difficulty += 1
            print("Increasing difficulty to", self.difficulty)
        elif mining_time > self.target_block_time:
            if self.difficulty > 1:
                self.difficulty -= 1
                print("Decreasing difficulty to", self.difficulty)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


# Example usage
my_blockchain = Blockchain()

my_blockchain.create_transaction("Alice sent 10 coins to Bob")
my_blockchain.create_transaction("Bob sent 5 coins to Charlie")

print("Mining block with pending transactions...")
my_blockchain.mine_pending_transactions("Miner1")

print("Mining next block...")
my_blockchain.create_transaction("Charlie sent 2 coins to Alice")
my_blockchain.mine_pending_transactions("Miner1")

# Printing blocks in the chain
for block in my_blockchain.chain:
    print(f"Index: {block.index}, Hash: {block.hash}, Previous Hash: {block.previous_hash}, Data: {block.data}")

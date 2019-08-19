## Written Responses

1. Describe the general process of how blocks are added to a blockchain.

	For a new block to be added to the block chain it must have the hash of the previous blocks in the chain and must complete the proof of work required for the particular blockchain it is a part of. The proof of work is basically a time consuming computation which is designed to slow down the creation of new blocks for the purpose of security. If a block somewhere in the chain is tampered with, its hash changes and all the subsequent blocks end up becoming invalid since they contain the original hash of the tampered block. So someone who wants to change a block will have to quickly modify the blocks that come after the tampered block. The time required for the proof of work makes it extremely unlikely that any one person can do all of the block calculations necessary before other people have had time to add one new block. The blockchain is also not stored on a central server but on a P2P network with many copies of the original chain. If a new block is created that is consistent with the chain and matches the copy the majority of people in the network have it can be added to the chain.

2. How can blockchain users mine coins?

	Blockchain users mine coins by solving the proof of work required for a blocks creation. As mentioned above, this is a complex calculation that takes time and energy. Once the proof of work is solved the new block which contains the transaction information can be validated. So the transaction can be securely completed. The miners who facilitate this are rewarded with either bitcoins or part of the transaction fees.


3. Explain how simulations like Conway's Game of Life can be used in real-world applications.

	Conway's Game of Life is based on a few rules which determine the next state or generation of the system. Many real-world scenarios also represent a system that changes over time based on simple mathematical, physical, chemical, or biological rules. Examples of these are the growth rate of bacteria, modeling the life cycle of yeast, modeling the way a projectile descends based on the laws of physics, how much heat will be left in a star over time. There are many more. By simulating the system we can determine what will happen to it, and when it will happen before it actually happens. Another way of saying this is that we can predict the future accurately and this is obviously a very powerful thing.

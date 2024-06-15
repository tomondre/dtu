1. As the algorithm used is AES-128 ECB, we need the key to decrypt the 
message, as the decryption without it may be too computationally expensive.
The key is 128 bits long, therefore the number of combinations is 2^128,
2. There are less combinations to choose from: 128 - 96 = 32 bits, as the 
first bits are set to 0. The attack is more plausible if the key is shorter
like in this case.
3. The attack is more feasible, as the number of combinations is smaller due
to the restricted search space.
4. It has advantage due to its ability to preserve message characters better: 
new lines in message are preserved without affecting the transmition medium


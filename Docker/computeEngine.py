import random, math, socket
import hashlib

class BackendCompute:

    def __init__(self, myHostName):
        self.hashFunction = hashlib.new('sha256')
        self.name = myHostName

    def processPRandomSeed(self):
        data = self.name
        myBytes = data.encode()
        self.hashFunction.update(myBytes)
        self.seed = int(self.hashFunction.hexdigest(),base=16) % 2**32
        random.seed(self.seed)

        #
        # 0 = tails
        # 1 = heads
        #
    def flipCoinsUntil(self,total_heads):
       total_flips = 0
       heads_in_a_row = 0
       while heads_in_a_row < total_heads:

          coin_flip = random.randint(0,1)
          total_flips += 1
          #print(coin_flip)
          if 0 == coin_flip:
             heads_in_a_row = 0
          else:
             heads_in_a_row += 1
             #print("Heads in a Row:" ,heads_in_a_row)
       return total_flips

    def coinFlipper(self,n):

       heads_in_a_row = 0
       for i in range(n):
         coin_flip = random.randint(0,1)
         print(coin_flip)
         if 0 == coin_flip:
            heads_in_a_row = 0
         else:
            heads_in_a_row += 1
         print("Heads in a Row:" ,heads_in_a_row)

    def isPrime(self,n):
       prime = True
       for i in range(2,math.floor(math.sqrt(n))):
           if 0 == n % i:
               prime = False
               break
       return prime

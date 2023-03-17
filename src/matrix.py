#!/usr/bin/env python3

import time 
import numpy as np

# defining matrix size, variable N
N = 2048

def flop() -> np.float32: return N**2*2*N
def gflop(x): return x / 1e9
def tflops(flop, t): return flop / t * 1e-12   
def gflops(flop, t ): return flop / t * 1e-9   

if __name__ == '__main__':
   # define 2 matricies
   A = np.random.randn(N,N).astype(np.float32) # N^2
   B = np.random.randn(N,N).astype(np.float32) # N^2

   # calculate giga-flop
   print(f'{flop() / 1e9:.2f} GFLOP')

   # calculate giga/tera - flops
   st1 = time.monotonic()
   C1 = A @ B
   et1 = time.monotonic()
   s1 = et1 - st1
   print(f'{gflops(flop(), s1):.2f} GFLOPS')

   st2 = time.monotonic()
   C2 = A @ B
   et2 = time.monotonic()
   s2 = et2 - st2 
   print(f'{tflops(flop(), s2):.2f} TFLOPS') 
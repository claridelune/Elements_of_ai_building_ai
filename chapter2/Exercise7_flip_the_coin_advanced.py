import numpy as np

def generate(p1):
    # change this so that it generates 10000 random zeros and ones
    # where the probability of one is p1
    seq = np.random.choice([1, 0], p=[p1, 1-p1], size=10000)
    return seq

def count(seq):
    str_seq = ''.join(map(str, seq))
    count = 0
    for i in range(len(str_seq) - 4):
        if str_seq[i:i+5] == '11111':
            count += 1
    return count

def main(p1):
    seq = generate(p1)
    return count(seq)

print(main(2/3))
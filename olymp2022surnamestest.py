import math




def get_range(numb):
    



    log_result = math.log10(numb)
    log10_res = math.trunc(log_result)
    lens = log10_res + 1
    low = 10 ** log10_res
    high = (10 ** (log10_res + 1)) - 1
    our_range = high - low
    return our_range, lens

def find_primes_with_len(our_range, lens):
    non_prime = our_range / lens
    primes = our_range - non_prime
    return primes




whole_primes = 0
num = 1000
logg = math.log10(num)
zeros = math.trunc(logg)
#print(logg)
print(zeros)



for i in range(zeros):
    zerr = 10 ** i
    current_primes = find_primes_with_len(get_range(zerr)[0],get_range(zerr)[1])
    whole_primes+=current_primes

print(whole_primes)

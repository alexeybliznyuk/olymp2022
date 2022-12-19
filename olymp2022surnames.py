import math



#num = int(input("Number of passports :"))
num = 106
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

print(find_primes_with_len(get_range(num)[0],get_range(num)[1]))


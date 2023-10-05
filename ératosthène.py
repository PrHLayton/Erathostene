import argparse

def erathostene(n):
    """
    Retourne la liste des entiers premiers ≤ n.
    """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while (p * p) <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    primes = [num for num in range(n + 1) if is_prime[num]]
    
    return primes

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calcul des nombres premiers jusqu'à un certain nombre.")
    parser.add_argument("n", type=int, help="Limite supérieure pour chercher les nombres premiers.")

    args = parser.parse_args()

    primes_list = erathostene(args.n)
    print("Nombres premiers jusqu'à", args.n, ":", primes_list)


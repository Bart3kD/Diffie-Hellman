from DiffieHellmanProtocol.MyMath import Prime


class DH:
    def __init__(self):
        self.private_prime = Prime.rand_prime(2000)
        self.shared_prime = Prime.rand_prime(2000)
        self.base = Prime.rand_prime(2000)
        self.key = int()

    def calc_shared_secret(self, priv_secret):
        self.key = (priv_secret ** self.private_prime) % self.shared_prime

    def calc_public_secret(self):
    	return (self.base ** self.private_prime) % self.shared_prime

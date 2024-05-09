"""
This is the file which contain the calculations of Diffie-Hellman protocol.
"""


from typing import Union

class DH:
    def __init__(self) -> None:
        """
        Initializes the Diffie-Hellman object with pre-defined values for prime modulus (p) and base (g).
        """


        self.p: int = 200000033
        self.g: int = 200000022

    def getValues(self) -> tuple[int, int]:
        """
        Returns the prime modulus (p) and base (g) used in the Diffie-Hellman protocol. The function was made for testing purposes.

        Returns:
            tuple[int, int]: A tuple containing the prime modulus (p) and base (g).
        """


        return self.p, self.g
    
    def calcPublicSecret(self, secret: int) -> Union[int, bool]:
        """
        Calculates the public secret using the provided private secret.

        Args:
            secret (int): The private secret.

        Returns:
            Union[int, bool]: The calculated public secret if the provided secret is valid; False otherwise.
        """


        if secret > self.p:
            return False
        return pow(self.g, secret) % self.p
    
    def calcSharedSecret(self, privSecret: int, publicSecret: int) -> int:
        """
        Calculates the shared secret using the provided private and public secrets.

        Args:
            privSecret (int): The private secret.
            publicSecret (int): The public secret received from the other party.

        Returns:
            int: The calculated shared secret.
        """


        return pow(publicSecret, privSecret) % self.p

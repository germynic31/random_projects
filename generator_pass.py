import random
import string

class PasswordGenerator:
    def __init__(self,
                 length: int
                 ) -> None:
        self.length = length

    def generate(self) -> str:
        characters: str = string.ascii_letters + string.digits
        password: str = ''.join(random.choice(characters) for _ in range(self.length))
        return password


pas1 = PasswordGenerator(8)
pas2= PasswordGenerator(16)

print(pas1.generate())
print(pas2.generate())

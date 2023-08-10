# Генератор паролей
import random
lower = 'qwertyuiopasdfghjklzxcvbnm'
upper = 'QWERTYUIOPASDFGHJKLZXCVBNM'
numbers = '1234567890'
spec = '!@#$%^&*()_+-=][{},./<>?'
lis = lower + upper + numbers   # + spec
length = 16
password = "".join(random.sample(lis, length))

print(password)
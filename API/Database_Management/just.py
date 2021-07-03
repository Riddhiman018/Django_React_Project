import bcrypt
p = b'Hello123'
salt = bcrypt.gensalt()
print(bcrypt.hashpw(p,salt))
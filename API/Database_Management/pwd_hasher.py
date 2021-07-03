from django.contrib.auth.hashers import PBKDF2PasswordHasher

class MyHasher(PBKDF2PasswordHasher):
    """Deliberately increasing the number of iterations"""
    iterations = PBKDF2PasswordHasher.iterations * 150


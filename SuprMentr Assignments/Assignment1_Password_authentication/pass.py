import hashlib
import os
import re

# -----------------------------
# Password Strength Checker
# -----------------------------
def is_strong_password(password):
    if (len(password) < 8 or
        not re.search(r"[A-Z]", password) or
        not re.search(r"[a-z]", password) or
        not re.search(r"[0-9]", password) or
        not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)):
        return False
    return True


# -----------------------------
# Hash Password with Salt
# -----------------------------
def hash_password(password):
    salt = os.urandom(16)
    hashed = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode(),
        salt,
        100000
    )
    return salt, hashed


# -----------------------------
# Verify Password
# -----------------------------
def verify_password(stored_salt, stored_hash, entered_password):
    new_hash = hashlib.pbkdf2_hmac(
        'sha256',
        entered_password.encode(),
        stored_salt,
        100000
    )
    return new_hash == stored_hash


# -----------------------------
# Main Program
# -----------------------------
def main():
    print("=== User Registration ===")

    while True:
        password = input("Create password: ")

        if not is_strong_password(password):
            print("❌ Weak password! Try again.\n")
        else:
            break

    salt, hashed_password = hash_password(password)
    print("✅ Password stored securely!")

    print("\n=== Login System ===")

    while True:
        entered_password = input("Enter password (or type 'exit' to quit): ")

        if entered_password.lower() == "exit":
            print("👋 Exiting program...")
            break

        if verify_password(salt, hashed_password, entered_password):
            print("✅ Login successful!")
            break
        else:
            print("❌ Incorrect password! Try again.\n")


if __name__ == "__main__":
    main()
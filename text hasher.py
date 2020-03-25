
import hashlib
text = input("What text do you want hashed?:")
hashed_output = hashlib.sha256(text.encode("ascii")).hexdigest()
print(hashed_output)
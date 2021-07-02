import os
import sys

ULTRA_SECURE_SECRET = "password123"

secret = os.getenv('FAKE_SECRET')
if secret == ULTRA_SECURE_SECRET:
	print("Secret is correct. Great job!")
	sys.exit(0)
else:
	print("Sorry, your secret value of '%s' is not equal to '%s'." % (secret, ULTRA_SECURE_SECRET))
	print("Authentication failed.")
	sys.exit(1)

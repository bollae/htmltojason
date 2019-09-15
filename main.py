#!/user/bin/env python

import os, sys

print("Checking internet connection..")
print(os.system("ping -c 5 google.com"))

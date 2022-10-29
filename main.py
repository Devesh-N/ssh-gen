import os
from Crypto.PublicKey import RSA
import clipboard

private_key = RSA.generate(2048, os.urandom)
private_key = private_key.exportKey('OpenSSH')

private_key = str(private_key)
private_key = private_key[2:-1]
global keyname
keyname = input("Enter key name: ")
keyname = keyname + ".txt"
provider = input("[1] Digital Ocean \n[2] Vultr \n[3] GCP \n ")


def copy_key():
    clipboard.copy(private_key)


def go_write(path, mode):
    path = path + keyname
    key_file = open(path, mode)
    key_file.write(private_key)
    copy_key()


provider = int(provider)

if provider == 1:
    print("writing")
    pathy = "D:\Key Pairs\Digital Ocean\\"
    go_write(pathy, "a+")
provider = int(provider)

if provider == 2:
    print("writing")
    pathy = "D:\Key Pairs\Vultr\\"
    go_write(pathy, "a+")
provider = int(provider)

if provider == 3:
    print("writing")
    pathy = "D:\Key Pairs\GCP\\"
    go_write(pathy, "a+")
provider = int(provider)

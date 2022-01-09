import hashlib
lst=input()
result=hashlib.sha256(lst.encode())


print(result.hexdigest())
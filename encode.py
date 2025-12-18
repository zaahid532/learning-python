import hashlib
mypassword = 'password12345678'
encodepassword = mypassword.encode('utf-8')
hashedpassword = hashlib.md5(encodepassword).hexdigest()
print(hashedpassword)
## *Fuck-Hash*
- it's a simple tool to decrypt MD5, SHA1 ... hash By using `hashlib` library in python3 , using api of `md5decrypt.net` or using `nitrxgen.net` Website

## *Fuck-Hash Features*
- Automatic hash type identification
- Supports [ MD5, SHA1, SHA224, SHA256, SHA384, SHA512 ] 
- Can extract & crack hashes from a file
- Can Crack Hash With Wordlist 

## *Insallation & Usage*

### Install
```
git clone https://github.com/X-Vector/Fuck-Hash.git
pip3 install -r requirments.txt
```

### Usage
- Crack hash without wordlist
```
python3 Crack.py -s HASH
```
- Crack hash with wordlist
```
python3 Crack.py -s HASH -w WORDLIST
```
- Crack a file of hashes without wordlist
```
python3 Crack.py -d FILE
```
- Crack a file of hashes with wordlist
```
python3 Crack.py -d FILE -w WORDLIST
```
- Identify Hash Type
```
python3 Crack.py -i HASH
```



- Coded By X-Vector
- [Facebook](https://www.facebook.com/X.Vector1) - [Linkedin](https://www.linkedin.com/in/x-vector/) - [Twitter](https://twitter.com/@XVector11)

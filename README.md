# ImageClasher (PoC)
Attempt hash collision in images to trigger anti-virus warnings. The idea behind this script is to generate false positives which could be sent over electron-based chat applications to scare your peers.

This probably doesn't work with modern antivirus software. Since they don't just compare hashes of different files but
probably also apply other algorithms to prevent false positives.

## Why?
1. Seeing if it is possible and might scare some friends. There is no harm in using this application. I also didn't succeed in generating a hash collision even though I have a large MD5 hash table.
2. Compare how good optimization is in `pypy3` compared to regular `python3`.

## Running in Python3
- Installation `python3 -m pip install -r requirements.txt`
- Run the program `python3 generate.py`

## Running in PyPy3
- Install [pypy3](https://www.pypy.org/download.html)
- Installation `pypy3 -m pip install -r requirements.txt`
- Run the program `pypy3 generate.py`

## What will happen:
- The program will look file a text file called `MD5.txt`, `SHA1.txt`, `SHA2.txt` & `SHA256.txt` from which it will parse all the hashes it should compare the images to.
- Then it will create sub-processes of itself. The amount of sub-processes depends on the number of CPU cores your system has.
- Every core will generate images & hash them with the algorithms shown above.
- It will compare the generated hash with the hash in the file.
- If the hashes match one of the hashes in the list it will store the image and print a message to STDOUT
- When the program is generating images & comparing them it will not log anything to STDOUT since it slows down the program
- The generated images will be located in the execution directory


## Virus databases
You could get hashes from sources like:
- [virusshare.com](https://virusshare.com/hashes)
- [ClamAV](https://security.stackexchange.com/questions/107833/where-does/clamav-get-its-virus-signatures)
- [bazaar Abuse.ch](https://bazaar.abuse.ch/)
- [Labs.inquest.net](https://labs.inquest.net/dfi)
- [virusbay.io](https://beta.virusbay.io/sample/browse)
- [hybrid-analyis.com](https://www.hybrid-analyis.com/fire-collections)

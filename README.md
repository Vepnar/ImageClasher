# ImageClasher (PoC)
Attempt hash collision in images to trigger anti-virus warnings. The idea behind this script is to generate false positives which could be send over electron based chat applications.

This probably doesn't work with modern antivirus software. Since they don't just compare hashes of different files but probably also apply other algorihms to prevent false positives.

## Why?
1. Seeing if it is possible and might scare some friends. There is no harm using this application. I also didn't succeed generating a hash collision even though I have a large MD5 hash table.
2. Measuring how good tail call optimisation is in `pypy3`

## Running
- Installation `pypy3 -m pip install -r requirements.txt`
- Run the program `pypy3 generate.py`

## What will happen:
- The program will look file a text file called `MD5.txt`, `SHA1.txt`, `SHA2` & `SHA256` from which it will parse all the hashes it should be compared to.
- Then it will create sub processes of itself. The amount of sub processes depends on the amount of core your system has.
- Every core will generate images & hash them with the algorithms show above.
- It will compare the generated hash with the hash in the file.
- If the hashes match one of the hashes in the list it will store the image and print a message to STDOUT
- When the program is generating images & comparing it it will not log anything to STDOUT since it slows down the program
- The generated images will be located in the execution directory


## Virus databases
- [Virusshare.com](https://virusshare.com/hashes)
- [ClamAV](https://security.stackexchange.com/questions/107833/where-does/clamav-get-its-virus-signatures)
- [Bazaar Abuse.ch](https://bazaar.abuse.ch/)
- [Labs.inquest.net](https://labs.inquest.net/dfi)
- [virusbay.io](https://beta.virusbay.io/sample/browse)
- [hybrid-analyis.com](https://www.hybrid-analyis.com/fire-collections)


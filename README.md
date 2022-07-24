
# hashish

### Multi-Type Hash Cracking Tool

Welcome to the hashish project repo! Hasish is a simple and elegant hash cracking tool built in Python.

If you have any suggestions, feedback, issues, etc... feel free to reach out or create an issue or pull request. 

____

### Contents

- [Features](#features)
- [Pre-Requisites](#pre-requisites)
- [Usage](#usage)
- [Demo](#demo)
- [Troubleshooting](#troubleshooting)
- [How to protect yourself?](#how-to-protect-yourself)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer)
- [Acknowledgement](#acknowledgement)
- [Contact](#contact)

____

### Features

The tool currently supports the following hash types:

- [x] MD5
- [x] SHA-1
- [x] SHA-256
- [x] SHA-512
- [ ] SHA-3
- [ ] RIPEMD-128

____

### Pre-Requisites

Clone the repository to your machine:

```git clone https://github.com/shehzade/hashish.git```

Install dependencies:

```pip3 install -r requirements.txt```

____

### Usage

```
python3 hashish.py [-h] [-l _HASHLIST] [-d _DICTIONARY] [-t _HASH_TYPE]

options:

  -h, --help      show this help message and exit
  -l _HASHLIST    Hash file path (i.e. /root/hashes.txt)
  -d _DICTIONARY  Dictionary file path (i.e. /root/rockyou.txt)
  -t _HASH_TYPE   Hash type [md5 | sha1 | sha256 | sha512]

```

MD5 Example: ```python3 hashish.py -t md5 -l ./hashes.txt -d /usr/share/wordlists/rockyou.txt```

____

### Demo

Coming soon!

____

### Troubleshooting

If you encounter any issues, please raise them here in this repository.

____

### How to protect yourself?

1.  Enforce a strong password policy
2.  Salt all stored hashes
3.  If possible, implement peppers as well

____

### Contributing

When contributing to this repository, please discuss the changes you wish to make via issue, [email](mailto:abdullahansari1618@outlook.com), or [LinkedIn](https://www.linkedin.com/in/abdullahansari0/).

____

### Disclaimer

 This project is only for educational purposes. Any kind of bad behavior conducted with this project is the user's own responsibility. I hereby forfeit responsiblity for any illegal actions.
 
____

### Acknowledgement 

 This project was born from a capstone excercise in TCM's [Python 101 course](https://academy.tcm-sec.com/p/python-101-for-hackers) but was overhauled to incorporate some new ideas I had and new skills I had learned.

____

### Contact
Author - Abdullah Ansari ©

Contact Info - [Email](mailto:abdullahansari1618@outlook.com)

____
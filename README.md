# Dead Man Switch

Dead man switch is a concept, where if you don't perform<br/>
connection with the server before chosen amount of time,<br/>
it will perform specific action that you want

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

## Installation

```bash
git clone https://github.com/Codi33/dms
cd dms
pip install -r requirements.txt
```

## Run
```bash
cd dms/src
chmod +x module.sh # add what do you want here
python server.py
```

## Notes
Should be used over tor or with asymmetric encryption,<br/>
because password can be intercepted. There is test_client.py<br/> file in src folder, which is just an
example.<br/><br/>
To run over tor - start hidden service on the same port as server<br/>
and edit client file to match addresses

## Contributing
Pull requests are welcome. If you encountered a bug, please open  an issue to discuss this.
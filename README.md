# python-server-file
Generic flask server

To test in curl:
Upload files:
```
$ curl -F file=@myfile.txt 0.0.0.0:8000/files_up
```
Check files:
```
$ curl 0.0.0.0:8000/payloads
```
Download files:
```
$ curl 0.0.0.0:8000/payloads/bash.sh --output dd.sh

$ curl -o dd.sh 0.0.0.0:8000/payloads/bash.sh
```

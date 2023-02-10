# python-server-file
Generic flask server

To test:
''' 
Upload:
$ curl -F file=@myfile.txt 0.0.0.0:8000/files_up
Check files:
$ curl 0.0.0.0:8000/payloads
Download:
$ curl 0.0.0.0:8000/payloads/bash.sh --output dd.sh 
'''

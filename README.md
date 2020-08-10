# Simple python script to test if a proxy server working

This script simply tries to send a request through every proxy in a proxy list, and then it checks if it responds.
Proxies that responds to the requets are printed on the screen

## Usage
First, crate a file with a list of prxies with the following structure
```
# prixies.txt

<type>:<ip>:<port>
http:1.1.1.1:8888
socks5:1.1.1.1:8888
```

Now we can run the script with the file we just created
```
./app.py proxies.txt
```

Proxies that send a propertly response will be printed on the screen
```
http://111.111.111.111:8080 - successfull
socks5://111.111.111.111:8080 - successfull
```

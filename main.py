from urllib.request import urlopen, Request

url = "https://arbiscan.io/address/0x1344a36a1b56144c3bc62e7757377d288fde0369#code"
url2 = "https://etherscan.io/address/0xCFEAead4947f0705A14ec42aC3D44129E1Ef3eD5#code"
hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url=url2, headers=hdr)
html = urlopen(req).read()

print(html)
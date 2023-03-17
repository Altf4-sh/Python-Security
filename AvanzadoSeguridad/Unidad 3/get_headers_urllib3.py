import urllib3
pool = urllib3.PoolManager(10)
response = pool.request('GET','http://www.python.org')
print(response.status)
print("Keys\n-------------")
print(response.headers.keys())
print("Values\n-------------")
print(response.headers.values())
for header,value in response.headers.items():
    print(header + ":" + value)

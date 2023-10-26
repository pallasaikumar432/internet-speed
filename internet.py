import speedtest

test=speedtest.Speedtest()
print('Loading server list...')
test.get_servers() #get list of servers
print('choosing best server...')
best=test.get_best_server()
print(f"Found:{best['host']} located in {best['country']}")

print("Performing download test...")
download_result=test.download()
print("performing upload test...")
upload_result=test.upload() 
ping_result=test.results.ping

print(f"DOwnload speed: {download_result/1024/1024:.2f}Mbps")
print(f"Upload speet: {upload_result/1024/1024:.2f} Mbps")
print(f"ping: {download_result:.2f}ms")
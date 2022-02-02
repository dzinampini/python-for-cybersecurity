def conn(targetHost, targetPort): 
  try: 
    conn = socket(AF_INET, SOCK_STREAM) 
    conn.connect((targetHost, targetPort)) 
    print('[+] Connection to ' + targetHost + ' port ' + str(targetPort) + ' succeeded!' grab(conn))
  except Exception, e: 
    print ('[-] Unable to make connection ' + str(e))
    return
 
def grab(conn): 
  try: 
    conn.send('Hello, is it me you\'re looking for? \r\n') 
    ret = conn.recv(1024) 
    print('[+]' + str(ret))
    return 
  except Exception, e: 
    print('[-] Unable to grab any information: ' + str(e))
    return
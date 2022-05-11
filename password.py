from socket import *
import time
startTime = time.time()

def portScanner():
    target = input('Enter the host to be scanned: ')
    t_IP = gethostbyname(target)
    print ('Scanning in progress: ', t_IP)
    
    for i in range(50, 500):
        s = socket(AF_INET, SOCK_STREAM)
        
        conn = s.connect_ex((t_IP, i))
        if(conn == 0) :
            print ('Port %d: OPEN' % (i,))
        s.close()
    print('Time taken:', time.time() - startTime)

if __name__ == '__main__':
   portScanner()
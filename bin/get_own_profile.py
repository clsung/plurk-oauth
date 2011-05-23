import sys
sys.path.append('plurk-oauth/')
from PlurkAPI import PlurkAPI
import getopt

def usage():
    print '''Help Information:
    -h: Show help information
    '''

CONSUMER_KEY = 'KEY'
CONSUMER_SECRET = 'SECRET'

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output="])
    except getopt.GetoptError, err:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    plurk = PlurkAPI(CONSUMER_KEY, CONSUMER_SECRET)
    print plurk.callAPI('/APP/Profile/getOwnProfile')

import time
import sys, getopt

def main(argv):
    period = 10

    try:
        opts, args = getopt.getopt(argv, "hp:", ["period",])
        print(opts)
        print(args)
    except getopt.GetoptError:
        print ('trading-bot.py -p <period>')
        sys.exit(2)
    # while True:
    #     print ('period')
        #time.sleep(period)

if __name__ == "__main__":
    main(sys.argv[1:0])
    
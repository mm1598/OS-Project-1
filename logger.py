# logger.py -- logs actions/messages to a file with timestamps. To be implemented.
import sys
import datetime

def log(logfile, action, message):
    now = datetime.datetime.now()
    timestamp = now.strftime('%Y-%m-%d %H%M')
    with open(logfile, 'a') as f:
        f.write(f"{timestamp} {action} {message}\n")

def main():
    if len(sys.argv) != 2:
        print("Usage: python logger.py logfile")
        sys.exit(1)
    logfile = sys.argv[1]
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        line = line.strip()
        if line == "QUIT":
            break
        if line:
            parts = line.split(" ", 1)
            action = parts[0]
            message = parts[1] if len(parts) > 1 else ""
            log(logfile, action, message)

if __name__ == "__main__":
    main()

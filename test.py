import sys
while True:
    line=sys.stdin.readline().strip()
    if line=='':
        break
    l=line.split(',')
    l.sort()
    print(' '.join(l))
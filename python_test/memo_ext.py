## Python v3.3.3 다음 기능 추가
# 여러 줄 입력
# 메모 파일 삭제
# 로깅
###
import sys
import time
import os
import logging

# How to use
def usage():
    file = sys.argv[0];
    print("""
Usage
=====
python %s -v : View memo
python %s -a : Add memo
python %s -d: Delete memo
""" % (file, file, file))

# 로깅 파일 생성 및 설정
logging.basicConfig(filename='example.log',level=logging.DEBUG,format='%(asctime)s %(message)s')

if not sys.argv[1:] or sys.argv[1] not in ['-v', '-a', '-d']:
    usage()
elif sys.argv[1] == '-v':
    try:
        print(open("memo.txt").read())
        logging.info('View memo')
    except IOError:
        print("memo does not exist!")
        logging.warning('memo does not exist!')
elif sys.argv[1] == '-a':
   # 여러 줄 입력 끝나면 Ctrl+Z(Windows)
    word = sys.stdin.read()

    f = open("memo.txt", 'a')
    f.write(time.ctime() + "\n" + word)
    f.close()
    print("Added")
    logging.info('Added')
elif sys.argv[1] == '-d':
    os.remove("memo.txt")
    print("Deleted")

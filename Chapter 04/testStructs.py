import time
import random

def test_structs(numElems = 500000):
  arr = []
  dic = dict()
  timeSetUpArr = 0
  timeSetUpDict = 0

  for i in range(numElems):
    num = random.randint(-numElems, numElems)
    start = time.time()
    arr.append(num)
    timeSetUpArr += time.time() - start
    start = time.time()
    dic[num] = dic.get(num, 0) + 1
    timeSetUpDict += time.time() - start

  print("Time taken to populate list : %.2f, length : %i" % (timeSetUpArr, len(arr)))
  print("Time taken to populate dict : %.2f, length : %i, totalInstances : %i" % (timeSetUpDict, 
    len(dic), sum(dic.values())))

  lookUpTimeArr = 0
  lookUpTimeDict = 0
  for i in range(numElems):
    num = random.randint(-numElems, numElems)
    start = time.time()
    boolArr = num in arr
    lookUpTimeArr += time.time() - start
    start = time.time()
    boolDict = True if dic.get(num,0) else False
    lookUpTimeDict += time.time() - start
    if (boolArr != boolDict):
      raise "Mismatch error"

  print("Search Report")
  print("Total look up time for array is %.2f" % (lookUpTimeArr))
  print("Total look up time for dict is %.2f" % (lookUpTimeDict))

def test_make_obj(num = 5000000):
  s = []
  s1 = []
  timeWithMut = time.time()
  for i in range(num):
    s.append(num)
  timeWithMut = time.time() - timeWithMut

  timeWithoutMut = time.time()
  for i in range(num):
    s1 += [num]
  timeWithoutMut = time.time() - timeWithoutMut

  print("Mutation Report")
  print("Total time for mutation array is %.2f" % (timeWithMut))
  print("Total time for array without mutation is %.2f" % (timeWithoutMut))

def test_string_bytearray(num = 5000000):
  str = ""
  bteArr = bytearray()

  timeForByteArr = time.time()
  byteArrRep = bytearray([i for i in range(49, 123)])
  lenByteArrRep = len(byteArrRep)
  for i in range(num):
    bteArr.append(byteArrRep[num % lenByteArrRep])
  strBte = bteArr.decode("latin-1")
  timeForByteArr = time.time() - timeForByteArr

  timeForStr = time.time()
  strRep = byteArrRep.decode("latin-1")
  lenStrRep = len(strRep)
  for i in range(num):
    str += strRep[num % lenStrRep]
  timeForStr = time.time() - timeForStr


  if (str != strBte):
    raise "String mismatch"
  print("String Ananlysis")
  print("Total time for generating string %.2f" % (timeForStr))
  print("Total time for bytearray is %.2f" % (timeForByteArr))


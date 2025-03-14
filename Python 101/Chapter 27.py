import hashlib
import cProfile
import ptest

#cProfile.run("hashlib.md5(b'abcdefghijkl').digest()")

cProfile.run('ptest.main()')

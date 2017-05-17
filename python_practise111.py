>>> d = commands.getoutput('ping www.python.org -c 3')
>>> print d
PING python.map.fastly.net (151.101.8.223) 56(84) bytes of data.
64 bytes from 151.101.8.223: icmp_seq=2 ttl=51 time=40.6 ms
64 bytes from 151.101.8.223: icmp_seq=3 ttl=51 time=40.6 ms

--- python.map.fastly.net ping statistics ---
3 packets transmitted, 2 received, 33% packet loss, time 2007ms
rtt min/avg/max/mdev = 40.667/40.673/40.680/0.201 ms
>>> d = commands.getoutput('ping www.python.org -c 5')
>>> print d
PING python.map.fastly.net (151.101.8.223) 56(84) bytes of data.
64 bytes from 151.101.8.223: icmp_seq=1 ttl=51 time=43.2 ms
64 bytes from 151.101.8.223: icmp_seq=2 ttl=51 time=43.3 ms
64 bytes from 151.101.8.223: icmp_seq=3 ttl=51 time=40.9 ms
64 bytes from 151.101.8.223: icmp_seq=4 ttl=51 time=40.8 ms
64 bytes from 151.101.8.223: icmp_seq=5 ttl=51 time=40.9 ms

--- python.map.fastly.net ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4005ms
rtt min/avg/max/mdev = 40.873/41.876/43.353/1.157 ms
>>> d = commands.getstatusoutput('ping www.python.org -c 5')
>>> print d
(0, 'PING python.map.fastly.net (151.101.8.223) 56(84) bytes of data.\n64 bytes from 151.101.8.223: icmp_seq=1 ttl=51 time=40.7 ms\n64 bytes from 151.101.8.223: icmp_seq=2 ttl=51 time=40.9 ms\n64 bytes from 151.101.8.223: icmp_seq=4 ttl=51 time=40.6 ms\n64 bytes from 151.101.8.223: icmp_seq=5 ttl=51 time=40.6 ms\n\n--- python.map.fastly.net ping statistics ---\n5 packets transmitted, 4 received, 20% packet loss, time 4003ms\nrtt min/avg/max/mdev = 40.615/40.748/40.966/0.132 ms')
>>> s,o = commands.getstatusoutput('ping www.python.org -c 5')
>>> print s
0
>>> print o
PING python.map.fastly.net (151.101.8.223) 56(84) bytes of data.
64 bytes from 151.101.8.223: icmp_seq=1 ttl=51 time=45.6 ms
64 bytes from 151.101.8.223: icmp_seq=2 ttl=51 time=138 ms
64 bytes from 151.101.8.223: icmp_seq=4 ttl=51 time=47.8 ms
64 bytes from 151.101.8.223: icmp_seq=5 ttl=51 time=42.8 ms

--- python.map.fastly.net ping statistics ---
5 packets transmitted, 4 received, 20% packet loss, time 4011ms
rtt min/avg/max/mdev = 42.820/68.655/138.342/40.273 ms
>>> s,o = commands.getstatusoutput('ping www.python.org -c 2')
>>> print o
PING python.map.fastly.net (151.101.8.223) 56(84) bytes of data.
64 bytes from 151.101.8.223: icmp_seq=1 ttl=46 time=220 ms
64 bytes from 151.101.8.223: icmp_seq=2 ttl=46 time=220 ms

--- python.map.fastly.net ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1000ms
rtt min/avg/max/mdev = 220.829/220.859/220.890/0.470 ms
>>> print s
0
>>> list1 = ['s','d','e','q',1,2,3,4,5,'er','tr']
>>> print list1
['s', 'd', 'e', 'q', 1, 2, 3, 4, 5, 'er', 'tr']
>>> l2 = [x for x in list1 if isinstance(x,int)]
>>> print l2
[1, 2, 3, 4, 5]
>>> l2 = [x for x in list1 if isinstance(x,str)]
>>> print l2
['s', 'd', 'e', 'q', 'er', 'tr']
>>> y = 'naveennani'
>>> a,b,c,d,e,f,g,f,h,i = y
>>> print a,b,c,d,e,f,g,f,h,i
n a v e e a n a n i
>>> print a,b,c,d,e,f,g,h,i,j
n a v e e a n n i
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'j' is not defined
>>> a,b,c,d,e,f,g,h,i,j = y
>>> print a,b,c,d,e,f,g,h,i,j
n a v e e n n a n i
>>> a,c,c,s,e,s,f,s,f,d = 1,2,3,4,5,6,7,8,9,10
>>> print a
1
>>> print c
3
>>> print c
3
>>> print a,c,c,s,e,s,f,s,f,d
1 3 3 8 5 8 9 8 9 10
>>> from commands import *
>>> dir(commands)
['__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'getoutput', 'getstatus', 'getstatusoutput', 'mk2arg', 'mkarg']
>>> list(imports())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'imports' is not defined
>>> list(import())
  File "<stdin>", line 1
    list(import())
              ^
SyntaxError: invalid syntax
>>> print sys.modules
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sys' is not defined
>>> import sys
>>> print sys.modules
{'cStringIO': <module 'cStringIO' (built-in)>, 'heapq': <module 'heapq' from '/usr/lib/python2.7/heapq.pyc'>, 'copy_reg': <module 'copy_reg' from '/usr/lib/python2.7/copy_reg.pyc'>, 'sre_compile': <module 'sre_compile' from '/usr/lib/python2.7/sre_compile.pyc'>, 'tokenize': <module 'tokenize' from '/usr/lib/python2.7/tokenize.pyc'>, 'locale': <module 'locale' from '/usr/lib/python2.7/locale.pyc'>, '_sre': <module '_sre' (built-in)>, 'functools': <module 'functools' from '/usr/lib/python2.7/functools.pyc'>, 'encodings': <module 'encodings' from '/usr/lib/python2.7/encodings/__init__.pyc'>, 'site': <module 'site' from '/usr/lib/python2.7/site.pyc'>, '__builtin__': <module '__builtin__' (built-in)>, 'subprocess': <module 'subprocess' from '/usr/lib/python2.7/subprocess.pyc'>, 'sysconfig': <module 'sysconfig' from '/usr/lib/python2.7/sysconfig.pyc'>, 'gc': <module 'gc' (built-in)>, '__main__': <module '__main__' (built-in)>, 'operator': <module 'operator' (built-in)>, 'encodings.encodings': None, 'pkgutil': <module 'pkgutil' from '/usr/lib/python2.7/pkgutil.pyc'>, 'select': <module 'select' (built-in)>, '_heapq': <module '_heapq' (built-in)>, 'abc': <module 'abc' from '/usr/lib/python2.7/abc.pyc'>, 'posixpath': <module 'posixpath' from '/usr/lib/python2.7/posixpath.pyc'>, '_weakrefset': <module '_weakrefset' from '/usr/lib/python2.7/_weakrefset.pyc'>, 'errno': <module 'errno' (built-in)>, 'binascii': <module 'binascii' (built-in)>, 'encodings.codecs': None, 'sre_constants': <module 'sre_constants' from '/usr/lib/python2.7/sre_constants.pyc'>, 're': <module 're' from '/usr/lib/python2.7/re.pyc'>, '_abcoll': <module '_abcoll' from '/usr/lib/python2.7/_abcoll.pyc'>, 'collections': <module 'collections' from '/usr/lib/python2.7/collections.pyc'>, 'types': <module 'types' from '/usr/lib/python2.7/types.pyc'>, '_codecs': <module '_codecs' (built-in)>, 'encodings.__builtin__': None, 'opcode': <module 'opcode' from '/usr/lib/python2.7/opcode.pyc'>, '_struct': <module '_struct' (built-in)>, '_warnings': <module '_warnings' (built-in)>, 'fcntl': <module 'fcntl' (built-in)>, 'genericpath': <module 'genericpath' from '/usr/lib/python2.7/genericpath.pyc'>, 'stat': <module 'stat' from '/usr/lib/python2.7/stat.pyc'>, 'zipimport': <module 'zipimport' (built-in)>, '_sysconfigdata': <module '_sysconfigdata' from '/usr/lib/python2.7/_sysconfigdata.pyc'>, 'string': <module 'string' from '/usr/lib/python2.7/string.pyc'>, 'warnings': <module 'warnings' from '/usr/lib/python2.7/warnings.pyc'>, 'UserDict': <module 'UserDict' from '/usr/lib/python2.7/UserDict.pyc'>, 'inspect': <module 'inspect' from '/usr/lib/python2.7/inspect.pyc'>, 'encodings.utf_8': <module 'encodings.utf_8' from '/usr/lib/python2.7/encodings/utf_8.pyc'>, 'repr': <module 'repr' from '/usr/lib/python2.7/repr.pyc'>, 'sys': <module 'sys' (built-in)>, '_collections': <module '_collections' (built-in)>, 'imp': <module 'imp' (built-in)>, 'codecs': <module 'codecs' from '/usr/lib/python2.7/codecs.pyc'>, 'readline': <module 'readline' from '/usr/lib/python2.7/lib-dynload/readline.x86_64-linux-gnu.so'>, 'commands': <module 'commands' from '/usr/lib/python2.7/commands.pyc'>, '_sysconfigdata_nd': <module '_sysconfigdata_nd' from '/usr/lib/python2.7/plat-x86_64-linux-gnu/_sysconfigdata_nd.pyc'>, 'token': <module 'token' from '/usr/lib/python2.7/token.pyc'>, 'os.path': <module 'posixpath' from '/usr/lib/python2.7/posixpath.pyc'>, 'struct': <module 'struct' from '/usr/lib/python2.7/struct.pyc'>, '_functools': <module '_functools' (built-in)>, '_locale': <module '_locale' (built-in)>, 'sitecustomize': <module 'sitecustomize' from '/usr/lib/python2.7/sitecustomize.pyc'>, 'thread': <module 'thread' (built-in)>, 'keyword': <module 'keyword' from '/usr/lib/python2.7/keyword.pyc'>, 'pickle': <module 'pickle' from '/usr/lib/python2.7/pickle.pyc'>, 'signal': <module 'signal' (built-in)>, 'traceback': <module 'traceback' from '/usr/lib/python2.7/traceback.pyc'>, 'marshal': <module 'marshal' (built-in)>, 'pydoc': <module 'pydoc' from '/usr/lib/python2.7/pydoc.pyc'>, 'linecache': <module 'linecache' from '/usr/lib/python2.7/linecache.pyc'>, 'itertools': <module 'itertools' (built-in)>, 'posix': <module 'posix' (built-in)>, 'encodings.aliases': <module 'encodings.aliases' from '/usr/lib/python2.7/encodings/aliases.pyc'>, 'time': <module 'time' (built-in)>, 'exceptions': <module 'exceptions' (built-in)>, 'sre_parse': <module 'sre_parse' from '/usr/lib/python2.7/sre_parse.pyc'>, 'os': <module 'os' from '/usr/lib/python2.7/os.pyc'>, '_weakref': <module '_weakref' (built-in)>, 'strop': <module 'strop' (built-in)>, 'dis': <module 'dis' from '/usr/lib/python2.7/dis.pyc'>}
>>> print sys.modules >> one.txt
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'one' is not defined
>>> d1 = commands.getoutput("ls /usr/lib/python2.7/keyword.pyc")
>>> print d1
/usr/lib/python2.7/keyword.pyc
>>> d1 = commands.getoutput("ls /usr/lib/python2.7/keyword.py")
>>> print d1
/usr/lib/python2.7/keyword.py
>>> d1 = commands.getoutput("ls /usr/lib/python2.7/keyword.pyb")
>>> print d1
ls: cannot access /usr/lib/python2.7/keyword.pyb: No such file or directory
>>> d1 = commands.getoutput("cat /usr/lib/python2.7/keyword.py")
>>> print d1
#! /usr/bin/python2.7

"""Keywords (from "graminit.c")

This file is automatically generated; please don't muck it up!

To update the symbols in this file, 'cd' to the top directory of
the python source tree after building the interpreter and run:

    ./python Lib/keyword.py
"""

__all__ = ["iskeyword", "kwlist"]

kwlist = [
#--start keywords--
        'and',
        'as',
        'assert',
        'break',
        'class',
        'continue',
        'def',
        'del',
        'elif',
        'else',
        'except',
        'exec',
        'finally',
        'for',
        'from',
        'global',
        'if',
        'import',
        'in',
        'is',
        'lambda',
        'not',
        'or',
        'pass',
        'print',
        'raise',
        'return',
        'try',
        'while',
        'with',
        'yield',
#--end keywords--
        ]

iskeyword = frozenset(kwlist).__contains__

def main():
    import sys, re

    args = sys.argv[1:]
    iptfile = args and args[0] or "Python/graminit.c"
    if len(args) > 1: optfile = args[1]
    else: optfile = "Lib/keyword.py"

    # scan the source file for keywords
    fp = open(iptfile)
    strprog = re.compile('"([^"]+)"')
    lines = []
    for line in fp:
        if '{1, "' in line:
            match = strprog.search(line)
            if match:
                lines.append("        '" + match.group(1) + "',\n")
    fp.close()
    lines.sort()

    # load the output skeleton from the target
    fp = open(optfile)
    format = fp.readlines()
    fp.close()

    # insert the lines of keywords
    try:
        start = format.index("#--start keywords--\n") + 1
        end = format.index("#--end keywords--\n")
        format[start:end] = lines
    except ValueError:
        sys.stderr.write("target does not contain format markers\n")
        sys.exit(1)

    # write the output file
    fp = open(optfile, 'w')
    fp.write(''.join(format))
    fp.close()

if __name__ == "__main__":
    main()
>>> if not has_imported("sys"):
...    import sys
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'has_imported' is not defined
>>> sys.path
['', '/usr/local/lib/python2.7/dist-packages/robotframework_requests-0.4.7-py2.7.egg', '/usr/lib/python2.7/dist-packages', '/usr/lib/python2.7', '/usr/lib/python2.7/plat-x86_64-linux-gnu', '/usr/lib/python2.7/lib-tk', '/usr/lib/python2.7/lib-old', '/usr/lib/python2.7/lib-dynload', '/usr/local/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages/PILcompat', '/usr/lib/python2.7/dist-packages/gtk-2.0', '/usr/lib/python2.7/dist-packages/ubuntu-sso-client', '/usr/lib/python2.7/dist-packages/wx-2.8-gtk2-unicode']
>>> os.getcwd()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'os' is not defined
>>> import os
>>> os.getcwd()
'/home/spanidea/naveen/python'
>>> os.listdir(os.getcwd())
['log_file.py', 'rev_1.pyc', 'a', 're', 'a.txt', 'test2.xml', 'pexpect1.py', 'max_digit.py', 'copied_data_through_screen', 'dict1.py', 'dis_module.py', 'file123.txt', 'f1', 'list_comprehension.py', 'hello.txt', 'file_open1.py', 'pexpect11.py', 'robot1.txt', 'list_int.py', 'xft7.txt', 'xft8.txt', 'reverse_list.py', 'file_handling.py', 'robotframework-requests-0.4.7', 'test11.txt', 'file2.py', 'robot2.txt', 'aqw', 'robotframework-requests-0.4.7.tar.gz', 'store_cmd_output_to_file.py', 'aqwq', 'rev_1.py', 'file3.py', 'if_else.py', 'for_loop.py', 'simple1.py', 'newdir', 'set_comprehension.py', 'sys_stdout.py', 'python.zip', 'example1.log', 'asd', 'outfile123.txt', 'file_hello.py', 'log.html', 'file2.robot', 'length.py', 'f3', 'example.log', 'hai.txt', 'f2.txt', 'range.py', 'fh.py', 'ip_addresses.txt', 'pwd.txt', 'robot1.rebot', 'append.py', 'output.xml', 'report.html', 'python1_bkp.py', 'file333.txt', 'as', 'testfile.txt', 'Animals', 'even_or_odd.python', 'even_or_odd.py', 'dict.py', 'file1.robot', 'split_lines_in_text_file.py', 'chfile', '.list_comprehension.py.swp', 'wa', 'f7', 're_org', 'filee.txt', 'set1.py', 'log_2.xml', 'read_file.py', 'teest.py', 'import_package.py', 'Package1', 'decorator.py', 'log_1.xml', 'regex_state.py', 're_org.txt', 'python1.py', 'count_list.robot', 'logging.pyc', 'file_open.py', 'robot3.robot', 'test1.xml', 'robot2.robot', 'life.txt', 'log.txt', 'sys_cmds.py']
>>> os.modules
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'modules'
>>> print os.modules
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'modules'
>>> sys.path
['', '/usr/local/lib/python2.7/dist-packages/robotframework_requests-0.4.7-py2.7.egg', '/usr/lib/python2.7/dist-packages', '/usr/lib/python2.7', '/usr/lib/python2.7/plat-x86_64-linux-gnu', '/usr/lib/python2.7/lib-tk', '/usr/lib/python2.7/lib-old', '/usr/lib/python2.7/lib-dynload', '/usr/local/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages/PILcompat', '/usr/lib/python2.7/dist-packages/gtk-2.0', '/usr/lib/python2.7/dist-packages/ubuntu-sso-client', '/usr/lib/python2.7/dist-packages/wx-2.8-gtk2-unicode']
>>> print os.path
<module 'posixpath' from '/usr/lib/python2.7/posixpath.pyc'>
>>> import glob
>>> glob.glob("/home/spanidea/naveen/python/*.txt")
['/home/spanidea/naveen/python/a.txt', '/home/spanidea/naveen/python/file123.txt', '/home/spanidea/naveen/python/hello.txt', '/home/spanidea/naveen/python/robot1.txt', '/home/spanidea/naveen/python/xft7.txt', '/home/spanidea/naveen/python/xft8.txt', '/home/spanidea/naveen/python/test11.txt', '/home/spanidea/naveen/python/robot2.txt', '/home/spanidea/naveen/python/outfile123.txt', '/home/spanidea/naveen/python/hai.txt', '/home/spanidea/naveen/python/f2.txt', '/home/spanidea/naveen/python/ip_addresses.txt', '/home/spanidea/naveen/python/pwd.txt', '/home/spanidea/naveen/python/file333.txt', '/home/spanidea/naveen/python/testfile.txt', '/home/spanidea/naveen/python/filee.txt', '/home/spanidea/naveen/python/re_org.txt', '/home/spanidea/naveen/python/life.txt', '/home/spanidea/naveen/python/log.txt']
>>> x = glob.glob("/home/spanidea/naveen/python/*.txt")
>>> print x
['/home/spanidea/naveen/python/a.txt', '/home/spanidea/naveen/python/file123.txt', '/home/spanidea/naveen/python/hello.txt', '/home/spanidea/naveen/python/robot1.txt', '/home/spanidea/naveen/python/xft7.txt', '/home/spanidea/naveen/python/xft8.txt', '/home/spanidea/naveen/python/test11.txt', '/home/spanidea/naveen/python/robot2.txt', '/home/spanidea/naveen/python/outfile123.txt', '/home/spanidea/naveen/python/hai.txt', '/home/spanidea/naveen/python/f2.txt', '/home/spanidea/naveen/python/ip_addresses.txt', '/home/spanidea/naveen/python/pwd.txt', '/home/spanidea/naveen/python/file333.txt', '/home/spanidea/naveen/python/testfile.txt', '/home/spanidea/naveen/python/filee.txt', '/home/spanidea/naveen/python/re_org.txt', '/home/spanidea/naveen/python/life.txt', '/home/spanidea/naveen/python/log.txt']
>>> 
>>> x[1]
'/home/spanidea/naveen/python/file123.txt'
>>> x[2]
'/home/spanidea/naveen/python/hello.txt'
>>> x[2].split('/')
['', 'home', 'spanidea', 'naveen', 'python', 'hello.txt']
>>> y = x[2].split('/')
>>> y[1]
'home'
>>> y[1].split('\w')
['home']
>>> x = glob.glob("/home/spanidea/naveen/python/*.py")
>>> x[2]
'/home/spanidea/naveen/python/max_digit.py'
>>> 



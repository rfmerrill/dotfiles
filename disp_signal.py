#!/usr/bin/env python
import ctypes
import signal
import sys

signum = int(sys.argv[1])

strsignal = ctypes.CDLL("libc.so.6").strsignal
strsignal.restype = ctypes.c_char_p

signames = []

for name in dir(signal):
    if name[0:3] != "SIG":
        continue
    if name[3] == '_':
        continue
    if getattr(signal, name) == signum:
        signames.append(name)

print strsignal(signum) + " (" + ", ".join(signames) + ")"

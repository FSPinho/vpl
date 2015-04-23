#!/usr/bin/env python

import sys
import tempfile
import os
import subprocess

def main():
    execFile = sys.argv[1]
    casesFile = sys.argv[2]

    textCases = "#" + open(casesFile).read()
    cases = textCases.split(">>\n")
    del cases[0]

    for caso in cases:
        in_out = caso.split("<<\n")
        in_ = in_out[0]
        out_ = in_out[1]
        in_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
        out_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
        alu_file = tempfile.NamedTemporaryFile(mode='w', delete=False)

        in_file.write(in_)
        out_file.write(out_)

        in_file.flush()#forca escrita agora
        out_file.flush()

        proc1 = subprocess.Popen(os.path.abspath(execFile), stdin = in_file, stdout = alu_file, shell = True)
        proc1.wait()
        alu_file.flush()
        alu_file.close()
        alu_file = open(alu_file.name, mode='r')

        #param = ['-Z', '-B', out_file.name, alu_file.name]
        #proc2 = subprocess.Popen(['diff'] + param)
        print "ENTRADA\n" + in_
        print "ESPERADO\n" + out_
        print "OBTIDO\n" + alu_file.read()
        #proc2.wait()

main()

#/usr/bin/env python3

import sys
import os
import subprocess

CASE_TAG = 'case'
INPUT_TAG = 'input'
OUTPUT_TAG = 'output'
GRADE_RED_TAG = 'grade reduction'

def formatOutput(text):
    while '\n\n' in text:
        text = text.replace('\n\n', '\n')
    while ' \n' in text:
        text = text.replace(' \n', '\n')
    while '  ' in text:
        text = text.replace('  ', ' ')

    return text

def removeDoubleWhiteSpaces(text):
    while '  ' in text:
        text = text.replace('  ', ' ')

    return text

def removeEnter(text):
    while '\n' in text:
        text = text.replace('\n', '')

    return text

def removeEnterAndSpaces(text):
    while ' ' in text:
        text = text.replace(' ', '')
    while '\n' in text:
        text = text.replace('\n', '')

    return text

def formatText(text):
    while '  ' in text:
        text = text.replace('  ', ' ')
    while '\n\n' in text:
        text = text.replace('\n\n', '\n')
    while '= ' in text:
        text = text.replace('= ', '=')
    while ' =' in text:
        text = text.replace(' =', '=')

    return text

def analizeCase(caseText, responseFile):
    caseNumber = caseText[0 : caseText.index(INPUT_TAG)]
    caseNumber = int(removeEnterAndSpaces(caseNumber))

    caseText = caseText[caseText.index(INPUT_TAG) : len(caseText)]

    caseInput = caseText[0 + len(INPUT_TAG) + 1 : caseText.index(OUTPUT_TAG)]
    caseInput = removeDoubleWhiteSpaces(caseInput)
    caseInput = removeEnter(caseInput)

    caseText = caseText[caseText.index(OUTPUT_TAG) : len(caseText)]

    caseOutput = caseText[0 + len(OUTPUT_TAG) + 1 : caseText.index(GRADE_RED_TAG)]
    caseOutput = caseOutput[0 : len(caseOutput)]
    caseOutput = formatOutput(caseOutput)

    caseText = caseText[caseText.index(GRADE_RED_TAG) : len(caseText)]

    caseGradeRed = caseText[0 + len(GRADE_RED_TAG) + 1 : len(caseText)]
    while caseGradeRed[len(caseGradeRed) - 1] == '\n':
        caseGradeRed = caseGradeRed[0 : len(caseGradeRed) - 1]

    open('temp', 'w').write(caseInput)
    #script = 'python ' + responseFile + ' < temp' #felipe
    script = './' + responseFile + ' < temp'#sena
    p = os.popen(script,"r")
    result = ''
    while 1:
        line = p.readline()
        if not line: break
        result += line

    if os.path.isfile('temp'):
        os.remove('temp')

    result = formatOutput(result)

    if result != caseOutput:
        print 'Test ', caseNumber
        print 'Incorrect result!'
        print 'output program:'
        print result
        print 'expected result:'
        print caseOutput
        return False

    return True



def main():
    responseFile = sys.argv[1]
    casesFile = sys.argv[2]

    textCases = open(casesFile).read()
    textCases = formatText(textCases)

    cases = textCases.split("case=")
    del cases[0]

    flagCorrect = True

    for i in cases:
        flagCorrect &= analizeCase(i, responseFile)

    if flagCorrect:
        print 'All tests are correct!'
    else:
        print 'Incorrect tests!'

main()

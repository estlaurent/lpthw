# 21.02.2018
# creates random sequences of chords
# use as a practice tool
# it will write the sequences to a text file named chords.txt

from random import randint

notes = ['C', 'C#', 'Db', 'D', 'Eb', 'E', 'F', 'F#',
'Gb', 'G', 'G#', 'Ab', 'A', 'Bb', 'B']

quality = ['', 'maj7', 'min', 'min7', 'min7b5', 'sus4', 'sus2', '7', '+', 'dim']

size = 4

def sequence():
    list = []
    i = 0
    list.append('\n'*2)
    while i <= size:
        list.append(notes[randint(0, 14)])
        list.append(quality[randint(0, 9)])
        list.append('  |  ')
        i += 1
    txt = open("chords.txt", 'a')
    txt.write(''.join(list))
    txt.close()

for _ in range(16):
    sequence()

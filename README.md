# The Enigma Machine

A simulator of the German Enigma Mahcine of WWII.<br>

## Paper Enigma

The paper enigma python script is based off the paper enigma found at:
[Paper Enigma](https://mckoss.com/posts/paper-enigma/)

Run the script by:

> $ python3 paper-enigma.py

You will see a print out of the first letter of Mr. Koss' example. The letter "E".<br>
the input keys, input/output sides of the rotors, and relector will be printed along with<br>
a detailed explanation of the input, output, and index of the letter as it progresses through<br>
the encoding process.<br>

After continuing, you will be able to input your own letters and view how they go through the<br>
encoding process. Please remember that before an entered letter is processed the right rotor<br>
will rotate one letter unit forward, (that is, in alphbeticall order). No other rotor will rotate<br>
which is unlike the real Enigma machine.<br>

There is no error checking so if things go wonky, pressing Ctrl-C will get you out. Normal quit<br>
is done by entering qq or QQ at the prompt.<br>

## Short Enigma

Run the script by:

> $ short-enigma.py

The short enigma is similar to the paper enigma but only uses the first 6 letters of the<br>
North American Alphabet. This is in hopes that it will be easier to read and understand what is<br>
going on with the machine and code.

## Enigma Machine

The enigma.py (Enigma Machine proper) is still in development.
<br><br>
## Operation Notes As a Reminder to itsf4llofstars

This will begin with a loosley based operation of the German Enigma Machine.

#### Order of Operation

+ Get input letter, and index of input letter. (H).
+ Map input letter to input of rotor.
+ Get letter and index of mapped letter.
+ Get letter on output side of rotor based on inputs index.
+ Repeat for the next two rotors.
+ Map last rotor output to first letter in reflector.
+ Get index of the second letter in reflector.

The above notes are for the author, they may not be readalbe or clear to others, please see<br>
script documentation if available.<br>

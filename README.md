# The Enigma Machine

## A simulator of the German Enigma Mahcine of WWII

This is in developmeant an in no way can a user excpect theses scripts to act or encode in<br>
the same way or manner as a real Enigma Macine does or did. Any text encoded using these<br>
scripts shall NOT be considered safe, secure or free from code breaking actions by other<br>
users or entities. This set of files are not be be considered as a secure way of encoding text,<br>
this is for entertainment purposes only. Thank you.<br>

Users and visitors of this repository are encourage to send me feedback and submit their own<br>
pull requests. I am new to processing pull request so it may take me a few days to process<br>
them.

Note: The code files here do not have any documentation as of yet.<br>
I apologize for any confusion this causes. This is a work in progress.

## Paper Enigma

The paper enigma python script is based off the paper enigma found here:
[Paper Enigma](https://mckoss.com/posts/paper-enigma/)

Run the script by:

> $ python3 paper-enigma.py

You will see a print out of the first letter of Mr. Koss' example. The letter "E". The input<br>
keys, input/output sides of the rotors, and relector will be printed along with a detailed<br>
explanation of the input, output, and index of the letter as it progresses through the<br>
encoding process.<br>

After continuing, you will be able to input your own letters and view how they go through the<br>
encoding process. Please remember that before an entered letter is processed the right rotor<br>
will rotate one letter unit forward, (that is, in alphbetical order with reference to the<br>
input side of the rotor). No other rotor will rotate which is unlike the real Enigma machine.<br>

There is no error checking so if things go wonky, pressing Ctrl-C will get you out. Normal<br>
quit is done by entering qq or QQ at the prompt.<br>

## Short Enigma

Run the script by:

> $ short-enigma.py

The short enigma is similar to the paper enigma but only uses the first 6 letters of the<br>
North American Alphabet. This is in hopes that it will be easier to read and understand what<br>
is going on with the machine and code.<br>

## Enigma Machine

The enigma.py and main.py utilites.py are still in development. You can technically run them<br>
but there is no assurance that they will work, or produce and outpu.<br>

You will need all three files in the directory.

Run the script by:

> $ python3 main.py

## Build Your Own Random Rotors

The build-rotors.py script will build 5 rotors consisting of 26 non-repeating randomized<br>
letter lists, suitable for use in Python code. It will also create 2 reflectors consisting of<br>
26 single-repeating randomized letter lists. The script will write them to a text file named<br>
rotors.txt in the working directory. If a rotors.txt file allredy exists the file will be<br>
overwritten.<br>

You can now use these rotors in your own Enigma Machine. You will need to copy and paste them<br>
into the code yourself.<br>

This first five lists in the rotors.txt file will be the random rotors and the last two lists<br>
will be the reflectors.<br>

Run the script by:

> $ python3 buildrotors.py

<br><br>
## Operation Notes As a Reminder to itsf4llofstars

The below notes are for the author, they may not be readalbe or clear to others,<br>
please see script documentation if available.<br>

This will begin with a loosely based operation of the German Enigma Machine.<br>

### Order of Operation

+ Get input letter, and index of input letter. (H).
+ Map input letter to input of rotor.
+ Get letter and index of mapped letter.
+ Get letter on output side of rotor based on inputs index.
+ Repeat for the next two rotors.
+ Map last rotor output to first letter in reflector.
+ Get index of the second letter in reflector.

The above notes are for the author, they may not be readalbe or clear to others,<br>
please see script documentation if available.<br>

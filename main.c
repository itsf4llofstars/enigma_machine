/*
 * Enigma machine in C
 * */
#include <stdio.h>

void rotateRotor(char rotor[], int n)
{
    for (int i = 0; i < n; ++i)
    {
        char temp = rotor[0];
        for (int i = 0; i < 25; ++i)
            rotor[i] = rotor[i + 1];
        rotor[25] = temp;
    }
}

void printRotor(char rotor[])
{
    for (int i = 0; i < 25; ++i)
        printf("%c ", rotor[i]);
}

int getIndex(char rotor[], char letter) {
    for (int i = 0; i < 25; ++i)
        if (rotor[i] == letter)
            return i;

    return -1;
}

char getLetter(char rotor[], int index) {
    return rotor[index];
}

int main(int argc, char **argv)
{
    char keyboard[] = {
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    };

    char rotorRightIn[] = {
        'A', 'B', 'C', 'E', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    };
    char rotorRightOut[] = {
        'S', 'N', 'M', 'Y', 'K', 'W', 'H', 'Q', 'L', 'F', 'C', 'O', 'E',
        'T', 'G', 'Z', 'D', 'B', 'A', 'I', 'V', 'U', 'J', 'X', 'P', 'R'
    };

    char rotorMiddleIn[] = {
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    };
    char rotorMiddleOut[] = {
        'Y', 'E', 'J', 'S', 'P', 'X', 'A', 'W', 'H', 'O', 'D', 'L', 'F',
        'Q', 'G', 'K', 'B', 'V', 'U', 'I', 'Z', 'N', 'T', 'C', 'R', 'M'
    };

    char rotorLeftIn[] = {
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    };
    char rotorLeftOut[] = {
        'J', 'Y', 'V', 'P', 'X', 'R', 'U', 'I', 'L', 'O', 'H', 'B', 'S',
        'Q', 'G', 'F', 'C', 'A', 'M', 'W', 'T', 'D', 'Z', 'K', 'N', 'E'
    };

    char rightRotor[2][26] = {
    {
        'A', 'B', 'C', 'E', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    },
    {
        'S', 'N', 'M', 'Y', 'K', 'W', 'H', 'Q', 'L', 'F', 'C', 'O', 'E',
        'T', 'G', 'Z', 'D', 'B', 'A', 'I', 'V', 'U', 'J', 'X', 'P', 'R'
    }};

    printRotor(keyboard);
    puts("");

    char letter = 'D';
    int index;
    index = getIndex(keyboard, letter);
    letter = getLetter(rotorRightIn, index);
    printf("%c - %d\n", letter, index);
    printRotor(rotorRightIn);



    puts("");
    return 0;
}


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

// getIndex
// getLetter

int main(int argc, char **argv)
{
    char keyboard[] = {
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    };

    char rotorRightIn[] = {
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    };
    char rotorMiddleIn[] = {
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    };
    char rotorLeftIn[] = {
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    };

    rotateRotor(rotorRightIn, 5);
    printRotor(rotorRightIn);

    puts("");
    return 0;
}


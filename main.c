/*
 * Enigma machine in C
 * */
#include <stdio.h>

void rotateRotor(char rotor[])
{
    char temp = rotorRightIn[0];

    for (int i = 0; i < (sizeof(rotor) / sizeof(char) - 1); ++i)
        rotorRightIn[i] = rotorRightIn[i + 1];

    rotorRightIn[(sizeof(rotor) / sizeof(char) - 1)] = temp;
}

int main(int argc, char **argv)
{
    char keyboard[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
    char rotorRightIn[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};

    int sizeChar = (sizeof(rotorRightIn) / sizeof(char)) - 1;
    printf("S: %d\n", sizeChar);

    for (size_t i = 0; i < (sizeof(rotorRightIn) / sizeof(char)); ++i)
        printf("%c ", rotorRightIn[i]);

    puts("");

    return 0;
}

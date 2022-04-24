/*
 * Enigma machine in C
 * */
#include <stdio.h>

int main(int argc, char **argv)
{
    char keyboard[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};

    char rotorRightIn[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};

    int sizeChar = (sizeof(rotorRightIn) / sizeof(char)) - 1;
    printf("S: %d\n", sizeChar);

    int index = 0;
    do
    {
        char temp = rotorRightIn[0];

        for (int i = 0; i < 25; ++i)
            rotorRightIn[i] = rotorRightIn[i + 1];

        rotorRightIn[25] = temp;

    }
    while (++index < 13);

    for (size_t i = 0; i < (sizeof(rotorRightIn) / sizeof(char)); ++i)
        printf("%c ", rotorRightIn[i]);

    puts("");

    return 0;
}

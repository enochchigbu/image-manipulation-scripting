#include <stdio.h>
#include <stdlib.h>

// Threshold program from C
int main(int argc, char const *argv[])
{
    for (int i = 1; i < argc; i++)
    {
        if (atoi(argv[i]) < 170)
        {
            printf("%d ", 0);
        }
        else
        {
            printf("%d ", 255);
        }
    }
    printf("\n");
}

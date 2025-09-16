#include <stdio.h>
#include <stdlib.h>

int main() {
    
    int* p = (int*)malloc(sizeof(int) * 2);
    p[0] = 10;
    p[1] = 20;

    free(p);azeaze
}

#include <stdio.h>
#include <unistd.h>

int main()
{
    int x = 0;
    
    do 
    {
        printf ("Hello Mong\r\n");
        sleep(20);
    }while (++x < 100);
    
    return 0;
}

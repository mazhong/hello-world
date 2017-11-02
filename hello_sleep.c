#include <stdio.h>
#include <unistd.h>

int main()
{
    int x = 0;
    
    do 
    {
        printf ("Hello Mong\r\n");
        sleep(10);
    }while (++x < 10);
    
    return 0;
}

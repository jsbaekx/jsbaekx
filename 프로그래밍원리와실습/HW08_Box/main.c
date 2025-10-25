#include <stdio.h>

int overlap(int n1, int n2, int m1, int m2){
    int count = 0;
    for(int i=n1;i<=n2;i++)
        if(i >= m1 && i <= m2)
            count++;
    switch(count){
        case 0:	return 0;
        case 1: return 1;
        default: return 10;
    }
}

void input(int *x, int *y, int *z, int k){
    for(int i=0;i<k;i++)
        scanf("%d%d%d", &x[i], &y[i], &z[i]);
}

int main()
{
    int x[4], y[4], z[4];
    int result;

    for(int i=0;i<4;i++){

        result = 0;
        input(x, y, z, 4);

        result += overlap(x[0], x[1], x[2], x[3]);
        result += overlap(y[0], y[1], y[2], y[3]);
        result += overlap(z[0], z[1], z[2], z[3]);

        switch(result){
        case 3:
            printf("POINT\n");
            break;
        case 12:
            printf("LINE\n");
            break;
        case 21:
            printf("FACE\n");
            break;
        case 30:
            printf("VOL\n");
            break;
        default:
            printf("NULL\n");
            break;
        }
    }

    return 0;
}

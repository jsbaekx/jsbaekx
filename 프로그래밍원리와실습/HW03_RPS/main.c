#include <stdio.h>

int main()
{
    int N;
    scanf("%d", &N);
    char RPS[30];
    char win = 'N';
    int sum = 0;
    int i, j;

    for(i = 0;i<N;i++)
        scanf(" %c", &RPS[i]);

    for(i=0;i<N;i++){
        sum = 0;
        for(j=i;j<N;j++){
            if(RPS[j] == 'R')
                sum += 1;
            else if(RPS[j] == 'P')
                sum += 100;
            else if(RPS[j] == 'S')
                sum += 10000;
        }
        if (sum < 100)
            break;
        else if((sum % 10000) == 0)
            break;
        else if ((sum % 100) == 0 && sum < 10000)
            break;
        else if(sum < 10000){
            win = 'P';
            break;
        }
        else if((sum % 100) == 0){
            win = 'S';
            break;
        }
        else if(((sum / 100) % 100) == 0){
            win = 'R';
            break;
        }
    }


    if (win == 'N')
        printf("0\n0");
    else{
        printf("%d\n", i);
        for(j=i;j<N-1;j++){
            if(RPS[j] == win)
                printf("%d ", (j+1));
        }
        if (RPS[j] == win)
            printf("%d", (j+1));
    }
    return 0;
}

#include <stdio.h>

int main()
{
    int N, i=0;
    scanf("%d", &N);
    int count;
    char name[5000][100];
    int price[5000];

    int nak = 10000;

    for(i=0;i<N;i++)
        scanf(" %s %d", name[i], &price[i]);
    while(nak > 0){
        count = 0;
        for (i=N-1;i>=0;i--){
            if(price[i] == nak)
                count += 1;
        }
        if(count == 1)
            break;
        nak--;
    }
    if(nak == 0)
        printf("NONE");
    else{
        for(i=N-1;i>=0;i--){
            if(price[i] == nak){
                printf("%s", name[i]);
                break;
            }
        }
    }
    return 0;
}

#include <stdio.h>
#include <string.h>

int main()
{
    int N, i, price, omax, omin, jmax, omaxi, omini, jmaxi;
    char name[30];
    int discount = 0, total = 0;
    int stdc = 0, oldc = 0, jurc = 0, adlc = 0;
    int STD[30], OLD[30], JUR[30], ADL[30];

    scanf("%d", &N);

    for(i=0;i<N;i++){
        scanf(" %s %d", name, &price);
        /*if(!strcmp(name, "STD"))
            STD[stdc++] = price;
        else if(!strcmp(name, "OLD"))
            OLD[oldc++] = price;
        else if(!strcmp(name, "JUR"))
            JUR[jurc++] = price;
        else if(!strcmp(name, "ADL"))
            ADL[adlc++] = price;*/
        switch(name[0]){
        case 'S':
            STD[stdc++] = price;
            break;
        case 'O':
            OLD[oldc++] = price;
            break;
        case 'J':
            JUR[jurc++] = price;
            break;
        case 'A':
            ADL[adlc++] = price;
            break;
        }
    }
    if (oldc > 0)
    {
    	omax = OLD[0];
    	omaxi = 0;
    	omin = OLD[0];
    	omini = 0;
	}
	if(jurc > 0){
		jmax = JUR[0];
		jmaxi = 0;
	}

    for(i=0;i<oldc;i++){
    	if(OLD[i] > omax){
    		omax = OLD[i];
    		omaxi = i;
		}
		if(OLD[i] < omin){
    		omin = OLD[i];
    		omini = i;
		}
	}
	for(i=0;i<jurc;i++){
    	if(JUR[i] > jmax){
    		jmax = JUR[i];
    		jmaxi = i;
		}
	}
    //discount 3,4,5

    if((stdc >= 1) && (oldc >= 1) && (jurc >= 1))
    	OLD[omaxi] = omax * 4 / 5;
    if(oldc >= 6)
    	OLD[omini] = 0;
    if(jurc >= 5)
    	JUR[jmaxi] = jmax * 7 / 10;

    //discount 1,2
    if((N >= 5) && (N == stdc))
    	discount += 15;
    if(N >= 10)
    	discount += 10;

    for(i=0;i<stdc;i++)
    	total += STD[i];
    for(i=0;i<oldc;i++)
    	total += OLD[i];
    for(i=0;i<jurc;i++)
    	total += JUR[i];
    for(i=0;i<adlc;i++)
    	total += ADL[i];

    total = total * (100-discount) / 100;

    printf("%d", total);
    return 0;
}

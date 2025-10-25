#include "mycrack.h"
#include <stdio.h>
#include <string.h>

int main(){
    char *word1, *word2;
    char myguess[1000];

    int i, j, k;

    myready();
    word1 = getword1();
    word2 = getword2();

    int len1 = strlen(word1);
    int len2 = strlen(word2);

    for(i=0;i<len2;i++){
        for(k=0;k<i;k++)
            myguess[k] = word2[k];
        for(j=i;j<len1+i;j++)
            myguess[j] = word1[j-i];
        for(k=i+len1;k<len1+len2;k++)
            myguess[k] = word2[k-len1];
        myguess[k] = '\0';
        if(crack(myguess))
            got_it(myguess);
    }
    for(i=0;i<len1;i++){
        for(k=0;k<i;k++)
            myguess[k] = word1[k];
        for(j=i;j<len2+i;j++)
            myguess[j] = word2[j-i];
        for(k=i+len2;k<len1+len2;k++)
            myguess[k] = word1[k-len2];
        myguess[k] = '\0';
        if(crack(myguess))
            got_it(myguess);
    }
    return 0;
}

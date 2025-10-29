#include <stdio.h>

void resetZero(int arr[], int N) {
	for (int i = 0; i < N; i++)
		arr[i] = 0;
}

void printSpace(int p[], int N) {
	for (int i = N - 1; i > 0; i--)
		printf("%d ", p[i]);
	printf("%d", p[0]);
}
int main() {
	int N1, N2, N;
	int i, j;
	int p1[30], p2[30], p[40];

	scanf("%d", &N1);
	for (i = 0; i < N1; i++)
		scanf("%d", &p1[N1-i-1]);
	scanf("%d", &N2);
	for (i = 0; i < N2; i++)
		scanf("%d", &p2[N2-i-1]);
	N = N1 + N2 - 1;

	resetZero(p, N);

	for (i = 0; i < N1; i++) 
		for (j = 0; j < N2; j++) 
			p[i + j] += p1[i] * p2[j];

	printSpace(p, N);
	return 0;
}
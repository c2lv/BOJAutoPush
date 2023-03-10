#include <stdio.h>

int main(void)
{
	int N; // DNA의 수 (1,000보다 작거나 같은 자연수)
	int M; // 문자열의 길이 (50보다 작거나 같은 자연수)
	int sum = 0; // s의 Hamming Distance의 합
	char ACGT[5] = "ACGT"; // 뉴클레오티드 문자
	char DNA[1001][51] = { 0 }; // DNA[i]: i + 1번째로 입력받은 DNA
	char s[51] = { 0 }; // Hamming Distance의 합이 가장 작은 DNA

	scanf("%d%d", &N, &M);
	for (int i = 0; i < N; i++)
		scanf("%s", DNA[i]);

	for (int i = 0; i < M; i++)
	{
		int count[4] = { 0 }; // 뉴클레오티드 문자의 수 (인덱스 순서대로 A, C, G, T)
		int temp = 0; // count 값 비교를 위해 사용하는 변수

		for (int j = 0; j < N; j++)
		{
			if (DNA[j][i] == 'A')
				count[0]++;
			else if (DNA[j][i] == 'C')
				count[1]++;
			else if (DNA[j][i] == 'G')
				count[2]++;
			else // (DNA[j][i] == 'T')
				count[3]++;
		}
		for (int j = 0; j < 4; j++)
		{
			if (temp < count[j])
			{
				temp = count[j];
				s[i] = ACGT[j];
			}
		}
		sum += N - temp;
	}
	printf("%s\n%d", s, sum);

	return 0;
}
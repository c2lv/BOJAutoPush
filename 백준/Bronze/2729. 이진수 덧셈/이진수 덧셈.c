#include <stdio.h>

int ft_strlen(char *s)
{
	int len = 0;

	while (s[len] != '\0')
		len++;
	
	return len;
}

void ft_strrev(char *s)
{
	int len = ft_strlen(s);

	for (int i = 0; i < len / 2; i++)
	{
		char temp;

		temp = s[i];
		s[i] = s[len - 1 - i];
		s[len - 1 - i] = temp;
	}
}

int main(void)
{
	int T;

	scanf("%d", &T);
	while (T)
	{
		int binsumlen, index = 0;
		char bin1[81] = "", bin2[81] = "", binsum[82] = "";

		scanf("%s%s", bin1, bin2);

		ft_strrev(bin1);
		ft_strrev(bin2);
		for (int i = 0; i < 80; i++)
		{
			if (bin1[i] != '\0' && bin2[i] != '\0')
				binsum[i] = bin1[i] + bin2[i] - '0';
			else if (bin1[i] == '\0' && bin2[i] == '\0')
				break;
			else if (bin1[i] == '\0')
				binsum[i] = bin2[i];
			else
				binsum[i] = bin1[i];
		}
		binsumlen = ft_strlen(binsum);
		for (int i = 0; i < binsumlen; i++)
		{
			if (binsum[i] == '2' || binsum[i] == '3')
			{
				binsum[i] -= 2;
				if (binsum[i + 1] == '\0')
					binsum[i + 1] = '1';
				else
					binsum[i + 1]++;
			}
		}
		binsumlen = ft_strlen(binsum);
		ft_strrev(binsum);
		while (index < binsumlen)
		{
			if (binsum[index] != '0')
				break;
			index++;
		}
		if (index == binsumlen)
			printf("0");
		else
		{
			for (int i = index; i < binsumlen; i++)
				printf("%c", binsum[i]);
		}
		printf("\n");
		T--;
	}

	return 0;
}
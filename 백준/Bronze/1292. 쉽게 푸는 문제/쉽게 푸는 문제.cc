using namespace std;
#include <iostream>

int main(void)
{
    // sum: a번째 숫자부터 b번째 숫자까지 합
    // 수열의 i번째 숫자: j
    int a, b, sum, i, j;

    sum = 0;
    i = 1;
    j = 1;
    cin >> a;
    cin >> b;
    while (i <= b)
    {
        for (int k = 0; k < j; k++) {
            if (i > b)
                break;
            if (a <= i)
                sum += j;
            i++;
        }
        j++;
    }
    cout << sum;
    return 0;
}
#include <stdio.h>

int is_prime(int a) {
  if (a == 1)
    return 0;
  for (int i = 2; i < a; i++) {
    if (a % i == 0)
      return 0;
  }
  return 1;
}

int main(void) {
  int m = 0, n = 0, s = 0, answer = 0, min_cnt = 0, min = 0;
  scanf("%d", &m);
  scanf("%d", &n);
  s = m;
  while (s >= m && s <= n) {
    int s_is_prime = is_prime(s);
    if (s_is_prime == 1) {
      min_cnt++;
      answer += s;
      if (min_cnt == 1) {
        min = s;
      }
    }
    s++;
  }
  if (answer == 0) {
    printf("%d", -1);
  } else {
    printf("%d\n", answer);
    printf("%d", min);
  }

  return 0;
}
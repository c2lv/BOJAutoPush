def before_45(h, m):
  """
  시와 분을 매개변수로 받아 45분전의 시와 분을 반환하는 함수
  반환값: 45분전의 시와 분
  """
  if m > 44: # 설정 시간이 45분보다 같거나 클경우
    return h, m-45 
  elif m < 45 and h>0: # 분이 45보다 작고 시간은 0보다 클 경우
    return h-1, m+15
  else: # 0시일 경우
    return 23, m+15

# 프로그램 시작
h, m = map(int,input().split())
h, m = before_45 (h, m)
print(h, m) # 함수 호출로 값을 구함
1| def tri(n):
2|     return n + tri(n - 1)

1| def tri1(n):
2|     if n == 1:
3|         return 1
4|     else:
5|         return n + tri(n-1)


1| def tri2(n):
2|     if n > 1:
3|         return n + tri(n-1)
4|     else:
5|         return 1


import math

n = 20
k = 20

routes = (math.factorial(n + k) / (math.factorial(k) * (math.factorial(n))))

print(routes)


# (n+k) C n
# (n+k)! / k!((n+k) - k)!)

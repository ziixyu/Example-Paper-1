
def equation(x):
    return (x**3+x**2)

def NumericalIntegration(a, b, x, w, n):
    sum = 0
    for i in range(0, n):
        f = equation(x[i])
        sum+=(w[i]*f)
    return (b-a)*(sum)

a = 0
b = 10
print(NumericalIntegration(a,b,[a,b],[1/2,1/2],2))
print(NumericalIntegration(a,b,[a,(a+b)/2, b],[1/6,2/3, 1/6],3))
print(NumericalIntegration(a,b,[(1/2)*(a+b+((b-a)/3**1/2)),(1/2)*(a+b+((b-a)/3**1/2))],[1/2,1/2],2))
# Unsure what the +- means and how to program that?
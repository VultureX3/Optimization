import math


def func(x):
    # return math.exp(x)
    # return (x - 15) ** 2 + 5
    return math.cos(x)


class Function:

    def __init__(self, func, left, right):
        self.func = func
        self.left = left
        self.right = right

    def dichotomy(self, eps):
        left = self.left
        right = self.right
        sigma = 2 + eps
        count = 0
        while (right - left) > eps:
            count += 1
            mid1 = (left + right) / 2 - eps / sigma
            mid2 = (left + right) / 2 + eps / sigma
            if self.func(mid1) > self.func(mid2):
                left = mid1
            else:
                right = mid2
            # print(left, right)
        return (left + right) / 2, count

    def golden_section(self, eps):
        left = self.left
        right = self.right
        count = 0
        while (right - left) > eps:
            count += 1
            mid1 = left + (right - left) * ((3 - math.sqrt(5)) / 2)
            mid2 = left + (right - left) * ((math.sqrt(5) - 1) / 2)
            if self.func(mid1) > self.func(mid2):
                left = mid1
            else:
                right = mid2
            # print(left, right)
        return (left + right) / 2, count

    def __fib(self, n):
        return (((1 + math.sqrt(5)) / 2) ** n - ((1 - math.sqrt(5)) / 2) ** n) / math.sqrt(5)

    def fibonacci(self, eps):
        left = self.left
        right = self.right
        n = 0
        while self.__fib(n) <= (right - left) / eps:
            n += 1
        count = 0
        while (right - left) > eps:
            count += 1
            mid1 = left + self.__fib(n-count - 1) * (right - left) / self.__fib(n - count + 1)
            mid2 = left + self.__fib(n - count) * (right - left) / self.__fib(n - count + 1)
            if self.func(mid1) > self.func(mid2):
                left = mid1
            else:
                right = mid2
            # print(left, right)
        return (left + right) / 2, count

    def on_line(self, eps, x0):
        if self.func(x0) > self.func(x0 + eps):
            x = x0 + eps
            h = eps
        elif self.func(x0) > self.func(x0 - eps):
            x = x0 - eps
            h = -eps
        while self.func(x0) > self.func(x):
            h *= 2
            x0, x = x, x + h
        return x0 - h/2, x


if __name__ == "__main__":
    foo = Function(func, 0, 2 * math.pi)
    eps = 0.001
    print(foo.dichotomy(eps))
    print(foo.golden_section(eps))
    print(foo.fibonacci(eps))
    print(foo.on_line(eps, 1))

def test_function(v):
    def inner_function(n):
        x = int(n)*5
        print(x)
        return x

    print(2*inner_function(v))

test_function(input())

inner_function(5)
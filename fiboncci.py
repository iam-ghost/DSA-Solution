def ret_fib_series(series):
    if series == 2:
        return 1
    elif series == 1:
        return 0
    else:
        return ret_fib_series(series-1) + ret_fib_series(series-2)



def dis_fib_series(no_element):
    return [ ret_fib_series(i) for i in range(1, no_element + 1) ]




elements = int(input("Enter no. of elements: ") )
fibonacci_series = dis_fib_series(elements)

print(fibonacci_series)

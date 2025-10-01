def test_exception(divisor: int):
    try:
        10 / divisor
    except ZeroDivisionError:
        print("Divide by zero is invalid")
    else:
        pass
        print("No Exception")
    finally:
        print("I run always!")

print('---------')
test_exception(0)
print('---------')
test_exception(2)
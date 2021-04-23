try:
    print("line1")
    try:
        print("line2")
        print("line3")
    except ZeroDivisionError:
        print("except 1")
    finally:
        print("finally1")
except TypeError:
    print("except2")

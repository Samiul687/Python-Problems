def iq_test(numbers):
    new = []
    check = []
    check2 = ["ree"]
    even = []
    odd = []

    for i in numbers.split(" "):
        new.append(int(i))

    for j in range(len(new)):
        if new[j] % 2 == 0:
            even.append(j+1)
        else:
            odd.append(j+1)


    if len(even) == 1:
        return even[0]
    else:
        return odd[0]

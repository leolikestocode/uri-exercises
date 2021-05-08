n = int(input())

ints = [1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1]
nums = ['M',  'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

ints_index = 0
roman = ''

while (n != 0):
    if (n - ints[ints_index] >= 0):
        roman += nums[ints_index]
        n -= ints[ints_index]

    if (n - ints[ints_index] < 0):
        ints_index += 1

print(roman)

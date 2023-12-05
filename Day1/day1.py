sum = 0
nums = {
    'one' : 'o1e',
    'two' : 't2o',
    'three' : 't3e',
    'four' : 'f4r',
    'five' : 'f5e',
    'six' : 's6x',
    'seven' : 's7n',
    'eight' : 'e8t',
    'nine' : 'n9e'
}

def replace_nums(s):
    l=0
    r=1
    while r<len(s):
        found = False
        for num in nums.keys():
            if num in s[l:r]:
                s = s.replace(num, nums[num])
                l=0
                r=1
                found = True
                break
        if not found:
            r += 1
    
    return s

with open("input.txt", 'r') as f:
    for line in f.readlines():
        line = replace_nums(line)
        first = None
        last = None
        for char in line:
            if char.isdigit() and not first:
                first = char
            elif char.isdigit():
                last = char
        if last:
            sum += int(f'{first}{last}')
        else:
            sum += int(first*2)
f.close()

print(sum)
digits_digits = []
digits_letter = []

for i in range(0,100):
    digit  = str(i)
    letter = num2words.num2words(str(i)).replace('-','').replace(' ','')
    digits_digits.append(digit)
    digits_letter.append(letter)
    
digits_rplace = dict(zip(digits_letter, digits_digits))

input_file = "C:/Users/Lilian/Desktop/Advent of Code 2023/input_day_1.txt"

numbers = []

with open(input_file, "r") as f:
    for line in f:
        l1 = line.replace('\n','')
        
        l2 = l1
        
        for k,v in sorted(digits_rplace.items(), key=lambda x:int(x[1]),reverse=True):  
            v  = k[0] + v + k[-1]
            l2 = l2.replace(k,v)
        
        l3 = ''.join([c for c in l2 if c in digits_digits])
        l4 = l3[0] + l3[-1]
        #print(l1,l2,l3,l4)
        numbers.append(l4)
        
result = sum([int(n) for n in numbers])
print(result)
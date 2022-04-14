#Q1 answer: we should define "main"

from pickle import TRUE 
while TRUE: 
    count = int(input("Enter X value: ")) 
    if (0< count <=10): 
            nums = [] 
            for i in range(count): 
                num = input(" ") 
                nums.append(int(num)) 
            print('\n') 
            for num in nums:     
                if num % 2 == 0: 
                    print(f"{num} is even") 
                else: 
                    print(f"{num} is odd") 
    if (0< count <=10): 
        break
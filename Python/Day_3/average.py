def listAverage(nums):
    sum = 0

    for item in nums:
        sum += item
    
    return sum/len(nums)

def main():
    nums = [1, 2, 3, 4, 5]
    print(f"The list is {nums}")

    avg = listAverage(nums)

    print(f"Average is: {avg}")

if __name__ == "__main__":
    main()
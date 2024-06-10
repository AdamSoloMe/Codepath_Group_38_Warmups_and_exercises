from collections import Counter

if __name__ == '__main__':
    nums=[2,2,1,1,1,2,2]
    c=Counter(nums)
    print(c)
    for v in c.values():
        if v>(len(nums)/2)+1:
            return v
    # Creating a hash table to keep track of the total value of each element in the array
    # total_elements_hashtable = {}
    #
    # # Looping over the array to Add numbers to the hash table
    # for num in nums:
    #     if num in total_elements_hashtable.keys():  # if the number has already been added to the hashtable increase the value by 1
    #         total_elements_hashtable[num] += 1
    #     else:  # else if the number has not already been added to the hashtable mark the vale with a 1
    #         total_elements_hashtable[num] = 1
    #
    #         # If the number of counts reach n/2 + 1 (more than n/2) return that number
    #     if total_elements_hashtable[num] > (len(nums) / 2):
    #         print(num)
    #
    #


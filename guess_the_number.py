import random

class GuessNumber:
    def __init__(self, picked_number):
        self.picked_number = picked_number
        self.total_tries_remaining = 10

    def check_prediction(self, guess):
        if self.total_tries_remaining == 0:
            raise Exception("You have reached your tries limit!")
        self.total_tries_remaining -= 1

        if guess < self.picked_number:
            return 1
        elif guess > self.picked_number:
            return -1
        else:
            return 0

    def guess_number(self):
        # Implement your code here
        arr = [i for i in range(0, 1001)] #creates an array from 1-1000 where index zero stores 0 as junk
        low = 0
        high = 1000

        while low <= high:
            mid = (low + high) // 2
            if self.picked_number < arr[mid]:
                high = mid -1
            elif self.picked_number > arr[mid]:
                low = mid + 1
            else:
                return mid
            
        return -555 #junk sentinal if not number not guessed or is out of bounds
            
    


        pass
    

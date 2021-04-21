class Solution:


    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order.
        Works  : brute force approach : might the ebst approach 
        """
        
        
        idx1 = 0
        idx2 = 1  
        
        while (idx1 != len(nums)-1 ):
            
            if nums[idx1 ] + nums[idx2] == target :
                return [idx1, idx2]
            else :
                
                if idx2 == len(nums)-1:
                    idx1=idx1+1
                    idx2=idx1+1
                else:
                    idx2 = idx2 +1            
            
        
        return [None, None]

    def twoSum_v2(self, nums: List[int], target: int) -> List[int]:
        
        collection ={} #Key -> value of list itself and   #value -> index of the value in the list.        
        for i, val  in enumerate(nums):            
            potential_val = target - val   # Asumming they are positive integers!            
            if potential_val not in collection:
                collection[val] = i                
            else:
                return [ collection[potential_val] , i  ]





"""

Design a logger system that receives a stream of messages along with their timestamps. Each unique message should only be printed at most every 10 seconds (i.e. a message printed at timestamp t will prevent other identical messages from being printed until timestamp t + 10).
All messages will come in chronological order. Several messages may arrive at the same timestamp.
Implement the Logger class:
Logger() Initializes the logger object.
bool shouldPrintMessage(int timestamp, string message) Returns true if the message should be printed in the given timestamp, otherwise returns false.
works: brute force approach
"""

class Logger:
    
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.recent_messages= {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        
        """
        
        if message in self.recent_messages:
            #check  how long ago it was 
            if (timestamp -10 ) >= self.recent_messages[message]:
                #if it is more than 10 ago
                self.recent_messages[message] = timestamp
                return True
            else:
                #self.recent_messages[message] = timestamp #This should be a question .  Does it need to be updated last time it was seen even tho is not printed ?
                return False
        else:
            self.recent_messages[message] = timestamp
            return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)


"""

You are given a data structure of employee information, which includes the employee's unique id, their importance value and their direct subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.

Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all their subordinates.

Example 1:

Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
Output: 11
Explanation:
Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.
 
Note:

One employee has at most one direct leader and may have several subordinates.
The maximum number of employees won't exceed 2000.

# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
Optimal Solution 
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        
        employees = { employee.id : employee for employee in employees} # Make set of employees to finding the employee converts to O(1)
        
        
        def find_importance( target_id ):
            
            #Find the employee
            selected= employees[target_id]
            
            if len(selected.subordinates) <= 0 :
                return selected.importance
            else:
                return selected.importance + sum( [ find_importance(subordinate_id) for subordinate_id in selected.subordinates  ]) 
            
            
        
        return find_importance(id )




"""



Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
Implement the MovingAverage class:
MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.
Example 1:

Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
 

Constraints:
1 <= size <= 1000
-105 <= val <= 105
At most 104 calls will be made to next.

 brute force approach
"""

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size =size
        self.vals_list= []
        

    def next(self, val: int) -> float: 
        
        self.vals_list.append(val)    
        len_vals=len(self.vals_list)
        fixed_length = len_vals if len_vals < self.size else self.size 
        
        
        return sum( self.vals_list[len_vals-fixed_length  :len_vals ] )/ fixed_length
        

##
### DEQUE APPROACH

from collections import deque 

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size        
        self.tracker = deque()
        self.sum = 0
        

    def next(self, val: int) -> float: 
        
        
        #Idea is to make self.sum always keep track of the sum using the deque
        self.tracker.append(val) # Is like double update once for the tracker and then for the sume 
        
        if len(self.tracker) > self.size:            
            self.sum-=self.tracker.popleft()# Deque used to substract what is not used anymore 
        
        self.sum += val
        
        return  self.sum / len(self.tracker)
        


"""
About Ranges :

       A                       B
  |---------|           |-----------|
start      end        star         end

if A.end > B.star  AND A.star < B.end  THEN they collide(edges EXCLUSIVE)

The problem was not really abuot this but I will keep this as a future resource
"""





"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1
 

Constraints:
1 <= intervals.length <= 104
0 <= starti < endi <= 106
Accepted

Good: brute force approach
"""
        
class Solution:
    
    #Can assumet the order if the input is sorted ?  No

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        def myFunc(e):
            return e[0]
    
        max_rooms=0
        current_times = []
        #sort intervals
        
        intervals.sort(key=myFunc )
        
        for new_interval in intervals:            
            
            #Find if any time is passed the time 
            counter=0
            while (counter < len(current_times)) :                
                if new_interval[0] >= (current_times[counter])[1]:
                    #delete this 
                    current_times.pop(counter)
                else:
                    counter += 1
            
            current_times.append(new_interval)            
            max_rooms =  max_rooms if max_rooms > len(current_times) else  len(current_times)

        return max_rooms




""""
Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.

For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each email[i], return the number of different addresses that actually receive mails.

best optimal solution :works : Unique Email Address 
""""


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            seen.add(local.replace('.', '')+'@'+domain)
        return len(seen)



"""
You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key.

 

Example 1:

Input: s = "5F3Z-2e-9-w", k = 4
Output: "5F3Z-2E9W"
Explanation: The string s has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.
Example 2:

Input: s = "2-5g-3-J", k = 2
Output: "2-5G-3J"
Explanation: The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.
 
"""
#My Brute force solution 
import math
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
        s=s.replace("-","")
        len_str=len(s)
        
        n_groups =math.floor(len_str /k) 
        
        every4=[ len_str- ( (i+1)*k ) for i in range(n_groups)]
        
        for i in every4:
            if i != 0:
                s=s[:i]+'-'+s[i:]
            
        return s.upper()
        


#Optimized SOlution 
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace("-", "").upper()[::-1]
        return '-'.join(S[i:i+K] for i in range(0, len(S), K))[::-1]
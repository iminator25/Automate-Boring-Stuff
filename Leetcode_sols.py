#-----------------------------------------====------------------------------------------
# 104. Maximum Depth of Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# sample input: [3,9,20,null,null,15,7]
#   3
#  / \
# 9  20
#   /  \
#  15   7
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        height = 0
        if root == None:
            return height
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left,right)+1


#-----------------------------------------====------------------------------------------
# 136. Single Number
# Given a non-empty array of integers nums, 
# every element appears twice except for one. Find that single one.

#Notes here are that sets can be "-" not arrays. 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        seen = set()
        seen1 = set()
        for v in nums:
            if v not in seen:
                seen.add(v)
            else:
                seen1.add(v)
        return int((seen - seen1).pop())


#-----------------------------------------====------------------------------------------

# 237. Delete Node in a Linked List
# Write a function to delete a node in a singly-linked list. 
# You will not be given access to the head of the list, instead 
# you will be given access to the node to be deleted directly.
# It is guaranteed that the node to be deleted is not a tail node in the list.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# what we are doing here is by passing the next node in the list
# making the current node have value of its next thing 
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


#-----------------------------------------====------------------------------------------

# 206. Reverse Linked List
# reverse SLL given pointer to the head. 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# draw it out if you need some clarification
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = None
        while head:
            nxt = head.next
            head.next = new_head
            new_head = head
            head = nxt
        return new_head


#-----------------------------------------====------------------------------------------

# 344. Reverse String

# Write a function that reverses a string. The input string is given as an array 
# of characters char[]. Do not allocate extra space for another array, 
# you must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]
          
#-----------------------------------------====------------------------------------------

# 169. Majority Element
# Given an array of size n, find the majority element. 
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # has to happen more than this
        num_times = len(nums)//2
        myd = {}
        for i in nums:
            if i not in myd:
                myd[i] = 1
            else:
                myd[i] += 1 
                
        for key,value in myd.items():
            if value > num_times:
                return key

#-----------------------------------------====------------------------------------------
# 108. Convert Sorted Array to Balanced Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # getting the middle of the array
        if len(nums) == 0:
            return 
        
        mid = len(nums)//2 
        root=TreeNode(nums[mid],
        self.sortedArrayToBST(nums[:mid]),
        self.sortedArrayToBST(nums[mid+1:]))
        return root

#-----------------------------------------====------------------------------------------
# 283. Move Zeroes
# Given an array nums, write a function to move all 0's to the end 
# of it while maintaining the relative order of the non-zero elements.
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = nums.count(0)
        while x:
            nums.append(0)
            nums.remove(0)
            x = x-1

#-----------------------------------------====------------------------------------------
# 122. Best Time to Buy and Sell Stock II
# Say you have an array prices for which the ith element is the
#  price of a given stock on day i. Design an algorithm to 
#  find the maximum profit. 

# we are just checking prices that are next to each other. 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                mp += prices[i+1]-prices[i]
        return mp
#-----------------------------------------====------------------------------------------

# 242. Valid Anagram
# Given two strings s and t , write a function to determine if t is an anagram of s.

# We could instead just sort both strings to see if the sorted version is equal
# if its not then we know we dont have an anagram else we do 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myds = {}
        mydt = {}
        for c in s:
            if c not in myds:
                myds[c] = 0
            else:
                myds[c] += 1
        
        for l in t:
            if l not in mydt:
                mydt[l] = 0
            else:
                mydt[l] +=1
                
        if myds != mydt:
            return False
        else:
            return True
#-----------------------------------------====------------------------------------------

# 21. Merge Two Sorted Lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dum_start = ListNode
        cur = dum_start
        
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next 
                cur = cur.next
            else:
                cur.next = l2
                l2 = l2.next
                cur = cur.next
        cur.next = l1 or l2
        return dum_start.next
#-----------------------------------------====------------------------------------------

# 20. Valid Parentheses


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        opener = ["(", "{", "["]
        stack = []
        for c in s:
            # encountered an opener bracket, put in on the stack
            if c in opener:
                stack.append(c)
            if len(stack) == 0:
                return False
            if c == ")":
                val = stack[-1]
                if val == "(":
                    stack.pop()
                else:
                    return False
            if c == "}":
                val = stack[-1]
                if val == "{":
                    stack.pop()
                else:
                    return False
            if c == "]":
                val = stack[-1]
                if val == "[":
                    stack.pop()
                else:
                    return False
            
        if len(stack) != 0:
            return False
        else:
            return True
#-----------------------------------------====------------------------------------------
# 167. Two Sum II - Input array is sorted

# Given an array of integers that is already sorted in ascending order, 
# find two numbers such that they add up to a specific target number.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers)-1
        
        while low < high:
            add = numbers[low] + numbers[high]
            if add == target:
                return (low+1, high+1)
            elif (add > target):
                high -= 1
            elif (add < target):
                low += 1
            
            



#-----------------------------------------====------------------------------------------
# 1265. Print Immutable Linked List in Reverse

# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        ret = []
        while head:
            ret.append(head)
            head = head.getNext()
            
        ret.reverse()
        
        for i in ret:
            i.printValue()



#-----------------------------------------====------------------------------------------

# 1323. Maximum 69 Number

# Given a positive integer num consisting only of digits 6 and 9.
# Return the maximum number you can get by changing at most one digit 
# (6 becomes 9, and 9 becomes 6).

class Solution:
    def maximum69Number (self, num: int) -> int:
        l = str(num)
        l = l.replace('6','9',1)
        l = int(l)
        return l 


#-----------------------------------------====------------------------------------------
# 1570. Dot Product of Two Sparse Vectors
# Given two sparse vectors, compute their dot product.

# Implement class SparseVector:

# SparseVector(nums) Initializes the object with the vector nums
# dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
# A sparse vector is a vector that has mostly zero values, you should store the
# sparse vector efficiently and compute the dot product between two SparseVector.


class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = {}
        for i in range(len(nums)):
            if nums[i] != 0:
                self.nums[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dp = 0
        
        for i, n1 in vec.nums.items():
            n2 = self.nums.get(i)
            
            if n2 != None:
                dp += n1*n2
            
        return dp
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

#-----------------------------------------====------------------------------------------




#-----------------------------------------====------------------------------------------


#method 1
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # first check each char in the string in a loop
        for c in s:
            if (c == "(" or c == "{" or c == "["):
                stack.append(c)
            else:  #else if the string is closing bracket
                #first check if the stack is empty
                if not stack:
                    return False
                # then check if the stack is ) and that when you use the peek function to check the top of the stack
                #it is a ( if so pop
                if c == ")" and stack[-1] == "(":
                    stack.pop()
                # then check if the stack is } and that when you use the peek function to check the top of the stack
                # it is a { if so pop
                elif c == "}" and stack[-1] == "{":
                    stack.pop()
                # then check if the stack is ] and that when you use the peek function to check the top of the stack
                # it is a [ if so pop
                elif c == "]" and stack[-1] == "[":
                    stack.pop()
                #else return false
                else:
                    return False
        #return if the stack is empty
        return not stack

#method 2

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[] #create a stack
        char_map={")":"(", "}":"{","]":"["}
        #use a hashmap to keep track of each bracket pair
        for c in s:
            if c in char_map.values(): # if the bracket is an open bracket
                stack.append(c) #add it to the stack
            elif c in char_map:# if the bracket is a closed bracket
                if stack and stack[-1]==char_map[c]:#if the stack is not empty
                    # and the value at the top of stack is a corresponding open bracket
                    stack.pop() #remove from the stack
                else:
                    return False
        # return if the stack is empty
        return not stack
"""Success Details 
Runtime: 73 ms, faster than 89.37% of Python3 online submissions for Evaluate Reverse Polish Notation.
Memory Usage: 14.4 MB, less than 57.72% of Python3 online submissions for Evaluate Reverse Polish Notation."""

import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)==1:
            return tokens[0]
        val=[]
        ops = { "+": operator.add, "-": operator.sub ,"*":operator.mul,"/":operator.truediv }
        res=0
        for i in tokens:
            if i.isnumeric()== True or i[1:].isdigit()==True:
                val.append(i)
            if i.isnumeric()== False:
                if i[1:].isdigit()==False:
                    res = ops[i](int(val[-2]),int(val[-1]))
                    val.pop(-1)
                    val.pop(-1)
                    val.append(res)
                    
        return int(res)
                

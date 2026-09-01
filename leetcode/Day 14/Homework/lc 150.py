class Solution:
    def evalRPN(self, t: List[str]) -> int:
        stack = []

        for value in t:
            if value in "+-*/":
                data1 = stack.pop()
                data2 = stack.pop()
                if value == "+":
                    stack.append(data2 + data1)
                elif value == "-":
                    stack.append(data2 - data1)
                elif value == "*":
                    stack.append(data2 * data1)
                elif value == "/":
                    stack.append(int(data2 / data1))
            else:
                stack.append(int(value))
        return stack[-1]
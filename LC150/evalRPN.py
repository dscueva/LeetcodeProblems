from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+", "-", "*", "/"]

        for token in tokens:
            if token not in operations:
                # Convert token to integer and append to the stack
                stack.append(int(token))
            else:
                first = stack.pop()
                second = stack.pop()
                if token == "+":
                    prev = second + first
                elif token == "-":
                    prev = second - first
                elif token == "*":
                    prev = second * first
                elif token == "/":
                    # Convert result to integer if division is used
                    prev = int(second / first)
                stack.append(prev)

        final_ans = stack.pop()
        return final_ans

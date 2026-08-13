class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()

        for token in tokens:
            if token in ['+', '-', '*', '/']:
                num1 = stack.pop()
                num2 = stack.pop()

                match token:
                    case '+':
                        stack.append(num2 + num1)
                    case '-':
                        stack.append(num2 - num1)
                    case '*':
                        stack.append(num2 * num1)
                    case '/':
                        stack.append(int(num2 / num1))
                
            else:
                stack.append(int(token))

        return stack.pop()
                
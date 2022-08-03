from stack import Stack


def balanced_parentheses(test_str: str) -> bool:

    open_close = {'(':')', '[':']', '{':'}'}
    stack = Stack()

    for char in test_str:

        if char in open_close.keys():
            stack.push(char)
            continue

        if stack.is_empty():
            return False
        else:
            open = stack.pop()
            if open_close[open] == char:
                continue
            return False

    if stack.is_empty():
        return True
    return False


if __name__=='__main__':

    str1 = '{[({})]}{[]}'
    str2 = '{[({})]}}'
    str3 = '{[({})]}{'
    str4 = '{[({})]}*'
    str5 = '{{[({})]}'
    str6 = '}{[({})]}'
    str7 = '{[({}})]}'
    print(f'{str1} is valid? {balanced_parentheses(str1)}')
    print(f'{str2} is valid? {balanced_parentheses(str2)}')
    print(f'{str3} is valid? {balanced_parentheses(str3)}')
    print(f'{str4} is valid? {balanced_parentheses(str4)}')
    print(f'{str5} is valid? {balanced_parentheses(str5)}')
    print(f'{str6} is valid? {balanced_parentheses(str6)}')
    print(f'{str7} is valid? {balanced_parentheses(str7)}')

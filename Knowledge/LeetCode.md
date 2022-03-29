# LeetCode 刷题

> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/

##### [20. 有效的括号](https://leetcode-cn.com/problems/valid-parentheses/)

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

**示例 1：**

```
输入：s = "()"
输出：true
```

题解：

```python
# 使用「栈」这一数据结构来解决 
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 ==1:
            return False

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for ch in s:
            # 遇到右括号 进行是否已经有对应左括号入栈判断
            if ch in pairs:     
                # 如果stack 为空 或 stack中的值非预期
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                # 将后续判断内容放在stack中 左括号
                stack.append(ch)    
        return not stack
```


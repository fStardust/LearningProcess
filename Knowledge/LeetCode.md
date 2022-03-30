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

**题解：**

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

##### [21. 合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/)

将两个升序链表合并为一个新的 **升序** 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

**示例 1：**

![img](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)

```
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
```

**题解：**

```Python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 前两个判断 处理边界情况 -- 空表
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        # 以下判断 判断两表头结点数据大小以最小的作为开头 并以此逻辑递归 与拼接
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

```


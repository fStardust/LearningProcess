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

###### [26. 删除有序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)

给你一个 升序排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。

由于在某些语言中不能改变数组的长度，所以必须将结果放在数组nums的第一部分。更规范地说，如果在删除重复项之后有 k 个元素，那么 nums 的前 k 个元素应该保存最终结果。

将最终结果插入 nums 的前 k 个位置后返回 k 。

不要使用额外的空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

**判题标准:**

系统会用下面的代码来测试你的题解:

```
int[] nums = [...]; // 输入数组
int[] expectedNums = [...]; // 长度正确的期望答案

int k = removeDuplicates(nums); // 调用

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```

如果所有断言都通过，那么您的题解将被 **通过**。

**示例 1：**

```
输入：nums = [1,1,2]
输出：2, nums = [1,2,_]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。
```

**题解：**

```python
# 使用快慢指针来“原地”判断所给数组前后值是否重复
# 由快指针判断值是否重复，若不重复则赋给慢指针
# 最后慢指针记录的即为所需结果
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
    
        n = len(nums)
        fast = 1
        slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow
```

###### [27. 移除元素](https://leetcode-cn.com/problems/remove-element/)

给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

**题解：**

```python
# 整体思路跟上一题(26)并无区别，主要区别在与 一个是有序 一个是无序
# 还是采用 双指针 的方法来处理
# 移除数组中所有等于目标值（val）的元素，即在慢指针记录的数组中不记录这些数即可

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a = 0
        b = 0

        while a < len(nums):
            if nums[a] != val:
                nums[b] = nums[a]
                b += 1
            a += 1
        
        return b
```

###### [28. 实现 strStr()](https://leetcode-cn.com/problems/implement-strstr/)

实现 `strStr()` 函数。

给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1 。

 

**说明：**

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。

**题解：**

```python
# 直接使用Python内建函数 -- .find()
## 使用 Sunday 算法
### Sunday 算法是 Daniel M.Sunday 于1990年提出的字符串模式匹配。
### 其效率在匹配随机的字符串时比其他匹配算法还要更快。 
### Sunday 算法的实现可比 KMP，BM 的实现容易太多。
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0

        lnd = len(needle)
        lnf = len(haystack)
        if lnd > lnf: return -1

        # 偏移表 -- 用来处理目标串中出现的字符
        # v:lnd-k 表示 value = lnd - key
        # k,v 表示 key 与 value 互换
        # enumerate() 表示 将一个可遍历的数据对象(needle)组合为一个索引序列，同时列出下标和数据
        dic={v:lnd-k for k, v in enumerate(needle)}
        idx = 0

        while idx+lnd <= lnf:
            # 取出待匹配字符串
            str_cut = haystack[idx:idx+lnd]
            # 判断是否匹配
            if str_cut == needle:
                return idx
            elif idx+lnd == lnf:    # 此处的 elif 目的是减少循环次数
                return -1
            else:
                # 不匹配时，根据狭义字符的偏移，移动idx
                nextc = haystack[idx+lnd]  
                # 三元判断，如果偏移后的值为偏移表 key，那么 idx 添加偏移表对应 value，
                # 若找不到，则idx 除添加 needle 长度外多加 1 -- 减少循环次数
                idx += dic[nextc] if dic.get(nextc) else lnd+1
        return -1

```

![28-输出结果](https://s2.loli.net/2022/04/02/DexAY2jhb75Zndi.png)

###### [35. 搜索插入位置](https://leetcode-cn.com/problems/search-insert-position/)

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。

**题解：**

```python
# 二分法
# 使用极端值，预测未找到时应该插入的位置
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return high + 1

```


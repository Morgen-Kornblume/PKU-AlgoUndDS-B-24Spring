class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 创建一个空字典用于存储数字及其出现的频率
        d = {}
        
        # 遍历给定的数字列表
        for i in nums:
            # 如果数字已经在字典中，则将其频率加1
            if i in d:
                d[i] += 1
            # 如果数字不在字典中，则将其添加到字典，并将其频率设置为1
            else:
                d[i] = 1
        
        # 创建一个空列表用于存储出现频率最高的k个数字
        res = []
        
        # 循环k次，每次找到字典中出现频率最高的数字，并将其添加到结果列表中
        for i in range(k):
            # 使用max函数和字典的get方法找到出现频率最高的数字
            max_key = max(d, key=d.get)
            # 将最高频率的数字添加到结果列表中
            res.append(max_key)
            # 从字典中移除已经添加到结果列表中的数字
            d.pop(max_key)
        
        # 返回结果列表
        return res
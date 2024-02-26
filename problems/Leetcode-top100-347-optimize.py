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
        
        # 将字典中的键值对转换为元组，并将其添加到一个新的列表中
        items = list(d.items())

        # 按照元组的第二个元素（即数字的频率）进行排序
        items.sort(key=lambda x: x[1], reverse=True)

        # 循环k次，每次找到出现频率最高的数字，并将其添加到结果列表中
        for i in range(k):
            # 将最高频率的数字添加到结果列表中
            res.append(items[i][0])
        
        # 返回结果列表
        return res
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort: create N amount of buckets, e.g. count=1, count=2, ...
        buckets = [set() for _ in range(len(nums) + 1)]

        # Use a dictionary to track current counts for efficiency and correctness
        counts = {}
        for num in nums:
            currentCount = counts.get(num, 0)
            if currentCount > 0:
                buckets[currentCount].discard(num)
            
            newCount = currentCount + 1
            counts[num] = newCount
            buckets[newCount].add(num)
        
        result = []
        bucketPointer = len(buckets) - 1

        while len(result) < k:
            while bucketPointer >= 0 and len(buckets[bucketPointer]) > 0:
                result.append(buckets[bucketPointer].pop())

                if len(result) == k:
                    return result

            bucketPointer -= 1
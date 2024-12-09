def distinctDifferenceArray(self, nums: List[int]) -> List[int]:

    prefix = []
    output = []

    for i in range(len(nums)):
        suffix = []
        if nums[i] not in prefix:
            prefix.append(nums[i])
        for j in range(i + 1, len(nums)):
            if nums[j] not in suffix:
                suffix.append(nums[j])
        output.append(len(prefix) - len(suffix))

    return output

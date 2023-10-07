# Insights:
# Binary search can be adapted to search for specific patterns or conditions, especially
# when there's an inherent ordering or sequence involved.
# When you know a certain condition must occur between two other observable conditions,
# binary search can quickly narrow down the potential region of interest.
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0

        if nums[0] > nums[1]:
            return 0

        if nums[-1] > nums[-2]:
            return len(nums) - 1

        left = 1
        right = len(nums) - 2

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] < nums[middle - 1]:
                right = middle - 1
            elif nums[middle] < nums[middle + 1]:
                left = middle + 1
            else:
                return middle

        raise RuntimeError()


if __name__ == "__main__":
    import csv
    from pathlib import Path

    solution = Solution()

    test_csv_path = Path(__file__).parent / "test.csv"
    with open(test_csv_path, mode="r") as test_csv:
        reader = csv.DictReader(test_csv)
        for test_row in reader:
            nums = [int(n) for n in test_row["nums"].split("|")]
            expected = int(test_row["expected"])

            actual = solution.findPeakElement(nums)
            assert actual == expected, f"{nums=}, {expected=}, {actual=}"
    print("All tests passed!")

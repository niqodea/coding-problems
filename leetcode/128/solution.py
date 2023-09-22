# Naive solution would be to sort it - O(N * logN)

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        checked_nums = set()

        longest_consecutive = 0
        for n in num_set:
            if n in checked_nums:
                continue

            checked_nums.add(n)

            consecutive = 1

            left_probe = n - 1
            while left_probe in num_set:
                consecutive += 1
                checked_nums.add(left_probe)
                left_probe -= 1

            right_probe = n + 1
            while right_probe in num_set:
                consecutive += 1
                checked_nums.add(right_probe)
                right_probe += 1

            longest_consecutive = max(consecutive, longest_consecutive)

        return longest_consecutive


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

            actual = solution.longestConsecutive(nums)
            assert actual == expected, f"{nums=}, {expected=}, {actual=}"
    print("All tests passed!")

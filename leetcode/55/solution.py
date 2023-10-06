class Solution:
    def canJump(self, nums: list[int]) -> bool:
        i: int = len(nums) - 2
        while i >= 0:
            if nums[i] > 0:
                i -= 1
                continue
            i -= 1
            j = 2
            while True:
                if i < 0:
                    return False
                if nums[i] >= j:
                    break
                i -= 1
                j += 1
        return True


if __name__ == "__main__":
    import csv
    from pathlib import Path

    solution = Solution()

    test_csv_path = Path(__file__).parent / "test.csv"
    with open(test_csv_path, mode="r") as test_csv:
        reader = csv.DictReader(test_csv)
        for test_row in reader:
            nums = [int(n) for n in test_row["nums"].split("|")]
            expected = {"true": True, "false": False}[test_row["expected"]]

            actual = solution.canJump(nums)
            assert actual == expected, f"{nums=}, {expected=}, {actual=}"
    print("All tests passed!")

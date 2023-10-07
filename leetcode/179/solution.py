# Insights:
# Think of a candidate solution, then check if you can improve it locally
# In this case, we can improve it by swapping two contiguous numbers


def quicksort(num_strings: list[str], left: int, right: int) -> None:
    if left >= right:
        return

    pivot_idx = int((left + right) / 2)
    pivot = num_strings[pivot_idx]

    # Put pivot on the right
    num_strings[right], num_strings[pivot_idx] = (
        num_strings[pivot_idx],
        num_strings[right],
    )

    left_partition_size = 0
    for i in range(left, right):
        if is_ordered(num_strings[i], pivot):
            num_strings[left + left_partition_size], num_strings[i] = (
                num_strings[i],
                num_strings[left + left_partition_size],
            )
            left_partition_size += 1

    num_strings[left + left_partition_size], num_strings[right] = (
        num_strings[right],
        num_strings[left + left_partition_size],
    )
    quicksort(num_strings, left, left + left_partition_size - 1)
    quicksort(num_strings, left + left_partition_size + 1, right)


def is_ordered(a: str, b: str) -> bool:
    ab = a + b
    ba = b + a
    for c_ab, c_ba in zip(ab, ba):
        if int(c_ab) > int(c_ba):
            return True
        elif int(c_ab) < int(c_ba):
            return False
    return True


class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        num_strings = [str(n) for n in nums]

        if set(num_strings) == {"0"}:
            return "0"

        quicksort(num_strings, 0, len(num_strings) - 1)
        max_num_str = "".join(num_strings)
        return max_num_str


if __name__ == "__main__":
    import csv
    from pathlib import Path

    solution = Solution()

    test_csv_path = Path(__file__).parent / "test.csv"
    with open(test_csv_path, mode="r") as test_csv:
        reader = csv.DictReader(test_csv)
        for test_row in reader:
            nums = [int(n) for n in test_row["nums"].split("|")]
            expected = str(test_row["expected"])

            actual = solution.largestNumber(nums)
            assert actual == expected, f"{nums=}, {expected=}, {actual=}"
    print("All tests passed!")

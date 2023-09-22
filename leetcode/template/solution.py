class Solution:
    def solve(self, a: str, b: int) -> bool:
        ...


if __name__ == "__main__":
    import csv
    from pathlib import Path

    solution = Solution()

    test_csv_path = Path(__file__).parent / "test.csv"
    with open(test_csv_path, mode="r") as test_csv:
        reader = csv.DictReader(test_csv)
        for test_row in reader:
            a = str(test_row["a"])
            b = int(test_row["b"])
            c = [int(n) for n in test_row["nums"].split("|")]
            expected = {"true": True, "false": False}[test_row["expected"]]

            actual = solution.solve(a, b)
            assert actual == expected, f"{a=}, {b=}, {expected=}, {actual=}"
    print("All tests passed!")

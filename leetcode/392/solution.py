class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_idx: int = 0
        s_idx: int = 0

        while s_idx < len(s) and t_idx < len(t):
            if s[s_idx] == t[t_idx]:
                s_idx += 1
            t_idx += 1

        if s_idx == len(s):
            return True
        else:
            return False


class FollowupSolution:
    def _build_jumps(self, t: str) -> tuple[dict[str, int], ...]:
        jumps: tuple[dict[str, int], ...] = tuple({} for _ in range(len(t) + 1))

        t_idx_jumps: dict[str, int] = {}
        for t_idx in range(len(t) - 1, -1, -1):
            t_char = t[t_idx]
            t_idx_jumps[t_char] = t_idx + 1
            jumps[t_idx].update(**t_idx_jumps)

        return jumps

    def isSubsequence(self, s: str, t: str) -> bool:
        jumps = self._build_jumps(t)

        char_jumps = jumps[0]
        for s_char in s:
            if s_char not in char_jumps:
                return False
            jump_idx = char_jumps[s_char]
            char_jumps = jumps[jump_idx]

        return True


if __name__ == "__main__":
    import csv
    from pathlib import Path

    solution = Solution()
    followup_solution = FollowupSolution()

    test_csv_path = Path(__file__).parent / "test.csv"
    with open(test_csv_path, mode="r") as test_csv:
        reader = csv.DictReader(test_csv)
        for test_row in reader:
            s = str(test_row["s"])
            t = str(test_row["t"])
            expected = {"true": True, "false": False}[test_row["expected"]]

            actual = solution.isSubsequence(s, t)
            assert actual == expected, f"{s=}, {t=}, {expected=}, {actual=}"

            followup_actual = followup_solution.isSubsequence(s, t)
            assert (
                followup_actual == expected
            ), f"{s=}, {t=}, {expected=}, {followup_actual=}"
    print("All tests passed!")

# Change

# In the mystical village of Coinholt, you stand behind the counter of your bakery, arranging a fresh batch of pastries. The door creaks open, and in walks Denara, a skilled merchant with a keen eye for quality goods. After a quick meal, she slides a shimmering coin across the counter, representing a value of 100 units.

# You smile, taking the coin, and glance at the total cost of the meal: 88 units. That means you need to return 12 units in change.

# Denara holds out her hand expectantly. "Just give me the fewest coins," she says with a smile. "My pouch is already full, and I don't want to risk losing them on the road."

# You know you have a few options. "We have Lumis (worth 10 units), Viras (worth 5 units), and Zenth (worth 2 units) available for change."

# You quickly calculate the possibilities in your head:

# one Lumis (1 × 10 units) + one Zenth (1 × 2 units) = 2 coins total
# two Viras (2 × 5 units) + one Zenth (1 × 2 units) = 3 coins total
# six Zenth (6 × 2 units) = 6 coins totalD

# Determine the fewest number of coins to give a customer so that the sum of their values equals the correct amount of change.

# Examples
# An amount of 15 with available coin values [1, 5, 10, 25, 100] should return one coin of value 5 and one coin of value 10, or [5, 10].
# An amount of 40 with available coin values [1, 5, 10, 25, 100] should return one coin of value 5, one coin of value 10, and one coin of value 25, or [5, 10, 25].
# # example when change cannot be made with the coins passed in
# raise ValueError("can't make target with given coins")

# Programação dinâmica (DP) >> Greedy


def find_fewest_coins(coins: list[int], target: int) -> list[int]:
    """
    Finds the minimum number of coins whose sum is equal to the given target value,
    using dynamic programming (DP). It always returns an optimal combination, even
    when a greedy strategy fails (for example, with coins [1, 10, 11] to make 20).

    The function builds a table `dp` where:
        - dp[x] stores the list of coins that sums to x using the smallest possible
        number of coins;
        - dp[0] = [];
        - dp[target] contains the final optimal solution.

    The algorithm tries all available coins and builds smaller solutions to compose
    larger values, ensuring that the final solution is optimal.

    Args:
        coins (list[int]):
            List of available coin denominations. It does not need to be sorted.
            Example: [1, 4, 15, 20, 50]

        target (int):
            The value to be formed using the coins.
            Must be >= 0.

    Raises:
        ValueError:
            If the target value is negative.
            ("target can't be negative")

        ValueError:
            If there is no possible combination of coins that sums to the target.
            ("can't make target with given coins")

    Returns:
        list[int]:
            A list of coins whose sum equals the target, containing the smallest
            possible total number of coins. The result is returned sorted in
            ascending order.

            Example:
                find_fewest_coins([1, 10, 11], 20) -> [10, 10]
    """
    if target < 0:
        raise ValueError("target can't be negative")
    if target == 0:
        return []

    dp: list[list[int]] = [[] for _ in range(target + 1)]

    for amount in range(1, target + 1):
        best: list[int] = []

        for coin in coins:
            if amount - coin >= 0:

                if dp[amount - coin] or amount - coin == 0:
                    candidate: list[int] = dp[amount - coin] + [coin]

                    if not best or len(candidate) < len(best):
                        best = candidate

        dp[amount] = best

    if not dp[target]:
        raise ValueError("can't make target with given coins")

    return sorted(dp[target])


# coins = [1,10,11] and target = 20

# amount | dp[amount]
# -------|-----------------------------
# 0      | []
# 1      | [1]
# 2      | [1,1]
# 3      | [1,1,1]
# 4      | [1,1,1,1]
# 5      | [1×5]
# 6      | [1×6]
# 7      | [1×7]
# 8      | [1×8]
# 9      | [1×9]
# 10     | [10]
# 11     | [11]
# 12     | [11,1]
# 13     | [11,1,1]
# 14     | [11,1×3]
# 15     | [11,1×4]
# 16     | [11,1×5]
# 17     | [11,1×6]
# 18     | [11,1×7]
# 19     | [11,1×8]
# 20     | [10,10]

# from functools import reduce
# from typing import Optional, List


# def find_fewest_coins(coins: list[int], target: int) -> list[int]:
#     if target < 0:
#         raise ValueError("target can't be negative")
#     if target == 0:
#         return []

#     def step(dp: list[Optional[list[int]]], amount: int) -> list[Optional[list[int]]]:
#         # escolhe todas as possibilidades válidas para formar `amount`
#         candidates = [
#             dp[amount - coin] + [coin]      # o candidato é dp[4 - a moeda 1] + [1] = dp[3] + [1] , aqui estamos no amount 4 testando a moeda 1, já tem o dp[3] = [1,1,1] e vai adicionar 1
#             for coin in coins
#             if amount - coin >= 0 and dp[amount - coin] is not None
#         ]

#         best = min(candidates, key=len) if candidates else None
#         dp.append(best)
#         return dp

#     # reduce gera todo dp: começando com [ [] ] e criando amounts 1..target
#     dp = reduce(step, range(1, target + 1), [ [] ])

#     result = dp[target]
#     if result is None:
#         raise ValueError("can't make target with given coins")

#     return sorted(result)

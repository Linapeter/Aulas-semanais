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
    Encontra a menor quantidade possível de moedas cuja soma é igual ao valor desejado (target),
    usando programação dinâmica (DP). Sempre retorna uma combinação ótima, mesmo quando uma
    estratégia gulosa falha (por exemplo, moedas [1, 10, 11] para fazer 20).

    A função constrói uma tabela `dp` onde:
        - dp[x] armazena a lista de moedas que soma x com a menor quantidade de moedas possível;
        - dp[0] = [];
        - dp[target] contém a solução ótima final.

    O algoritmo tenta todas as moedas disponíveis e constrói soluções menores para formar
    valores maiores, garantindo que a solução final é ótima.

    Args:
        coins (list[int]):
            Lista de denominações das moedas disponíveis. Não precisa estar ordenada.
            Exemplo: [1, 4, 15, 20, 50]

        target (int):
            O valor que deve ser formado com as moedas.
            Deve ser >= 0.

    Raises:
        ValueError:
            Se o valor do target for negativo.
            ("target can't be negative")

        ValueError:
            Se não existir nenhuma combinação de moedas que some ao target.
            ("can't make target with given coins")

    Returns:
        list[int]:
            Uma lista de moedas cuja soma é igual ao target, contendo a menor quantidade total
            de moedas possível. O resultado é retornado ordenado em ordem crescente.

            Exemplo:
                find_fewest_coins([1, 10, 11], 20) -> [10, 10]
    """
    if target < 0:
        raise ValueError("target can't be negative")
    if target == 0:
        return []

    dp: list[list[int] | None] = [None] * (target + 1)          # uma lista grande que armazena listas de melhores trocos
    dp[0] = []
    # queremos dp[20] = [10,10]
    for amount in range(1, target + 1):                         # vai até o target, armazendando os melhores trocos
        best: list[int] | None = None

        for coin in coins:                                      # de moeda em moeda disponível
            if amount - coin >= 0 and dp[amount - coin] is not None:                # se a moeda for menor que o troco e se ainda não tiver uma lista de trocos atualizado para o amount
                candidate: list[int] | None = dp[amount - coin] + [coin]            # o candidato é dp[4 - a moeda 1] + [1] = dp[3] + [1] , aqui estamos no amount 4 testando a moeda 1, já tem o dp[3] = [1,1,1] e vai adicionar 1
                if best is None or len(candidate) < len(best):
                    best = candidate

        dp[amount] = best

    if dp[target] is None:
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

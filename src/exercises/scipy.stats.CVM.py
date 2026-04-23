import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import cramervonmises, nbinom

n = 5
p = 0.3
rng = np.random.default_rng(seed=1)
x = nbinom.rvs(n, p, size=300, random_state=rng)
print(repr(x))


def result_cvm(x: np.ndarray, distribution: str, args: tuple) -> str:
    res = cramervonmises(x, distribution, args)
    print("Teste de aderência para a distribuição")
    print(f"Estatística CVM: {res.statistic}, P-valor: {res.pvalue}")
    if res.pvalue < 0.05:
        return "Rejeitamos a hipótese nula: os dados não seguem a distribuição teórica"
    else:
        return "Não rejeitamos a hipótese nula: os dados seguem a distribuição teórica"


print(result_cvm(x, "nbinom", (n, p)))

x_sorted = np.sort(x)
ecdf = np.arange(1, len(x) + 1) / len(x)
x_range = np.arange(0, max(x) + 1)

plt.step(
    x_range,
    nbinom.cdf(x_range, n, p),
    where="post",
    label="Teórica (NBinom)",
    color="red",
)
plt.step(
    x_sorted, ecdf, where="post", label="Empírica (Dados)", color="blue", alpha=0.6
)
plt.title("ECDF vs CDF Teórica (Foco do Cramer-von Mises)")
plt.legend()
plt.show()


# 1. Transformar os dados 'x' em uma tabela de frequências
df = pd.Series(x).value_counts().sort_index().reset_index()
df.columns = ["valor", "contagem"]

# 2. Calcular V(i) - Indivíduos em risco (sobreviventes)
df["V_i"] = df["contagem"].iloc[::-1].cumsum().iloc[::-1]

# 3. Intensidade Empírica
df["h_emp"] = df["contagem"] / df["V_i"]

# 4. Intensidade Teórica (usando n e p da binomial negativa)
df["h_teo"] = nbinom.pmf(df["valor"], n, p) / (1 - nbinom.cdf(df["valor"] - 1, n, p))

# 5. Log-Rank e CvM (conforme PDF)
df["diff"] = df["h_emp"] - df["h_teo"]
df["LR"] = df["diff"].cumsum()
cvm_manual = (df["LR"] ** 2).sum()

print(f"Estatística CvM (via Intensidade): {cvm_manual}")

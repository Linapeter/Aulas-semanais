import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import cramervonmises, nbinom, norm, poisson


def result_cvm(x: np.ndarray, distribution: str, args: tuple) -> str:
    res = cramervonmises(x, distribution, args)
    print(f"Teste de aderência para a distribuição {distribution}")
    print(f"Estatística CVM: {res.statistic}, P-valor: {res.pvalue}")
    if res.pvalue < 0.05:
        return "Rejeitamos a hipótese nula: os dados não seguem a distribuição teórica"
    else:
        return "Não rejeitamos a hipótese nula: os dados seguem a distribuição teórica"


def plotar_empiric_vs_teoric(x: np.ndarray, params: tuple, distrib: str) -> None:
    x_sorted = np.sort(x)
    empiric = np.arange(1, len(x) + 1) / len(x)
    x_range = np.arange(0, max(x) + 1)

    if distrib == "nbinom":
        plt.step(
            x_range,
            nbinom.cdf(x_range, *params),
            where="post",
            label="FDA: Teórica (NBinom)",
            color="red",
        )
    if distrib == "poisson":
        plt.step(
            x_range,
            poisson.cdf(x_range, *params),
            where="post",
            label="FDA: Teórica (Poisson)",
            color="red",
        )
    if distrib == "norm":
        x_range = np.linspace(min(x), max(x), 1_000)
        plt.plot(
            x_range,
            norm.cdf(x_range, *params),
            label="FDA: Teórica (Normal)",
            color="red",
        )

    plt.step(
        x_sorted,
        empiric,
        where="post",
        label="FDA Empírica (Dados)",
        color="blue",
        alpha=0.6,
    )
    plt.title("FDA: Empirico vs Teórica")
    plt.legend()
    plt.show()


def cvm_manual(x: np.ndarray, params: tuple, distrib: str, plot: bool) -> str:

    df = pd.Series(x).value_counts().sort_index().reset_index()
    df.columns = ["i", "ocorrencias"]
    # sobreviventes
    df["sobreviventes"] = df["ocorrencias"].iloc[::-1].cumsum().iloc[::-1]
    # Função de intensidade (empirico) = ocorrencias / sobreviventes
    df["h_emp"] = df["ocorrencias"] / df["sobreviventes"]

    if distrib == "nbinom":
        # Função de intensidade (teórico) = P(X=i) / P(X>=i) = P(X=i) / (1 - P(X<=i-1))
        df["h_teo"] = nbinom.pmf(df["i"], *params) / (
            1 - nbinom.cdf(df["i"] - 1, *params)
        )
    if distrib == "poisson":
        df["h_teo"] = poisson.pmf(df["i"], *params) / (
            1 - poisson.cdf(df["i"] - 1, *params)
        )

        df["h_teo"] = norm.pdf(df["i"], *params) / (1 - norm.cdf(df["i"], *params))

    # Log-Rank e CVM
    df["diff"] = df["h_emp"] - df["h_teo"]
    df["LR"] = df["diff"].cumsum()
    cvm_manual = (df["LR"] ** 2).sum()

    if plot:
        i_range = df["i"].values
        plt.figure(figsize=(12, 6))
        plt.step(
            i_range,
            df["h_teo"],
            where="post",
            label="Função de Intensidade Teórica",
            color="red",
            lw=2,
            linestyle="--",
        )
        plt.scatter(
            i_range,
            df["h_emp"],
            color="blue",
            label="Função de Intensidade Empírica",
            zorder=3,
        )
        plt.vlines(i_range, 0, df["h_emp"], color="blue", alpha=0.2, linestyle="dotted")
        plt.title("Função de Intensidade: Empírica vs Teórica")
        plt.xlabel("Valor (i)")
        plt.ylabel("h(i) = P(X=i) / P(X>=i)")
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()

    return f"Estatística CVM (Manual): {cvm_manual}"


# Negativa binomial

n = 5
p = 0.3
rng = np.random.default_rng(seed=1)
x = nbinom.rvs(n, p, size=10_000, random_state=rng)
# print(result_cvm(x, "nbinom", (n, p)))
# plotar_empiric_vs_teoric(x, (n, p), "nbinom")
# print(cvm_manual(x, (n, p), "nbinom", plot=True))

# desenho teorico NB
probabilidades = np.linspace(0, 1, 10_000)
x_teorico = nbinom.ppf(probabilidades, n, p)
# print(cvm_manual(x_teorico, (n, p), "nbinom", plot=True))
# print(result_cvm(x_teorico, "nbinom", (n, p)))

# # Poisson
lamb = 3.5
# x_poisson = poisson.rvs(lamb, size=10_000, random_state=rng)
# print(result_cvm(x_poisson, "poisson", (lamb,)))
# plotar_empiric_vs_teoric(x_poisson, (lamb,), "poisson")
# print(cvm_manual(x_poisson, (lamb,), "poisson", plot=True))

# # desenho teorico Poisson
# probabilidades = np.linspace(0, 1, 10_000)
# x_teorico = poisson.ppf(probabilidades, lamb)
# print(cvm_manual(x_teorico, (lamb,), "poisson", plot=True))

# normal
mi = 0
sd = 1
x_norm = norm.rvs(size=10_000, random_state=rng)
res = cramervonmises(x, "norm")
print(result_cvm(x_norm, "norm", (mi, sd)))
plotar_empiric_vs_teoric(x_norm, (mi, sd), "norm")

# Desafio #365 [Intermediário] Comissões de Vendas
# Descrição
# Você é gerente regional de uma empresa de vendas de bebidas para escritório e, no momento, é responsável por pagar à sua equipe de vendas comissões mensais.

# Os vendedores são pagos usando a seguinte fórmula para a comissão total: a comissão é de 6,2% do lucro, sem comissão para qualquer produto com total inferior a zero.

# Descrição de entrada
# Você receberá duas matrizes mostrando o valor das vendas por vendedor para cada produto vendido e as despesas por produto por vendedor. Exemplo:

# Receita

#         Frank Jane
# Chá 120 145
# Café 243 265

# Despesas

#         Frank Jane
# Chá 130 59
# Café 143 198

# Descrição da saída

# Seu programa deve calcular a comissão de cada vendedor do mês. Exemplo:

#                 Frank Jane
# Comissão 6,20 9,49


# Entrada do Desafio
# Receita

#             Johnver Vanston Danbree Vansey Mundyke
# Chá 190 140 1926 14 143
# Café 325 19 293 1491 162
# Água 682 14 852 56 659
# Leite 829 140 609 120 87

# Despesas

#             Johnver Vanston Danbree Vansey Mundyke
# Chá 120 65 890 54 430
# Café 300 10 23 802 235
# Água 50 299 1290 12 145
# Leite 67 254 89 129 76
# Resultado do desafio
#             Johnver Vanston Danbree Vansey Mundyke
# Comissão 92 5 113 45 32


#' Commission
#'
#' @description
#' Calculates commission values based on revenue and expense tables
#' provided in a single text input.
#'
#' @author linapeter
#'
#' @param input Character. A text string containing two tabular sections:
#' a revenue table and an expense table, separated by the keyword
#' \code{"Despesas"}.
#'
#' @details
#' The input text is split at the keyword \code{"Despesas"}.
#' The first section is interpreted as a revenue table and the second as
#' an expense table. The commission is computed as 6.2\% of the
#' column-wise sum of (revenue minus expenses) if this amount is positive.
#'
#' @return
#' A numeric vector containing the commission for each column,
#' rounded to two decimal places.
#'
#' @examples
#' text <- "Receita
#'
#'         Frank Jane
#' Chá 120 145
#' Café 243 265
#'
#' Despesas
#'
#'        Frank Jane
#' Chá 130 59
#' Café 143 198"
#'
#' commission(text)
#'
#' @export
#'
commission <- function(input){

    split <- strsplit(input, "Despesas")[[1]]

    receita <- read.table(
      text = gsub(paste0("^\\s*", "Receita"), "", split[1]),
      header = TRUE,
      row.names = 1,
      check.names = FALSE
    )

    despesas <- read.table(
      text = gsub(paste0("^\\s*", "Despesas"), "", split[2]),
      header = TRUE,
      row.names = 1,
      check.names = FALSE
    )

    round(apply(receita - despesas, 2, function(item) sum(item[item > 0])*0.062),2)
}

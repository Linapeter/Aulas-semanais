# Desafio [Fácil] Gerador de sequência de dobra de papel regular
# Descrição
# Em matemática, a sequência regular de dobramento de papel , também conhecida como sequência da curva do dragão, é uma sequência automática infinita de 0s e 1s.
# Em cada estágio uma sequência alternada de 1s e 0s é inserida entre os termos da sequência anterior. As primeiras gerações da sequência são assim:

# 1
# 1 1 0
# 1 1 0 1 1 0 0
# 1 1 0 1 1 0 0 1 1 1 0 0 1 0 0

# A sequência leva esse nome porque representa a sequência de dobras à esquerda e à direita ao longo de uma tira de papel que é dobrada repetidamente ao meio na mesma direção.
# Se cada dobra for aberta para criar um canto em ângulo reto, a forma resultante se aproxima do fractal da curva do dragão.

# Entrada do desafio
# Seu desafio hoje é implementar um gerador regular de sequência de dobra de papel de até 8 ciclos (fica demorado rapidamente).

# Resultado do desafio
# (Com quebras de linha para facilitar a leitura)

# 110110011100100111011000110010011101100111001000110110001100100111011001110010
# 011101100011001000110110011100100011011000110010011101100111001001110110001100
# 100111011001110010001101100011001000110110011100100111011000110010001101100111
# 001000110110001100100111011001110010011101100011001001110110011100100011011000
# 110010011101100111001001110110001100100011011001110010001101100011001000110110
# 011100100111011000110010011101100111001000110110001100100011011001110010011101
# 1000110010001101100111001000110110001100100

# https://docs.ufpr.br/~ewkaras/ensino/fractais/dragao.pdf



#' (Internal) Invert and reverse a binary sequence
#'
#' @description
#' This function takes a binary sequence (containing only 0s and 1s),
#' inverts its values (0 becomes 1 and 1 becomes 0), and then reverses
#' the order of the sequence.
#'
#' @author linapeter
#'
#' @param sequence A numeric vector containing only 0s and 1s.
#'
#' @return
#' A numeric vector corresponding to the inverted and reversed input sequence.
#'
#' @examples
#' invert__(c(0, 1, 1, 0))
#'
#' @keywords internal
#'
#' @export
#'
invert__ <- function(sequence) sequence <- 1 - sequence

#' Generate the Dragon Curve turn sequence
#'
#' @description
#' This function generates the sequence of turns corresponding to the
#' Dragon Curve fractal. Starting from an empty sequence, each iteration
#' appends a right turn (represented by 1) followed by the inverted and
#' reversed version of the previous sequence.
#'
#' @author linapeter
#'
#' @param - iterations An integer indicating the number of iterations
#' to be performed.
#'
#' @details
#' At each iteration, the sequence is updated according to the rule:
#' \deqn{S_{n+1} = S_n \; 1 \; \text{invert}(S_n)}
#' where \code{invert} denotes reversing the sequence and swapping
#' 0s and 1s.
#'
#' @return
#' A numeric vector of 0s and 1s representing left and right turns
#' in the Dragon Curve construction.
#'
#' @examples
#' dragon_curve(1)
#' dragon_curve(3)
#'
#' @inherit invert__ return details
#'
#' @export
#'
dragon_curve <- function(iterations){
    sequence <- integer(0)

    for (step in 1:iterations){
        sequence <- c(sequence,1,invert__(rev(sequence)))
    }
    return (sequence)
}
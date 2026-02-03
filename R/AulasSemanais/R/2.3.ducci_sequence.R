# Desafio #364 [Intermediário] A Sequência Ducci
# Descrição
# Uma sequência Ducci é uma sequência de n-tuplas de inteiros, às vezes conhecida como "jogo Diffy", porque é baseada em sequências. Dada uma n-tupla de inteiros (a_1, a_2, ... a_n), a próxima n-tupla na sequência é formada tomando as diferenças absolutas dos inteiros vizinhos. As sequências de Ducci têm o nome de Enrico Ducci (1864-1940), o matemático italiano responsável pela sua descoberta.

# Algumas sequências Ducci descem até zeros ou uma sequência repetida. Um exemplo é (1,2,1,2,1,0) -> (1,1,1,1,1,1) -> (0,0,0,0,0,0).

# Informações adicionais sobre a sequência de Ducci podem ser encontradas em este artigo de Greg Brockman, um estudante de matemática.

# É divertido brincar com o código depois de fazê-lo funcionar e tentar encontrar sequências que nunca entrem em colapso e se repitam. Um que encontrei foi (2, 4126087, 4126085), e continua indefinidamente.

# Também é divertido plotá-los em 3 dimensões. Aqui está um exemplo da sequência "(129,12,155,772,63,4)" transformada em 2 conjuntos de linhas (x1, y1, z1, x2, y2, z2).

# Descrição de entrada
# Você receberá uma tupla n, uma por linha. Exemplo:

# (0, 653, 1854, 4063)

# Descrição da saída
# Seu programa deve emitir o número de etapas executadas para chegar a uma tupla totalmente 0 ou quando entrar em um padrão de repetição estável. Exemplo:

# [0; 653; 1854; 4063]
# [653; 1201; 2209; 4063]
# [548; 1008; 1854; 3410]
# [460; 846; 1556; 2862]
# [386; 710; 1306; 2402]
# [324; 596; 1096; 2016]
# [272; 500; 920; 1692]
# [228; 420; 772; 1420]
# [192; 352; 648; 1192]
# [160; 296; 544; 1000]
# [136; 248; 456; 840]
# [112; 208; 384; 704]
# [96; 176; 320; 592]
# [80; 144; 272; 496]
# [64; 128; 224; 416]
# [64; 96; 192; 352]
# [32; 96; 160; 288]
# [64; 64; 128; 256]
# [0; 64; 128; 192]
# [64; 64; 64; 192]
# [0; 0; 128; 128]
# [0; 128; 0; 128]
# [128; 128; 128; 128]
# [0; 0; 0; 0]
# 24 passos

# Entrada do desafio
# (1, 5, 7, 9, 9)
# (1, 2, 1, 2, 1, 0)
# (10, 12, 41, 62, 31, 50)
# (10, 12, 41, 62, 31)

#' (Internal) Perform one step of the Diffy Game
#'
#' @description
#' Given a numeric sequence, this function computes the absolute differences
#' between consecutive elements, treating the sequence as circular (i.e.,
#' the last element is compared with the first).
#'
#' @author linapeter
#'
#' @param - sequence A numeric vector.
#'
#' @details
#' For a sequence \eqn{(x_1, x_2, \dots, x_n)}, the result is
#' \eqn{(|x_1 - x_2|, |x_2 - x_3|, \dots, |x_n - x_1|)}.
#'
#' @examples
#' step__(c(1, 5, 3, 9))
#'
#' @return
#' A numeric vector of the same length as `sequence`, containing the
#' absolute differences.
#'
#' @keywords internal
#'
step__ <- function(sequence){
  c(
    abs(sequence[-length(sequence)] - sequence[-1]),
    abs(sequence[1] - sequence[length(sequence)])
  )
}

#' Ducci (Diffy) Sequence
#'
#' @description
#' Applies the Ducci (also known as Diffy Game) transformation repeatedly
#' to a numeric sequence. At each iteration, the sequence is replaced by
#' the absolute differences between consecutive elements, with the last
#' element defined as the absolute difference between the first and last
#' elements of the previous sequence (see `step__`).
#'
#' The process stops when one of the following conditions is met:
#' \itemize{
#'   \item all elements of the sequence are zero;
#'   \item the sequence is repeated (the sequence appeared once already).
#' }
#'
#' @author linapeter
#'
#' @param sequence
#' A numeric vector or an object coercible to a numeric vector.
#'
#' @details
#' At each iteration, the updated sequence is printed to the console.
#' The initial sequence counts as the first step.
#'
#' @return
#' An integer giving the number of iterations performed until the stopping
#' criterion is reached.
#'
#' @examples
#' ducci_sequence(c(1, 5, 7, 9, 9))
#' ducci_sequence(c(1, 2, 1, 2, 1, 0))
#'
#' @export
#'
ducci_sequence <- function(sequence){
    sequence <- unlist(sequence)
    acc <- 1
    seen <- list()

    while (any(sequence != 0)){
        key <- paste(sequence, collapse = ",")

        if (key %in% seen){
            break
        }

        seen <- c(seen,key)

        sequence <- step__(sequence)
        acc <- acc + 1
    }
    return (acc)
}

#' Diffy Game for Multiple Sequences
#'
#' @description
#' Applies the Ducci (Diffy Game) process to multiple sequences.
#' Each sequence is processed independently using `ducci_sequence()`.
#'
#' @author linapeter
#'
#' @param sequences
#' A list of numeric vectors (or objects coercible to numeric vectors),
#' each representing an initial sequence for the Diffy Game.
#'
#' @return
#' A vector of integers, where each element corresponds to the number of
#' iterations performed for the respective input sequence.
#'
#' @details
#' This function is a thin wrapper around `lapply()`, delegating the
#' computation to `ducci_sequence()` for each element of `sequences`.
#'
#' @examples
#' seqs <- list(
#'   c(1, 5, 7, 9, 9),
#'   c(1, 2, 1, 2, 1, 0),
#'   c(10, 12, 41, 62, 31, 50),
#'   c(10, 12, 41, 62, 31)
#' )
#'
#' diffy_game(seqs)
#'
#' @export
#'
diffy_game <- function(sequences) unlist(lapply(sequences, ducci_sequence))

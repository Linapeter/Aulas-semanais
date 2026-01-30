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
#' @param sequence A numeric vector.
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
    first <- sequence[1]
    for (index in 1:(length(sequence)-1)){
        sequence[index] <- abs(sequence[index] - sequence[index+1])
    }
    sequence[length(sequence)] <- abs(first - sequence[length(sequence)])

    return (sequence)
}

#' Diffy Game
#'
#' @description
#' This function repeatedly applies the Diffy Game transformation
#' (see `step__`) to a numeric sequence until one of the following
#' stopping criteria is met:
#' \itemize{
#'   \item all elements are zero;
#'   \item the sequence stabilizes (the next sequence equals the previous one).
#' }
#'
#' @author linapeter
#'
#' @param - sequence A numeric vector or an object coercible to a numeric vector.
#'
#' @details
#' At each iteration, the function prints the updated sequence.
#' The process stops when the sequence reaches the zero vector or a fixed point.
#'
#' @return
#' An integer indicating the number of iterations performed.
#'
#' @examples
#' diffy_game(c(1, 5, 3, 9))
#'
#' @inherit step__
#'
#' @export
#'
diffy_game <- function(sequence){
    sequence <- unlist(sequence)
    acc <- 0

    while (any(sequence != 0) && !identical(prev_sequence == sequence)){
        prev_sequence <- sequence
        sequence <- step__(sequence)
        print(sequence)
        acc <- acc + 1
    }
    return (acc)
}

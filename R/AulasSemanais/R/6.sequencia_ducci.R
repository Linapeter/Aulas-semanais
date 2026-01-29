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

step__ <- function(sequence){
    first <- sequence[1]
    for (index in 1:(length(sequence)-1)){
        sequence[index] <- abs(sequence[index] - sequence[index+1])
    }
    sequence[length(sequence)] <- abs(first - sequence[length(sequence)])

    return (sequence)
}

diffy_game <- function(sequence){
    sequence <- unlist(sequence)
    acc <- 0

    while (any(sequence != 0)){
        sequence <- step__(sequence)
        print(sequence)
        acc <- acc + 1
    }
    return (acc)
}

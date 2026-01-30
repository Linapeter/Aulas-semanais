context("Testing code of commission")

example <- "Receita

        Frank Jane
Chá 120 145
Café 243 265

Despesas

        Frank Jane
Chá 130 59
Café 143 198"

test_that("Given example", {
    input <- example
    output <- c(Frank = 5.58,Jane  = 9.49)

    expect_equal(commission(input), output)
})

exercise <- "Receita

            Johnver Vanston Danbree Vansey Mundyke
Chá 190 140 1926 14 143
Café 325 19 293 1491 162
Água 682 14 852 56 659
Leite 829 140 609 120 87

Despesas

            Johnver Vanston Danbree Vansey Mundyke
Chá 120 65 890 54 430
Café 300 10 23 802 235
Água 50 299 1290 12 145
Leite 67 254 89 129 76"

test_that("Given exercise", {
    input <- exercise
    output <- c(Johnver = 92, Vanston = 5, Danbree = 113, Vansey = 45, Mundyke = 32)

    expect_equal(commission(input), output)
})




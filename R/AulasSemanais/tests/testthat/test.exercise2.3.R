
test_that("Given example", {
    input <- list(c(0, 653, 1854, 4063))
    output <- c(24)

    expect_equal(diffy_game(input), output)
})

test_that("Given exercise", {
    input <- list(
      c(1, 5, 7, 9, 9),
      c(1, 2, 1, 2, 1, 0),
      c(10, 12, 41, 62, 31, 50),
      c(10, 12, 41, 62, 31)
    )
    output <- c(23,3,22,30)

    expect_equal(diffy_game(input), output)
})

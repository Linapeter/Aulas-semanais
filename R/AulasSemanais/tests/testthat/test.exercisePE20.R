test_that("Sum of digits of result of 10!", {
  output <- 27
  expect_equal(factorial_digit_sum(10), output)
})

test_that("Sum of digits of result of 100!", {
  output <- 648
  expect_equal(factorial_digit_sum(100), output)
})
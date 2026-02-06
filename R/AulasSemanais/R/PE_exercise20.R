# https://projecteuler.net/problem=20

# Factorial Digit Sum

# n! means n x (n-1) x ... x 3 x 2 x 1.
# For example, 10! = 362880
# and the sum of te digits in the number 10! is 3+6+2+8+8+0+0 = 27

# Find the sum of the digits in the number 100!

#' Sum of the digits of a factorial
#'
#' Computes the sum of the digits of \code{number!}. The factorial is calculated
#' using arbitrary-precision arithmetic from the \pkg{gmp} package, allowing
#' the function to handle large values of \code{number}.
#'
#' @author linapeter
#'
#' @param number - A non-negative integer. The number whose factorial digits will
#'   be summed.
#'
#' @return A numeric scalar representing the sum of the digits of
#'   \code{number!}.
#'
#' @details
#' This function first computes the factorial of \code{number} using
#' \code{\link[gmp]{factorialZ}}, converts it to a character string without
#' scientific notation, splits the digits, and then sums them.
#'
#' @examples
#' factorial_digit_sum(10)
#' # 10! = 3628800 -> 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27
#'
#' factorial_digit_sum(100)
#'
#' @importFrom gmp factorialZ
#'
#' @export
#'
factorial_digit_sum <- function(number) factorialZ(number) |>
    strsplit("") |>
    unlist() |>
    as.numeric() |>
    sum()

#' sum_squares_difference
#'
#' @description
#' This function returns the difference between Sum of squares and Square of sums,
#' beginning on 1 until limit.
#'
#' @param limit Integer. A positive number indicating the upper bound of the
#' sequence starting at 1.
#'
#' @details
#' This function corresponds to Problem 6 of the Project Euler problem set.
#'
#' @return
#' A numeric value representing the difference between the square of the sum
#' and the sum of the squares from 1 to \code{limit}.
#'
#' @examples
#' sum_squares_difference(10)
#' sum_squares_difference(100)
#'
#' @author
#' lina park
#'
#' @export

sum_squares_difference <- function(limit){
    return ((sum(c(1:limit)))^2 - sum(c(1:limit)^2))
}

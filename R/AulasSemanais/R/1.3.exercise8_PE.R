# Largest Product in a series
# Problem 8 - Project Euler

# The four adjacent digits in the 1000-digit number that have the greatest product are 9x9x8x9 = 5832.
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
# What is the value of this product?

#' Largest product of consecutive digits
#'
#' @description
#' This function finds the greatest product obtained from multiplying
#' a fixed number of consecutive elements in a numeric sequence.
#'
#' @param series A numeric vector containing the sequence of numbers.
#' @param digits An integer indicating how many consecutive elements
#' are used to compute each product.
#'
#' @details
#' This function corresponds to Exercise 8 from the Project Euler
#' problem set.
#'
#' @return
#' A numeric value corresponding to the largest product of
#' \code{digits} consecutive elements in the sequence.
#'
#' @examples
#' largest_product(c(2, 3, 4, 3, 2, 5, 3, 2, 1, 4), 2)
#'
#' @author
#' Lina Park
#'
#' @export
#'
largest_product <- function(series,digits){
    products <- unlist(
        Map(function (index) prod(series[index:(index+digits - 1)]),
        1:(length(series) - digits) + 1))

    return (max(products))
}

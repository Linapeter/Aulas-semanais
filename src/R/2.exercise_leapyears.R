# Leap year (exercism)

# A leap year (in the Gregorian calendar) occurs:

# In every year that is evenly divisible by 4.
# Unless the year is evenly divisible by 100, in which case it's only a leap year if the year is also evenly divisible by 400.
# Some examples:

# 1997 was not a leap year as it's not divisible by 4.
# 1900 was not a leap year as it's not divisible by 400.
# 2000 was a leap year!

#' Leap_year
#'
#' @description
#' This function returns whether the year is a leap year or not
#'
#' @param year Integer. A positive number indicating the year in question
#'
#' @details
#' This function corresponds to the Leap Year exercise from Exercism.
#'
#' @return
#' A logical value: \code{TRUE} if the year is a leap year, \code{FALSE} otherwise.
#'
#' @examples
#' leap_year(2000)
#' leap_year(1900)
#'
#' @author
#' lina park
#'
#' @export

leap_year <- function(year){
    (year %% 4 == 0 && year %% 100 != 0) || (year %% 400 == 0)
}
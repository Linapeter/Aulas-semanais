
read_file <- function() {
  path <- system.file("data", "exercise8_PE.txt", package = "AulasSemanais")
  content <- readLines(path)
  content <- gsub("\\s+", "", content)
  as.numeric(strsplit(content, "")[[1]])
}


test_that("Given example", {
    input <- 4
    output <- 5832

    expect_equal(largest_product(read_file(), input), output)
})

test_that("Wanted value", {
    input <- 13
    output <- 23514624000

    expect_equal(largest_product(read_file(), input), output)
})
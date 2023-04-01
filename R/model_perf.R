library(rmarkdown)
library(reticulate)

#' @example {
#' plot_region_var(lst$mitigation_rate_all_regions)
#' }
plot_region_var <- function(mat) {
  col <- terrain.colors(ncol(mat))
  plot(1:nrow(mat), mat[,1], col=col[1], ylim=c(0,max(mat)))

  sapply(2:ncol(mat), function(j) {
    xs <- mat[,j]
    lines(xs, col=col[j])
  })
  invisible()
}


#' Series generated with negotiation have duplicate data based on the proposal
#' and evaluation steps where the simulation doesn't run.
#' Remove these duplicates to get a proper view.
trim_nego_series <- function(xs) {
  idx <- 1:length(xs)
  keep <- ifelse(idx %% 3 == 1, idx, NA)
  idx <- keep[!is.na(keep)]
  xs[idx]
}

plot_temperature <- function(lst, has.nego=TRUE) {
  vs <- lst$global_temperature[,1]
  if (has.nego) {
    vs <- trim_nego_series(vs)
  } 

  # Use 2023 as start point
  vs <- c(0,vs)
  xs <- 2023 + (1:length(vs))*5
  plot(xs, vs, type='l', main='Global temperature increase from 2023 (C)')
}

plot_carbon <- function(lst, has.nego=TRUE) {
  vs <- lst$global_carbon_mass[,1]
  if (has.nego) {
    vs <- trim_nego_series(vs)
  } 

  # Use 2023 as start point
  vs <- c(0,vs)
  xs <- 2023 + (1:length(vs))*5
  plot(xs, vs, type='l', main='Global temperature increase from 2023 (C)')
}

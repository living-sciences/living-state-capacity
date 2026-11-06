load("/workspace/eval/followup_staging/shared-data/vdem/vdem_v16.RData")
cols <- c("country_name","country_text_id","country_id","COWcode","year",
          "e_polity2","e_p_polity","e_lexical_index","v2xcl_prpty","v2x_polyarchy","v2x_rule","histname")
cols <- cols[cols %in% names(vdem)]
sub <- vdem[, cols]
write.csv(sub, "/workspace/eval/followup/001-001-living-update/workspace/data/vdem_core.csv", row.names=FALSE)
cat("WROTE", nrow(sub), "rows", ncol(sub), "cols\n")
cat("year range", min(sub$year), max(sub$year), "\n")

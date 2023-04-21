# Cafe cannot work on deep phylogenies if, for any given gene family, the difference in count between the largest count and the smallest count is more than "X". "X" can be different for different datasets. This script takes the original data from orthofinder and produces an output that cafe can actually produce.

using CSV, DataFrames, ArgParse

S = ArgParseSettings()

@add_arg_table S begin
    "--min"
    help = "How many minimum non-zero values in a row. Default is 2."
    arg_type = Int
    default = 2
    "--tsv"
    help = "What is the name of the tsv file."
    "--o"
    help = "What is the name of the output file."
    default = "counts.tsv"
    "--diff"
    default = 68
    help = "What difference between the minimum and the maximum value do you want to filter for? Default 68"
    arg_type = Int
end

S = parse_args(S)

df = DataFrame(CSV.File(S["tsv"], delim='\t'))

select!(df, Not(:Total))

# In the dataframe, the first column is a non-integer value (names of families). Use `df[:, 2:end])` to drop that.
# For each row count the number of non-zero values and drop if the number of non-zero values is too small 
# (the gene family is useless if it only has genes from two species in it in a group of 112 species).
df1 = df[[count(!iszero, row) > S["min"] for row in eachrow(df[:, 2:end])],:]

df2 = df1[[(maximum(row) - minimum(row)) < S["diff"] for row in eachrow(df1[:, 2:end])],:]

# Add a column named 'null' to the first column and set every value to '(null)'
insertcols!(df2, 1, :Desc => "(null)")

println("The size of the dataframe this has created is", size(df2))

CSV.write(S["o"], df2, delim='\t')

# NCBI datasets [https://www.ncbi.nlm.nih.gov/datasets/] can be used to produce insights on the available genomic data for any given species
# The data filteration tools for NCBI Datasets have felt somewhat constrained. This script is to help to wrangle the data produced by NCBI Datasets.
# @params - Input -> JSONs produced by NCBI Datasets
# @params - Output -> TSV file with columns: Species_name (Name of species), Counts (Counts of complete genomes in NCBI databases)


using JSON, ArgParse

S = ArgParseSettings()

@add_arg_table S begin
    "--dir"
    help = "The directory that contains the JSONs. The current directory will be used by default."
    default = "."
    "--o"
    help = "The name for the output file. The default is 'counts.tsv'."
    default = "counts.tsv"
end

S = parse_args(S)

json_files = filter(file -> ispath(joinpath(S["dir"], file)) && splitext(file)[2] == ".json", readdir(S["dir"]))

if length(json_files) == 0
    error("The directory you supplied has no json files.")
end

if isfile(S["o"])
    error("The file ",S["o"]," already exists. Please provide a different name")
end

open(S["o"],"a") do writefile
    init = "species_name" * "\t" * "count"
    println(writefile, init)
    for i in json_files
        fileloc = S["dir"] * "/" *i
        open(fileloc) do file
            json_content = JSON.parse(read(file, String))
            j = replace(split(i,".")[1],"_" => " ")
            countomics = json_content["total_count"]
            line = j * "\t" * "$countomics"
            println(writefile,line)
        end
    end
end
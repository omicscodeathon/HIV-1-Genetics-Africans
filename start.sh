#!/usr/bin/env bash

function searchSequences() {
    # a script to initiate the analysis by calling the python scripts that
    # search and download sequences from NCBI

    script_dir=./workflow/scripts
    countries="Guinea_bissau Kenya Uganda Cameroon Tanzania Nigeria Ethiopia Zambia Rwanda South_Africa"

    rm sequences.fasta # remove any copy of sequences.fasta file that may exist in the working directory

    for country in $countries
    do
        echo Now searching sequences from "${country}"
        python3 "${script_dir}"/sequence_search.py "${country}" 15 # Run the ncbi sequence search and download
        python3 "${script_dir}"/fasta_edit.py ./sequences_query.fasta script # edit the downloaded fasta files.
        cat ./edited_sequence.fasta >> sequences.fasta # append the edited sequence to the sequences.fasta file

    done
}

searchSequences # call the function here

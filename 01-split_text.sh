#!/bin/bash

awk '
BEGIN {
    RS = " "; ORS = ""; 
    chunk_num = 1; 
    print_chunk = sprintf("chunk_%02d.txt", chunk_num);
}
{
    if (length(buffer) + length($0) >= 5000) {
        print buffer > print_chunk;
        close(print_chunk);
        buffer = $0; 
        chunk_num++;
        print_chunk = sprintf("chunk_%02d.txt", chunk_num);
    } else {
        buffer = (length(buffer) > 0 ? buffer " " : "") $0
    }
}
END {
    if (length(buffer) > 0) {
        print buffer > print_chunk;
        close(print_chunk);
    }
}' "$1"

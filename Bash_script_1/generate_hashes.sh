#!/bin/bash

# Check if the user provided a list of files
if [ $# -eq 0 ]; then
  echo "Usage: $0 <file1> <file2> ..."
  exit 1
fi

# Specify the output file
output_file="checksums.txt"

# Clear the contents of the output file or create it if it doesn't exist
> "$output_file"

# Loop through the provided files and calculate MD5 and SHA-1 checksums
for file in "$@"; do
  if [ -f "$file" ]; then
    md5sum_value=$(md5sum "$file" | awk '{print $1}')
    sha1sum_value=$(sha1sum "$file" | awk '{print $1}')
    echo "File: $file" >> "$output_file"
    echo "MD5: $md5sum_value" >> "$output_file"
    echo "SHA-1: $sha1sum_value" >> "$output_file"
    echo "------------------------" >> "$output_file"
  else
    echo "File not found: $file" >> "$output_file"
  fi
done

echo "Checksums written to $output_file"

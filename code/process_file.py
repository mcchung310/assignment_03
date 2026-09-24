"""
process_file.py — Part 2: one file of package descriptions, uploaded.

A Streamlit app that accepts an uploaded text file with one package description
per line, shows the total for every line, and writes the parsed packages to a
JSON file in the `data/` folder — `data/packaging1.txt` in, `data/packaging1.json`
out.

New here: an uploaded file arrives as **bytes**, not text, so it has to be
decoded before it can be split into lines. And a text file usually ends with a
newline, so the last "line" is empty and must be skipped rather than parsed.

Run it:  Run and Debug -> "Streamlit Run: Current File"   (see README Reference #1)
Test it: pytest tests/test_streamlit.py -k process_file
"""

# --- The page ---------------------------------------------------------------------
#
# Less scaffolding this time. The steps are described, but which widget and which
# function does each job — and what to call the result — is now yours to work out.
# `one_package.py` is your worked example for anything structural, and README
# Reference #4 and #5 cover the two things that are new here.

# Imports — streamlit, json, and what you need from packaging_parser.
import streamlit as st
import json
from packaging_parser import calc_total_units, get_unit, parse_packaging

# The title, exactly:   Process File of Packages
st.title("Process File of Packages")

package_file = st.file_uploader(
    "Upload package file",
    key = "package_file"
)

if package_file is not None:
    content = package_file.read().decode("utf-8")
    lines = content.splitlines()
    parsed_packages = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        package = parse_packaging(line)
        parsed_packages.append(package)
        total = calc_total_units(package)
        unit = get_unit(package)
        st.info(f"{line} ➡️ Total 📦 Size: {total} {unit}")


    output_filename = package_file.name.replace(".txt", ".json")
    output_path = f"data/{output_filename}"
    with open(output_path, "w") as f:
        json.dump(parsed_packages, f)

    st.success(f"{len(parsed_packages)} packages written to {output_path}")



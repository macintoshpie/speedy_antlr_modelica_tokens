#!/bin/bash

docker build -t antlr4:latest -f antlr/Dockerfile .

# Generate C++ target with visitor
docker run -v "$(pwd)/src/modelica/parser":/var/antlrResult \
        antlr4:latest \
        -Dlanguage=Cpp -visitor -listener -o /var/antlrResult/cpp_src /var/antlrResult/modelica.g4

# Generate Python target
docker run -v "$(pwd)/src/modelica/parser":/var/antlrResult \
        antlr4:latest \
        -Dlanguage=Python3 -no-visitor -listener -o /var/antlrResult /var/antlrResult/modelica.g4

# Run antlr tool to generate the accelerator files
python3 <<EOF
from speedy_antlr_tool import generate

generate(
    py_parser_path="src/modelica/parser/modelicaParser.py",
    cpp_output_dir="src/modelica/parser/cpp_src",
)
EOF

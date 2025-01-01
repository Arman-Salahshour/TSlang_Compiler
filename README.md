# TSlang Compiler

TSlang Compiler is a custom compiler designed to process the TSlang language. TSlang is a procedural programming language featuring constructs like variables, lists, conditional statements, loops, and function definitions. The compiler includes lexical analysis, parsing, and code generation components.

## Features

1. **Lexical Analysis**: Implements tokenization for TSlang syntax, identifying variables, reserved keywords, operators, delimiters, and constants.
2. **Parsing**: Employs a parser to validate syntax and build an abstract syntax tree (AST) using the grammar rules defined for TSlang.
3. **Intermediate Representation (IR)**: Generates intermediate code for executing TSlang programs.
4. **Support for Constructs**:
   - Variables (`num`, `list`)
   - Conditional statements (`if`, `else`)
   - Loops (`for`, `while`)
   - Functions with parameters and return types
   - Arithmetic and logical operations

## Example Program

The following TSlang program demonstrates the compiler's capabilities:

```tslang
num find(list A, num x) {
  num i;
  num n;
  i = 0;
  for (n in A) {
    if (n == x) {
      return i;
    }
    i = i + 1;
  }
  return -1;
}

num main() {
  list A;
  num a;
  A = makeList(3);
  a = 5;
  A[2] = a + 2;
  A[1] = 6;
  numprint(find(A, 5));
  return 0;
}
```

### Expected Output
For the above program, the output will print the index of the element `5` in the list `A`.

## Compiler Components

### 1. Lexical Analyzer

Located in `Lexical_Analyzer.py` and `LA_ply.py`, this module tokenizes the TSlang code. Key functions:
- **Finite State Machine (FSM)**: The lexical analyzer uses an FSM-based approach to identify tokens such as numbers, identifiers, and reserved keywords. Delimiters and operators are detected using predefined patterns.
- **Regular Expressions**: Patterns for tokens are defined using regular expressions to efficiently match keywords, numbers, and symbols in the source code.
- **Error Handling**: The analyzer detects and handles illegal characters or unrecognized patterns gracefully.

### 2. Parser

The parser in `PARSER_ply.py` ensures the syntactic correctness of TSlang programs based on the grammar defined in `grammar.txt`. It builds an Abstract Syntax Tree (AST) using:
- **LALR Parsing Algorithm**: This efficient parsing technique is used to process the TSlang grammar rules and resolve conflicts, ensuring correctness and performance.
- **Grammar Validation**: The parser validates constructs such as expressions, loops, and functions against the BNF grammar, ensuring strict adherence to language rules.

### 3. Intermediate Code Generator

Implemented in `middle_code_generator.py`, this module:
- **Three-Address Code (TAC)**: Converts high-level TSlang constructs into a lower-level, assembly-like representation suitable for execution.
- **Symbol Table Management**: Tracks variable types, scopes, and function definitions during code generation.
- **Label and Temporary Variable Generation**: Ensures unique labels and temporaries for control flow and computation.
- **Error Checking**: Validates type compatibility and ensures semantic correctness during generation.

### 4. Grammar

The grammar file `grammar.txt` defines the rules for TSlang's syntax using BNF (Backus-Naur Form). Example:

```
func := iden ( flist ) : type { body } ^;
stmt := expr ; | if ( expr ) stmt else stmt | while ( expr ) stmt ^;
```

The grammar is designed for modularity and supports recursive constructs, allowing complex expressions and nested functions.

## Key Algorithms

1. **Lexical Analysis**:
   - Finite State Machine: Handles transitions between states based on input characters.
   - Regular Expression Matching: Identifies tokens by applying regex patterns.

2. **Parsing**:
   - LALR Algorithm: Efficiently resolves shift-reduce conflicts and constructs the parse tree or AST.
   - Recursive Descent Parsing: Validates nested constructs and generates intermediate nodes.

3. **Code Generation**:
   - TAC Generation: Breaks down high-level constructs into a sequence of operations with temporaries and labels.
   - Control Flow Graph (CFG): Used to manage and validate control structures such as loops and conditionals.

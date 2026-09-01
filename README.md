# Adaptable Decoder

A Python script that decrypts text encoded with a whatever techniques for transforming text you want and exports the decoded output to a file.

## Features

- **Pattern Matching Decoding**: Uses Python's `match-case` structural pattern matching for character substitution.
- **Punctuation Formatting**: Replaces standard punctuation marks with delimiter characters (`|`).
- **File Export**: Automatically saves the resulting output string into `result.txt`.

## Prerequisites

- Python 3.10+ (required for `match-case` syntax)

## Installation & Usage

1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/caesar-cipher-decoder.git](https://github.com/your-username/caesar-cipher-decoder.git)
   cd caesar-cipher-decoder
   ```
## 💡 Usage Guide

### 1. Adaptable Decoder (`adaptable_decoder.py`)
1. Save `adaptable_decoder.py` in an empty folder.
2. Open `website_image_downloader.py` and paste your encripted text in the `encrypted_text` variable:
   ```python
   encrypted_text = "EXAMPLE"

   ```
2. Define your decryption alphabet:
   ```python
   def decode_character(char):
      match char:
         case "a":
            return "c"
         case "b":
            return "d"
         case "c":
            return "e"
         case "," | "." | "!":
            return "|"
        case " ":
            return " "
        case _:
            return char
   ```
3. View the terminal output or check the generated `result.txt` file in the working directory.

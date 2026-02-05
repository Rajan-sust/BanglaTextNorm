<!-- # Bangla Text Normalization (BanglaTextNorm)



### installation
```bash
git clone https://github.com/Rajan-sust/BanglaTextNorm.git
cd BanglaTextNorm
# virtual environment setup
python3 -m venv BnTn
source BnTn/bin/activate
# install dependencies
pip install -r requirements.txt
```

### Environment Variable
Set your Groq API key  as an environment variable for LLama multilingual LLM:
```
export GROQ_API_KEY=<your-api-key-here>
```

### Usage

```bash
python3 main.py --text "আপনার টেক্সট এখানে"
```

### License
This project is licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Others can use, modify, and distribute, but not for commercial purposes. -->

# Kingfisher: Bangla Text Normalization

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

A hybrid LLM-augmented Bangla text normalization system for enhanced text-to-speech applications, achieving 96% accuracy (95%–97% CI).

## Overview

Kingfisher is a three-stage hybrid framework that combines:
1. **LLM-based tokenization and semiotic class annotation** using Meta Llama 3.3
2. **Lexicon-driven context-aware verbalization** with rule-based verbalizers
3. **Error correction** to ensure high-quality normalized output

### Key Features

- **High Accuracy**: 96% overall accuracy, significantly outperforming existing solutions
- **Comprehensive Coverage**: Handles 9+ semiotic classes including symbols, abbreviations, acronyms, cardinal/ordinal numbers, decimals, money, dates, times, and electronic addresses
- **Context-Aware**: Resolves ambiguous cases using contextual information (e.g., "-" as "থেকে" vs "মাইনাস")
- **Open Source**: Full source code, datasets, and linguistic resources publicly available

### Supported Semiotic Classes

| Semiotic Class | Description                                         | Example Input                                             |
|----------------|-----------------------------------------------------|-----------------------------------------------------------|
| SYMBOL         | A mark or notation indicating something              | ২৬°৩৮´ উত্তর অক্ষাংশ (26°38´ North latitude)              |
| ABBREVIATION   | Shortened form of a word                              | মো: (Md.), ডা. (Dr.)                                      |
| ACRONYM        | A word formed from the initial letters of other words| ডি-৮ (D-8), টি-২০ (T-20)                                  |
| CARDINAL       | A number denoting quantity, amount, or measurement   | ১৪৯৩৫ জন (14,935 people)                                  |
| ORDINAL        | Denotes the position or rank                          | ১ম (1st), ২য় (2nd)                                       |
| DECIMAL        | A whole number with a fractional part                 | ১.৪৭ মাইল (1.47 miles)                                   |
| DIGIT          | Verbalized digit-by-digit                             | হেল্পলাইন ১৬২৬৩ (Helpline 16263)                          |
| MONEY          | Quantities with currency                              | ১.৫ টাকা (1.5 taka)                                      |
| DATE           | Date expression                                       | ৬/১২/২০২২ খ্রিস্টাব্দ (6/12/2022 AD)                     |
| TIME           | Time expression                                       | সকাল ৯:৩০ (9:30 AM)                                      |
| ELECTRONIC     | Email addresses and URLs                              | ওয়েবসাইট: www.sust.edu (Website: www.sust.edu)           |


## Installation

### Prerequisites
- Python 3.8 or higher
- Groq API key (for LLM access)

### Setup

```bash
# Clone the repository
git clone https://github.com/Rajan-sust/BanglaTextNorm.git
cd BanglaTextNorm

# Create virtual environment
python3 -m venv BnTn
source BnTn/bin/activate  # On Windows: BnTn\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Environment Configuration

Set your Groq API key as an environment variable:

```bash
# Linux/MacOS
export GROQ_API_KEY=<your-api-key-here>

# Windows (Command Prompt)
set GROQ_API_KEY=<your-api-key-here>

# Windows (PowerShell)
$env:GROQ_API_KEY="<your-api-key-here>"
```

To get a Groq API key, visit: https://console.groq.com/

## Usage

### Basic Usage

```bash
python3 main.py --text "আপনার টেক্সট এখানে"
```

### Examples

```bash
# Normalize numbers and dates
python3 main.py --text "৬/১২/২০২২ খ্রিস্টাব্দে ১৪৯৩৫ জন উপস্থিত ছিলেন।"

# Output: ছয় ডিসেম্বর দুই হাজার বাইশ খ্রিস্টাব্দে চৌদ্দ হাজার নয়শ পঁয়ত্রিশ জন উপস্থিত ছিলেন।

# Normalize money and symbols
python3 main.py --text "পণ্যের দাম ৳৭.১০ এবং তাপমাত্রা -১৭৩ ডিগ্রী সেলসিয়াস।"

# Output: পণ্যের দাম সাত টাকা দশ পয়সা এবং তাপমাত্রা মাইনাস একশ তিয়াত্তর ডিগ্রী সেলসিয়াস।
```

## Dataset

The project includes a comprehensive Bangla text normalization dataset with 2,766 annotated tokens across 9 semiotic classes:

- **Sentence-level**: Complete sentences with normalized forms
- **Token-level**: Individual tokens with semiotic class annotations

Dataset location: `Dataset/`

### Dataset Statistics

| Semiotic Class | Annotated Tokens |
|----------------|------------------|
| SYMBOL | 1,090 |
| CARDINAL | 550 |
| DATE | 412 |
| DECIMAL | 164 |
| TIME | 128 |
| ACRONYM | 126 |
| ABBREVIATION | 125 |
| MONEY | 117 |
| ORDINAL | 54 |
| **Total** | **2,766** |

### Dataset Format

**Token-level format example:  `৮ টি বিভাগ।` **



| Input Token | Semiotic Class |
|-------------|----------------|
| ৮           | CARDINAL       |
| টি          | PLAIN          |
| বিভাগ       | PLAIN          |
| । | SYMBOL| 
| &lt;eos&gt;     | &lt;eos&gt;          |


## Linguistic Resources

Comprehensive lexicons are provided in `linguistic-resources/`:

- **Symbols**: Unambiguous and context-dependent symbols with phonetic representations
- **Abbreviations**: Common abbreviations and their expanded forms (Dr., Md., Lt., etc.)
- **Acronyms**: International and local acronyms with pronunciation guides (NATO, OIC, ডি-৮, etc.)
- **Ordinal Numbers**: Ordinal mappings (১ম → প্রথম, ২য় → দ্বিতীয়, etc.)
- **Context Lexicons**: Disambiguation lexicons for ambiguous symbols and abbreviations

These resources are essential for accurate context-aware verbalization.

## System Architecture

### Three-Stage Pipeline

```
Input Text
    ↓
[Stage 1: LLM-based Tokenization & Semiotic Annotation]
    ↓
[Stage 2: Context-Aware Verbalization]
    ├── Symbol Verbalizer (with disambiguation)
    ├── Abbreviation Verbalizer (with disambiguation)
    ├── Acronym Verbalizer
    ├── Cardinal Verbalizer
    ├── Ordinal Verbalizer
    ├── Decimal Verbalizer
    ├── Money Verbalizer
    ├── Date Verbalizer
    ├── Time Verbalizer
    └── Electronic Verbalizer
    ↓
[Stage 3: LLM-based Error Correction & Completion]
    ↓
Normalized Output
```

## License

This project is licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).


## Acknowledgments

- Meta Llama 3.3 (70B parameters)
- Comparison baseline: Google's Sparrowhawk system
- Groq for providing LLM API access

## Support & Contact

- **Issues**: Please report bugs and feature requests via [GitHub Issues](https://github.com/Rajan-sust/BanglaTextNorm/issues)
- **Email**: `rajan-ictc [at] sust.edu`




## FAQ

**Q: Do I need an internet connection to use Kingfisher?**  
A: Yes, currently the system requires internet access to call the Groq API for LLM inference.

**Q: Can I use this for commercial TTS applications?**  
A: No, the CC BY-NC 4.0 license prohibits commercial use. Contact the authors for commercial licensing options.

**Q: How accurate is it compared to human annotators?**  
A: The system achieves 96% accuracy on our test dataset. Human evaluation shows high agreement with gold-standard normalizations.

**Q: Does it handle informal social media text?**  
A: Preliminary testing shows 80% accuracy on social media text. This is an area for future improvement.

**Q: Can I add my own custom abbreviations or symbols?**  
A: Yes! You can extend the lexicons in the `linguistic-resources/` directory with your domain-specific terms.

**Q: What about other low-resource languages?**  
A: The three-stage hybrid approach can be adapted to other languages.
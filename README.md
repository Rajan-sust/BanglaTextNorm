# Bangla Text Normalization (BanglaTextNorm)



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
This project is licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Others can use, modify, and distribute, but not for commercial purposes.
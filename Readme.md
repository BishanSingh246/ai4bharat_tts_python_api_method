<h1 align="center">
    <b> Ai4Bharat Model Running Locally through Api Method</b> 
<br>
</h1>

## Description
This repository will help you to run TTS AI4Bharat model locally through <a href='https://pypi.org/project/TTS/'>TTS</a> python api method and generate audio output for Indian language in ```.wav``` format. All Pre-Trained Models are avalable <a href='https://github.com/AI4Bharat/Indic-TTS/releases/tag/v1-checkpoints-release'>here</a>.


### We can use AI4Bharat for these languages.
| Indian Languages | Language Code | TTS  | STT |
|------------------|---------------|------|-----|
| Assamese         | as            | Yes  | No  |
| Bengali(Bangal)  | bn            | Yes  | Yes |
| Bhojpuri         |               | No   | No  |
| Boro             | brx           | Yes  | No  |
| Dogri            |               | No   | No  |
| Gujarati         | gu            | Yes  | Yes |
| Hindi            | hi            | Yes  | Yes |
| Kannada          | kn            | Yes  | Yes |
| Kashmiri         |               | No   | No  |
| Konkani          |               | No   | No  |
| Marathi          | mr            | Yes  | Yes |
| Manipuri         | mni           | Yes  | No  |
| Malayalam        | ml            | Yes  | Yes |
| Maithili         |               | No   | No  |
| Nepali           |               | No   | No  |
| Odia (Oriya)     | or            | Yes  | Yes |
| Punjabi          | pa            | Yes  | Yes |
| Rajasthani       | raj           | Yes  | No  |
| Sanskrit         |               | No   | Yes |
| Sindhi           |               | No   | No  |
| Telugu           | te            | Yes  | Yes |
| Tamil            | ta            | Yes  | Yes |
| Urdu             |               | No   | Yes |

## Required Package 

```pip install -U pip```

```pip install TTS```


## Instruction

1. You need to download and unzip the file for that follow below commands.
    
    ```
    - wget https://github.com/AI4Bharat/Indic-TTS/releases/download/v1-checkpoints-release/hi.zip
    - unzip hi.zip
    - rm hi.zip
    ```

2. Open ```hi/fastpitch/config.json``` file and remove this path ```"models/v1/hi/fastpitch/speakers.pth"``` and change path to ```hi/fastpitch/speakers.pth``` for ```speakers_file``` key in line number 181 and 194.

3. To run app.py file ```python app.py``` in terminal. it will generate aufio file and you can change text in ```app.py```.

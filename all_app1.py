import torch
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)

speakers_file_path = "hi/fastpitch/speakers.pth"

text_arr = ["व्यक्तिगत विकास से समृद्धि होती है, यह आवश्यक है।",
"सफलता उसे मिलती है जो हारने के बाद भी नहीं हारता।",
"आपकी सोच आपके जीवन को बना सकती है या तोड़ सकती है।",
"प्रेरणा वो चीज़ है जो हमें अपने लक्ष्य की ओर बढ़ाती है।",
"आत्मविश्वास सफलता की कुंजी है, कभी हार नहीं मानना।"
]

tts = TTS(
        model_name = None,
        model_path = "hi/fastpitch/best_model.pth",
        config_path = "hi/fastpitch/config.json",
        vocoder_path = "hi/hifigan/best_model.pth",
        vocoder_config_path = "hi/hifigan/config.json",
        gpu = True)

for index,value in enumerate(text_arr):

    wav = tts.tts_to_file(value,
        speaker = "female",
        file_path = f"output_array_{index}.wav",)



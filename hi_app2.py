import torch
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)

speakers_file_path = "hi/fastpitch/speakers.pth"

text_arr = ["सफलता उनकी मिलती है जो कभी हार नहीं मानते, उनकी मेहनत कभी नहीं टूटती।",
"संवाद और सहयोग समस्याओं का समाधान आसानी से कर सकते हैं।",
"जीवन को आपके अपने तरीके से जिएं, हर पल का आनंद उठाएं।",
"सफलता की ऊँचाइयों को छूने के लिए सपनों का पीछा करो और कभी हार नहीं मानना।",
"आत्मविश्वास सफलता का महत्वपूर्ण हिस्सा है, इसे कभी हार नहीं मानना चाहिए।"
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



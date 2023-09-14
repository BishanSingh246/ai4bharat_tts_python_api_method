import torch
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)

speakers_file_path = "hi/fastpitch/speakers.pth"

text_arr = ["पाँचदशक के अंत में, उनका जश्न पचासवें जन्मदिन के साथ मनाया गया।",
"पाचास किलोमीटर की यात्रा पर जाने के बाद, वह थक कर गए।",
"उन्होंने पाचास दिनों में एक नया कार्यक्रम तैयार किया।",
"साल 2050 में, यह विश्व तकनीक के क्षेत्र में प्रमुख उधारणा बनेगा।",
"जब उन्होंने पचास गुणा स्कोर किया, तो वे प्रतियोगिता में विजयी बने।"]

# ["व्यक्तिगत विकास से समृद्धि होती है, यह आवश्यक है।",
# "सफलता उसे मिलती है जो हारने के बाद भी नहीं हारता।",
# "आपकी सोच आपके जीवन को बना सकती है या तोड़ सकती है।",
# "प्रेरणा वो चीज़ है जो हमें अपने लक्ष्य की ओर बढ़ाती है।",
# "आत्मविश्वास सफलता की कुंजी है, कभी हार नहीं मानना।"
# ]
# ["सफलता उनकी मिलती है जो कभी हार नहीं मानते, उनकी मेहनत कभी नहीं टूटती।",
# "संवाद और सहयोग समस्याओं का समाधान आसानी से कर सकते हैं।",
# "जीवन को आपके अपने तरीके से जिएं, हर पल का आनंद उठाएं।",
# "सफलता की ऊँचाइयों को छूने के लिए सपनों का पीछा करो और कभी हार नहीं मानना।",
# "आत्मविश्वास सफलता का महत्वपूर्ण हिस्सा है, इसे कभी हार नहीं मानना चाहिए।"
# ]
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



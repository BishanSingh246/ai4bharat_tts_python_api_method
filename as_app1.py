import torch
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)


text_arr =[
"আপোনাৰ চিন্তাধাৰাই আপোনাৰ জীৱনটো বনাব পাৰে বা ভাঙিব পাৰে।",
"প্ৰেৰণা হৈছে সেই বস্তু যিয়ে আমাক আমাৰ লক্ষ্যৰ দিশে আগুৱাই লৈ যায়।",
"আত্মবিশ্বাসেই সফলতাৰ চাবিকাঠি, কেতিয়াও হাৰ নামানিব।",
"সফলতা সেইসকলৰ বাবেই আহে যিয়ে কেতিয়াও হাৰ নামানে, তেওঁলোকৰ কঠোৰ পৰিশ্ৰম কেতিয়াও বিফল নহয়।",
"যোগাযোগ আৰু সহযোগিতাই সমস্যাসমূহ সহজে সমাধান কৰিব পাৰে।",
"জীৱনটো নিজৰ মতে জীয়াই থাকক, প্ৰতিটো মুহূৰ্ত উপভোগ কৰক।",
"সফলতাৰ উচ্চতাত উপনীত হ’বলৈ নিজৰ সপোনক খেদি ফুৰক আৰু কেতিয়াও হাৰ নামানিব।",
"আত্মবিশ্বাস সফলতাৰ এক গুৰুত্বপূৰ্ণ অংশ, ইয়াক কেতিয়াও এৰি দিয়া উচিত নহয়।"
]

tts = TTS(
        model_name = None,
        model_path = "as/fastpitch/best_model.pth",
        config_path = "as/fastpitch/config.json",
        vocoder_path = "as/hifigan/best_model.pth",
        vocoder_config_path = "as/hifigan/config.json",
        gpu = True)
        # gpu = False)

for index,value in enumerate(text_arr):

    wav = tts.tts_to_file(value,
        speaker = "female",
        file_path = f"output_array_{index}.wav",)

import torch
from TTS.api import TTS
# models/v1/or/fastpitch/speakers.pth'
# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)

# speakers_file_path = "hi/fastpitch/speakers.pth"

text_arr = [

"ତୁମର ଚିନ୍ତାଧାରା ତୁମ ଜୀବନକୁ ବନାଇପାରେ କିମ୍ବା ଭାଙ୍ଗିପାରେ |",
"ପ୍ରେରଣା ହେଉଛି ସେହି ଜିନିଷ ଯାହା ଆମକୁ ଆମର ଲକ୍ଷ୍ୟ ଆଡକୁ ଗତି କରେ |",
"ଆତ୍ମବିଶ୍ୱାସ ସଫଳତାର ଚାବିକାଠି, କେବେ ହାର ମାନ ନାହିଁ |",
"ସଫଳତା ଆସେ ଯେଉଁମାନେ କେବେ ହାର ମାନନ୍ତି ନାହିଁ, ସେମାନଙ୍କର କଠିନ ପରିଶ୍ରମ କେବେ ବିଫଳ ହୁଏ ନାହିଁ |",
"ଯୋଗାଯୋଗ ଏବଂ ସହଯୋଗ ସହଜରେ ସମସ୍ୟାର ସମାଧାନ କରିପାରିବ |",
"ଜୀବନକୁ ନିଜ ପଥରେ ବଞ୍ଚାନ୍ତୁ, ପ୍ରତ୍ୟେକ ମୁହୂର୍ତ୍ତକୁ ଉପଭୋଗ କରନ୍ତୁ |",
"ସଫଳତାର ଉଚ୍ଚତାରେ ପହଞ୍ଚିବା ପାଇଁ ତୁମର ସ୍ୱପ୍ନକୁ ଗୋଡ଼ାନ୍ତୁ ଏବଂ କେବେ ବି ଛାଡନ୍ତୁ ନାହିଁ |",
"ଆତ୍ମବିଶ୍ୱାସ ସଫଳତାର ଏକ ଗୁରୁତ୍ୱପୂର୍ଣ୍ଣ ଅଂଶ, ଏହାକୁ କେବେବି ଛାଡିବା ଉଚିତ୍ ନୁହେଁ |"

]

tts = TTS(
        model_name = None,
        model_path = "or/fastpitch/best_model.pth",
        config_path = "or/fastpitch/config.json",
        vocoder_path = "or/hifigan/best_model.pth",
        vocoder_config_path = "or/hifigan/config.json",
        gpu = True)
        # gpu = False)

for index,value in enumerate(text_arr):

    wav = tts.tts_to_file(value,
        speaker = "female",
        file_path = f"output_array_{index}.wav",)



import glob
from elevenlabs import generate, save, set_api_key
from env import ELEVEN_API_KEY

set_api_key(ELEVEN_API_KEY)

def read_file(file_path):
    with open(file_path, 'r') as file:
        file_contents = file.read()
    return file_contents

# Get list of all files that match the pattern
file_list = glob.glob('./chunk_*.txt')

# Iterate over the files
for file_path in sorted(file_list):
    file_contents = read_file(file_path)

    audio = generate(
        text=file_contents,
        voice="Bella",
        model="eleven_multilingual_v1"
    )

    # Parse the file number from the file name for output file name
    i = file_path.split('_')[-1].split('.')[0]
    save(audio, f"output-{str(i).zfill(2)}.wav")  # Similarly for the output file


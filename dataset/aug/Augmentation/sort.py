import os
import shutil
import miditoolkit

def parse_midi_file(sample_midi_path: str):
  midi_obj = miditoolkit.midi.parser.MidiFile(sample_midi_path)
  midi_name = sample_midi_path.split('/')[-1].split('.')[0]
  return midi_obj, midi_name

count = 0
subfolder=0
for root, folders, files in os.walk('./'):
    if files:
        for idx, file in enumerate(sorted(files)):
            try:
                midi_obj, midi_name = parse_midi_file(root+'/'+file)
            except:
                continue
            curr_folder = root.split('/')[-1]
            shutil.copy(f'{root}/{file}',f'./result/{str(subfolder)}/{curr_folder}_{file}')
            count += 1
            if count >= 96:
                subfolder+=1
                count=0

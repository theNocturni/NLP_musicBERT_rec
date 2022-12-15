## Music Recommendation System by leveraging Accompaniment Suggestion of MusicBERT

Junsoo Lee, Soowung Shin

PiRhDy data generation code taken and modified from https://github.com/mengshor/PiRhDy

musicBERT model taken from https://github.com/microsoft/muzic/tree/main/musicbert

### instruction
run PiRhDy.ipynb after putting midi files in dataset/lakh_dataset/{folder names} to create context embedded dataset.

After the data is created in context_acc, run musicBERT_data.ipynb to convert the dataset into OctupleMIDI format.

Alternatively, unzip acc_data_bin.zip(data used for finetuning) acc_augdata_bin.zip(data used for inference) in musicbert folder to skip the previous steps or to use the same data used for the experiment.

download the [MusicBERT base pre-trained checkpoint](https://msramllasc.blob.core.windows.net/modelrelease/checkpoint_last_musicbert_base.pt) or the checkpoint used for the experiment [here](https://drive.google.com/file/d/1IxFu4qdcUyBj4ghZx1Tn8H_OrVCf4PJK/view?usp=share_link), and put them in the musicbert/checkpoints folder

run musicbert.ipynb to either finetune the model or run inference on them
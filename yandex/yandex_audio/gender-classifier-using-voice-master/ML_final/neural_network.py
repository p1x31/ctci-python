#recording folder must exist at ML_final\recorded_audio

import numpy as np 
import librosa
from keras.models import load_model
import os
import soundfile as sf
# Load various imports 
from datetime import datetime
from os import listdir
from os.path import isfile, join
import numpy as np
import pandas as pd

mypath = "/home/vadim/ctci-python/edx/cf/more_yandex/test"
filenames = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and f.endswith('.wav'))] 
p_id_in_file = [] # patient IDs corresponding to each file
for name in filenames:
    p_id_in_file.append(name[:-4])

p_id_in_file = np.array(p_id_in_file) 
dataset = pd.DataFrame({'id': p_id_in_file[:]})
df = dataset
df["gender"] = 1
path="/home/vadim/yandex/gender-classifier-using-voice-master/ML_final/"


Model = load_model('neural_network.h5')
g=[]
for audiofile in os.listdir(path+'recorded_audio/'):
            try:
                y_in, sr = sf.read(os.path.join(path+'recorded_audio/',audiofile))
                y_in = librosa.resample(y_in, sr, 8000)
                y_in = y_in[0:40000]
                y_in = np.concatenate((y_in, [0]* (40000 - y_in.shape[0])), axis=0)
                g.append(y_in)
            except RuntimeError:
                print(".DS_Store file detected and dismissed")
                pass
x_in = np.array(g)
x_in.shape
x_in = x_in.reshape(x_in.shape[0],200,200)
result = Model.predict(x_in)
m=0
res = []
for r in result:
    if r>0.5:
        print("Male Voice Predicted")
        res.append(r)
    else:
        print("Female Voice Predicted")
        res.append(r)

for i in df.index:
    df.at[i, 'gender'] = res[i]  

df.to_csv('submission.tsv', sep='\t', header=None)

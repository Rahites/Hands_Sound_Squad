import numpy as np
import pandas as pd
import math

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from torch.utils.data import Dataset
from torch.utils.data import DataLoader

from tqdm import tqdm

def predict_word(pt_path, npy_path, update_progress_callback):
    npy = np.load(npy_path)
    batch_size = npy.shape[0] # 하나의 영상을 한 번에
    
    word_torch = torch.tensor(npy).float()
    
    test_dataset = MyDataset(word_torch)
    test_dataloader = DataLoader(test_dataset, batch_size, shuffle=True)
    
    device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    test_model = MyModel().to(device)
    
    checkpoint = torch.load(pt_path, map_location=torch.device('cpu')) #
    test_model.load_state_dict(checkpoint)
    
    total_data = len(test_dataloader.dataset)

    # predict 
    
    test_model.eval()
    with torch.no_grad():
        for batch_idx, batch_data in enumerate(test_dataloader):
            processed_data = len(batch_data)

            # 모델 입력 데이터와 레이블을 GPU 또는 CPU로 이동시킵니다.
            batch_data = batch_data.to(device)

            # 모델에 데이터를 전달하여 예측합니다.
            outputs = test_model(batch_data)

            # 확률 분포에서 최댓값을 가지는 클래스를 선택합니다.
            _, predicted = torch.max(outputs, 1)
            
            current_data_processed = test_dataloader.batch_size * batch_idx + processed_data
            progress_value = (current_data_processed / total_data) * 100
            update_progress_callback(progress_value)
    
    print(f'예측한 결과 인덱스 : {predicted}')
    # predicted에서 나온 인덱스를 가지고 예측한 라벨 출력
    label = pd.read_csv("final_words.csv")
    predict_word = label['최종단어'][predicted.cpu().numpy()[0]]
    print(f'예측한 결과 단어 : {predict_word}')
    
    return predict_word




class MyDataset(Dataset):
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

# Attention Class
class SelfAttention(nn.Module):
    def __init__(self, hidden_size):
        super(SelfAttention, self).__init__()
        self.hidden_size = hidden_size
        self.attn_weights = nn.Parameter(torch.Tensor(1, hidden_size), requires_grad=True)
    
        stdv = 1.0 / math.sqrt(self.hidden_size)
        for weight in self.attn_weights:
            nn.init.uniform_(weight, -stdv, stdv)

    def forward(self, inputs):
        # Compute attention scores
        attn_scores = torch.sum(self.attn_weights * inputs, dim=2) # LSTM 출력 그대로 받아서 계산
        
        # Compute attention weights
        attn_weights = F.softmax(attn_scores, dim=1).unsqueeze(1)
        
        # Compute weighted sum of inputs
        weighted_sum = torch.bmm(attn_weights, inputs)
        
        return weighted_sum.squeeze(1)
    
class MyModel(nn.Module):
    def __init__(self, input_size=274, hidden_layer_size=404, hidden_layer_size2=505, hidden_layer_size3=606, output_size=707, num_layers=3):
        super().__init__()
        self.lstm1 = nn.LSTM(input_size, hidden_layer_size, num_layers=num_layers, batch_first=True, dropout=0.5, bidirectional=True)
        self.lstm2 = nn.LSTM(input_size, hidden_layer_size, num_layers=num_layers, batch_first=True, dropout=0.5, bidirectional=True)
        self.lstm3 = nn.LSTM(input_size, hidden_layer_size, num_layers=num_layers, batch_first=True, dropout=0.5, bidirectional=True)

        self.attention1 = SelfAttention(hidden_layer_size * 2) # Bidirectional LSTM이므로 hidden_layer_size가 2배
        self.attention2 = SelfAttention(hidden_layer_size * 2) # Bidirectional LSTM이므로 hidden_layer_size가 2배
        self.attention3 = SelfAttention(hidden_layer_size * 2)

        self.dropout = nn.Dropout(0.5)

        self.fc1 = nn.Linear(hidden_layer_size * 2, hidden_layer_size2) # Bidirectional LSTM이므로 입력 차원이 2배
        self.residual_block = nn.Linear(hidden_layer_size * 2, hidden_layer_size3) # attn_out을 output_size로 변환하는 layer 추가

        self.fc2 = nn.Linear(hidden_layer_size2, hidden_layer_size3)
        self.fc3 = nn.Linear(hidden_layer_size3, output_size)
        

    def forward(self, input_seq):
        lstm_out1, (_, _) = self.lstm1(input_seq)
        lstm_out2, (_, _) = self.lstm2(input_seq)
        lstm_out3, (_, _) = self.lstm3(input_seq)

        attn_out1 = self.attention1(lstm_out1)
        attn_out2 = self.attention2(lstm_out2)
        attn_out3 = self.attention3(lstm_out3)

        # Multi-Head Attention
        attn_out = attn_out1 + attn_out2 + attn_out3

        out = self.fc1(attn_out)
        residual = self.residual_block(attn_out)

        out = self.dropout(out)
        out = self.fc2(out)

        # Residual connection
        out = out + residual
        out = self.dropout(out)
        out = self.fc3(out)

        return out


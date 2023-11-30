import json
import os
import numpy as np

from natsort import natsorted
from glob import glob

def collect_keypoints(file_paths):
    json_data = natsorted(glob(file_paths))
    folder_res = []
    for file_path in json_data:
        sequence_res = []
        with open(file_path,'r',encoding = 'utf-8') as file:
            json_file = json.load(file)
            # 각 keypoint 값들을 합치기
            key_list = ['face_keypoints_2d', 'pose_keypoints_2d', 'hand_left_keypoints_2d', 'hand_right_keypoints_2d']
            for key in key_list: # face_keypoints_2d, pose_keypoints_2d, hand_left_keypoints_2d, hand_right_keypoints_2d
                for idx,keypoint in enumerate(json_file['people'][0][key],start=1):
                    # confidence 값 버리기
                    if idx % 3 != 0:
                        sequence_res.append(keypoint)
        folder_res.append(sequence_res)
    return folder_res

def normalize_keypoint(keypoint_sequences):
    normalized_fold_keypoints = []
    for frame in keypoint_sequences:
        x = (frame[142],frame[148])
        y = (frame[143],frame[149])
        x_mean, x_std = np.mean(x), np.std(x)
        y_mean, y_std = np.mean(y), np.std(y)
        
        normalized_values = []
        # 정규화 진행
        for idx,value in enumerate(frame):
            if idx % 2 == 0:
                normalized_values.append(round((value - x_mean)/x_std, 5)) # round를 치는게 좋아보임
            else:
                normalized_values.append(round((value - y_mean)/y_std, 5))
        # 각 프레임마다 해당 folder로 추가
        normalized_fold_keypoints.append(normalized_values)

    return normalized_fold_keypoints

def padding_sequence(seq, length=253):

    original_array = np.array(seq)
    original_shape = original_array.shape[0]

    repeat = length - original_shape # 최대 길이보다 짧아서 반복해서 입력해야 하는 횟수
    pad_iter = (repeat // original_shape) + 1 

    if pad_iter >=2: # 길이가 2배를 넘을 때
        for i in range(pad_iter):
            # original_array = np.vstack((original_array,original_array[:repeat,:])) # 반복해야하는만큼 앞을 채워줌
            original_array = np.vstack((original_array,np.zeros([repeat, 274]))) # 반복해야하는만큼 앞을 채워줌
            if repeat - original_shape <0:
                repeat %= original_shape
            else:
                repeat -= original_shape
            
            if original_array.shape[0] == length:
                return original_array
    else:
        return np.vstack((original_array,original_array[:repeat,:]))


if __name__ == '__main__':
    # change your path
    file_name = 'use_your_video_name'
    
    file_paths = f'./export/{file_name}/*'
    
    keypoint_sequence = collect_keypoints(file_paths)
    normalized_keypoints = normalize_keypoint(np.array(keypoint_sequence))
    padding_data = []
    padding_data.append(padding_sequence(normalized_keypoints))

    np.save(f'{file_name}.npy',padding_data)
    print(f'{file_name} convert finished!!')
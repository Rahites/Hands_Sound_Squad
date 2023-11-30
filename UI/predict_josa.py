from transformers import BertForMaskedLM, AutoTokenizer, pipeline

from tqdm import tqdm
from gtts import gTTS
import playsound
import io
import os



def JOSA(lst, update_progress_callback):
    model = BertForMaskedLM.from_pretrained('klue/bert-base') #, from_pt=True)
    tokenizer = AutoTokenizer.from_pretrained('klue/bert-base')

    pipe = pipeline(
        "fill-mask",
        model=model,
        tokenizer=tokenizer
    )

    target_postpositions = ["은", "는", "이", "가", "에서", "에", "과", "와", "을", "를", "의"]
    text = '[MASK] '.join(lst)+'.'
    results = pipe(text)
    josa = []

    # 예측 결과 중에서 조사인 단어만 출력
    if text.count('MASK')==1:
        josa_ = []
        for result in results:
            predicted_word = result['token_str'].replace('##','')
            if predicted_word in target_postpositions:
                #print(f"예측된 조사: {predicted_word} (확률: {result['score']:.4f})")
                josa_.append(predicted_word)
        try: josa.append(josa_[0])
        except IndexError: josa.append('?')
    else:
        for result_ in results:
            josa_ = []
            for result in result_:
                predicted_word = result['token_str'].replace('##','')
                if predicted_word in target_postpositions:
                    #print(f"예측된 조사: {predicted_word} (확률: {result['score']:.4f})")
                    josa_.append(predicted_word)
            try: josa.append(josa_[0])
            except IndexError: josa.append('?')
            
            progress_value = (len(josa) / text.count("MASK")) * 100
            update_progress_callback(progress_value)

    if len(lst)==2:
        lst.insert(1,josa[0]+' ')
        answer = ''.join(lst)
        
    elif len(lst)==3:
        lst.insert(1,josa[0]+' ')
        lst.insert(3,josa[1]+' ')
        answer = ''.join(lst)

    # 기본 TTS mp3 저장
    tts = gTTS(answer, lang='ko', slow=False)

    #mp3_fp = io.BytesIO()
    #tts.write_to_fp(mp3_fp)
    
    mp3_save_path = r'./tts/'
    
    if not os.path.exists(mp3_save_path):
        os.makedirs(mp3_save_path)
    # file_name = os.path.join(mp3_save_path, f'{answer}.mp3')
    file_name = os.path.join(mp3_save_path, 'result.mp3')
    
    if os.path.exists(file_name):
        os.remove(file_name)

    tts.save(file_name)

    # with open(os.path.join(mp3_save_path, f'{answer}.mp3'), "wb") as f:
    # with open(os.path.join(mp3_save_path, 'result.mp3'), "wb") as f:
        # f.write(mp3_fp.getvalue())
        
    return answer
        
def tts(mp3_path):
    playsound.playsound(mp3_path)

import os.path, glob
import re

# 파일 경로를 넣으면 -> 정답(국가 코드), 알파벳 빈도를 계산한 데이터를 리턴하는 함수
def detect_trans_lang_freq(file_path):
    
    # 파일명 획득
    name = os.path.basename(file_path)
    
    # 정답, 국가 코드 획득
    p = re.compile('^[a-z]{2,}')
    
    if p.match(name):
        lang = p.match(name).group()
    else:
        return None, None
    
    # -------------------------------------
    
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read().lower()    # 전부 읽어서 소문자로 리턴
        p = re.compile('[^a-z]')   # 정규식(알파벳 소문자만 제외)
        text = p.sub('', text)     # 소문자만 남는다.
        
    counts = [0 for n in range(26)]    # 알파벳 별 카운트를 담을 공간(리스트)
    
    limit_a = ord('a')    # 매번 반복해서 작업하니까 그냥 최초 한 번 변수로 받아서 사용
    for word in text:
        counts[ord(word) - limit_a] += 1    # 문자 한 개당 카운트 추가
    
    # 빈도수는 값이 너무 퍼져 있어서 0~1 사이로 정규화를 하겠다. -> 학습 효과가 뛰어나니까
    total_count = sum(counts)
    freq = list(map(lambda x: x / total_count, counts))
    
    return lang, freq

# train을 입력으로 넣으면 훈련용 데이터를 모두 가져온다. (<-> test)
def load_data(style='train'):
    langs = []
    freqs = []
    
    file_list = glob.glob('./ml/data/%s/*.txt' % style)
    
    for file in file_list:
        lang, freq = detect_trans_lang_freq(file)
        langs.append(lang)
        freqs.append(freq)
        
    # 딕셔너리 정적 구성으로 최종 데이터 형태를 맞춰준다. -> DataFrame 형태 고려   
    return {'labels': langs, 'freqs': freqs}

print(load_data())
print(load_data('test'))
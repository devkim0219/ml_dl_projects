from sklearn.externals import joblib
from sklearn import metrics
import json, re
import os
import sys
import urllib.request

# 1. python 3.3 이하 버전과 하위 호환을 위해서 사용
# 2. 패키지 자체를 지칭할 때 사용

# 0. 경로 -> 상수값 -> 환경변수 혹은 DB에서 획득
MODEL_PATH = './ml/service/ml/clf_model_202001161419.model'
LABEL_PATH = './ml/service/ml/clf_labels.label'

# 1. 모델 로드(1회만) -> 요청이 많아지면 컨트롤이 가능한지 체크
clf = joblib.load(MODEL_PATH)

# 2. 레이블 로드
with open(LABEL_PATH, 'r') as f:
    clf_label = json.load(f)

# 3. 예측 함수 (in: 텍스트, out: 예측결과)
def detect_lang(text):
    
    # text -> 빈도 계산
    text = text.lower()        # 1. 소문자 처리
    p = re.compile('[^a-z]')   # 2. 정규식(알파벳 소문자만 제외)
    text = p.sub('', text)     # 3. 소문자만 남는다.

    try:
        counts = [0 for n in range(26)]
        limit_a = ord('a')

        for word in text:    
            counts[ord(word) - limit_a] += 1

        total_count = sum(counts)

        freq = list(map(lambda x: x / total_count, counts))    # 정규화

        # 알고리즘에 예측 요청(데이터 주입)
        predict = clf.predict([freq])   # 입력 형태를 개발했던 형태와 동일하게 차원을 맞춘다.

        na_code = predict[0]            # 'en' or 'fr' ...
        na_str = clf_label[na_code]     # '영어', '프랑스어', ...

    except:
        na_code = 'unknown'
        na_str = '해당 언어 없음'

    # 결과를 리턴
    return na_code, na_str

# 개인별로 신청한 키
CLIENT_ID = 'VWnNJ5PgyBZhhQNaxDo8'
SECRET_KEY = 'N0qaBO5A_G'
PAPAGO_URL = "https://openapi.naver.com/v1/papago/n2mt"

'''
curl "https://openapi.naver.com/v1/papago/n2mt" \
-H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" \
-H "X-Naver-Client-Id: VWnNJ5PgyBZhhQNaxDo8" \
-H "X-Naver-Client-Secret: N0qaBO5A_G" \
-d "source=ko&target=en&text=만나서 반갑습니다." -v
'''

# 4. 번역 함수 (현재: 파파고 연동, 향후: RMM 구현)
def transfer_lang(text, na_input_code='en', na_output_code='ko'):
    print('파파고와 연동한 번역 처리 시작')

    encText = urllib.parse.quote(text)      # 한글의 URL 인코딩 처리 -> %2D... 변환처리
    data = "source={}&target={}&text={}".format(na_input_code, na_output_code, encText)  
    request = urllib.request.Request(PAPAGO_URL)            # 요청객체 생성
    request.add_header("X-Naver-Client-Id", CLIENT_ID)      # 헤더 설정
    request.add_header("X-Naver-Client-Secret", SECRET_KEY) # 헤더 설정
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))   # 요청
    rescode = response.getcode()    # 응답코드 획득

    if rescode == 200:   # 응답 성공
        return json.load(response)

    else:
        return {}

# 이 코드는 개발 시 테스트 했던 코드이다.
# 의도(개발 시) 될 때만 작동해야 한다.
if __name__ == '__main__':
    test_str = 'hello'
    
    transfer_lang(test_str)
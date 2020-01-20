# 엔트리 포인트 : 진입로, 시작점, 모든 경로법은 엔트리로부터 따진다.
# 1. 모듈 가져오기
# 플라스트 관련 모듈 가져오기
from flask import Flask, render_template, request, jsonify, redirect

# 언어감지 및 번역 모듈 가져오기
from ml import detect_lang as dl, transfer_lang as tl
from db import insert_trans_log

# 2. Flask 객체 생성
app = Flask(__name__)

# 3. 라우팅
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':        
        return render_template('index.html')
    
    else:
        input_text = request.form['input_text']
        print(input_text)

        na_code, na_str = dl(input_text)
        print(na_code, na_str)

    return jsonify({'na_code': na_code, 'na_str': na_str})

# restful
@app.route('/bsgo', methods=['GET', 'POST'])
def bsgo():
    if request.method == 'GET':
        return render_template('bsgo.html')

    else:
        
        # 전달된 데이터 획득
        oriText = request.form.get('o')     # 내용이 들어있고, 100글자 이상이다.

        # 언어감지
        na_code, na_str = dl(oriText)

        # 결과를 응답
        if na_code:
            res = {
                'code': na_code,
                'code_str': na_str
            }

        else:
            res = {
                'code': '0',
                'code_str': '해당 언어 없음'
            }

        return jsonify(res)

# 번역 처리
@app.route('/transfer', methods=['POST'])
def transfer():

    # 데이터 획득
    oriText = request.form.get('o')
    na = request.form.get('na')

    # 번역
    res = tl(oriText, na)
    print(res)

    # 로그 처리
    tCode = res['message']['result']['tarLangType']
    tStc = res['message']['result']['translatedText']

    # 접속 오류 가능성만 있음
    try:
        insert_trans_log(na, tCode, oriText, tStc)

    except:
        pass

    # 응답
    return jsonify(res)

# 4. 서버 가동
if __name__ == '__main__':
    app.run(debug=True)
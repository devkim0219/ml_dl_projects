# 엔트리 포인트 : 진입로, 시작점, 모든 경로법은 엔트리로부터 따진다.
# 1. 모듈 가져오기
from flask import Flask, render_template, request, jsonify, redirect
from ml.mod import PI
from ml import PI2, predict_lang

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

        lang = predict_lang(input_text)
        print(lang)

        return jsonify({'na': lang[0]})

# 4. 서버 가동
if __name__ == '__main__':
    app.run(debug=True)
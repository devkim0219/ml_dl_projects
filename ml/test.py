# 모듈 가져오기
import re
import os.path, glob

### 데이터 준비 ###

# 데이터를 모두 읽어들인다. -> 파일 목록이 필요
# glob: 특정 패턴을 부여해서 특정 위치의 파일 목록을 가져온다.
file_list = glob.glob('./ml/data/train/*.txt')
# print(file_list)

fNames = [os.path.basename(fName) for fName in file_list]
# print(fNames)

p = re.compile('[^a-zA-Z]*')

alp_cnt = dict()

for file_path in file_list:
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
        tmp = p.sub('', text).lower()

        for alp in tmp:
            if alp not in alp_cnt.keys():
                alp_cnt[alp] = 1
            else:
                alp_cnt[alp] = alp_cnt[alp] + 1

tot_cnt = 0

for cnt in alp_cnt.values():
    tot_cnt += cnt

alp_cnt['total'] = tot_cnt

print(alp_cnt)
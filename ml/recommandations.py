critics = {
    'Lisa Rose': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'Superman Returns': 3.5,
        'You, Me and Dupree': 2.5,
        'The Night Listener': 3.0
    },

    'Gene Seymour': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 1.5,
        'Superman Returns': 5.0,
        'The Night Listener': 3.0,
        'You, Me and Dupree': 3.5
    },

    'Michael Phillips': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.5,
        'Superman Returns': 3.5,
        'The Night Listener': 4.0
    },

    'Claudia Puig': {
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'The Night Listener': 4.5,
        'Superman Returns': 4.0,
        'You, Me and Dupree': 2.5
    },

    'Mick LaSalle': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'Just My Luck': 2.0,
        'Superman Returns': 3.0,
        'The Night Listener': 3.0,
        'You, Me and Dupree': 2.0
    },

    'Jack Mattheuws': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'The Night Listener': 3.0,
        'Superman Returns': 5.0,
        'You, Me and Dupree': 3.5
    },

    'Toby': {
        'Snakes on a Plane': 4.5,
        'You, Me and Dupree': 1.0,
        'Superman Returns': 4.0
    }
}

# Euclidean Distance
def sim_distance(prefs, person1, person2):
    # 공통 항목 추출
    si = dict()

    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    # 공통 평가 항목이 없는 경우 0 리턴
    if len(si) == 0: return 0

    # person1의 item이 person2에서도 존재한다면, person1과 person2의 item 평점 차이의 제곱한 값을 더한 후 제곱 근을 계산
    sum_of_squares = sum([(prefs[person1][item] - prefs[person2][item])**2 for item in prefs[person1] if item in prefs[person2]])

    return 1/(1+sqrt(sum_of_squares))

# Pearson correlation coefficient
def sim_pearson(prefs, p1, p2):
    # 같이 평가한 항목들의 목록을 구함
    si = dict()

    for item in prefs[p1]:
        if item in prefs[p2]: si[item] = 1

    # 공통 항목 개수
    n = len(si)

    # 공통 항목이 없으면 0 리턴
    if n==0: return 0

    # 모든 선호도를 합산
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])

    # 제곱의 합을 계산
    sum1Sq = sum([(prefs[p1][it])**2 for it in si])
    sum2Sq = sum([(prefs[p2][it])**2 for it in si])

    # 곱의 합을 계산
    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])

    # 피어슨 점수 계산
    num = pSum - (sum1*sum2/n)
    den = sqrt((sum1Sq-pow(sum1,2)/n) * (sum2Sq-pow(sum2,2)/n))
    if den==0: return 0

    r = num/den

    return r
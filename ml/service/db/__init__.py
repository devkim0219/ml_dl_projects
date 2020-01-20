import pymysql

def insert_trans_log(oCode, tCode, oStr, tStc):

    # 차후 DB쪽 연결은 pooling 이나 ORM 방식을 이용하여 최대 동접에 대한 안정적인 처리를 
    # 구현한다. 현재는 그냥 요청하면 접속, 쿼리, 접속해제 순으로 처리
    # 해당 접속법은 임시적이다.
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='1234',
                                db='py_db',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    try:
        # 쿼리
        with connection.cursor() as cursor:
        
            # 쿼리문
            sql = '''
            INSERT INTO `py_db`.`tbl_trans_lang_log` 
                (`oCode`, `tCode`, `oStr`, `tStc`) 
            VALUES 
                (%s, %s, %s, %s);
            '''

            # 쿼리수행
            cursor.execute(sql, (oCode, tCode, oStr, tStc))

        # 커밋 수행(DB에 실제 반영)
        connection.commit()
        
    except Exception as e:
        print(e)

    finally:
        if connection:
            connection.close()
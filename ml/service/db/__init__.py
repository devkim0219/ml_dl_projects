import pymysql

def connect_db(oCode, tCode, oStr, tStc):
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
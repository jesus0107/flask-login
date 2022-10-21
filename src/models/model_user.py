from entities.user import User
class ModelUser:

    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, username, password, fullname FROM flask_login.users WHERE username = {}".format(user.username)
            cursor.execute(sql)
            data = cursor.fetchone()
            if data != None:
                user = User(data[0], data[1], User.check_password(data[2], user.password), data[3])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
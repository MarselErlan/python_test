
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("violet")

tess.penup()
size = 1
for i in range(88):
   tess.stamp()
   size = size + 7
   tess.forward(size)
   tess.left(99)
wn.mainloop()



# import sqlite3
# from random import randint
#
#
#
# database_1 = sqlite3.connect('server.sqlite3')
# sql = database_1.cursor()
#
# sql.execute(
#     """
#     CREATE TABLE  IF NOT EXISTS users (
#     login TEXT,S
#     password TEXT,
#     cash INT
#     )
#     """
# )
# database_1.commit()
#
#
# def register_user():
#     enter_user()
#     global user_login, user_password, balance
#     user_login = input('Login:')
#     user_password = input('Password:')
#     number = randint(1, 2)
#
#
#     for i in sql.execute(f"SELECT cash FROM users WHERE login = '{user_login}'"):
#         balance = i[0]
#
#     sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
#     if sql.fetchone() is None:
#         sql.execute(f"INSERT INTO users VALUES (?, ?, ?)", (user_login, user_password, 0))
#         database_1.commit()
#         print('User registered')
#         for value in sql.execute("SELECT * FROM users "):
#             print(value)
#     else:
#         if number == 1:
#             sql.execute(f"UPDATE users SET cash = {120 + balance} WHERE login = '{user_login}'")
#             print('You win money!')
#             database_1.commit()
#
#         # print('Usernsame already exists! Choose another one')
#             for value in sql.execute('SELECT * FROM users'):
#                 print(value)
#         else:
#             print('You lose')
#             delete_user()
#             for value in sql.execute('SELECT * FROM users'):
#                 print(value)
#
# def delete_user():
#     sql.execute(f"DELETE FROM users WHERE login = '{user_login}'")
#     database_1.commit()
#     print('User deleted')
#
#
# def enter_user():
#     print('Welcome to the Fortune')
#     sql.execute(f"SELECT login, cash FROM users")
#     row = sql.fetchall()
#     print(row)
#
# if __name__=='__main__':
#     register_user()

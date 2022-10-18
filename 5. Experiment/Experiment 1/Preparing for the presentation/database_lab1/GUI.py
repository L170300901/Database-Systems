import tkinter as tk  # 导入 Tkinter 库
from tkinter import *
import pymysql
#root = Tk()


global db


def birthInYangzhou():
    win = tk.Tk()
    win.title('001')
    win.geometry('400x90')

    # 비밀번호 입력 창
    tk.Label(win, text="请输入密码：").grid(row=0)
    tk.Label(win, text="密码：").grid(row=1)
    e2 = tk.Entry(win, show='*')
    e2.grid(row=1, column=1, padx=10, pady=5)
    global conn

    def read_inf():
        ass = "\"" + str(e2.get()) + "\""

        if(ass == "\"1234\""):
            print("success(성공)")
            win.destroy()
            hongbaoshu()
        else:
            # 비밀번호 오류시
            winson = tk.Tk()
            tk.Label(winson, text="密码错误").grid(row=0)

    # 로그인, 취소 버튼
    tk.Button(win, text='登录', width=10, command=read_inf).grid(
        row=0, column=2, sticky="w", padx=10, pady=5)
    tk.Button(win, text='退出', width=10, command=win.destroy).grid(
        row=1, column=2, sticky="w", padx=10, pady=5)
    win.mainloop()


def openchar1():
    db = pymysql.connect(host="localhost", user="root",
                         password="1234", port=3306, db='mydbtrain')
    win = tk.Tk()
    win.title('铁路局')
    win.geometry('626x417')

    def search():
        winson = tk.Tk()
        cur = db.cursor()
        e1 = tk.Entry(winson)
        e1.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        e2 = tk.Entry(winson)
        e2.grid(row=1, column=0, sticky="w", padx=10, pady=5)

        def insee1():
            strr = " SELECT * from railwaybeureau where id = "+e1.get()+";"
            print(strr)
            cur.execute(strr)
            lis = cur.fetchall()
            if(len(lis) != 0):
                winsonson = tk.Tk()
                tk.Label(winsonson, text=str("铁路局编号")).grid(
                    row=1, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("铁路局名称")).grid(
                    row=2, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("所在城市")).grid(
                    row=3, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("辖车站个数")).grid(
                    row=4, column=0, padx=5, pady=5)
                for i in range(len(lis[0])):
                    tk.Label(winsonson, text=str(lis[0][i])).grid(
                        row=i+1, column=1, padx=10, pady=5)
            else:
                winsonson = tk.Tk()
                tk.Label(winsonson, text="no findings").grid(row=0)

        def insee2():
            strr = " SELECT * from railwaybeureau where city = "+"'"+e2.get()+"'"+";"
            print(strr)
            cur.execute(strr)
            lis = cur.fetchall()
            if (len(lis) != 0):
                winsonson = tk.Tk()
                tk.Label(winsonson, text=str("铁路局编号")).grid(
                    row=1, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("铁路局名称")).grid(
                    row=2, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("所在城市")).grid(
                    row=3, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("辖车站个数")).grid(
                    row=4, column=0, padx=5, pady=5)
                for j in range(len(lis)):
                    for i in range(len(lis[0])):
                        tk.Label(winsonson, text=str(lis[j][i])).grid(
                            row=i+1, column=1+j, padx=10, pady=5)
            else:
                winsonson = tk.Tk()
                tk.Label(winsonson, text="no findings").grid(row=0)
        tk.Button(winson, text=str("id查询"), command=insee1).grid(
            row=0, column=1, padx=10, pady=5)
        tk.Button(winson, text=str("城市查询"), command=insee2).grid(
            row=1, column=1, padx=10, pady=5)

    def insert():
        winson = tk.Tk()
        e1 = tk.Entry(winson)
        e1.grid(row=1, column=1, padx=20, pady=5)
        e2 = tk.Entry(winson)
        e2.grid(row=2, column=1, padx=20, pady=5)
        e3 = tk.Entry(winson)
        e3.grid(row=3, column=1, padx=20, pady=5)
        tk.Label(winson, text=str("请输入信息")).grid(
            row=0, column=0, padx=10, pady=5)
        tk.Label(winson, text=str("铁路局编号")).grid(
            row=1, column=0, padx=5, pady=5)
        tk.Label(winson, text=str("铁路局名称")).grid(
            row=2, column=0, padx=5, pady=5)
        tk.Label(winson, text=str("所在城市")).grid(
            row=3, column=0, padx=5, pady=5)
        cur = db.cursor()

        def insee():
            strr = " SELECT * from railwaybeureau where id = " + e1.get() + ";"
            print(strr)
            cur.execute(strr)
            lis = cur.fetchall()
            if (len(lis) != 0):
                winsonson = tk.Tk()
                tk.Label(winsonson, text="error::this primary key has already exsisted").grid(
                    row=0)
            else:
                instr = "INSERT INTO railwaybeureau (id, name ,city) VALUES ("+e1.get(
                )+"," + "'" + e2.get() + "'" + "," + "'" + e3.get() + "'"+");"
                cur.execute(instr)
                winson.destroy()
            db.commit()
        tk.Button(winson, text='confirm', width=10, command=insee).grid(
            row=0, column=1, sticky="w", padx=10, pady=5)

    def listall():
        '''
        winson2 = tk.Tk()
        scr = Scrollbar(winson2)
        lb = Listbox(winson2)
        scr.config(command=lb.yview)
        lb.config(yscrollcommand=scr.set)
        '''
        ss = "ss"
        cur = db.cursor()
        cur.execute(" SELECT * from railwaybeureau;")
        lis = cur.fetchall()
        ss = []
        tk.Label(win, text=str("铁路局编号")).grid(row=2, column=0, padx=5, pady=5)
        tk.Label(win, text=str("铁路局名称")).grid(row=2, column=1, padx=5, pady=5)
        tk.Label(win, text=str("所在城市")).grid(row=2, column=2, padx=5, pady=5)
        tk.Label(win, text=str("下辖车站个数")).grid(row=2, column=3, padx=5, pady=5)
        for i in range(len(lis)):
            for j in range(len((lis[0]))):
                ss.append(lis[i][j])
                tk.Label(win, text=str(lis[i][j])).grid(
                    row=3+i, column=j, padx=5, pady=5)

    def change():
        cur = db.cursor()
        winson = tk.Tk()
        tk.Label(winson, text="输入id").grid(row=0)
        ee = tk.Entry(winson)
        ee.grid(row=1, column=1, padx=20, pady=5)

        def insee2():
            cur.execute(
                "SELECT * from railwaybeureau where id =" + ee.get() + ";")
            finding = cur.fetchall()
            if len(finding) == 0:
                winson = tk.Tk()
                tk.Label(winson, text="no findings").grid(row=0)
            else:
                winson = tk.Tk()
                tk.Label(winson, text="输入新的信息值").grid(row=0)
                tk.Label(winson, text="id").grid(
                    row=1, column=0, padx=10, pady=5)
                tk.Label(winson, text="name").grid(
                    row=2, column=0, padx=10, pady=5)
                tk.Label(winson, text="city").grid(
                    row=3, column=0, padx=10, pady=5)
                e1 = tk.Entry(winson)
                e1.grid(row=1, column=1, padx=20, pady=5)
                e2 = tk.Entry(winson)
                e2.grid(row=2, column=1, padx=20, pady=5)
                e3 = tk.Entry(winson)
                e3.grid(row=3, column=1, padx=20, pady=5)

                def insee():
                    instr = "UPDATE railwaybeureau SET id = "+e1.get()+", name=" + "'" + e2.get() + \
                        "'" + " ,city = "+"'"+e3.get()+"'"+" WHERE id = "+ee.get()+";"
                    # print(instr)
                    cur.execute(instr)
                    winson.destroy()
                    db.commit()

                tk.Button(winson, text='confirm', width=10, command=insee).grid(
                    row=0, column=1, sticky="w", padx=10, pady=5)

        db.commit()
        tk.Button(winson, text='confirm', width=10, command=insee2).grid(
            row=0, column=1, sticky="w", padx=10, pady=5)

    def deletea():
        cur = db.cursor()
        winson = tk.Tk()
        tk.Label(winson, text="输入id").grid(row=0)
        ee = tk.Entry(winson)
        ee.grid(row=1, column=1, padx=20, pady=5)

        def insee2():
            cur.execute(
                "SELECT * from railwaybeureau where id =" + ee.get() + ";")
            finding = cur.fetchall()
            if len(finding) == 0:
                winson = tk.Tk()
                tk.Label(winson, text="no findings").grid(row=0)
            else:
                winson2 = tk.Tk()
                tk.Label(winson2, text="确认让它消失了吗？").grid(row=0)

                def insee():
                    instr = "DELETE FROM railwaybeureau WHERE id = "+ee.get()+";"
                    print(instr)
                    cur.execute(instr)
                    db.commit()
                    winson2.destroy()

                tk.Button(winson2, text='confirm', width=10, command=insee).grid(
                    row=1, column=0, sticky="w", padx=10, pady=5)
                tk.Button(winson2, text='no', width=10, command=winson2.destroy).grid(
                    row=1, column=2, sticky="w", padx=10, pady=5)
                db.commit()

        db.commit()
        tk.Button(winson, text='confirm', width=10, command=insee2).grid(
            row=0, column=1, sticky="w", padx=10, pady=5)

    tk.Button(win, text='查找', width=10, command=search).grid(
        row=1, column=0, sticky="w", padx=10, pady=5)
    tk.Button(win, text='列表', width=10, command=listall).grid(
        row=1, column=1, sticky="w", padx=10, pady=5)
    tk.Button(win, text='插入', width=10, command=insert).grid(
        row=1, column=2, sticky="w", padx=10, pady=5)
    tk.Button(win, text='修改', width=10, command=change).grid(
        row=1, column=3, sticky="w", padx=10, pady=5)
    tk.Button(win, text='删除', width=10, command=deletea).grid(
        row=1, column=4, sticky="w", padx=10, pady=5)
    cur = db.cursor()
    cur.execute(" SELECT * from railwaybeureau;")
    lis = cur.fetchall()
    for i in range(len(lis)):
        strr = " SELECT * from trainstation where upbeureau = " + \
            str(lis[i][0]) + ";"
        cur.execute(strr)
        liss = cur.fetchall()
        instr = "UPDATE railwaybeureau SET id = " + str(lis[i][0]) + ", name=" + "'" + str(lis[i][1]) + "'" + " ,city = " + "'" + str(
            lis[i][2]) + "'" + " ,numberofstation = " + str(len(liss)) + " WHERE id = " + str(lis[i][0]) + ";"
        # print(instr)
        cur.execute(instr)
    db.commit()
    win.mainloop()


def openchar2():
    db = pymysql.connect(host="localhost", user="root",
                         password="1234", port=3306, db='mydbtrain')
    win = tk.Tk()
    win.title('火车站')
    win.geometry('626x417')

    def search():
        winson = tk.Tk()
        cur = db.cursor()
        e1 = tk.Entry(winson)
        e1.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        e2 = tk.Entry(winson)
        e2.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        e3 = tk.Entry(winson)
        e3.grid(row=2, column=0, sticky="w", padx=10, pady=5)

        def insee1():
            strr = " SELECT * from trainstation where name = "+"'"+e1.get()+"'"+";"
            print(strr)
            cur.execute(strr)
            lis = cur.fetchall()
            if(len(lis) != 0):
                winsonson = tk.Tk()
                tk.Label(winsonson, text=str("车站")).grid(
                    row=1, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("城市")).grid(
                    row=2, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("所属铁路局id")).grid(
                    row=3, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("所属铁路局")).grid(
                    row=4, column=0, padx=5, pady=5)
                strr = " SELECT * from railwaybeureau where id = " + \
                    str(lis[0][2]) + ";"
                cur.execute(strr)
                print(strr)
                liss = cur.fetchall()
                tk.Label(winsonson, text=str(liss[0][1])).grid(
                    row=4, column=1, padx=5, pady=5)
                for i in range(len(lis[0])):
                    tk.Label(winsonson, text=str(lis[0][i])).grid(
                        row=i+1, column=1, padx=10, pady=5)
            else:
                winsonson = tk.Tk()
                tk.Label(winsonson, text="no findings").grid(row=0)

        def insee2():
            strr = " SELECT * from trainstation where city = "+"'"+e2.get()+"'"+";"
            print(strr)
            cur.execute(strr)
            lis = cur.fetchall()
            if (len(lis) != 0):
                winsonson = tk.Tk()
                tk.Label(winsonson, text=str("车站")).grid(
                    row=1, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("城市")).grid(
                    row=2, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("所属铁路局id")).grid(
                    row=3, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("所属铁路局")).grid(
                    row=4, column=0, padx=5, pady=5)
                for j in range(len(lis)):
                    strr = " SELECT * from railwaybeureau where id = " + \
                        str(lis[j][2]) + ";"
                    cur.execute(strr)
                    liss = cur.fetchall()
                    tk.Label(winsonson, text=str(liss[0][1])).grid(
                        row=4, column=1+j, padx=5, pady=5)
                    for i in range(len(lis[0])):
                        tk.Label(winsonson, text=str(lis[j][i])).grid(
                            row=i+1, column=1+j, padx=10, pady=5)
            else:
                winsonson = tk.Tk()
                tk.Label(winsonson, text="no findings").grid(row=0)

        def insee3():
            strr = " SELECT * from trainstation where upbeureau = "+e3.get()+";"
            print(strr)
            cur.execute(strr)
            lis = cur.fetchall()
            if (len(lis) != 0):
                winsonson = tk.Tk()
                tk.Label(winsonson, text=str("车站")).grid(
                    row=1, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("城市")).grid(
                    row=2, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("所属铁路局id")).grid(
                    row=3, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("所属铁路局")).grid(
                    row=4, column=0, padx=5, pady=5)
                for j in range(len(lis)):
                    strr = " SELECT * from railwaybeureau where id = " + \
                        str(lis[j][2]) + ";"
                    cur.execute(strr)
                    liss = cur.fetchall()
                    tk.Label(winsonson, text=str(liss[0][1])).grid(
                        row=4, column=1 + j, padx=5, pady=5)
                    for i in range(len(lis[0])):
                        tk.Label(winsonson, text=str(lis[j][i])).grid(
                            row=i+1, column=1+j, padx=10, pady=5)
            else:
                winsonson = tk.Tk()
                tk.Label(winsonson, text="no findings").grid(row=0)
        tk.Button(winson, text=str("车站查询"), command=insee1).grid(
            row=0, column=1, padx=10, pady=5)
        tk.Button(winson, text=str("城市查询"), command=insee2).grid(
            row=1, column=1, padx=10, pady=5)
        tk.Button(winson, text=str("铁路局查询"), command=insee3).grid(
            row=2, column=1, padx=10, pady=5)

    def insert():
        winson = tk.Tk()
        e1 = tk.Entry(winson)
        e1.grid(row=1, column=1, padx=20, pady=5)
        e2 = tk.Entry(winson)
        e2.grid(row=2, column=1, padx=20, pady=5)
        e3 = tk.Entry(winson)
        e3.grid(row=3, column=1, padx=20, pady=5)
        tk.Label(winson, text=str("请输入信息")).grid(
            row=0, column=0, padx=10, pady=5)
        tk.Label(winson, text=str("车站")).grid(row=1, column=0, padx=5, pady=5)
        tk.Label(winson, text=str("城市")).grid(row=2, column=0, padx=5, pady=5)
        tk.Label(winson, text=str("所属铁路局id")).grid(
            row=3, column=0, padx=5, pady=5)
        cur = db.cursor()

        def insee():
            strr = " SELECT * from trainstation where name = " + "'"+e1.get() + "'"+";"
            cur.execute(strr)
            lis = cur.fetchall()
            if (len(lis) != 0):
                winsonson = tk.Tk()
                tk.Label(winsonson, text="error::this primary key has already exsisted").grid(
                    row=0)
            else:
                strr = " SELECT * from railwaybeureau where id = " + e3.get() + ";"
                cur.execute(strr)
                liss = cur.fetchall()
                if(len(liss) == 0):
                    winsonson = tk.Tk()
                    tk.Label(winsonson, text="error::not avaliable beureau id").grid(
                        row=0)
                else:
                    instr = "INSERT INTO trainstation (name, city, upbeureau) VALUES ("+"'"+e1.get(
                    )+"'"+"," + "'" + e2.get() + "'" + "," + e3.get() + ");"
                    print(instr)
                    cur.execute(instr)
                    winson.destroy()
            db.commit()
        tk.Button(winson, text='confirm', width=10, command=insee).grid(
            row=0, column=1, sticky="w", padx=10, pady=5)

    def listall():
        '''
        winson2 = tk.Tk()
        scr = Scrollbar(winson2)
        lb = Listbox(winson2)
        scr.config(command=lb.yview)
        lb.config(yscrollcommand=scr.set)
        '''
        ss = "ss"
        cur = db.cursor()
        cur.execute(" SELECT * from trainstation;")
        lis = cur.fetchall()
        ss = []
        tk.Label(win, text=str("车站")).grid(row=2, column=0, padx=5, pady=5)
        tk.Label(win, text=str("城市")).grid(row=2, column=1, padx=5, pady=5)
        tk.Label(win, text=str("所属铁路局id")).grid(
            row=2, column=2, padx=5, pady=5)
        tk.Label(win, text=str("所属铁路局")).grid(row=2, column=3, padx=5, pady=5)
        for i in range(len(lis)):
            strr = " SELECT * from railwaybeureau where id = " + \
                str(lis[i][2]) + ";"
            cur.execute(strr)
            liss = cur.fetchall()
            tk.Label(win, text=str(liss[0][1])).grid(
                row=3+i, column=3, padx=5, pady=5)
            for j in range(len((lis[0]))):
                ss.append(lis[i][j])
                tk.Label(win, text=str(lis[i][j])).grid(
                    row=3+i, column=j, padx=5, pady=5)

    def change():
        cur = db.cursor()
        winson = tk.Tk()
        tk.Label(winson, text="输入id").grid(row=0)
        ee = tk.Entry(winson)
        ee.grid(row=1, column=1, padx=20, pady=5)

        def insee2():
            cur.execute("SELECT * from trainstation where name =" +
                        "'" + ee.get() + "'"+";")
            finding = cur.fetchall()
            if len(finding) == 0:
                winson = tk.Tk()
                tk.Label(winson, text="no findings").grid(row=0)
            else:
                winson = tk.Tk()
                tk.Label(winson, text="输入新的信息值").grid(row=0)
                tk.Label(winson, text="name").grid(
                    row=1, column=0, padx=10, pady=5)
                tk.Label(winson, text="city").grid(
                    row=2, column=0, padx=10, pady=5)
                tk.Label(winson, text="beureauid").grid(
                    row=3, column=0, padx=10, pady=5)
                e1 = tk.Entry(winson)
                e1.grid(row=1, column=1, padx=20, pady=5)
                e2 = tk.Entry(winson)
                e2.grid(row=2, column=1, padx=20, pady=5)
                e3 = tk.Entry(winson)
                e3.grid(row=3, column=1, padx=20, pady=5)

                def insee():
                    instr = "UPDATE trainstation SET upbeureau = "+e3.get()+", city=" + "'" + e2.get() + \
                        "'" + " ,name = "+"'"+e1.get()+"'"+" WHERE name = "+"'"+ee.get()+"'"+";"
                    print(instr)
                    cur.execute(instr)
                    winson.destroy()
                    db.commit()

                tk.Button(winson, text='confirm', width=10, command=insee).grid(
                    row=0, column=1, sticky="w", padx=10, pady=5)

        db.commit()
        tk.Button(winson, text='confirm', width=10, command=insee2).grid(
            row=0, column=1, sticky="w", padx=10, pady=5)

    def deletea():
        cur = db.cursor()
        winson = tk.Tk()
        tk.Label(winson, text="输入id").grid(row=0)
        ee = tk.Entry(winson)
        ee.grid(row=1, column=1, padx=20, pady=5)

        def insee2():
            cur.execute("SELECT * from trainstation where name =" +
                        "'"+ee.get() + "'"+";")
            finding = cur.fetchall()
            if len(finding) == 0:
                winson = tk.Tk()
                tk.Label(winson, text="no findings").grid(row=0)
            else:
                winson2 = tk.Tk()
                tk.Label(winson2, text="确认让它消失了吗？").grid(row=0)

                def insee():
                    instr = "DELETE FROM trainstation WHERE name = "+"'"+ee.get()+"'"+";"
                    print(instr)
                    cur.execute(instr)
                    db.commit()
                    winson2.destroy()

                tk.Button(winson2, text='confirm', width=10, command=insee).grid(
                    row=1, column=0, sticky="w", padx=10, pady=5)
                tk.Button(winson2, text='no', width=10, command=winson2.destroy).grid(
                    row=1, column=2, sticky="w", padx=10, pady=5)
                db.commit()

        db.commit()
        tk.Button(winson, text='confirm', width=10, command=insee2).grid(
            row=0, column=1, sticky="w", padx=10, pady=5)

    tk.Button(win, text='查找', width=10, command=search).grid(
        row=1, column=0, sticky="w", padx=10, pady=5)
    tk.Button(win, text='列表', width=10, command=listall).grid(
        row=1, column=1, sticky="w", padx=10, pady=5)
    tk.Button(win, text='插入', width=10, command=insert).grid(
        row=1, column=2, sticky="w", padx=10, pady=5)
    tk.Button(win, text='修改', width=10, command=change).grid(
        row=1, column=3, sticky="w", padx=10, pady=5)
    tk.Button(win, text='删除', width=10, command=deletea).grid(
        row=1, column=4, sticky="w", padx=10, pady=5)
    win.mainloop()


def openchar3():
    db = pymysql.connect(host="localhost", user="root",
                         password="1234", port=3306, db='mydbtrain')
    win = tk.Tk()
    win.title('站台')
    win.geometry('626x417')

    def search():
        winson = tk.Tk()
        cur = db.cursor()
        e1 = tk.Entry(winson)
        e1.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        e2 = tk.Entry(winson)
        e2.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        e3 = tk.Entry(winson)
        e3.grid(row=2, column=0, sticky="w", padx=10, pady=5)

        def insee1():
            strr = " SELECT * from platform where stationbelong = " + "'" + e1.get() + \
                "'" + ";"
            print(strr)
            cur.execute(strr)
            lis = cur.fetchall()
            if (len(lis) != 0):
                winsonson = tk.Tk()
                tk.Label(winsonson, text=str("id")).grid(
                    row=1, column=0, padx=3, pady=5)
                tk.Label(winsonson, text=str("车站")).grid(
                    row=2, column=0, padx=3, pady=5)
                tk.Label(winsonson, text=str("长度")).grid(
                    row=3, column=0, padx=3, pady=5)
                tk.Label(winsonson, text=str("类型")).grid(
                    row=4, column=0, padx=3, pady=5)
                for j in range(len(lis)):
                    for i in range(len(lis[0])):
                        tk.Label(winsonson, text=str(lis[j][i])).grid(
                            row=i + 1, column=j + 1, padx=3, pady=5)
            else:
                winsonson = tk.Tk()
                tk.Label(winsonson, text="no findings").grid(row=0)

        def insee2():
            strr = " SELECT * from platform where stationbelong = " + \
                "'" + e1.get() + "'" + "and kind = 'side' " + ";"
            print(strr)
            cur.execute(strr)
            lis = cur.fetchall()
            if (len(lis) != 0):
                winsonson = tk.Tk()
                tk.Label(winsonson, text=str("id")).grid(
                    row=1, column=0, padx=3, pady=5)
                tk.Label(winsonson, text=str("车站")).grid(
                    row=2, column=0, padx=3, pady=5)
                tk.Label(winsonson, text=str("长度")).grid(
                    row=3, column=0, padx=3, pady=5)
                tk.Label(winsonson, text=str("类型")).grid(
                    row=4, column=0, padx=3, pady=5)
                for j in range(len(lis)):
                    for i in range(len(lis[0])):
                        tk.Label(winsonson, text=str(lis[j][i])).grid(
                            row=i + 1, column=j + 1, padx=3, pady=5)
            else:
                winsonson = tk.Tk()
                tk.Label(winsonson, text="no findings").grid(row=0)

        def insee3():
            strr = " SELECT * from platform where stationbelong = " + \
                "'" + e1.get() + "'" + "and kind = 'island' " + ";"
            print(strr)
            cur.execute(strr)
            lis = cur.fetchall()
            if (len(lis) != 0):
                winsonson = tk.Tk()
                tk.Label(winsonson, text=str("id")).grid(
                    row=1, column=0, padx=3, pady=5)
                tk.Label(winsonson, text=str("车站")).grid(
                    row=2, column=0, padx=3, pady=5)
                tk.Label(winsonson, text=str("长度")).grid(
                    row=3, column=0, padx=3, pady=5)
                tk.Label(winsonson, text=str("类型")).grid(
                    row=4, column=0, padx=3, pady=5)
                for j in range(len(lis)):
                    for i in range(len(lis[0])):
                        tk.Label(winsonson, text=str(lis[j][i])).grid(
                            row=i + 1, column=j + 1, padx=3, pady=5)
            else:
                winsonson = tk.Tk()
                tk.Label(winsonson, text="no findings").grid(row=0)

        tk.Button(winson, text=str("车站站台查询"), command=insee1).grid(
            row=0, column=1, padx=10, pady=5)
        tk.Button(winson, text=str("车站边式站台查询"), command=insee2).grid(
            row=1, column=1, padx=10, pady=5)
        tk.Button(winson, text=str("车站岛式站台查询"), command=insee3).grid(
            row=2, column=1, padx=10, pady=5)

    def insert():
        winson = tk.Tk()
        e1 = tk.Entry(winson)
        e1.grid(row=1, column=1, padx=20, pady=5)
        e2 = tk.Entry(winson)
        e2.grid(row=2, column=1, padx=20, pady=5)
        e3 = tk.Entry(winson)
        e3.grid(row=3, column=1, padx=20, pady=5)
        e4 = tk.Entry(winson)
        e4.grid(row=4, column=1, padx=20, pady=5)
        tk.Label(winson, text=str("请输入信息")).grid(
            row=0, column=0, padx=10, pady=5)
        tk.Label(winson, text=str("站台号")).grid(row=1, column=0, padx=5, pady=5)
        tk.Label(winson, text=str("车站")).grid(row=2, column=0, padx=5, pady=5)
        tk.Label(winson, text=str("长度")).grid(row=4, column=0, padx=5, pady=5)
        tk.Label(winson, text=str("类型")).grid(row=3, column=0, padx=5, pady=5)
        cur = db.cursor()

        def insee():
            strr = " SELECT * from trainstation where name = " + "'" + e2.get() + "'" + ";"
            cur.execute(strr)
            liss = cur.fetchall()
            if (len(liss) == 0):
                winsonson = tk.Tk()
                tk.Label(winsonson, text="error::not avaliable station").grid(
                    row=0)
            else:
                strr = " SELECT * from platform where stationbelong = " + \
                    "'" + e2.get() + "'" + " and id = " + e1.get() + ";"
                cur.execute(strr)
                liss = cur.fetchall()
                if(len(liss) != 0):
                    winsonson = tk.Tk()
                    tk.Label(winsonson, text="error::exsisting platform").grid(
                        row=0)
                else:
                    if(e3.get() != 'island' and e3.get() != 'side'):
                        winsonson = tk.Tk()
                        tk.Label(winsonson, text="error::not avaliable kind").grid(
                            row=0)
                    else:
                        instr = "INSERT INTO platform  VALUES (" + e1.get() + "," + "'" + e2.get(
                        ) + "'" + "," + e4.get()+"," + "'" + e3.get() + "'" + ");"
                        print(instr)
                        cur.execute(instr)
                        winson.destroy()
            db.commit()

        tk.Button(winson, text='confirm', width=10, command=insee).grid(
            row=0, column=1, sticky="w", padx=10, pady=5)

    def change():
        cur = db.cursor()
        winson = tk.Tk()
        tk.Label(winson, text="输入车站").grid(row=0, column=1)
        tk.Label(winson, text="输入站台号").grid(row=0, column=2)
        ee1 = tk.Entry(winson)
        ee1.grid(row=1, column=1, padx=20, pady=5)
        ee2 = tk.Entry(winson)
        ee2.grid(row=1, column=2, padx=20, pady=5)

        def insee2():
            strr = " SELECT * from platform where stationbelong = " + \
                "'" + ee1.get() + "'" + " and id = " + ee2.get() + ";"
            cur.execute(strr)
            liss = cur.fetchall()
            strr = " SELECT * from trainstation where name = " + "'" + ee1.get() + "'" + ";"
            cur.execute(strr)
            liss2 = cur.fetchall()
            if len(liss) == 0:
                winson = tk.Tk()
                tk.Label(winson, text="no findings train station").grid(row=0)
            elif len(liss2) == 0:
                winson = tk.Tk()
                tk.Label(winson, text="no findings platform").grid(row=0)
            else:
                winson = tk.Tk()
                tk.Label(winson, text="输入新的信息值").grid(row=0)
                tk.Label(winson, text="kind").grid(
                    row=1, column=0, padx=10, pady=5)
                tk.Label(winson, text="length").grid(
                    row=2, column=0, padx=10, pady=5)
                e1 = tk.Entry(winson)
                e1.grid(row=1, column=1, padx=20, pady=5)
                e2 = tk.Entry(winson)
                e2.grid(row=2, column=1, padx=20, pady=5)

                def insee():
                    instr = "UPDATE platform SET length = " + e2.get() + ", kind=" + "'" + e1.get() + "'" + \
                        " WHERE stationbelong = " + "'" + ee1.get() + "'" + " and id = " + ee2.get() + ";"
                    print(instr)
                    cur.execute(instr)
                    winson.destroy()
                    db.commit()

                tk.Button(winson, text='confirm', width=10, command=insee).grid(row=0, column=1, sticky="w", padx=10,
                                                                                pady=5)

        db.commit()
        tk.Button(winson, text='confirm', width=10, command=insee2).grid(
            row=3, column=1, sticky="w", padx=10, pady=5)

    def deletea():
        cur = db.cursor()
        winson = tk.Tk()
        tk.Label(winson, text="输入id").grid(row=0)
        ee = tk.Entry(winson)
        ee.grid(row=1, column=1, padx=20, pady=5)

        tk.Label(winson, text="输入车站").grid(row=2)
        ee2 = tk.Entry(winson)
        ee2.grid(row=3, column=1, padx=20, pady=5)

        def insee2():
            strr = " SELECT * from platform where stationbelong = " + \
                "'" + ee2.get() + "'" + " and id = " + ee.get() + ";"
            cur.execute(strr)
            finding = cur.fetchall()
            if len(finding) == 0:
                winson = tk.Tk()
                tk.Label(winson, text="no findings").grid(row=0)
            else:
                winson2 = tk.Tk()
                tk.Label(winson2, text="确认让它消失了吗？").grid(row=0)

                def insee():
                    instr = "DELETE FROM platform WHERE stationbelong = " + \
                        "'" + ee2.get() + "'" + " and id = " + ee.get() + ";"
                    print(instr)
                    cur.execute(instr)
                    db.commit()
                    winson2.destroy()

                tk.Button(winson2, text='confirm', width=10, command=insee).grid(row=1, column=0, sticky="w", padx=10,
                                                                                 pady=5)
                tk.Button(winson2, text='no', width=10, command=winson2.destroy).grid(row=1, column=2, sticky="w",
                                                                                      padx=10, pady=5)
                db.commit()

        db.commit()
        tk.Button(winson, text='confirm', width=10, command=insee2).grid(
            row=0, column=3, sticky="w", padx=10, pady=5)

    tk.Button(win, text='查找', width=10, command=search).grid(
        row=1, column=0, sticky="w", padx=10, pady=5)
    tk.Button(win, text='插入', width=10, command=insert).grid(
        row=1, column=1, sticky="w", padx=10, pady=5)
    tk.Button(win, text='修改', width=10, command=change).grid(
        row=1, column=2, sticky="w", padx=10, pady=5)
    tk.Button(win, text='删除', width=10, command=deletea).grid(
        row=1, column=3, sticky="w", padx=10, pady=5)
    win.mainloop()


def openchar4():
    db = pymysql.connect(host="localhost", user="root",
                         password="1234", port=3306, db='mydbtrain')
    win = tk.Tk()
    win.title('车站车次')
    win.geometry('626x417')

    def search():
        winson = tk.Tk()
        cur = db.cursor()
        e1 = tk.Entry(winson)
        e1.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        e2 = tk.Entry(winson)
        e2.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        e3 = tk.Entry(winson)
        e3.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        e4 = tk.Entry(winson)
        e4.grid(row=3, column=0, sticky="w", padx=10, pady=5)
        e5 = tk.Entry(winson)
        e5.grid(row=4, column=0, sticky="w", padx=10, pady=5)

        def insee1():
            atf2 = False
            atf3 = False
            atf4 = False
            atf5 = False
            strr = " SELECT * from trainnumber where "
            if (e1.get() != ""):
                strr += " passstation = '"+e1.get()+"' "
                atf2 = True
            if (e2.get() != ""):
                if atf2:
                    strr += "and startstation = '"+e2.get()+"' "
                else:
                    strr += "startstation = '"+e2.get()+"' "
                atf3 = True
            if (e3.get() != ""):
                if atf3 or atf2:
                    strr += "and endstation = '"+e3.get()+"' "
                else:
                    strr += "endstation = '"+e3.get()+"' "
                atf4 = True
            if (e4.get() != ""):
                if atf4 or atf3 or atf2:
                    strr += "and startdate = '"+e4.get()+"' "
                else:
                    strr += "startdate = '" + e4.get() + "' "
                atf5 = True
            if (e5.get() != ""):
                if atf5 or atf4 or atf3 or atf2:
                    strr += "and numberid = '"+e5.get()+"' "
                else:
                    strr += " numberid = '" + e5.get() + "' "
            print(strr)
            cur.execute(strr)
            lis = cur.fetchall()
            if (len(lis) != 0):
                winsonson = tk.Tk()
                tk.Label(winsonson, text=str("车次")).grid(
                    row=1, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("日期")).grid(
                    row=2, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("始发站")).grid(
                    row=3, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("终点站")).grid(
                    row=4, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("经停站")).grid(
                    row=5, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("司机")).grid(
                    row=6, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("列车长")).grid(
                    row=7, column=0, padx=5, pady=5)

                for j in range(len(lis)):
                    for i in range(len(lis[0])):
                        if i == 5:
                            strr2 = " SELECT * from traindriver where idcard = " + \
                                "'" + str(lis[j][5]) + "'" + ";"
                            print(strr2)
                            cur.execute(strr2)

                            liss2 = cur.fetchall()
                            if(len(liss2) != 0):
                                tk.Label(winsonson, text=liss2[0][0]).grid(
                                    row=i + 1, column=1 + j, padx=3, pady=5)
                        elif i == 6:
                            strr3 = " SELECT * from traincaptain where idcard = " + \
                                "'" + str(lis[j][6]) + "'" + ";"
                            print(strr3)
                            cur.execute(strr3)
                            liss2 = cur.fetchall()
                            if (len(liss2) != 0):
                                tk.Label(winsonson, text=liss2[0][0]).grid(
                                    row=i + 1, column=1 + j, padx=3, pady=5)

                        else:
                            tk.Label(winsonson, text=str(lis[j][i])).grid(
                                row=i + 1, column=1+j, padx=3, pady=5)

            else:
                winsonson = tk.Tk()
                tk.Label(winsonson, text="no findings").grid(row=0)

        tk.Label(winson, text=str("经过车站查询")).grid(
            row=0, column=1, padx=10, pady=5)
        tk.Label(winson, text=str("始发车站查询")).grid(
            row=1, column=1, padx=10, pady=5)
        tk.Label(winson, text=str("终点车站查询")).grid(
            row=2, column=1, padx=10, pady=5)
        tk.Label(winson, text=str("日期查询")).grid(
            row=3, column=1, padx=10, pady=5)
        tk.Label(winson, text=str("车次查询")).grid(
            row=4, column=1, padx=10, pady=5)
        tk.Button(winson, text=str("查找"), command=insee1).grid(
            row=5, column=1, padx=10, pady=5)

    def insert():
        winson = tk.Tk()
        e1 = tk.Entry(winson)
        e1.grid(row=1, column=1, padx=20, pady=5)
        e2 = tk.Entry(winson)
        e2.grid(row=2, column=1, padx=20, pady=5)
        e3 = tk.Entry(winson)
        e3.grid(row=3, column=1, padx=20, pady=5)
        e4 = tk.Entry(winson)
        e4.grid(row=4, column=1, padx=20, pady=5)
        e5 = tk.Entry(winson)
        e5.grid(row=5, column=1, padx=20, pady=5)
        e6 = tk.Entry(winson)
        e6.grid(row=6, column=1, padx=20, pady=5)
        e7 = tk.Entry(winson)
        e7.grid(row=7, column=1, padx=20, pady=5)
        tk.Label(winson, text=str("请输入信息")).grid(
            row=0, column=0, padx=10, pady=5)
        tk.Label(winson, text=str("车次")).grid(row=1, column=0, padx=5, pady=5)
        tk.Label(winson, text=str("发车日期")).grid(
            row=2, column=0, padx=5, pady=5)
        tk.Label(winson, text=str("始发站")).grid(row=3, column=0, padx=5, pady=5)
        tk.Label(winson, text=str("终点站")).grid(row=4, column=0, padx=5, pady=5)
        tk.Label(winson, text=str("经停站")).grid(row=5, column=0, padx=5, pady=5)
        tk.Label(winson, text=str("司机身份证号")).grid(
            row=6, column=0, padx=5, pady=5)
        tk.Label(winson, text=str("列车长身份证号")).grid(
            row=7, column=0, padx=5, pady=5)
        cur = db.cursor()

        def insee():
            strr = " SELECT * from trainnumber where numberid = " + "'" + e1.get() + "'" + " and startdate = " + \
                "'" + e2.get() + "'" + " and passstation = " + "'" + e5.get() + "'" + ";"
            cur.execute(strr)
            lis = cur.fetchall()
            if (len(lis) != 0):
                winsonson = tk.Tk()
                tk.Label(winsonson, text="error::this primary key has already exsisted").grid(
                    row=0)
            else:
                strr = " SELECT * from trainstation where name = " + "'" + e4.get() + "'" + ";"
                strr2 = " SELECT * from trainstation where name = " + "'" + e5.get() + "'" + ";"
                strr3 = " SELECT * from trainstation where name = " + "'" + e3.get() + "'" + ";"
                cur.execute(strr)
                liss = cur.fetchall()
                cur.execute(strr2)
                liss2 = cur.fetchall()
                cur.execute(strr3)
                liss3 = cur.fetchall()
                if (len(liss) == 0 or len(liss2) == 0 or len(liss3) == 0):
                    winsonson = tk.Tk()
                    tk.Label(winsonson, text="error::not avaliable trainstation").grid(
                        row=0)
                else:
                    strr2 = " SELECT * from traindriver where idcard = " + "'" + e6.get() + \
                        "'" + ";"
                    strr3 = " SELECT * from traincaptain where idcard = " + "'" + e7.get() + \
                        "'" + ";"

                    cur.execute(strr2)
                    liss2 = cur.fetchall()
                    cur.execute(strr3)
                    liss3 = cur.fetchall()
                    if(len(liss2) == 0 and len(liss3) == 0):
                        instr = "INSERT INTO trainnumber (numberid, startdate, startstation, endstation, passstation) VALUES (" + "'" + e1.get(
                        ) + "'" + "," + "'" + e2.get() + "'" + "," + "'" + e3.get() + "'" + "," + "'" + e4.get() + "'" + "," + "'" + e5.get() + "'" + ");"

                    if(len(liss2) == 0 and len(liss3) != 0):
                        instr = "INSERT INTO trainnumber (numberid, startdate, startstation, endstation, passstation, captain) VALUES (" + "'" + e1.get() + "'" + "," + "'" + e2.get(
                        ) + "'" + "," + "'" + e3.get() + "'" + "," + "'" + e4.get() + "'" + "," + "'" + e5.get() + "'" + "," + "'" + e7.get() + "'" + ");"

                    if(len(liss3) == 0 and len(liss2) != 0):
                        instr = "INSERT INTO trainnumber (numberid, startdate, startstation, endstation, passstation, driver) VALUES (" + "'" + e1.get() + "'" + "," + "'" + e2.get(
                        ) + "'" + "," + "'" + e3.get() + "'" + "," + "'" + e4.get() + "'" + "," + "'" + e5.get() + "'" + "," + "'" + e6.get() + "'" + ");"
                    if (len(liss3) != 0 and len(liss2) != 0):
                        instr = "INSERT INTO trainnumber (numberid, startdate, startstation, endstation, passstation, driver, captain) VALUES (" + "'" + e1.get() + "'" + "," + "'" + e2.get(
                        ) + "'" + "," + "'" + e3.get() + "'" + "," + "'" + e4.get() + "'" + "," + "'" + e5.get() + "'" + "," + "'" + e6.get() + "'" + "," + "'" + e7.get() + "'" + ");"
                    print(instr)
                    cur.execute(instr)
                    winson.destroy()
            db.commit()

        tk.Button(winson, text='confirm', width=10, command=insee).grid(
            row=0, column=1, sticky="w", padx=10, pady=5)

    def change():
        cur = db.cursor()
        winson = tk.Tk()
        tk.Label(winson, text="输入车次、日期、经停站").grid(row=0)
        tk.Label(winson, text="修改某日车次的始发站、终点站").grid(row=4)
        tk.Label(winson, text="输入车次").grid(row=5, column=0)
        tk.Label(winson, text="日期").grid(row=6, column=0)
        tk.Label(winson, text="删除某经停站").grid(row=7)
        tk.Label(winson, text="输入车次").grid(row=8, column=0)
        tk.Label(winson, text="日期").grid(row=9, column=0)
        tk.Label(winson, text="增加某经停站").grid(row=10)
        tk.Label(winson, text="输入车次").grid(row=11, column=0)
        tk.Label(winson, text="日期").grid(row=12, column=0)
        ee = tk.Entry(winson)
        ee.grid(row=1, column=1, padx=20, pady=5)
        ee2 = tk.Entry(winson)
        ee2.grid(row=2, column=1, padx=20, pady=5)
        ee3 = tk.Entry(winson)
        ee3.grid(row=3, column=1, padx=20, pady=5)
        ee4 = tk.Entry(winson)
        ee4.grid(row=5, column=1, padx=20, pady=5)
        ee5 = tk.Entry(winson)
        ee5.grid(row=6, column=1, padx=20, pady=5)
        ee6 = tk.Entry(winson)
        ee6.grid(row=8, column=1, padx=20, pady=5)
        ee7 = tk.Entry(winson)
        ee7.grid(row=9, column=1, padx=20, pady=5)
        ee8 = tk.Entry(winson)
        ee8.grid(row=11, column=1, padx=20, pady=5)
        ee9 = tk.Entry(winson)
        ee9.grid(row=12, column=1, padx=20, pady=5)

        def insee2():
            strr = "SELECT * from trainnumber where numberid =" + "'" + ee.get() + "'" + " and " + \
                " startdate = '" + ee2.get() + "'" + " and " + "passstation = '" + \
                ee3.get() + "'" + ";"
            print(strr)
            cur.execute(strr)
            finding = cur.fetchall()
            if len(finding) == 0:
                winson = tk.Tk()
                tk.Label(winson, text="no findings").grid(row=0)
            else:
                winson = tk.Tk()
                tk.Label(winson, text="输入新的信息值").grid(row=0)
                tk.Label(winson, text="始发站").grid(
                    row=1, column=0, padx=10, pady=5)
                tk.Label(winson, text="终点站").grid(
                    row=2, column=0, padx=10, pady=5)
                tk.Label(winson, text="经停站").grid(
                    row=3, column=0, padx=10, pady=5)
                tk.Label(winson, text="司机").grid(
                    row=4, column=0, padx=10, pady=5)
                tk.Label(winson, text="列车长").grid(
                    row=5, column=0, padx=10, pady=5)
                e1 = tk.Entry(winson)
                e1.grid(row=1, column=1, padx=20, pady=5)
                e2 = tk.Entry(winson)
                e2.grid(row=2, column=1, padx=20, pady=5)
                e3 = tk.Entry(winson)
                e3.grid(row=3, column=1, padx=20, pady=5)
                e4 = tk.Entry(winson)
                e4.grid(row=4, column=1, padx=20, pady=5)
                e5 = tk.Entry(winson)
                e5.grid(row=5, column=1, padx=20, pady=5)

                def insee():
                    strr = " SELECT * from trainstation where name = " + "'" + e1.get() + "'" + ";"
                    strr2 = " SELECT * from trainstation where name = " + "'" + e2.get() + "'" + ";"
                    strr3 = " SELECT * from trainstation where name = " + "'" + e3.get() + "'" + ";"
                    cur.execute(strr)
                    liss = cur.fetchall()
                    cur.execute(strr2)
                    liss2 = cur.fetchall()
                    cur.execute(strr3)
                    liss3 = cur.fetchall()

                    if (len(liss) == 0 or len(liss2) == 0 or len(liss3) == 0):
                        winsonson = tk.Tk()
                        tk.Label(winsonson, text="error::not avaliable trainstation").grid(
                            row=0)
                    else:
                        strr2 = " SELECT * from traindriver where idcard = " + "'" + e4.get() + \
                            "'" + ";"
                        strr3 = " SELECT * from traincaptain where idcard = " + "'" + e5.get() + \
                            "'" + ";"

                        cur.execute(strr2)
                        liss2 = cur.fetchall()
                        cur.execute(strr3)
                        liss3 = cur.fetchall()
                        if (len(liss2) == 0 and len(liss3) == 0):
                            instr = "UPDATE trainnumber SET startstation = " + "'" + e1.get() + "'" + ", endstation=" + "'" + e2.get() + "'" + " ,passstation = " + "'" + e3.get() + \
                                "'" + " WHERE numberid =" + "'" + ee.get() + "'" + " and " + " startdate = '" + \
                                ee2.get() + "'" + " and " + "passstation = '" + ee3.get() + "'" + ";"

                        if (len(liss2) == 0 and len(liss3) != 0):
                            instr = "UPDATE trainnumber SET startstation = " + "'" + e1.get() + "'" + ", endstation=" + "'" + e2.get() + "'" + " ,passstation = " + "'" + e3.get() + "'" + " ,driver = " + \
                                "'" + e4.get() + "'" + " WHERE numberid =" + "'" + ee.get() + "'" + " and " + \
                                " startdate = '" + ee2.get() + "'" + " and " + "passstation = '" + \
                                ee3.get() + "'" + ";"

                        if (len(liss3) == 0 and len(liss2) != 0):
                            instr = "UPDATE trainnumber SET startstation = " + "'" + e1.get() + "'" + ", endstation=" + "'" + e2.get() + "'" + " ,passstation = " + "'" + e3.get() + "'" + " ,captain = " + \
                                "'" + e5.get() + "'" + " WHERE numberid =" + "'" + ee.get() + "'" + " and " + \
                                " startdate = '" + ee2.get() + "'" + " and " + "passstation = '" + \
                                ee3.get() + "'" + ";"

                        if (len(liss3) != 0 and len(liss2) != 0):
                            instr = "UPDATE trainnumber SET startstation = " + "'" + e1.get() + "'" + ", endstation=" + "'" + e2.get() + "'" + " ,passstation = " + "'" + e3.get() + "'" + " ,driver = " + "'" + e4.get() + \
                                "'" + " ,captain = " + "'" + e5.get() + "'" + " WHERE numberid =" + "'" + ee.get() + "'" + " and " + \
                                " startdate = '" + ee2.get() + "'" + " and " + "passstation = '" + \
                                ee3.get() + "'" + ";"

                        print(instr)
                        cur.execute(instr)
                        winson.destroy()
                    db.commit()

                tk.Button(winson, text='confirm', width=10, command=insee).grid(row=0, column=1, sticky="w", padx=10,
                                                                                pady=5)

        def insee3():
            strr = "SELECT * from trainnumber where numberid =" + "'" + \
                ee4.get() + "'" + " and " + " startdate = '" + ee5.get() + "'" + ";"
            print(strr)
            cur.execute(strr)
            finding = cur.fetchall()
            if len(finding) == 0:
                winson = tk.Tk()
                tk.Label(winson, text="no findings").grid(row=0)
            else:
                winson = tk.Tk()
                tk.Label(winson, text="输入新的信息值").grid(row=0)
                tk.Label(winson, text="始发站").grid(
                    row=1, column=0, padx=10, pady=5)
                tk.Label(winson, text="终点站").grid(
                    row=2, column=0, padx=10, pady=5)
                e1 = tk.Entry(winson)
                e1.grid(row=1, column=1, padx=20, pady=5)
                e2 = tk.Entry(winson)
                e2.grid(row=2, column=1, padx=20, pady=5)

                def insee():
                    strr = " SELECT * from trainstation where name = " + "'" + e1.get() + "'" + ";"
                    strr2 = " SELECT * from trainstation where name = " + "'" + e2.get() + "'" + ";"
                    cur.execute(strr)
                    liss = cur.fetchall()
                    cur.execute(strr2)
                    liss2 = cur.fetchall()

                    if (len(liss) == 0 or len(liss2) == 0):
                        winsonson = tk.Tk()
                        tk.Label(winsonson, text="error::not avaliable trainstation").grid(
                            row=0)
                    else:
                        instr = "UPDATE trainnumber SET startstation = " + "'" + e1.get() + "'" + ", endstation=" + "'" + e2.get() + \
                            "'" + " WHERE numberid =" + "'" + ee4.get() + "'" + " and " + \
                            " startdate = '" + ee5.get() + "'" + ";"

                        print(instr)
                        cur.execute(instr)
                        winson.destroy()
                    db.commit()

                tk.Button(winson, text='confirm', width=10, command=insee).grid(
                    row=0, column=1, sticky="w", padx=10, pady=5)

        def insee4():
            strr = "SELECT * from trainnumber where numberid =" + "'" + \
                ee6.get() + "'" + " and " + " startdate = '" + ee7.get() + "'" + ";"
            print(strr)
            cur.execute(strr)
            finding = cur.fetchall()
            if len(finding) == 0:
                winson = tk.Tk()
                tk.Label(winson, text="no findings").grid(row=0)
            else:
                winson = tk.Tk()
                tk.Label(winson, text="输入新的信息值").grid(row=0)
                tk.Label(winson, text="删除车站").grid(
                    row=2, column=0, padx=10, pady=5)
                e2 = tk.Entry(winson)
                e2.grid(row=2, column=1, padx=20, pady=5)

                def insee():
                    strr2 = " SELECT * from trainstation where name = " + "'" + e2.get() + "'" + ";"

                    cur.execute(strr2)
                    liss2 = cur.fetchall()

                    if (len(liss2) == 0):
                        winsonson = tk.Tk()
                        tk.Label(winsonson, text="error::not avaliable trainstation").grid(
                            row=0)
                    else:
                        instr = "DELETE FROM trainnumber WHERE numberid =" + "'" + ee6.get() + "'" + " and " + \
                            " startdate = '" + ee7.get() + "'" + " and " + \
                            " passstation = '" + e2.get() + "'" + ";"
                        print(instr)
                        cur.execute(instr)
                        winson.destroy()
                    db.commit()

                tk.Button(winson, text='confirm', width=10, command=insee).grid(
                    row=0, column=1, sticky="w", padx=10, pady=5)

        def insee5():
            strr = "SELECT * from trainnumber where numberid =" + "'" + \
                ee8.get() + "'" + " and " + " startdate = '" + ee9.get() + "'" + ";"
            print(strr)
            cur.execute(strr)
            finding = cur.fetchall()
            if len(finding) == 0:
                winson = tk.Tk()
                tk.Label(winson, text="no findings").grid(row=0)
            else:
                winson = tk.Tk()
                tk.Label(winson, text="输入新的信息值").grid(row=0)
                tk.Label(winson, text="增加车站").grid(
                    row=2, column=0, padx=10, pady=5)
                tk.Label(winson, text="增加司机").grid(
                    row=3, column=0, padx=10, pady=5)
                tk.Label(winson, text="增加列车长").grid(
                    row=4, column=0, padx=10, pady=5)
                e2 = tk.Entry(winson)
                e2.grid(row=2, column=1, padx=20, pady=5)
                e3 = tk.Entry(winson)
                e3.grid(row=3, column=1, padx=20, pady=5)
                e4 = tk.Entry(winson)
                e4.grid(row=4, column=1, padx=20, pady=5)

                def insee():
                    strr2 = " SELECT * from trainstation where name = " + "'" + e2.get() + "'" + ";"

                    cur.execute(strr2)
                    liss2 = cur.fetchall()

                    if (len(liss2) == 0):
                        winsonson = tk.Tk()
                        tk.Label(winsonson, text="error::not avaliable trainstation").grid(
                            row=0)
                    else:
                        strr2 = " SELECT * from traindriver where idcard = " + "'" + e3.get() + \
                            "'" + ";"
                        strr3 = " SELECT * from traincaptain where idcard = " + "'" + e4.get() + \
                            "'" + ";"
                        cur.execute(strr2)
                        liss2 = cur.fetchall()
                        cur.execute(strr3)
                        liss3 = cur.fetchall()
                        if (len(liss2) == 0 and len(liss3) == 0):
                            instr = "INSERT INTO trainnumber (numberid, startdate, startstation, endstation, passstation) VALUES (" + "'" + \
                                finding[0][0] + "'" + "," + "'" + finding[0][1] + "'" + "," + "'" + finding[0][2] + \
                                    "'" + "," + "'" + \
                                finding[0][3] + "'" + "," + \
                                    "'" + e2.get() + "'" + ");"

                        if (len(liss2) == 0 and len(liss3) != 0):
                            instr = "INSERT INTO trainnumber (numberid, startdate, startstation, endstation, passstation, captain) VALUES (" + "'" + finding[0][0] + "'" + "," + "'" + finding[
                                0][1] + "'" + "," + "'" + finding[0][2] + "'" + "," + "'" + finding[0][3] + "'" + "," + "'" + e2.get() + "'" + "," + "'" + e4.get() + "'" + ");"

                        if (len(liss3) == 0 and len(liss2) != 0):
                            instr = "INSERT INTO trainnumber (numberid, startdate, startstation, endstation, passstation, driver) VALUES (" + "'" + finding[0][0] + "'" + "," + "'" + finding[
                                0][1] + "'" + "," + "'" + finding[0][2] + "'" + "," + "'" + finding[0][3] + "'" + "," + "'" + e2.get() + "'" + "," + "'" + e3.get() + "'" + ");"
                        if (len(liss3) != 0 and len(liss2) != 0):
                            instr = "INSERT INTO trainnumber (numberid, startdate, startstation, endstation, passstation, driver, captain) VALUES (" + "'" + finding[0][0] + "'" + "," + "'" + finding[0][
                                1] + "'" + "," + "'" + finding[0][2] + "'" + "," + "'" + finding[0][3] + "'" + "," + "'" + e2.get() + "'" + "," + "'" + e3.get() + "'" + "," + "'" + e4.get() + "'" + ");"
                        print(instr)
                        cur.execute(instr)
                        winson.destroy()
                    db.commit()

                tk.Button(winson, text='confirm', width=10, command=insee).grid(
                    row=0, column=1, sticky="w", padx=10, pady=5)

        db.commit()
        tk.Button(winson, text='confirm', width=10, command=insee2).grid(
            row=0, column=1, sticky="w", padx=10, pady=5)
        tk.Button(winson, text='confirm', width=10, command=insee3).grid(
            row=4, column=1, sticky="w", padx=10, pady=5)
        tk.Button(winson, text='confirm', width=10, command=insee4).grid(
            row=7, column=1, sticky="w", padx=10, pady=5)
        tk.Button(winson, text='confirm', width=10, command=insee5).grid(
            row=10, column=1, sticky="w", padx=10, pady=5)

    def deletea():
        cur = db.cursor()
        winson = tk.Tk()
        tk.Label(winson, text="输入停运列车车次以及日期").grid(row=0)
        ee = tk.Entry(winson)
        ee.grid(row=1, column=1, padx=20, pady=5)
        ee2 = tk.Entry(winson)
        ee2.grid(row=2, column=1, padx=20, pady=5)

        def insee2():
            strr = "SELECT * from trainnumber where numberid =" + "'" + \
                ee.get() + "'" + " and " + " startdate = '" + ee2.get() + "'" + ";"
            print(strr)
            cur.execute(strr)
            finding = cur.fetchall()
            if len(finding) == 0:
                winson = tk.Tk()
                tk.Label(winson, text="no findings").grid(row=0)
            else:
                winson2 = tk.Tk()
                tk.Label(winson2, text="确认让它消失了吗？").grid(row=0)

                def insee():
                    instr = "DELETE FROM trainnumber where numberid =" + "'" + \
                        ee.get() + "'" + " and " + " startdate = '" + ee2.get() + "'" + ";"
                    print(instr)
                    cur.execute(instr)
                    db.commit()
                    winson2.destroy()

                tk.Button(winson2, text='confirm', width=10, command=insee).grid(row=1, column=0, sticky="w", padx=10,
                                                                                 pady=5)
                tk.Button(winson2, text='no', width=10, command=winson2.destroy).grid(row=1, column=2, sticky="w",
                                                                                      padx=10, pady=5)
                db.commit()

        db.commit()
        tk.Button(winson, text='confirm', width=10, command=insee2).grid(
            row=0, column=1, sticky="w", padx=10, pady=5)

    tk.Button(win, text='查找', width=10, command=search).grid(
        row=1, column=0, sticky="w", padx=10, pady=5)
    tk.Button(win, text='插入', width=10, command=insert).grid(
        row=1, column=2, sticky="w", padx=10, pady=5)
    tk.Button(win, text='修改', width=10, command=change).grid(
        row=1, column=3, sticky="w", padx=10, pady=5)
    tk.Button(win, text='删除', width=10, command=deletea).grid(
        row=1, column=4, sticky="w", padx=10, pady=5)
    win.mainloop()


def openchar5():
    db = pymysql.connect(host="localhost", user="root",
                         password="1234", port=3306, db='mydbtrain')
    win = tk.Tk()
    win.title('车皮查询')
    win.geometry('626x417')
    kinds = ['yingwo', 'yingzuo', 'ruanzuo', 'ruanwo', 'canche', 'xingli',
             'kongtiaofadian', 'yideng', 'erdeng', 'shangwu', 'gaoruan', 'ruanbao']

    def search():
        winson = tk.Tk()
        cur = db.cursor()
        e1 = tk.Entry(winson)
        e1.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        e2 = tk.Entry(winson)
        e2.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        e3 = tk.Entry(winson)
        e3.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        e4 = tk.Entry(winson)
        e4.grid(row=3, column=0, sticky="w", padx=10, pady=5)
        e5 = tk.Entry(winson)
        e5.grid(row=4, column=0, sticky="w", padx=10, pady=5)

        def insee1():
            atf2 = False
            atf3 = False
            atf4 = False
            atf5 = False
            strr = " SELECT * from traincoach where "
            if (e1.get() != ""):
                strr += " id = "+e1.get() + " "
                atf2 = True
            if (e2.get() != ""):
                if atf2:
                    strr += "and trainnub = '"+e2.get()+"' "
                else:
                    strr += "trainnub = '"+e2.get()+"' "
                atf3 = True
            if (e3.get() != ""):
                if atf3 or atf2:
                    strr += "and traindate = '"+e3.get()+"' "
                else:
                    strr += "traindate = '"+e3.get()+"' "
                atf4 = True
            if (e4.get() != ""):
                if atf4 or atf3 or atf2:
                    strr += "and kind = '"+e4.get()+"' "
                else:
                    strr += "kind = '" + e4.get() + "' "
                atf5 = True
            if (e5.get() != ""):
                if atf5 or atf4 or atf3 or atf2:
                    strr += "and upperid = "+e5.get()+" "
                else:
                    strr += " upperid = " + e5.get() + " "
            print(strr)
            cur.execute(strr)
            lis = cur.fetchall()
            if (len(lis) != 0):
                winsonson = tk.Tk()
                tk.Label(winsonson, text=str("共")).grid(
                    row=0, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str(len(lis))).grid(
                    row=0, column=1, padx=5, pady=5)
                tk.Label(winsonson, text=str("节车厢")).grid(
                    row=0, column=2, padx=5, pady=5)
                tk.Label(winsonson, text=str("id")).grid(
                    row=1, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("执行车次")).grid(
                    row=2, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("日期")).grid(
                    row=3, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("种类")).grid(
                    row=4, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("所属铁路局")).grid(
                    row=5, column=0, padx=5, pady=5)

                for j in range(len(lis)):
                    strr2 = " SELECT * from railwaybeureau where id = " + \
                        str(lis[j][4]) + ";"
                    cur.execute(strr2)
                    liss2 = cur.fetchall()
                    tk.Label(winsonson, text=str(liss2[0][1])).grid(
                        row=6, column=1 + j, padx=3, pady=5)
                    for i in range(len(lis[0])):
                        tk.Label(winsonson, text=str(lis[j][i])).grid(
                            row=i + 1, column=1+j, padx=3, pady=5)

            else:
                winsonson = tk.Tk()
                tk.Label(winsonson, text="no findings").grid(row=0)

        tk.Label(winson, text=str("id查询")).grid(
            row=0, column=1, padx=10, pady=5)
        tk.Label(winson, text=str("执行车次查询")).grid(
            row=1, column=1, padx=10, pady=5)
        tk.Label(winson, text=str("日期查询")).grid(
            row=2, column=1, padx=10, pady=5)
        tk.Label(winson, text=str("车厢类型查询")).grid(
            row=3, column=1, padx=10, pady=5)
        tk.Label(winson, text=str("铁路局查询")).grid(
            row=4, column=1, padx=10, pady=5)
        tk.Button(winson, text=str("查找"), command=insee1).grid(
            row=5, column=1, padx=10, pady=5)

    def insert():
        winson = tk.Tk()
        e1 = tk.Entry(winson)
        e1.grid(row=1, column=1, padx=20, pady=5)
        e2 = tk.Entry(winson)
        e2.grid(row=2, column=1, padx=20, pady=5)
        e3 = tk.Entry(winson)
        e3.grid(row=3, column=1, padx=20, pady=5)
        e4 = tk.Entry(winson)
        e4.grid(row=4, column=1, padx=20, pady=5)
        e5 = tk.Entry(winson)
        e5.grid(row=5, column=1, padx=20, pady=5)
        tk.Label(winson, text=str("请输入信息")).grid(
            row=0, column=0, padx=10, pady=5)
        tk.Label(winson, text=str("车皮id")).grid(
            row=1, column=0, padx=5, pady=5)
        tk.Label(winson, text=str("执行车次")).grid(
            row=2, column=0, padx=5, pady=5)
        tk.Label(winson, text=str("日期")).grid(row=3, column=0, padx=5, pady=5)
        tk.Label(winson, text=str("车皮类型")).grid(
            row=4, column=0, padx=5, pady=5)
        tk.Label(winson, text=str("所属铁路局id")).grid(
            row=5, column=0, padx=5, pady=5)
        cur = db.cursor()

        def insee():
            strr = " SELECT * from traincoach where id = " + e1.get() + ";"
            cur.execute(strr)
            lis = cur.fetchall()
            if (len(lis) != 0):
                winsonson = tk.Tk()
                tk.Label(winsonson, text="error::this primary key has already exsisted").grid(
                    row=0)
            else:
                strr2 = " SELECT * from railwaybeureau where id = " + e5.get() + ";"
                cur.execute(strr2)
                liss2 = cur.fetchall()
                if (len(liss2) == 0 or kinds.index(e4.get()) < 0):
                    winsonson = tk.Tk()
                    tk.Label(winsonson, text="error::not avaliable trainscoach").grid(
                        row=0)
                else:
                    strr = " SELECT * from trainnumber where numberid = " + "'" + \
                        e2.get() + "'"   " and startdate = '" + e3.get() + "'" + ";"
                    cur.execute(strr)
                    print(strr)
                    liss = cur.fetchall()
                    if(len(liss) > 0):
                        instr = "INSERT INTO traincoach (id, trainnub, traindate, kind, upperid) VALUES (" + e1.get(
                        ) + "," + "'" + e2.get() + "'" + "," + "'" + e3.get() + "'" + "," + "'" + e4.get() + "'" + "," + e5.get() + ");"

                    else:
                        instr = "INSERT INTO traincoach (id, kind, upperid) VALUES (" + "'" + e1.get(
                        ) + "'" + "," + "'" + e4.get() + "'" + "," + e5.get() + ");"

                    print(instr)
                    cur.execute(instr)
                    winson.destroy()
            db.commit()

        tk.Button(winson, text='confirm', width=10, command=insee).grid(
            row=0, column=1, sticky="w", padx=10, pady=5)

    def change():
        cur = db.cursor()
        winson = tk.Tk()
        tk.Label(winson, text="输入车皮id").grid(row=0)

        ee = tk.Entry(winson)
        ee.grid(row=1, column=1, padx=20, pady=5)

        def insee2():
            strr = "SELECT * from traincoach where id =" + ee.get() + ";"
            print(strr)
            cur.execute(strr)
            finding = cur.fetchall()
            if len(finding) == 0:
                winson = tk.Tk()
                tk.Label(winson, text="no findings").grid(row=0)
            else:
                winson = tk.Tk()
                tk.Label(winson, text="输入新的信息值").grid(row=0)
                tk.Label(winson, text="车次").grid(
                    row=1, column=0, padx=10, pady=5)
                tk.Label(winson, text="日期").grid(
                    row=2, column=0, padx=10, pady=5)
                e1 = tk.Entry(winson)
                e1.grid(row=1, column=1, padx=20, pady=5)
                e2 = tk.Entry(winson)
                e2.grid(row=2, column=1, padx=20, pady=5)

                def insee():
                    strr = " SELECT * from trainnumber where numberid = " + "'" + \
                        e1.get() + "'"   " and startdate = '" + e2.get() + "'" + ";"
                    cur.execute(strr)
                    print(strr)
                    liss = cur.fetchall()

                    if (len(liss) == 0):
                        winsonson = tk.Tk()
                        tk.Label(winsonson, text="error::not avaliable trainnumber").grid(
                            row=0)
                    else:
                        instr = "UPDATE traincoach SET trainnub = " + "'" + e1.get() + "'" + ", traindate=" + \
                            "'" + e2.get() + "' where id = " + ee.get() + " ;"

                        print(instr)
                        cur.execute(instr)
                        winson.destroy()
                    db.commit()

                tk.Button(winson, text='confirm', width=10, command=insee).grid(row=0, column=1, sticky="w", padx=10,
                                                                                pady=5)

        db.commit()
        tk.Button(winson, text='confirm', width=10, command=insee2).grid(
            row=0, column=1, sticky="w", padx=10, pady=5)

    def deletea():
        cur = db.cursor()
        winson = tk.Tk()
        tk.Label(winson, text="输入停运列车车皮id").grid(row=0)
        ee = tk.Entry(winson)
        ee.grid(row=1, column=1, padx=20, pady=5)

        def insee2():
            strr = "SELECT * from traincoach where id =" + ee.get() + ";"
            print(strr)
            cur.execute(strr)
            finding = cur.fetchall()
            if len(finding) == 0:
                winson = tk.Tk()
                tk.Label(winson, text="no findings").grid(row=0)
            else:
                winson2 = tk.Tk()
                tk.Label(winson2, text="确认让它消失了吗？").grid(row=0)

                def insee():
                    instr = "DELETE FROM traincoach where id =" + ee.get() + ";"
                    print(instr)
                    cur.execute(instr)
                    db.commit()
                    winson2.destroy()

                tk.Button(winson2, text='confirm', width=10, command=insee).grid(row=1, column=0, sticky="w", padx=10,
                                                                                 pady=5)
                tk.Button(winson2, text='no', width=10, command=winson2.destroy).grid(row=1, column=2, sticky="w",
                                                                                      padx=10, pady=5)
                db.commit()

        db.commit()
        tk.Button(winson, text='confirm', width=10, command=insee2).grid(
            row=0, column=1, sticky="w", padx=10, pady=5)

    tk.Button(win, text='查找', width=10, command=search).grid(
        row=1, column=0, sticky="w", padx=10, pady=5)
    tk.Button(win, text='插入', width=10, command=insert).grid(
        row=1, column=2, sticky="w", padx=10, pady=5)
    tk.Button(win, text='修改', width=10, command=change).grid(
        row=1, column=3, sticky="w", padx=10, pady=5)
    tk.Button(win, text='删除', width=10, command=deletea).grid(
        row=1, column=4, sticky="w", padx=10, pady=5)
    win.mainloop()


def openchar6():
    db = pymysql.connect(host="localhost", user="root",
                         password="1234", port=3306, db='mydbtrain')
    win = tk.Tk()
    win.title('司机主页')
    win.geometry('626x417')

    def search():
        winson = tk.Tk()
        cur = db.cursor()
        e1 = tk.Entry(winson)
        e1.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        e2 = tk.Entry(winson)
        e2.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        e3 = tk.Entry(winson)
        e3.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        e4 = tk.Entry(winson)
        e4.grid(row=3, column=0, sticky="w", padx=10, pady=5)
        e5 = tk.Entry(winson)
        e5.grid(row=4, column=0, sticky="w", padx=10, pady=5)

        def insee1():
            atf2 = False
            atf3 = False
            atf4 = False
            atf5 = False
            atf6 = False
            strr = " SELECT * from traindriver where "
            if (e1.get() != ""):
                strr += " name = '"+e1.get() + "' "
                atf2 = True
            if (e2.get() != ""):
                if atf2:
                    strr += "and idcard = '"+e2.get()+"' "
                else:
                    strr += "idcard = '"+e2.get()+"' "
                atf3 = True
            if (e3.get() != ""):
                if atf3 or atf2:
                    strr += "and beureauid = "+e3.get()+" "
                else:
                    strr += "beureauid  = " + e3.get()+" "
                atf4 = True
            if (e4.get() != ""):
                if atf4 or atf3 or atf2:
                    strr += "and workage >= "+e4.get()+" "
                else:
                    strr += "workage >= " + e4.get() + " "
                atf5 = True
            if (e5.get() != ""):
                if atf5 or atf4 or atf3 or atf2:
                    strr += "and workage <= "+e5.get()+" "
                else:
                    strr += "workage <= " + e5.get() + " "
                atf6 = True
            if(atf5 or atf6):
                strr += ";"
            else:
                strr += ";"
            print(strr)
            cur.execute(strr)
            lis = cur.fetchall()
            if (len(lis) != 0):
                winsonson = tk.Tk()
                tk.Label(winsonson, text=str("共")).grid(
                    row=0, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str(len(lis))).grid(
                    row=0, column=1, padx=5, pady=5)
                tk.Label(winsonson, text=str("名司机")).grid(
                    row=0, column=2, padx=5, pady=5)
                tk.Label(winsonson, text=str("姓名")).grid(
                    row=1, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("身份证号")).grid(
                    row=2, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("所属铁路局id")).grid(
                    row=3, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("工龄")).grid(
                    row=4, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("所属铁路局")).grid(
                    row=5, column=0, padx=5, pady=5)

                for j in range(len(lis)):
                    strr2 = " SELECT * from railwaybeureau where id = " + \
                        str(lis[j][2]) + ";"
                    cur.execute(strr2)
                    liss2 = cur.fetchall()
                    tk.Label(winsonson, text=liss2[0][1]).grid(
                        row=5, column=1 + j, padx=3, pady=5)
                    for i in range(len(lis[0])):
                        tk.Label(winsonson, text=str(lis[j][i])).grid(
                            row=i + 1, column=1+j, padx=3, pady=5)

            else:
                winsonson = tk.Tk()
                tk.Label(winsonson, text="no findings").grid(row=0)

        tk.Label(winson, text=str("姓名查询")).grid(
            row=0, column=1, padx=10, pady=5)
        tk.Label(winson, text=str("身份证号查询")).grid(
            row=1, column=1, padx=10, pady=5)
        tk.Label(winson, text=str("所属铁路局id查询")).grid(
            row=2, column=1, padx=10, pady=5)
        tk.Label(winson, text=str("工龄下限查询")).grid(
            row=3, column=1, padx=10, pady=5)
        tk.Label(winson, text=str("工龄上限查询")).grid(
            row=4, column=1, padx=10, pady=5)
        tk.Button(winson, text=str("查找"), command=insee1).grid(
            row=5, column=1, padx=10, pady=5)

    def insert():
        winson = tk.Tk()
        e1 = tk.Entry(winson)
        e1.grid(row=1, column=1, padx=20, pady=5)
        e2 = tk.Entry(winson)
        e2.grid(row=2, column=1, padx=20, pady=5)
        e3 = tk.Entry(winson)
        e3.grid(row=3, column=1, padx=20, pady=5)
        e4 = tk.Entry(winson)
        e4.grid(row=4, column=1, padx=20, pady=5)
        tk.Label(winson, text=str("请输入信息")).grid(
            row=0, column=0, padx=10, pady=5)
        tk.Label(winson, text=str("姓名")).grid(row=1, column=0, padx=5, pady=5)
        tk.Label(winson, text=str("身份证号")).grid(
            row=2, column=0, padx=5, pady=5)
        tk.Label(winson, text=str("所属铁路局id")).grid(
            row=3, column=0, padx=5, pady=5)
        tk.Label(winson, text=str("工龄")).grid(row=4, column=0, padx=5, pady=5)
        cur = db.cursor()

        def insee():
            strr = " SELECT * from traindriver where idcard = '" + e2.get() + "' ;"
            cur.execute(strr)
            lis = cur.fetchall()
            if (len(lis) != 0):
                winsonson = tk.Tk()
                tk.Label(winsonson, text="error::this primary key has already exsisted").grid(
                    row=0)
            else:
                strr2 = " SELECT * from railwaybeureau where id = " + e3.get() + ";"
                cur.execute(strr2)
                liss2 = cur.fetchall()
                if (len(liss2) == 0):
                    winsonson = tk.Tk()
                    tk.Label(winsonson, text="error::not avaliable beureau").grid(
                        row=0)
                else:
                    instr = "INSERT INTO traindriver (name, idcard, beureauid, workage) VALUES (" + "'" + e1.get(
                    ) + "'" + "," + "'" + e2.get() + "'" + "," + e3.get() + "," + e4.get() + ");"

                    print(instr)
                    cur.execute(instr)
                    winson.destroy()
            db.commit()

        tk.Button(winson, text='confirm', width=10, command=insee).grid(
            row=0, column=1, sticky="w", padx=10, pady=5)

    def change():
        cur = db.cursor()
        winson = tk.Tk()
        tk.Label(winson, text="输入身份证号").grid(row=0)

        ee = tk.Entry(winson)
        ee.grid(row=1, column=1, padx=20, pady=5)

        def insee2():
            strr = "SELECT * from traindriver where idcard = '" + ee.get() + "' ;"
            print(strr)
            cur.execute(strr)
            finding = cur.fetchall()
            if len(finding) == 0:
                winson = tk.Tk()
                tk.Label(winson, text="no findings").grid(row=0)
            else:
                winson = tk.Tk()
                tk.Label(winson, text="输入新的信息值").grid(row=0)
                tk.Label(winson, text="工龄").grid(
                    row=2, column=0, padx=10, pady=5)
                e1 = tk.Entry(winson)
                e1.grid(row=1, column=1, padx=20, pady=5)

                def insee():
                    instr = "UPDATE traindriver SET workage = " + \
                        e1.get() + " where idcard = '" + ee.get() + "' ;"
                    print(instr)
                    cur.execute(instr)
                    winson.destroy()
                    db.commit()

                tk.Button(winson, text='confirm', width=10, command=insee).grid(row=0, column=1, sticky="w", padx=10,
                                                                                pady=5)

        db.commit()
        tk.Button(winson, text='confirm', width=10, command=insee2).grid(
            row=0, column=1, sticky="w", padx=10, pady=5)

    def deletea():
        cur = db.cursor()
        winson = tk.Tk()
        tk.Label(winson, text="输入解雇司机").grid(row=0)
        ee = tk.Entry(winson)
        ee.grid(row=1, column=1, padx=20, pady=5)

        def insee2():
            strr = "SELECT * from traindriver where idcard = '" + ee.get() + "' ;"
            print(strr)
            cur.execute(strr)
            finding = cur.fetchall()
            if len(finding) == 0:
                winson = tk.Tk()
                tk.Label(winson, text="no findings").grid(row=0)
            else:
                winson2 = tk.Tk()
                tk.Label(winson2, text="确认让它消失了吗？").grid(row=0)
                tk.Label(winson2, text=finding[0][0]).grid(
                    row=1, column=0, padx=5)
                tk.Label(winson2, text=finding[0][1]).grid(
                    row=1, column=1, padx=5)

                def insee():
                    instr = "DELETE FROM traindriver where idcard = '" + ee.get() + "' ;"
                    print(instr)
                    cur.execute(instr)
                    db.commit()
                    winson2.destroy()

                tk.Button(winson2, text='confirm', width=10, command=insee).grid(row=2, column=0, sticky="w", padx=10,
                                                                                 pady=5)
                tk.Button(winson2, text='no', width=10, command=winson2.destroy).grid(row=2, column=2, sticky="w",
                                                                                      padx=10, pady=5)
                db.commit()

        db.commit()
        tk.Button(winson, text='confirm', width=10, command=insee2).grid(
            row=0, column=1, sticky="w", padx=10, pady=5)

    tk.Button(win, text='查找', width=10, command=search).grid(
        row=1, column=0, sticky="w", padx=10, pady=5)
    tk.Button(win, text='插入', width=10, command=insert).grid(
        row=1, column=2, sticky="w", padx=10, pady=5)
    tk.Button(win, text='修改', width=10, command=change).grid(
        row=1, column=3, sticky="w", padx=10, pady=5)
    tk.Button(win, text='删除', width=10, command=deletea).grid(
        row=1, column=4, sticky="w", padx=10, pady=5)
    win.mainloop()


def openchar7():
    db = pymysql.connect(host="localhost", user="root",
                         password="1234", port=3306, db='mydbtrain')
    win = tk.Tk()
    win.title('列车长主页')
    win.geometry('626x417')

    def search():
        winson = tk.Tk()
        cur = db.cursor()
        e1 = tk.Entry(winson)
        e1.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        e2 = tk.Entry(winson)
        e2.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        e3 = tk.Entry(winson)
        e3.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        e4 = tk.Entry(winson)
        e4.grid(row=3, column=0, sticky="w", padx=10, pady=5)
        e5 = tk.Entry(winson)
        e5.grid(row=4, column=0, sticky="w", padx=10, pady=5)

        def insee1():
            atf2 = False
            atf3 = False
            atf4 = False
            atf5 = False
            strr = " SELECT * from traincaptain where "
            if (e1.get() != ""):
                strr += " name = '"+e1.get() + "' "
                atf2 = True
            if (e2.get() != ""):
                if atf2:
                    strr += "and idcard = '"+e2.get()+"' "
                else:
                    strr += "idcard = '"+e2.get()+"' "
                atf3 = True
            if (e3.get() != ""):
                if atf3 or atf2:
                    strr += "and beauid = "+e3.get()+" "
                else:
                    strr += "beauid  = " + e3.get()+" "
                atf4 = True
            if (e4.get() != ""):
                if atf4 or atf3 or atf2:
                    strr += "and workage >= "+e4.get()+" "
                else:
                    strr += "workage >= " + e4.get() + " "
                atf5 = True
            if (e5.get() != ""):
                if atf5 or atf4 or atf3 or atf2:
                    strr += "and workage <= "+e5.get()+" "
                else:
                    strr += "workage <= " + e5.get() + " "
            print(strr)
            cur.execute(strr)
            lis = cur.fetchall()
            if (len(lis) != 0):
                winsonson = tk.Tk()
                tk.Label(winsonson, text=str("共")).grid(
                    row=0, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str(len(lis))).grid(
                    row=0, column=1, padx=5, pady=5)
                tk.Label(winsonson, text=str("名列车长")).grid(
                    row=0, column=2, padx=5, pady=5)
                tk.Label(winsonson, text=str("姓名")).grid(
                    row=1, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("身份证号")).grid(
                    row=2, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("所属铁路局id")).grid(
                    row=3, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("工龄")).grid(
                    row=4, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("所属铁路局")).grid(
                    row=5, column=0, padx=5, pady=5)

                for j in range(len(lis)):
                    strr2 = " SELECT * from railwaybeureau where id = " + \
                        str(lis[j][2]) + ";"
                    cur.execute(strr2)
                    liss2 = cur.fetchall()
                    tk.Label(winsonson, text=liss2[0][1]).grid(
                        row=5, column=1 + j, padx=3, pady=5)
                    for i in range(len(lis[0])):
                        tk.Label(winsonson, text=str(lis[j][i])).grid(
                            row=i + 1, column=1+j, padx=3, pady=5)

            else:
                winsonson = tk.Tk()
                tk.Label(winsonson, text="no findings").grid(row=0)

        tk.Label(winson, text=str("姓名查询")).grid(
            row=0, column=1, padx=10, pady=5)
        tk.Label(winson, text=str("身份证号查询")).grid(
            row=1, column=1, padx=10, pady=5)
        tk.Label(winson, text=str("所属铁路局id查询")).grid(
            row=2, column=1, padx=10, pady=5)
        tk.Label(winson, text=str("工龄下限查询")).grid(
            row=3, column=1, padx=10, pady=5)
        tk.Label(winson, text=str("工龄上限查询")).grid(
            row=4, column=1, padx=10, pady=5)
        tk.Button(winson, text=str("查找"), command=insee1).grid(
            row=5, column=1, padx=10, pady=5)

    def insert():
        winson = tk.Tk()
        e1 = tk.Entry(winson)
        e1.grid(row=1, column=1, padx=20, pady=5)
        e2 = tk.Entry(winson)
        e2.grid(row=2, column=1, padx=20, pady=5)
        e3 = tk.Entry(winson)
        e3.grid(row=3, column=1, padx=20, pady=5)
        e4 = tk.Entry(winson)
        e4.grid(row=4, column=1, padx=20, pady=5)
        tk.Label(winson, text=str("请输入信息")).grid(
            row=0, column=0, padx=10, pady=5)
        tk.Label(winson, text=str("姓名")).grid(row=1, column=0, padx=5, pady=5)
        tk.Label(winson, text=str("身份证号")).grid(
            row=2, column=0, padx=5, pady=5)
        tk.Label(winson, text=str("所属铁路局id")).grid(
            row=3, column=0, padx=5, pady=5)
        tk.Label(winson, text=str("工龄")).grid(row=4, column=0, padx=5, pady=5)
        cur = db.cursor()

        def insee():
            strr = " SELECT * from traincaptain where idcard = '" + e2.get() + "' ;"
            cur.execute(strr)
            lis = cur.fetchall()
            if (len(lis) != 0):
                winsonson = tk.Tk()
                tk.Label(winsonson, text="error::this primary key has already exsisted").grid(
                    row=0)
            else:
                strr2 = " SELECT * from railwaybeureau where id = " + e3.get() + ";"
                cur.execute(strr2)
                liss2 = cur.fetchall()
                if (len(liss2) == 0):
                    winsonson = tk.Tk()
                    tk.Label(winsonson, text="error::not avaliable beureau").grid(
                        row=0)
                else:
                    instr = "INSERT INTO traincaptain (name, idcard, beauid, workage) VALUES (" + "'" + e1.get(
                    ) + "'" + "," + "'" + e2.get() + "'" + "," + e3.get() + "," + e4.get() + ");"

                    print(instr)
                    cur.execute(instr)
                    winson.destroy()
            db.commit()

        tk.Button(winson, text='confirm', width=10, command=insee).grid(
            row=0, column=1, sticky="w", padx=10, pady=5)

    def change():
        cur = db.cursor()
        winson = tk.Tk()
        tk.Label(winson, text="输入身份证号").grid(row=0)

        ee = tk.Entry(winson)
        ee.grid(row=1, column=1, padx=20, pady=5)

        def insee2():
            strr = "SELECT * from traincaptain where idcard = '" + ee.get() + "' ;"
            print(strr)
            cur.execute(strr)
            finding = cur.fetchall()
            if len(finding) == 0:
                winson = tk.Tk()
                tk.Label(winson, text="no findings").grid(row=0)
            else:
                winson = tk.Tk()
                tk.Label(winson, text="输入新的信息值").grid(row=0)
                tk.Label(winson, text="工龄").grid(
                    row=2, column=0, padx=10, pady=5)
                e1 = tk.Entry(winson)
                e1.grid(row=1, column=1, padx=20, pady=5)

                def insee():
                    instr = "UPDATE traincaptain SET workage = " + \
                        e1.get() + " where idcard = '" + ee.get() + "' ;"
                    print(instr)
                    cur.execute(instr)
                    winson.destroy()
                    db.commit()

                tk.Button(winson, text='confirm', width=10, command=insee).grid(row=0, column=1, sticky="w", padx=10,
                                                                                pady=5)

        db.commit()
        tk.Button(winson, text='confirm', width=10, command=insee2).grid(
            row=0, column=1, sticky="w", padx=10, pady=5)

    def deletea():
        cur = db.cursor()
        winson = tk.Tk()
        tk.Label(winson, text="输入解雇列车长").grid(row=0)
        ee = tk.Entry(winson)
        ee.grid(row=1, column=1, padx=20, pady=5)

        def insee2():
            strr = "SELECT * from traincaptain where idcard = '" + ee.get() + "' ;"
            print(strr)
            cur.execute(strr)
            finding = cur.fetchall()
            if len(finding) == 0:
                winson = tk.Tk()
                tk.Label(winson, text="no findings").grid(row=0)
            else:
                winson2 = tk.Tk()
                tk.Label(winson2, text="确认让它消失了吗？").grid(row=0)
                tk.Label(winson2, text=finding[0][0]).grid(
                    row=1, column=0, padx=5)
                tk.Label(winson2, text=finding[0][1]).grid(
                    row=1, column=1, padx=5)

                def insee():
                    instr = "DELETE FROM traincaptain where idcard = '" + ee.get() + "' ;"
                    print(instr)
                    cur.execute(instr)
                    db.commit()
                    winson2.destroy()

                tk.Button(winson2, text='confirm', width=10, command=insee).grid(row=2, column=0, sticky="w", padx=10,
                                                                                 pady=5)
                tk.Button(winson2, text='no', width=10, command=winson2.destroy).grid(row=2, column=2, sticky="w",
                                                                                      padx=10, pady=5)
                db.commit()

        db.commit()
        tk.Button(winson, text='confirm', width=10, command=insee2).grid(
            row=0, column=1, sticky="w", padx=10, pady=5)

    tk.Button(win, text='查找', width=10, command=search).grid(
        row=1, column=0, sticky="w", padx=10, pady=5)
    tk.Button(win, text='插入', width=10, command=insert).grid(
        row=1, column=2, sticky="w", padx=10, pady=5)
    tk.Button(win, text='修改', width=10, command=change).grid(
        row=1, column=3, sticky="w", padx=10, pady=5)
    tk.Button(win, text='删除', width=10, command=deletea).grid(
        row=1, column=4, sticky="w", padx=10, pady=5)
    win.mainloop()


def openchar8():
    db = pymysql.connect(host="localhost", user="root",
                         password="1234", port=3306, db='mydbtrain')
    win = tk.Tk()
    win.title('列车员主页')
    win.geometry('626x417')

    def search():
        winson = tk.Tk()
        cur = db.cursor()
        e1 = tk.Entry(winson)
        e1.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        e2 = tk.Entry(winson)
        e2.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        e3 = tk.Entry(winson)
        e3.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        e4 = tk.Entry(winson)
        e4.grid(row=3, column=0, sticky="w", padx=10, pady=5)
        e5 = tk.Entry(winson)
        e5.grid(row=4, column=0, sticky="w", padx=10, pady=5)
        e6 = tk.Entry(winson)
        e6.grid(row=5, column=0, sticky="w", padx=10, pady=5)

        def insee1():
            atf2 = False
            atf3 = False
            atf4 = False
            atf5 = False
            atf6 = False
            strr = " SELECT * from trainserver where "
            if (e1.get() != ""):
                strr += " name = '"+e1.get() + "' "
                atf2 = True
            if (e2.get() != ""):
                if atf2:
                    strr += "and idcard = '"+e2.get()+"' "
                else:
                    strr += "idcard = '"+e2.get()+"' "
                atf3 = True
            if (e3.get() != ""):
                if atf3 or atf2:
                    strr += "and beauid = "+e3.get()+" "
                else:
                    strr += "beauid  = " + e3.get()+" "
                atf4 = True
            if (e4.get() != ""):
                if atf4 or atf3 or atf2:
                    strr += "and workage >= "+e4.get()+" "
                else:
                    strr += "workage >= " + e4.get() + " "
                atf5 = True
            if (e5.get() != ""):
                if atf5 or atf4 or atf3 or atf2:
                    strr += "and workage <= "+e5.get()+" "
                else:
                    strr += "workage <= " + e5.get() + " "

                atf6 = True
            if (e6.get() != ""):
                if atf5 or atf4 or atf3 or atf2:
                    strr += "and captainnumber = '"+e6.get()+"' "
                else:
                    strr += "captainnumber = '" + e6.get() + "' "

                atf6 = True
            print(strr)
            cur.execute(strr)
            lis = cur.fetchall()
            if (len(lis) != 0):
                winsonson = tk.Tk()
                tk.Label(winsonson, text=str("共")).grid(
                    row=0, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str(len(lis))).grid(
                    row=0, column=1, padx=5, pady=5)
                tk.Label(winsonson, text=str("名列车员")).grid(
                    row=0, column=2, padx=5, pady=5)
                tk.Label(winsonson, text=str("姓名")).grid(
                    row=1, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("身份证号")).grid(
                    row=2, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("所属铁路局id")).grid(
                    row=3, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("工龄")).grid(
                    row=4, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("所属列车长id")).grid(
                    row=5, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("所属铁路局")).grid(
                    row=6, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("所属列车长")).grid(
                    row=7, column=0, padx=5, pady=5)

                for j in range(len(lis)):
                    strr2 = " SELECT * from railwaybeureau where id = " + \
                        str(lis[j][2]) + ";"
                    cur.execute(strr2)
                    liss2 = cur.fetchall()
                    tk.Label(winsonson, text=liss2[0][1]).grid(
                        row=6, column=1 + j, padx=3, pady=5)

                    strr2 = " SELECT * from traincaptain where idcard = '" + \
                        str(lis[j][4]) + "';"
                    print(strr2)
                    cur.execute(strr2)
                    liss2 = cur.fetchall()
                    if(len(liss2) > 0):
                        tk.Label(winsonson, text=liss2[0][0]).grid(
                            row=7, column=1 + j, padx=3, pady=5)

                    for i in range(len(lis[0])):
                        tk.Label(winsonson, text=str(lis[j][i])).grid(
                            row=i + 1, column=1+j, padx=3, pady=5)

            else:
                winsonson = tk.Tk()
                tk.Label(winsonson, text="no findings").grid(row=0)

        tk.Label(winson, text=str("姓名查询")).grid(
            row=0, column=1, padx=10, pady=5)
        tk.Label(winson, text=str("身份证号查询")).grid(
            row=1, column=1, padx=10, pady=5)
        tk.Label(winson, text=str("所属铁路局id查询")).grid(
            row=2, column=1, padx=10, pady=5)
        tk.Label(winson, text=str("工龄下限查询")).grid(
            row=3, column=1, padx=10, pady=5)
        tk.Label(winson, text=str("工龄上限查询")).grid(
            row=4, column=1, padx=10, pady=5)
        tk.Label(winson, text=str("列车长id查询")).grid(
            row=5, column=1, padx=10, pady=5)
        tk.Button(winson, text=str("查找"), command=insee1).grid(
            row=6, column=1, padx=10, pady=5)

    def insert():
        winson = tk.Tk()
        e1 = tk.Entry(winson)
        e1.grid(row=1, column=1, padx=20, pady=5)
        e2 = tk.Entry(winson)
        e2.grid(row=2, column=1, padx=20, pady=5)
        e3 = tk.Entry(winson)
        e3.grid(row=3, column=1, padx=20, pady=5)
        e4 = tk.Entry(winson)
        e4.grid(row=4, column=1, padx=20, pady=5)
        e5 = tk.Entry(winson)
        e5.grid(row=5, column=1, padx=20, pady=5)
        tk.Label(winson, text=str("请输入信息")).grid(
            row=0, column=0, padx=10, pady=5)
        tk.Label(winson, text=str("姓名")).grid(row=1, column=0, padx=5, pady=5)
        tk.Label(winson, text=str("身份证号")).grid(
            row=2, column=0, padx=5, pady=5)
        tk.Label(winson, text=str("所属铁路局id")).grid(
            row=3, column=0, padx=5, pady=5)
        tk.Label(winson, text=str("工龄")).grid(row=4, column=0, padx=5, pady=5)
        tk.Label(winson, text=str("所属列车长id")).grid(
            row=5, column=0, padx=5, pady=5)
        cur = db.cursor()

        def insee():
            strr = " SELECT * from trainserver where idcard = '" + e2.get() + "' ;"
            cur.execute(strr)
            lis = cur.fetchall()
            if (len(lis) != 0):
                winsonson = tk.Tk()
                tk.Label(winsonson, text="error::this primary key has already exsisted").grid(
                    row=0)
            else:
                strr2 = " SELECT * from railwaybeureau where id = " + e3.get() + ";"
                cur.execute(strr2)
                liss2 = cur.fetchall()
                if (len(liss2) == 0):
                    winsonson = tk.Tk()
                    tk.Label(winsonson, text="error::not avaliable").grid(row=0)
                else:

                    strr3 = " SELECT * from traincaptain where idcard = '" + e5.get() + "' ;"
                    cur.execute(strr3)
                    liss3 = cur.fetchall()

                    if(len(liss3) > 0):
                        instr = "INSERT INTO trainserver (name, idcard, beauid, workage, captainnumber) VALUES (" + "'" + e1.get(
                        ) + "'" + "," + "'" + e2.get() + "'" + "," + e3.get() + "," + e4.get() + "," + "'" + e5.get() + "'" + ");"
                    else:
                        instr = "INSERT INTO trainserver (name, idcard, beauid, workage) VALUES (" + "'" + e1.get(
                        ) + "'" + "," + "'" + e2.get() + "'" + "," + e3.get() + "," + e4.get() + ");"

                    print(instr)
                    cur.execute(instr)
                    winson.destroy()
            db.commit()

        tk.Button(winson, text='confirm', width=10, command=insee).grid(
            row=0, column=1, sticky="w", padx=10, pady=5)

    def change():
        cur = db.cursor()
        winson = tk.Tk()
        tk.Label(winson, text="输入身份证号").grid(row=0)

        ee = tk.Entry(winson)
        ee.grid(row=1, column=1, padx=20, pady=5)

        def insee2():
            strr = "SELECT * from trainserver where idcard = '" + ee.get() + "' ;"
            print(strr)
            cur.execute(strr)
            finding = cur.fetchall()
            if len(finding) == 0:
                winson = tk.Tk()
                tk.Label(winson, text="no findings").grid(row=0)
            else:
                winson = tk.Tk()
                tk.Label(winson, text="输入新的信息值").grid(row=0)
                tk.Label(winson, text="工龄").grid(
                    row=2, column=0, padx=10, pady=5)
                tk.Label(winson, text="列车长id").grid(
                    row=3, column=0, padx=10, pady=5)
                e1 = tk.Entry(winson)
                e1.grid(row=2, column=1, padx=20, pady=5)
                e2 = tk.Entry(winson)
                e2.grid(row=3, column=1, padx=20, pady=5)

                def insee():
                    if(len(e1.get()) > 0):
                        instr = "UPDATE trainserver SET workage = " + \
                            e1.get() + " where idcard = '" + ee.get() + "' ;"
                        print(instr)
                        cur.execute(instr)
                    if(len(e2.get()) > 0):
                        instr = "UPDATE trainserver SET captainnumber = '" + \
                            e2.get() + "' where idcard = '" + ee.get() + "' ;"
                        print(instr)
                        cur.execute(instr)

                    winson.destroy()
                    db.commit()

                tk.Button(winson, text='confirm', width=10, command=insee).grid(row=0, column=1, sticky="w", padx=10,
                                                                                pady=5)

        db.commit()
        tk.Button(winson, text='confirm', width=10, command=insee2).grid(
            row=0, column=1, sticky="w", padx=10, pady=5)

    def deletea():
        cur = db.cursor()
        winson = tk.Tk()
        tk.Label(winson, text="输入解雇列车员").grid(row=0)
        ee = tk.Entry(winson)
        ee.grid(row=1, column=1, padx=20, pady=5)

        def insee2():
            strr = "SELECT * from trainserver where idcard = '" + ee.get() + "' ;"
            print(strr)
            cur.execute(strr)
            finding = cur.fetchall()
            if len(finding) == 0:
                winson = tk.Tk()
                tk.Label(winson, text="no findings").grid(row=0)
            else:
                winson2 = tk.Tk()
                tk.Label(winson2, text="确认让它消失了吗？").grid(row=0)
                tk.Label(winson2, text=finding[0][0]).grid(
                    row=1, column=0, padx=5)
                tk.Label(winson2, text=finding[0][1]).grid(
                    row=1, column=1, padx=5)

                def insee():
                    instr = "DELETE FROM traincaptain where idcard = '" + ee.get() + "' ;"
                    print(instr)
                    cur.execute(instr)
                    db.commit()
                    winson2.destroy()

                tk.Button(winson2, text='confirm', width=10, command=insee).grid(row=2, column=0, sticky="w", padx=10,
                                                                                 pady=5)
                tk.Button(winson2, text='no', width=10, command=winson2.destroy).grid(row=2, column=2, sticky="w",
                                                                                      padx=10, pady=5)
                db.commit()

        db.commit()
        tk.Button(winson, text='confirm', width=10, command=insee2).grid(
            row=0, column=1, sticky="w", padx=10, pady=5)

    tk.Button(win, text='查找', width=10, command=search).grid(
        row=1, column=0, sticky="w", padx=10, pady=5)
    tk.Button(win, text='插入', width=10, command=insert).grid(
        row=1, column=2, sticky="w", padx=10, pady=5)
    tk.Button(win, text='修改', width=10, command=change).grid(
        row=1, column=3, sticky="w", padx=10, pady=5)
    tk.Button(win, text='删除', width=10, command=deletea).grid(
        row=1, column=4, sticky="w", padx=10, pady=5)
    win.mainloop()


def openchar9():
    db = pymysql.connect(host="localhost", user="root",
                         password="1234", port=3306, db='mydbtrain')
    win = tk.Tk()
    win.title('安检员主页')
    win.geometry('626x417')

    def search():
        winson = tk.Tk()
        cur = db.cursor()
        e1 = tk.Entry(winson)
        e1.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        e2 = tk.Entry(winson)
        e2.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        e3 = tk.Entry(winson)
        e3.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        e4 = tk.Entry(winson)
        e4.grid(row=3, column=0, sticky="w", padx=10, pady=5)
        e5 = tk.Entry(winson)
        e5.grid(row=4, column=0, sticky="w", padx=10, pady=5)

        def insee1():
            atf2 = False
            atf3 = False
            atf4 = False
            atf5 = False
            strr = " SELECT * from checker where "
            if (e1.get() != ""):
                strr += " name = '" + e1.get() + "' "
                atf2 = True
            if (e2.get() != ""):
                if atf2:
                    strr += "and idcard = '" + e2.get() + "' "
                else:
                    strr += "idcard = '" + e2.get() + "' "
                atf3 = True
            if (e3.get() != ""):
                if atf3 or atf2:
                    strr += "and beauid = " + e3.get() + " "
                else:
                    strr += "beauid  = " + e3.get() + " "
                atf4 = True
            if (e4.get() != ""):
                if atf4 or atf3 or atf2:
                    strr += "and workage >= " + e4.get() + " "
                else:
                    strr += "workage >= " + e4.get() + " "
                atf5 = True
            if (e5.get() != ""):
                if atf5 or atf4 or atf3 or atf2:
                    strr += "and workage <= " + e5.get() + " "
                else:
                    strr += "workage <= " + e5.get() + " "
            print(strr)
            cur.execute(strr)
            lis = cur.fetchall()
            if (len(lis) != 0):
                winsonson = tk.Tk()
                tk.Label(winsonson, text=str("共")).grid(
                    row=0, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str(len(lis))).grid(
                    row=0, column=1, padx=5, pady=5)
                tk.Label(winsonson, text=str("名安检员")).grid(
                    row=0, column=2, padx=5, pady=5)
                tk.Label(winsonson, text=str("姓名")).grid(
                    row=1, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("身份证号")).grid(
                    row=2, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("所属铁路局id")).grid(
                    row=3, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("工龄")).grid(
                    row=4, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("所属铁路局")).grid(
                    row=5, column=0, padx=5, pady=5)

                for j in range(len(lis)):
                    strr2 = " SELECT * from railwaybeureau where id = " + \
                        str(lis[j][2]) + ";"
                    cur.execute(strr2)
                    liss2 = cur.fetchall()
                    tk.Label(winsonson, text=liss2[0][1]).grid(
                        row=5, column=1 + j, padx=3, pady=5)
                    for i in range(len(lis[0])):
                        tk.Label(winsonson, text=str(lis[j][i])).grid(
                            row=i + 1, column=1 + j, padx=3, pady=5)

            else:
                winsonson = tk.Tk()
                tk.Label(winsonson, text="no findings").grid(row=0)

        tk.Label(winson, text=str("姓名查询")).grid(
            row=0, column=1, padx=10, pady=5)
        tk.Label(winson, text=str("身份证号查询")).grid(
            row=1, column=1, padx=10, pady=5)
        tk.Label(winson, text=str("所属铁路局id查询")).grid(
            row=2, column=1, padx=10, pady=5)
        tk.Label(winson, text=str("工龄下限查询")).grid(
            row=3, column=1, padx=10, pady=5)
        tk.Label(winson, text=str("工龄上限查询")).grid(
            row=4, column=1, padx=10, pady=5)
        tk.Button(winson, text=str("查找"), command=insee1).grid(
            row=5, column=1, padx=10, pady=5)

    def insert():
        winson = tk.Tk()
        e1 = tk.Entry(winson)
        e1.grid(row=1, column=1, padx=20, pady=5)
        e2 = tk.Entry(winson)
        e2.grid(row=2, column=1, padx=20, pady=5)
        e3 = tk.Entry(winson)
        e3.grid(row=3, column=1, padx=20, pady=5)
        e4 = tk.Entry(winson)
        e4.grid(row=4, column=1, padx=20, pady=5)
        tk.Label(winson, text=str("请输入信息")).grid(
            row=0, column=0, padx=10, pady=5)
        tk.Label(winson, text=str("姓名")).grid(row=1, column=0, padx=5, pady=5)
        tk.Label(winson, text=str("身份证号")).grid(
            row=2, column=0, padx=5, pady=5)
        tk.Label(winson, text=str("所属铁路局id")).grid(
            row=3, column=0, padx=5, pady=5)
        tk.Label(winson, text=str("工龄")).grid(row=4, column=0, padx=5, pady=5)
        cur = db.cursor()

        def insee():
            strr = " SELECT * from checker where idcard = '" + e2.get() + "' ;"
            cur.execute(strr)
            lis = cur.fetchall()
            if (len(lis) != 0):
                winsonson = tk.Tk()
                tk.Label(winsonson, text="error::this primary key has already exsisted").grid(
                    row=0)
            else:
                strr2 = " SELECT * from railwaybeureau where id = " + e3.get() + ";"
                cur.execute(strr2)
                liss2 = cur.fetchall()
                if (len(liss2) == 0):
                    winsonson = tk.Tk()
                    tk.Label(winsonson, text="error::not avaliable beureau").grid(
                        row=0)
                else:
                    instr = "INSERT INTO checker (name, idcard, beauid, workage) VALUES (" + "'" + e1.get(
                    ) + "'" + "," + "'" + e2.get() + "'" + "," + e3.get() + "," + e4.get() + ");"

                    print(instr)
                    cur.execute(instr)
                    winson.destroy()
            db.commit()

        tk.Button(winson, text='confirm', width=10, command=insee).grid(
            row=0, column=1, sticky="w", padx=10, pady=5)

    def change():
        cur = db.cursor()
        winson = tk.Tk()
        tk.Label(winson, text="输入身份证号").grid(row=0)

        ee = tk.Entry(winson)
        ee.grid(row=1, column=1, padx=20, pady=5)

        def insee2():
            strr = "SELECT * from checker where idcard = '" + ee.get() + "' ;"
            print(strr)
            cur.execute(strr)
            finding = cur.fetchall()
            if len(finding) == 0:
                winson = tk.Tk()
                tk.Label(winson, text="no findings").grid(row=0)
            else:
                winson = tk.Tk()
                tk.Label(winson, text="输入新的信息值").grid(row=0)
                tk.Label(winson, text="工龄").grid(
                    row=2, column=0, padx=10, pady=5)
                e1 = tk.Entry(winson)
                e1.grid(row=1, column=1, padx=20, pady=5)

                def insee():
                    instr = "UPDATE checker SET workage = " + \
                        e1.get() + " where idcard = '" + ee.get() + "' ;"
                    print(instr)
                    cur.execute(instr)
                    winson.destroy()
                    db.commit()

                tk.Button(winson, text='confirm', width=10, command=insee).grid(row=0, column=1, sticky="w", padx=10,
                                                                                pady=5)

        db.commit()
        tk.Button(winson, text='confirm', width=10, command=insee2).grid(
            row=0, column=1, sticky="w", padx=10, pady=5)

    def deletea():
        cur = db.cursor()
        winson = tk.Tk()
        tk.Label(winson, text="输入解雇安检员").grid(row=0)
        ee = tk.Entry(winson)
        ee.grid(row=1, column=1, padx=20, pady=5)

        def insee2():
            strr = "SELECT * from checker where idcard = '" + ee.get() + "' ;"
            print(strr)
            cur.execute(strr)
            finding = cur.fetchall()
            if len(finding) == 0:
                winson = tk.Tk()
                tk.Label(winson, text="no findings").grid(row=0)
            else:
                winson2 = tk.Tk()
                tk.Label(winson2, text="确认让它消失了吗？").grid(row=0)
                tk.Label(winson2, text=finding[0][0]).grid(
                    row=1, column=0, padx=5)
                tk.Label(winson2, text=finding[0][1]).grid(
                    row=1, column=1, padx=5)

                def insee():
                    instr = "DELETE FROM checker where idcard = '" + ee.get() + "' ;"
                    print(instr)
                    cur.execute(instr)
                    db.commit()
                    winson2.destroy()

                tk.Button(winson2, text='confirm', width=10, command=insee).grid(row=2, column=0, sticky="w", padx=10,
                                                                                 pady=5)
                tk.Button(winson2, text='no', width=10, command=winson2.destroy).grid(row=2, column=2, sticky="w",
                                                                                      padx=10, pady=5)
                db.commit()

        db.commit()
        tk.Button(winson, text='confirm', width=10, command=insee2).grid(
            row=0, column=1, sticky="w", padx=10, pady=5)

    tk.Button(win, text='查找', width=10, command=search).grid(
        row=1, column=0, sticky="w", padx=10, pady=5)
    tk.Button(win, text='插入', width=10, command=insert).grid(
        row=1, column=2, sticky="w", padx=10, pady=5)
    tk.Button(win, text='修改', width=10, command=change).grid(
        row=1, column=3, sticky="w", padx=10, pady=5)
    tk.Button(win, text='删除', width=10, command=deletea).grid(
        row=1, column=4, sticky="w", padx=10, pady=5)
    win.mainloop()


def openchar10():
    db = pymysql.connect(host="localhost", user="root",
                         password="1234", port=3306, db='mydbtrain')
    win = tk.Tk()
    win.title('车皮检查清单')
    win.geometry('626x417')

    def search():
        winson = tk.Tk()
        cur = db.cursor()
        e1 = tk.Entry(winson)
        e1.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        e2 = tk.Entry(winson)
        e2.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        e3 = tk.Entry(winson)
        e3.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        e4 = tk.Entry(winson)
        e4.grid(row=3, column=0, sticky="w", padx=10, pady=5)
        e5 = tk.Entry(winson)
        e5.grid(row=4, column=0, sticky="w", padx=10, pady=5)

        def insee1():
            atf2 = False
            atf3 = False
            atf4 = False
            atf5 = False
            strr = " SELECT * from checklist where "
            if (e1.get() != ""):
                strr += " id = " + e1.get() + " "
                atf2 = True
            if (e2.get() != ""):
                if atf2:
                    strr += "and coachid = " + e2.get() + " "
                else:
                    strr += "coachid = " + e2.get() + " "
                atf3 = True
            if (e3.get() != ""):
                if atf3 or atf2:
                    strr += "and timedate = '" + e3.get() + "' "
                else:
                    strr += "timadate  = '" + e3.get() + "' "
                atf4 = True
            if (e4.get() != ""):
                if atf4 or atf3 or atf2:
                    strr += "and checkerid = '" + e4.get() + "' "
                else:
                    strr += "checkerid = '" + e4.get() + "' "
                atf5 = True
            if (e5.get() != ""):
                if atf5 or atf4 or atf3 or atf2:
                    strr += "and result= '" + e5.get() + "' "
                else:
                    winsonson = tk.Tk()
                    tk.Label(winsonson, text=str("非法输入")).grid(
                        row=0, column=0, padx=5, pady=5)
            print(strr)
            cur.execute(strr)
            lis = cur.fetchall()
            if (len(lis) != 0):
                winsonson = tk.Tk()
                tk.Label(winsonson, text=str("共")).grid(
                    row=0, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str(len(lis))).grid(
                    row=0, column=1, padx=5, pady=5)
                tk.Label(winsonson, text=str("次检测记录")).grid(
                    row=0, column=2, padx=5, pady=5)
                tk.Label(winsonson, text=str("车厢号")).grid(
                    row=1, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("检测业务流水号")).grid(
                    row=2, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("检测时间")).grid(
                    row=3, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("检测员id")).grid(
                    row=4, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("检测部分")).grid(
                    row=5, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("检测结果")).grid(
                    row=6, column=0, padx=5, pady=5)
                tk.Label(winsonson, text=str("检测员")).grid(
                    row=7, column=0, padx=5, pady=5)

                for j in range(len(lis)):
                    strr2 = " SELECT * from checker where idcard = '" + \
                        str(lis[j][3]) + "';"
                    cur.execute(strr2)
                    liss2 = cur.fetchall()
                    tk.Label(winsonson, text=liss2[0][0]).grid(
                        row=7, column=1 + j, padx=3, pady=5)
                    for i in range(len(lis[0])):
                        tk.Label(winsonson, text=str(lis[j][i])).grid(
                            row=i + 1, column=1 + j, padx=3, pady=5)

            else:
                winsonson = tk.Tk()
                tk.Label(winsonson, text="no findings").grid(row=0)

        tk.Label(winson, text=str("作业流水号查询")).grid(
            row=0, column=1, padx=10, pady=5)
        tk.Label(winson, text=str("车厢号查询")).grid(
            row=1, column=1, padx=10, pady=5)
        tk.Label(winson, text=str("日期查询")).grid(
            row=2, column=1, padx=10, pady=5)
        tk.Label(winson, text=str("检测员id查询")).grid(
            row=3, column=1, padx=10, pady=5)
        tk.Label(winson, text=str("检测结果查询")).grid(
            row=4, column=1, padx=10, pady=5)
        tk.Button(winson, text=str("查找"), command=insee1).grid(
            row=5, column=1, padx=10, pady=5)

    def insert():
        winson = tk.Tk()
        e1 = tk.Entry(winson)
        e1.grid(row=1, column=1, padx=20, pady=5)
        e2 = tk.Entry(winson)
        e2.grid(row=2, column=1, padx=20, pady=5)
        e3 = tk.Entry(winson)
        e3.grid(row=3, column=1, padx=20, pady=5)
        e4 = tk.Entry(winson)
        e4.grid(row=4, column=1, padx=20, pady=5)
        e5 = tk.Entry(winson)
        e5.grid(row=5, column=1, padx=20, pady=5)
        e6 = tk.Entry(winson)
        e6.grid(row=6, column=1, padx=20, pady=5)
        tk.Label(winson, text=str("请输入信息")).grid(
            row=0, column=0, padx=10, pady=5)
        tk.Label(winson, text=str("车厢号")).grid(row=1, column=0, padx=5, pady=5)
        tk.Label(winson, text=str("检测流水号")).grid(
            row=2, column=0, padx=5, pady=5)
        tk.Label(winson, text=str("时间")).grid(row=3, column=0, padx=5, pady=5)
        tk.Label(winson, text=str("检测员id")).grid(
            row=4, column=0, padx=5, pady=5)
        tk.Label(winson, text=str("检测部分")).grid(
            row=5, column=0, padx=5, pady=5)
        tk.Label(winson, text=str("检测结果评定")).grid(
            row=6, column=0, padx=5, pady=5)
        cur = db.cursor()

        def insee():
            strr = " SELECT * from checklist where id = '" + e2.get() + "' ;"
            cur.execute(strr)
            lis = cur.fetchall()
            if (len(lis) != 0):
                winsonson = tk.Tk()
                tk.Label(winsonson, text="error::this primary key has already exsisted").grid(
                    row=0)
            else:
                strr2 = " SELECT * from checker where idcard = " + e4.get() + ";"
                cur.execute(strr2)
                liss2 = cur.fetchall()
                strr3 = " SELECT * from traincoach where id = " + e1.get() + ";"
                cur.execute(strr3)
                liss3 = cur.fetchall()
                if (len(liss2) == 0 or len(liss3) == 0):
                    winsonson = tk.Tk()
                    tk.Label(winsonson, text="error::not avaliable").grid(row=0)
                else:
                    instr = "INSERT INTO checklist (coachid, id, timedate, checkerid, checkpart, result) VALUES (" + e1.get(
                    ) + "," + e2.get() + ", '" + e3.get() + "' , '" + e4.get() + "' , '" + e5.get() + "' , '" + e6.get() + "' );"

                    print(instr)
                    cur.execute(instr)
                    winson.destroy()
            db.commit()

        tk.Button(winson, text='confirm', width=10, command=insee).grid(
            row=0, column=1, sticky="w", padx=10, pady=5)

    def change():
        cur = db.cursor()
        winson = tk.Tk()
        tk.Label(winson, text="检测流水号").grid(row=0)

        ee = tk.Entry(winson)
        ee.grid(row=1, column=1, padx=20, pady=5)

        def insee2():
            strr = "SELECT * from chacklist where id = " + ee.get() + " ;"
            print(strr)
            cur.execute(strr)
            finding = cur.fetchall()
            if len(finding) == 0:
                winson = tk.Tk()
                tk.Label(winson, text="no findings").grid(row=0)
            else:
                winson = tk.Tk()
                tk.Label(winson, text="输入新的信息值").grid(row=0)
                tk.Label(winson, text="检测内容").grid(
                    row=1, column=0, padx=10, pady=5)
                tk.Label(winson, text="检测等级").grid(
                    row=2, column=0, padx=10, pady=5)
                e1 = tk.Entry(winson)
                e1.grid(row=1, column=1, padx=20, pady=5)
                e2 = tk.Entry(winson)
                e2.grid(row=2, column=1, padx=20, pady=5)

                def insee():
                    instr = "UPDATE checklist SET checkpart = '" + e1.get() + "' , result = '" + \
                        e2.get() + "' where idcard = '" + ee.get() + "' ;"
                    print(instr)
                    cur.execute(instr)
                    winson.destroy()
                    db.commit()

                tk.Button(winson, text='confirm', width=10, command=insee).grid(row=0, column=1, sticky="w", padx=10,
                                                                                pady=5)

        db.commit()
        tk.Button(winson, text='confirm', width=10, command=insee2).grid(
            row=0, column=1, sticky="w", padx=10, pady=5)

    def deletea():
        cur = db.cursor()
        winson = tk.Tk()
        tk.Label(winson, text="输入要删除的检测流水号").grid(row=0)
        ee = tk.Entry(winson)
        ee.grid(row=1, column=1, padx=20, pady=5)

        def insee2():
            strr = "SELECT * from checklist where id = " + ee.get() + " ;"
            print(strr)
            cur.execute(strr)
            finding = cur.fetchall()
            if len(finding) == 0:
                winson = tk.Tk()
                tk.Label(winson, text="no findings").grid(row=0)
            else:
                winson2 = tk.Tk()
                tk.Label(winson2, text="确认让它消失了吗？").grid(row=0)
                tk.Label(winson2, text=finding[0][0]).grid(
                    row=1, column=0, padx=5)
                tk.Label(winson2, text=finding[0][1]).grid(
                    row=1, column=1, padx=5)

                def insee():
                    instr = "DELETE FROM checklist where id " + ee.get() + " ;"
                    print(instr)
                    cur.execute(instr)
                    db.commit()
                    winson2.destroy()

                tk.Button(winson2, text='confirm', width=10, command=insee).grid(row=2, column=0, sticky="w", padx=10,
                                                                                 pady=5)
                tk.Button(winson2, text='no', width=10, command=winson2.destroy).grid(row=2, column=2, sticky="w",
                                                                                      padx=10, pady=5)
                db.commit()

        db.commit()
        tk.Button(winson, text='confirm', width=10, command=insee2).grid(
            row=0, column=1, sticky="w", padx=10, pady=5)

    tk.Button(win, text='查找', width=10, command=search).grid(
        row=1, column=0, sticky="w", padx=10, pady=5)
    tk.Button(win, text='插入', width=10, command=insert).grid(
        row=1, column=2, sticky="w", padx=10, pady=5)
    tk.Button(win, text='修改', width=10, command=change).grid(
        row=1, column=3, sticky="w", padx=10, pady=5)
    tk.Button(win, text='删除', width=10, command=deletea).grid(
        row=1, column=4, sticky="w", padx=10, pady=5)
    win.mainloop()


def openchar11():
    pass


def openchar12():
    db = pymysql.connect(host="localhost", user="root",
                         password="1234", port=3306, db='mydbtrain')
    win = tk.Tk()
    win.title('提高姿势水平之后的查询')
    win.geometry('626x417')

    def select1():
        cur = db.cursor()
        winson = tk.Tk()
        tk.Label(winson, text="列车紧急事故，列车长紧急联系安检员").grid(row=0)
        tk.Label(winson, text="输入列车长id").grid(row=1, column=0)
        ee = tk.Entry(winson)
        ee.grid(row=1, column=1, padx=20, pady=5)

        def contact():
            winsons = tk.Tk()
            tk.Label(winsons, text="message has sent").grid(row=1)

        def search():
            instr = "select beauid from traincaptain where idcard = '" + ee.get() + "' ;"
            print(instr)
            cur.execute(instr)
            liss = cur.fetchall()
            if len(liss) == 0:
                winsons = tk.Tk()
                tk.Label(winsons, text="no findings").grid(row=0)
            else:
                instr = "SELECT b.name, b.idcard, b.workage FROM traincaptain as a join checker as b on a.beauid = b.beauid where a.beauid = " + \
                    str(liss[0][0]) + " ;"
                print(instr)
                cur.execute(instr)
                liss2 = cur.fetchall()
                tk.Label(winson, text="姓名").grid(
                    row=2, column=0, padx=5, pady=5)
                tk.Label(winson, text="身份证号").grid(
                    row=2, column=1, padx=5, pady=5)
                tk.Label(winson, text="工龄").grid(
                    row=2, column=2, padx=5, pady=5)
                for i in range(len(liss2)):
                    for j in range(len(liss2[i])):
                        tk.Label(winson, text=liss2[i][j]).grid(
                            row=3 + i, column=j, padx=5, pady=5)

                    ee1 = tk.Entry(winson)
                    ee1.grid(row=3 + i, column=1 +
                             len(liss2[i]), padx=20, pady=5)
                    tk.Button(winson, text='联系他', width=10, command=contact).grid(
                        row=3 + i, column=2+len(liss2[i]), sticky="w", padx=10, pady=5)
        tk.Button(winson, text='查找', width=10, command=search).grid(
            row=1, column=2, sticky="w", padx=10, pady=5)

    def select2():
        cur = db.cursor()
        winson = tk.Tk()
        tk.Label(winson, text="检查某车次所用车皮的检测结果").grid(row=0)
        tk.Label(winson, text="输入车次，日期").grid(row=1, column=0)
        ee = tk.Entry(winson)
        ee.grid(row=1, column=1, padx=20, pady=5)
        ee2 = tk.Entry(winson)
        ee2.grid(row=2, column=1, padx=20, pady=5)
        # select * from checklist where coachid in (select id from traincoach where trainnub = 'Z18' and traindate = 20200702);

        def search():
            instr = "select id from traincoach where trainnub = '" + \
                ee.get() + "' and traindate = " + ee2.get() + ";"
            print(instr)
            cur.execute(instr)
            liss = cur.fetchall()
            if len(liss) == 0:
                winsons = tk.Tk()
                tk.Label(winsons, text="no findings").grid(row=0)
            else:
                instrr = "select * from checklist where coachid in (" + instr[0:len(
                    instr)-1] + ");"
                print(instrr)
                cur.execute(instrr)
                liss2 = cur.fetchall()
                tk.Label(winson, text="车厢号").grid(
                    row=3, column=0, padx=5, pady=5)
                tk.Label(winson, text="作业流水号").grid(
                    row=3, column=1, padx=5, pady=5)
                tk.Label(winson, text="检测时间").grid(
                    row=3, column=2, padx=5, pady=5)
                tk.Label(winson, text="检测员身份证号").grid(
                    row=3, column=3, padx=5, pady=5)
                tk.Label(winson, text="检测部分").grid(
                    row=3, column=4, padx=5, pady=5)
                tk.Label(winson, text="检测结果").grid(
                    row=3, column=5, padx=5, pady=5)
                tk.Label(winson, text="检测员姓名").grid(
                    row=3, column=6, padx=5, pady=5)
                for i in range(len(liss2)):
                    for j in range(len(liss2[i])):
                        tk.Label(winson, text=liss2[i][j]).grid(
                            row=4 + i, column=j, padx=5, pady=5)
                    strr2 = " SELECT * from checker where idcard = '" + \
                        str(liss2[i][3]) + "';"
                    cur.execute(strr2)
                    liss = cur.fetchall()
                    tk.Label(winson, text=liss[0][0]).grid(
                        row=4 + i, column=len(liss2[i]), padx=3, pady=5)
        tk.Button(winson, text='查找', width=10, command=search).grid(
            row=2, column=2, sticky="w", padx=10, pady=5)

    def select3():
        cur = db.cursor()
        winson = tk.Tk()
        tk.Label(winson, text="查询各铁路局年龄段的员工").grid(row=0)
        tk.Label(winson, text="输入年龄下限和上限").grid(row=1, column=0)
        ee = tk.Entry(winson)
        ee.grid(row=1, column=1, padx=20, pady=5)
        ee2 = tk.Entry(winson)
        ee2.grid(row=2, column=1, padx=20, pady=5)

        def search1():
            # SELECT count(*),beureauid from traindriver where workage >= 0 and workage <= 144 group by beureauid;
            instrr = "SELECT count(*),beureauid from traindriver where workage >= " + \
                ee.get() + " and workage <= " + ee2.get() + " group by beureauid;"
            print(instrr)
            cur.execute(instrr)
            liss2 = cur.fetchall()
            tk.Label(winson, text="人数").grid(row=4, column=0, padx=5, pady=5)
            tk.Label(winson, text="铁路局id").grid(
                row=4, column=1, padx=5, pady=5)
            tk.Label(winson, text="铁路局").grid(row=4, column=2, padx=5, pady=5)
            for i in range(len(liss2)):
                for j in range(len(liss2[i])):
                    tk.Label(winson, text=liss2[i][j]).grid(
                        row=5 + i, column=j, padx=5, pady=5)
                strr2 = " SELECT * from railwaybeureau where id = '" + \
                    str(liss2[i][1]) + "';"
                cur.execute(strr2)
                liss = cur.fetchall()
                tk.Label(winson, text=liss[0][1]).grid(
                    row=5 + i, column=len(liss2[i]), padx=3, pady=5)

        def search2():
            instrr = "SELECT count(*),beauid from trainserver where workage >= " + \
                ee.get() + " and workage <= " + ee2.get() + " group by beauid;"
            print(instrr)
            cur.execute(instrr)
            liss2 = cur.fetchall()
            tk.Label(winson, text="人数").grid(row=4, column=0, padx=5, pady=5)
            tk.Label(winson, text="铁路局id").grid(
                row=4, column=1, padx=5, pady=5)
            tk.Label(winson, text="铁路局").grid(row=4, column=2, padx=5, pady=5)
            for i in range(len(liss2)):
                for j in range(len(liss2[i])):
                    tk.Label(winson, text=liss2[i][j]).grid(
                        row=5 + i, column=j, padx=5, pady=5)
                strr2 = " SELECT * from railwaybeureau where id = '" + \
                    str(liss2[i][1]) + "';"
                cur.execute(strr2)
                liss = cur.fetchall()
                tk.Label(winson, text=liss[0][1]).grid(
                    row=5 + i, column=len(liss2[i]), padx=3, pady=5)

        def search3():
            instrr = "SELECT count(*),beauid from traincaptain where workage >= " + \
                ee.get() + " and workage <= " + ee2.get() + " group by beauid;"
            print(instrr)
            cur.execute(instrr)
            liss2 = cur.fetchall()
            tk.Label(winson, text="人数").grid(row=4, column=0, padx=5, pady=5)
            tk.Label(winson, text="铁路局id").grid(
                row=4, column=1, padx=5, pady=5)
            tk.Label(winson, text="铁路局").grid(row=4, column=2, padx=5, pady=5)
            for i in range(len(liss2)):
                for j in range(len(liss2[i])):
                    tk.Label(winson, text=liss2[i][j]).grid(
                        row=5 + i, column=j, padx=5, pady=5)
                strr2 = " SELECT * from railwaybeureau where id = '" + \
                    str(liss2[i][1]) + "';"
                cur.execute(strr2)
                liss = cur.fetchall()
                tk.Label(winson, text=liss[0][1]).grid(
                    row=5 + i, column=len(liss2[i]), padx=3, pady=5)
        tk.Button(winson, text='司机', width=10, command=search1).grid(
            row=3, column=0, sticky="w", padx=10, pady=5)
        tk.Button(winson, text='列车员', width=10, command=search2).grid(
            row=3, column=1, sticky="w", padx=10, pady=5)
        tk.Button(winson, text='列车长', width=10, command=search3).grid(
            row=3, column=2, sticky="w", padx=10, pady=5)

    def select4():
        # SELECT * FROM `checklist` WHERE MATCH(`checkpart`) AGAINST ('受电弓');
        cur = db.cursor()
        winson = tk.Tk()
        tk.Label(winson, text="查询各铁车皮检测作业内容").grid(row=0)
        tk.Label(winson, text="输入年龄下限和上限").grid(row=1, column=0)
        ee = tk.Entry(winson)
        ee.grid(row=1, column=1, padx=20, pady=5)

        def search():
            instrr = "SELECT * FROM `checklist` WHERE MATCH(`checkpart`) AGAINST ('" + ee.get(
            ) + "');"
            print(instrr)
            cur.execute(instrr)
            liss2 = cur.fetchall()
            tk.Label(winson, text="车皮").grid(row=4, column=0, padx=5, pady=5)
            tk.Label(winson, text="流水号").grid(row=4, column=1, padx=5, pady=5)
            tk.Label(winson, text="时间").grid(row=4, column=2, padx=5, pady=5)
            tk.Label(winson, text="检测员id").grid(
                row=4, column=3, padx=5, pady=5)
            tk.Label(winson, text="检测部分").grid(row=4, column=4, padx=5, pady=5)
            tk.Label(winson, text="检测结果").grid(row=4, column=5, padx=5, pady=5)
            tk.Label(winson, text="检测员").grid(row=4, column=6, padx=5, pady=5)

            for i in range(len(liss2)):
                for j in range(len(liss2[i])):
                    tk.Label(winson, text=liss2[i][j]).grid(
                        row=5 + i, column=j, padx=5, pady=5)
                strr2 = strr2 = " SELECT * from checker where idcard = '" + \
                    str(liss2[i][3]) + "';"
                cur.execute(strr2)
                liss = cur.fetchall()
                tk.Label(winson, text=liss[0][0]).grid(
                    row=5 + i, column=len(liss2[i]), padx=3, pady=5)
        tk.Button(winson, text='查询', width=10, command=search).grid(
            row=3, column=3, sticky="w", padx=10, pady=5)
    tk.Button(win, text='连接查询', width=10, command=select1).grid(
        row=1, column=0, sticky="w", padx=10, pady=5)
    tk.Button(win, text='嵌套查询', width=10, command=select2).grid(
        row=1, column=2, sticky="w", padx=10, pady=5)
    tk.Button(win, text='分组查询', width=10, command=select3).grid(
        row=1, column=3, sticky="w", padx=10, pady=5)
    tk.Button(win, text='查询其它', width=10, command=select4).grid(
        row=1, column=4, sticky="w", padx=10, pady=5)
    win.mainloop()

# 로그인 성공시 여기로 옴


def hongbaoshu():
    db = pymysql.connect(host="localhost", user="root",
                         password="1234", port=3306, db='mydbtrain')
    win = tk.Tk()
    win.title('0002')
    win.geometry('426x217')
    tk.Label(win, text="请选择需要查看的服务").grid(row=0, sticky="w")
    tk.Button(win, text='铁路局', width=10, command=openchar1).grid(
        row=1, column=0, sticky="w", padx=10, pady=5)
    tk.Button(win, text='火车站', width=10, command=openchar2).grid(
        row=1, column=1, sticky="w", padx=10, pady=5)
    tk.Button(win, text='站台', width=10, command=openchar3).grid(
        row=1, column=2, sticky="w", padx=10, pady=5)
    tk.Button(win, text='车次', width=10, command=openchar4).grid(
        row=2, column=0, sticky="w", padx=10, pady=5)
    tk.Button(win, text='车皮', width=10, command=openchar5).grid(
        row=2, column=1, sticky="w", padx=10, pady=5)
    tk.Button(win, text='司机', width=10, command=openchar6).grid(
        row=2, column=2, sticky="w", padx=10, pady=5)
    tk.Button(win, text='列车长', width=10, command=openchar7).grid(
        row=3, column=0, sticky="w", padx=10, pady=5)
    tk.Button(win, text='列车员', width=10, command=openchar8).grid(
        row=3, column=1, sticky="w", padx=10, pady=5)
    tk.Button(win, text='检测员', width=10, command=openchar9).grid(
        row=3, column=2, sticky="w", padx=10, pady=5)
    tk.Button(win, text='检测记录', width=10, command=openchar10).grid(
        row=4, column=1, sticky="w", padx=10, pady=5)
    tk.Button(win, text='退出', width=10, command=win.destroy).grid(
        row=4, column=0, sticky="w", padx=10, pady=5)
    tk.Button(win, text='高级查询', width=10, command=openchar12).grid(
        row=4, column=2, sticky="w", padx=10, pady=5)
    win.mainloop()


if __name__ == '__main__':
    # hongbaoshu()
    birthInYangzhou()

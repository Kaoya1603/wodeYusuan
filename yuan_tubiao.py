import sqlite3
import matplotlib.pyplot as plt


def huaqilai_yuan_tubiao():
    cur = sqlite3.connect('wode_huafei.db').cursor()

    zhonglei = list(map(lambda x: x[0], cur.execute('SELECT title FROM zhonglei').fetchall()))
    zhonglei1 = list()

    zonghe = list()
    for i in range(len(zhonglei)):
        a = list(map(lambda x: x[0], cur.execute('SELECT сумма FROM huafei WHERE категория = ?', [zhonglei[i]]).fetchall()))
        if sum(a) > 0:
            zonghe.append(sum(a))
            if zhonglei[i] == 'коммунальные платежи':
                zhonglei[i] = 'коммунальные' + '\n' + 'платежи'
            zhonglei1.append(zhonglei[i])

    fig1, ax1 = plt.subplots()
    ax1.pie(zonghe, labels=zhonglei1, autopct='%1.1f%%',
            shadow=True, startangle=90)
    plt.savefig('yuan_tubiao.png')


huaqilai_yuan_tubiao()
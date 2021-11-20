import sys
import sqlite3
from PIL import Image

from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCalendarWidget, QLabel, \
    QCheckBox, QInputDialog, QScrollArea, QVBoxLayout, QMessageBox, QTableWidgetItem, QTableWidget, QComboBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Мой бюджет')
        self.setStyleSheet("background-color: #F5DEB3;")

        self.biaoti = QLabel('Мой бюджет', self)
        self.biaoti.move(220, 100)

        self.rili_anniu = QPushButton('Открыть календарь', self)
        self.rili_anniu.setGeometry(150, 180, 300, 35)
        self.rili_anniu.setStyleSheet(
            "border: 0;\n"
            "border-radius: 15px;\n"
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 172, 235), stop:1 rgba(72,102,175));\n"
            "color: #FFFFFF;\n"
            "padding: 8px 16px;\n"
            "font-size: 16px;")
        self.rili_anniu.clicked.connect(self.dakai_riliwindow)

        self.tongji_anniu = QPushButton('Просмотр статистики', self)
        self.tongji_anniu.setGeometry(150, 230, 300, 35)
        self.tongji_anniu.setStyleSheet(
            "border: 0;\n"
            "border-radius: 15px;\n"
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 172, 235), stop:1 rgba(72,102,175));\n"
            "color: #FFFFFF;\n"
            "padding: 8px 16px;\n"
            "font-size: 16px;")
        self.tongji_anniu.clicked.connect(self.dakai_tongjiwindow)

        self.gaibian_zhonglei_qingdan = QPushButton('Редактировать перечень категорий', self)
        self.gaibian_zhonglei_qingdan.setGeometry(150, 280, 300, 35)
        self.gaibian_zhonglei_qingdan.setStyleSheet(
            "border: 0;\n"
            "border-radius: 15px;\n"
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 172, 235), stop:1 rgba(72,102,175));\n"
            "color: #FFFFFF;\n"
            "padding: 8px 16px;\n"
            "font-size: 16px;")
        self.gaibian_zhonglei_qingdan.clicked.connect(self.dakai_zhongleiwindow)

    def dakai_riliwindow(self):
        self.riliwindow = RiliWindow()
        self.riliwindow.show()
        self.hide()

    def dakai_zhongleiwindow(self):
        self.zhongleiwindow = ZhongleiWindow()
        self.zhongleiwindow.show()
        self.hide()

    def dakai_tongjiwindow(self):
        self.tongjiwindow = TongjiWindow()
        self.tongjiwindow.show()
        self.hide()


class TongjiWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Моя статистика')
        self.setStyleSheet("background-color: #F5DEB3;")

        self.huidao_mainwindow_anniu = QPushButton('<-- на главный экран', self)
        self.huidao_mainwindow_anniu.setGeometry(10, 5, 200, 35)
        self.huidao_mainwindow_anniu.setStyleSheet(
            "border: 0;\n"
            "border-radius: 15px;\n"
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 172, 235), stop:1 rgba(72,102,175));\n"
            "color: #FFFFFF;\n"
            "padding: 8px 16px;\n"
            "font-size: 16px;")
        self.huidao_mainwindow_anniu.clicked.connect(self.huidao_mainwindow)

        self.yuan_tubiao = QPixmap('yuan_tubiao')

        self.zhanshi_1 = QLabel(self)
        self.zhanshi_1.move(15, 45)
        self.zhanshi_1.setPixmap(self.yuan_tubiao)

        tupian = Image.open('yuan_tubiao.png')
        x, y = tupian.size

        self.setGeometry(300, 300, x + 35, y + 55)

    def huidao_mainwindow(self):
        self.mainwindow = MainWindow()
        self.mainwindow.show()
        self.hide()


class ZhongleiWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.out = list()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Редактирование перечня категорий')

        self.huilai_anniu = QPushButton('<-- На главный экран', self)
        self.huilai_anniu.setGeometry(5, 5, 200, 35)
        self.huilai_anniu.setStyleSheet(
            "border: 0;\n"
            "border-radius: 15px;\n"
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 172, 235), stop:1 rgba(72,102,175));\n"
            "color: #FFFFFF;\n"
            "padding: 8px 16px;\n"
            "font-size: 16px;")
        self.huilai_anniu.clicked.connect(self.huidao_mainwindow)

        self.tianjia_zhonglei_anniu = QPushButton('+', self)
        self.tianjia_zhonglei_anniu.setGeometry(430, 5, 50, 35)
        self.tianjia_zhonglei_anniu.setStyleSheet(
            "border: 0;\n"
            "border-radius: 15px;\n"
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 172, 235), stop:1 rgba(72,102,175));\n"
            "color: #FFFFFF;\n"
            "padding: 8px 16px;\n"
            "font-size: 16px;")
        self.tianjia_zhonglei_anniu.clicked.connect(self.tianjia_zhonglei)

        self.scrollarea = QScrollArea(self)
        self.widget = QWidget(self)
        self.vbox = QVBoxLayout(self)

        self.jiazai_database()

        self.widget.setLayout(self.vbox)
        self.scrollarea.setWidget(self.widget)
        self.scrollarea.setWidgetResizable(True)
        self.scrollarea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollarea.setGeometry(50, 50, 500, 300)

        self.yichu_zhonglei_anniu = QPushButton('удалить', self)
        self.yichu_zhonglei_anniu.setGeometry(490, 5, 100, 35)
        self.yichu_zhonglei_anniu.setStyleSheet(
            "border: 0;\n"
            "border-radius: 15px;\n"
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 172, 235), stop:1 rgba(72,102,175));\n"
            "color: #FFFFFF;\n"
            "padding: 8px 16px;\n"
            "font-size: 16px;")
        self.yichu_zhonglei_anniu.setEnabled(False)
        self.yichu_zhonglei_anniu.clicked.connect(self.yichu_zhonglei)

    def jiazai_database(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('wode_huafei.db')
        db.open()

        query = QSqlQuery()
        query.exec_('SELECT * FROM zhonglei')

        query.first()
        c = 1

        while query.isValid():
            zhonglei = query.value(1)
            self.zhonglei = QCheckBox(zhonglei, self)
            self.zhonglei.move(50, 50 * c)
            self.zhonglei.setStyleSheet('font-size: 12pt;')
            self.zhonglei.stateChanged.connect(self.zhuangtai_gaibian)
            self.vbox.addWidget(self.zhonglei)
            c += 1
            query.next()

    def zhuangtai_gaibian(self, state):
        if state == Qt.Checked:
            self.out.append(self.sender().text())
            self.yichu_zhonglei_anniu.setEnabled(True)
        else:
            self.out.remove(self.sender().text())
            self.yichu_zhonglei_anniu.setEnabled(False if not self.out else True)

    def tianjia_zhonglei(self):
        mingcheng, ok_pressed = QInputDialog.getText(self, "Добавление категории",
                                                     "Как называется новая категория расходов?")
        if ok_pressed:
            if mingcheng:
                query = QSqlQuery()
                query.prepare('INSERT INTO zhonglei(title) VALUES(?);')
                query.addBindValue(mingcheng)
                query.exec()

                for x in reversed(range(self.vbox.count())):
                    self.vbox.itemAt(x).widget().setParent(None)
                self.jiazai_database()
            else:
                QMessageBox.critical(self, 'ошибка!', "Совершен некорректный ввод")
                self.tianjia_zhonglei()

    def yichu_zhonglei(self):
        for i in self.out:
            query = QSqlQuery()
            query.prepare('DELETE FROM zhonglei WHERE title =(?)')
            query.addBindValue(i)
            query.exec()

            for x in reversed(range(self.vbox.count())):
                self.vbox.itemAt(x).widget().setParent(None)
            self.jiazai_database()

    def huidao_mainwindow(self):
        self.mainwindow = MainWindow()
        self.mainwindow.show()
        self.hide()


class RiliWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Календарь')

        self.huilai_anniu = QPushButton('<-- На главный экран', self)
        self.huilai_anniu.setGeometry(5, 5, 200, 35)
        self.huilai_anniu.setStyleSheet(
            "border: 0;\n"
            "border-radius: 15px;\n"
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 172, 235), stop:1 rgba(72,102,175));\n"
            "color: #FFFFFF;\n"
            "padding: 8px 16px;\n"
            "font-size: 16px;")
        self.huilai_anniu.clicked.connect(self.huidao_mainwindow)

        self.rili = QCalendarWidget(self)
        self.rili.setGeometry(5, 50, 590, 300)
        self.rili.clicked.connect(self.jiacha_mouzhong_rizi)

    def huidao_mainwindow(self):
        self.mainwindow = MainWindow()
        self.mainwindow.show()
        self.hide()

    def jiacha_mouzhong_rizi(self):
        self.mouzong_rizi = MouzhongRizi(self.rili.selectedDate().day(), self.rili.selectedDate().month(),
                                         self.rili.selectedDate().year())
        self.mouzong_rizi.show()
        self.hide()


class MouzhongRizi(QWidget):
    def __init__(self, rizi, yue, nian):
        super().__init__()
        self.dangshi_rizi = rizi
        self.dangshi_yue = yue
        self.dangshi_nian = nian
        self.yue = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                    'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
        self.initUi()

    def initUi(self):
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle(f'{self.dangshi_rizi} {self.yue[self.dangshi_yue - 1]}')
        self.setStyleSheet("background-color: #F5DEB3;")

        self.rizi = QLabel(f'{self.dangshi_rizi} {self.yue[self.dangshi_yue - 1]}', self)
        self.rizi.move(18, 48)

        self.huilai_anniu = QPushButton('<-- Назад', self)
        self.huilai_anniu.setGeometry(5, 5, 150, 35)
        self.huilai_anniu.setStyleSheet(
            "border: 0;\n"
            "border-radius: 15px;\n"
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 172, 235), stop:1 rgba(72,102,175));\n"
            "color: #FFFFFF;\n"
            "padding: 8px 16px;\n"
            "font-size: 16px;")
        self.huilai_anniu.clicked.connect(self.huidao_riliwindow)

        self.gaibian_mouzhong_rizi_huafei_biaoge_anniu = QPushButton('Редактировать таблицу расходов', self)
        self.gaibian_mouzhong_rizi_huafei_biaoge_anniu.setGeometry(290, 50, 300, 35)
        self.gaibian_mouzhong_rizi_huafei_biaoge_anniu.setStyleSheet(
            "border: 0;\n"
            "border-radius: 15px;\n"
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 172, 235), stop:1 rgba(72,102,175));\n"
            "color: #FFFFFF;\n"
            "padding: 8px 16px;\n"
            "font-size: 16px;")
        self.gaibian_mouzhong_rizi_huafei_biaoge_anniu.clicked.connect(self.dakai_gaibian_mouzhong_rizi_huafei_biaoge)

        self.con = sqlite3.connect('wode_huafei.db')
        self.cur = self.con.cursor()
        dangshi_biaoge = self.cur.execute(f'''SELECT категория,сумма FROM huafei WHERE дата = 
                                    "{self.dangshi_rizi}.{self.dangshi_yue}.{self.dangshi_nian}"''').fetchall()
        if dangshi_biaoge:
            self.huafei_biaoge = QTableWidget(self)
            self.huafei_biaoge.setGeometry(10, 100, 580, 280)

            self.huafei_biaoge.setColumnCount(2)
            self.huafei_biaoge.setRowCount(len(dangshi_biaoge))

            self.huafei_biaoge.setHorizontalHeaderLabels(["категория", "сумма"])
            self.huafei_biaoge.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
            self.huafei_biaoge.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
            self.huafei_biaoge.horizontalHeader().setMinimumSectionSize(290)

            for i in range(len(dangshi_biaoge)):
                for j in range(2):
                    self.huafei_biaoge.setItem(i, j, QTableWidgetItem(str(dangshi_biaoge[i][j])))
        else:
            self.meiyou_huafei_xinxi = QLabel('Записи в выбранный день отсутствуют!', self)
            self.meiyou_huafei_xinxi.move(65, 150)

    def huidao_riliwindow(self):
        self.riliwindow = RiliWindow()
        self.riliwindow.show()
        self.hide()

    def dakai_gaibian_mouzhong_rizi_huafei_biaoge(self):
        self.gaibian_huafeibiaoge = GaibianHuafeiBiaoge(self.dangshi_rizi, self.dangshi_yue, self.dangshi_nian)
        self.gaibian_huafeibiaoge.show()
        self.hide()


class GaibianHuafeiBiaoge(QWidget):
    def __init__(self, rizi, yue, nian):
        super().__init__()
        self.dangshi_rizi = rizi
        self.dangshi_yue = yue
        self.dangshi_nian = nian
        self.xuanze_zhonglei = list()
        self.initUi()

    def initUi(self):
        self.setGeometry(300, 300, 650, 470)
        self.setWindowTitle('Редактировать таблицу расходов')

        self.huilai_anniu = QPushButton('<-- Назад', self)
        self.huilai_anniu.setGeometry(5, 10, 120, 35)
        self.huilai_anniu.setStyleSheet(
            "border: 0;\n"
            "border-radius: 15px;\n"
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 172, 235), stop:1 rgba(72,102,175));\n"
            "color: #FFFFFF;\n"
            "padding: 8px 16px;\n"
            "font-size: 16px;")
        self.huilai_anniu.clicked.connect(self.huidao_mouzhonf_rizi)

        self.tianjia_anniu = QPushButton('Добавить статью расходов', self)
        self.tianjia_anniu.setGeometry(10, 55, 300, 35)
        self.tianjia_anniu.setStyleSheet(
            "border: 0;\n"
            "border-radius: 15px;\n"
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 172, 235), stop:1 rgba(72,102,175));\n"
            "color: #FFFFFF;\n"
            "padding: 8px 16px;\n"
            "font-size: 16px;")
        self.tianjia_anniu.clicked.connect(self.tianjia)

        self.yichu_anniu = QPushButton('Удалить статью расходов', self)
        self.yichu_anniu.setGeometry(340, 55, 300, 35)
        self.yichu_anniu.setStyleSheet(
            "border: 0;\n"
            "border-radius: 15px;\n"
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 172, 235), stop:1 rgba(72,102,175));\n"
            "color: #FFFFFF;\n"
            "padding: 8px 16px;\n"
            "font-size: 16px;")
        self.yichu_anniu.clicked.connect(self.yichu)

        self.baocun_anniu = QPushButton('Сохранить изменения', self)
        self.baocun_anniu.setGeometry(10, 400, 250, 35)
        self.baocun_anniu.setStyleSheet(
            "border: 0;\n"
            "border-radius: 15px;\n"
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 172, 235), stop:1 rgba(72,102,175));\n"
            "color: #FFFFFF;\n"
            "padding: 8px 16px;\n"
            "font-size: 16px;")
        self.baocun_anniu.clicked.connect(self.baocun)

        self.zhuangtai = QLabel(self)
        self.zhuangtai.move(10, 438)

        self.con = sqlite3.connect('wode_huafei.db')
        self.cur = self.con.cursor()
        dangshi_biaoge = self.cur.execute(f'''SELECT категория,сумма FROM huafei WHERE дата = 
                            "{self.dangshi_rizi}.{self.dangshi_yue}.{self.dangshi_nian}"''').fetchall()

        self.huafei_biaoge = QTableWidget(self)
        self.huafei_biaoge.setGeometry(10, 110, 630, 280)

        self.huafei_biaoge.setColumnCount(2)
        self.huafei_biaoge.setRowCount(len(dangshi_biaoge))

        self.huafei_biaoge.setHorizontalHeaderLabels(["категория", "сумма"])
        self.huafei_biaoge.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
        self.huafei_biaoge.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        self.huafei_biaoge.horizontalHeader().setMinimumSectionSize(315)

        for i in range(len(dangshi_biaoge)):
            for j in range(2):
                self.huafei_biaoge.setItem(i, j, QTableWidgetItem(str(dangshi_biaoge[i][j])))
        self.benlai_rows_shuliang = self.huafei_biaoge.rowCount()

    def tianjia(self):
        dangshi_zhonglei = list(map(lambda x: x[0], self.cur.execute('SELECT title FROM zhonglei').fetchall()))

        xuanze_zhonglei = QComboBox(self)
        xuanze_zhonglei.addItems(dangshi_zhonglei)

        self.huafei_biaoge.insertRow(self.huafei_biaoge.rowCount())
        self.huafei_biaoge.setCellWidget(self.huafei_biaoge.rowCount() - 1, 0, xuanze_zhonglei)

        self.xuanze_zhonglei.append(xuanze_zhonglei)

    def yichu(self):
        if self.huafei_biaoge.selectionModel().selectedRows():
            xuanze_rows = self.huafei_biaoge.selectionModel().selectedRows()
            data = list(map(lambda x: (f'{self.dangshi_rizi}.{self.dangshi_yue}.{self.dangshi_nian}',
                                       self.huafei_biaoge.item(x.row(), 0).text(),
                                       self.huafei_biaoge.item(x.row(), 1).text()), xuanze_rows))

            while xuanze_rows:
                self.huafei_biaoge.removeRow(xuanze_rows[0].row())
                del xuanze_rows[0]

            valid = QMessageBox.question(
                self, '', 'Действительно удалить выбранные элементы?', QMessageBox.Yes, QMessageBox.No)

            if valid == QMessageBox.Yes:
                cur = self.con.cursor()
                for i in range(len(data)):
                    cur.execute('DELETE FROM huafei WHERE (дата, категория, сумма) = (?, ?, ?);', data[i])
                self.con.commit()

    def baocun(self):
        a = list(map(lambda x: x.currentText(), self.xuanze_zhonglei))
        b = list()

        try:
            for i in range(1, self.huafei_biaoge.rowCount() - self.benlai_rows_shuliang + 1):
                b.append(float(self.huafei_biaoge.item(self.huafei_biaoge.rowCount() - i, 1).text()))
        except (ValueError, AttributeError):
            self.zhuangtai.setText('Некорректный формат данных')
        b.reverse()

        jieguo = list(zip(a, b))
        for i in range(len(jieguo)):
            self.cur.execute(f'''INSERT INTO huafei(дата, категория, сумма) VALUES(?, ?, ?);''',
                             (
                                 f'{self.dangshi_rizi}.{self.dangshi_yue}.{self.dangshi_nian}', jieguo[i][0],
                                 jieguo[i][1]))
        self.con.commit()

    def huidao_mouzhonf_rizi(self):
        self.mouzhong_rizi = MouzhongRizi(self.dangshi_rizi, self.dangshi_yue, self.dangshi_nian)
        self.mouzhong_rizi.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('icon.jpg'))
    app.setStyleSheet("QLabel{font-size: 20pt;}")
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())

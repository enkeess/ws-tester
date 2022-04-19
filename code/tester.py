# coding: utf-8
import os
import xlsxwriter as excel

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog

from des import Ui_MainWindow

import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.button.clicked.connect(self.btnClicked)
        self.ui.findFolder.clicked.connect(self.getdir)

    def btnClicked(self):
        globals()['directory'] = self.ui.way.text() + '/'
        try:
            globals()['admission'] = float(self.ui.admission_line.text())
            if admission < 0: raise ValueError
        except ValueError:
            show_error('admission')
            return

        try:
            globals()['percentage'] = float(self.ui.percentage_line.text())
            if percentage < 0: raise ValueError
        except ValueError:
            show_error('percentage')
            return

        if os.path.exists(directory):
            try:
                processing()
                showdialog()
            except Exception:
                show_error('UnknownError')
        else:
            show_error('folder')

        self.update()

    def getdir(self):
        fname = QFileDialog.getExistingDirectory(self)
        print(fname)
        globals()['directory'] = fname
        self.ui.way.setText(directory)
        self.update()


def show_error(msg_er):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)

    msg.setText("Warning!")
    msg.setInformativeText('Wrong input for "' + msg_er + '"\n\n Try Again!')
    msg.setWindowTitle("Warning!")
    msg.setStandardButtons(QMessageBox.Ok)

    retval = msg.exec_()


def showdialog():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)

    msg.setText("Done")
    msg.setInformativeText('Find results in folder: \n"' + directory + 'Results/"')
    msg.setWindowTitle("Ok!")
    msg.setStandardButtons(QMessageBox.Ok)
    retval = msg.exec_()


def reader(file):
    last_index = 1
    sum = 0
    count = 0
    data = [['Element label'], ['Dev']]
    res = [['Element'], ['Tolerance labels'], ['Percentage of Labels'], ['Result']]

    f = open(file, 'r')
    element = ''
    for line in f:
        if line.find('Element') != -1: continue
        list = line.split(delimeter)

        data[0].append(list[0])
        data[1].append(list[4])

        index = int(list[0].split()[1])
        element = list[0].split()[0]
        list[4] = list[4].replace('???', str(admission + 1))

        tmp = int(abs(float(list[4])) <= admission)
        if (last_index != index):
            res[0].append(element + ' ' + str(last_index))
            res[1].append(sum)
            res[2].append(sum * 100 / count)
            res[3].append(1 if (sum * 100 / count) >= percentage else 0)
            sum = tmp
            count = 1
            last_index = index
        else:
            sum += tmp
            count += 1

    print('here')

    res[0].append(element + ' ' + str(last_index))
    res[1].append(sum)
    res[2].append(sum * 100 / count)
    res[3].append(1 if (sum * 100 / count) >= percentage else 0)

    f.close()
    return [data, res]


def is_digit(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


def test(filename, data):
    workbook = excel.Workbook(filename[:-4] + '.xlsx')
    worksheet = workbook.add_worksheet()

    cell_format = workbook.add_format({'bold': True})
    cell_format.set_bg_color('green')
    cell_format.set_border_color('red')


    worksheet.set_column('A:B', 16)
    worksheet.set_column('D:G', 16)

    worksheet.write_column(0, 0, data[0][0])
    worksheet.write_column(0, 1, data[0][1])

    for i in range(0, len(data[0][1])):
        if is_digit(data[0][1][i]):
            value = float(data[0][1][i])
            if abs(value) <= admission:
                worksheet.write(i, 1, data[0][1][i], cell_format)
            else:
                worksheet.write(i, 1, data[0][1][i])
        else:
            worksheet.write(i, 1, data[0][1][i])

    worksheet.write_column(0, 3, data[1][0])
    worksheet.write_column(0, 4, data[1][1])
    worksheet.write_column(0, 5, data[1][2])
    worksheet.write_column(0, 6, data[1][3])

    for i in range(0, len(data[1][3])):
        if data[1][3][i] == 1:
            worksheet.write_number(i, 6, 1, cell_format)

    data[1][3].pop(0)

    cell_format_1 = workbook.add_format()
    cell_format_1.set_bold(True)
    cell_format_1.set_border(1)

    worksheet.write(len(data[1][0]), 6, sum(data[1][3]), cell_format_1)

    workbook.close()

    return 'Result ' + str(sum(data[1][3])) + '\n\n'


def common_file(data):
    workbook = excel.Workbook(directory + 'Results/' + 'General Pivot Table' + '.xlsx')
    worksheet = workbook.add_worksheet()

    header_format = workbook.add_format({'bold': True,
                                         'align': 'center',
                                         'valign': 'vcenter',
                                         'fg_color': '#D7E4BC',
                                         'border': 1})
    center_format = workbook.add_format({'align': 'center'})
    if len(data) != 0:
        worksheet.freeze_panes(1, 1)
        column = len(data)
        lines = len(data[0])
        worksheet.set_column(0, column, 20)
        for i in range(0, column):
            for j in range(0, lines):
                if i == 0 or j == 0:
                    worksheet.write(j, i, data[i][j], header_format)
                else:
                    worksheet.write(j, i, data[i][j], center_format)

    workbook.close()


common_table = []
percentage = 70
admission = 0.2
delimeter = ','
directory = '/Users/user/Downloads/'


def keyFunc(item):
    return item[0]


def processing():
    if not os.path.exists(directory + 'Results/'):
        os.mkdir(directory + 'Results/')
    outfile = open(directory + 'Results/log.txt', 'w')
    files = os.listdir(directory)
    first_col = []
    for filename in files:
        print(filename)
    for filename in files:
        tmp_name = directory + 'Results/' + filename
        if filename[-4:] == '.csv':

            d = reader(directory + filename)
            msg = test(tmp_name, d)
            outfile.write(filename + ' DONE\n')
            outfile.write(msg)
            to_cmn_tbl = [filename[:-4]] + d[1][3]
            if len(common_table) == 0:
                first_col = d[1][0]
            common_table.append(to_cmn_tbl)

    outfile.close()
    if len(common_table):
        common_table.sort(key=keyFunc)
    if len(first_col) != 0:
        common_table.insert(0, first_col)
        common_file(common_table)
    common_table.clear()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()

    sys.exit(app.exec())

import pyforms
from   pyforms.basewidget import BaseWidget
from   pyforms.controls   import ControlText
from   pyforms.controls   import ControlLabel
from   pyforms.controls   import ControlTextArea
from   pyforms.controls   import ControlButton
import xlwt
class SimpleExample1(BaseWidget):
    def __init__(self):
        super(SimpleExample1,self).__init__('接龙格式化工具-----Lakphy')
        self._fullname      = ControlTextArea('接龙内容')
        self._test          = ControlLabel('请输入接龙内容后点击格式化，即可转换为表格\n请注意使用\'--\'即两个减号为每个数据分隔符，使用换行作为每个人的数据分隔符！\nCopyRight Lakphy 2020\n网站:lakphy.me')
        self._button        = ControlButton('格式化')
        self._button.value  = self.__buttonAction
    def __buttonAction(self):
        self._test.value = str(self._fullname.value.split('\n'))
        a      = self._fullname.value.split('\n')
        wk     = xlwt.Workbook()
        sheet1 = wk.add_sheet("数据", cell_overwrite_ok=True)
        for i in range(0,len(a)):
            b  = a[i].split('--')
            for j in range(0,len(b)):
                if j == 0:
                    d = b[j].split('. ',2)
                    if len(d) == 2:
                        c = d[1]
                    else:
                        d = b[j].split('.',2)
                        if len(d) == 2:
                            c = d[1]
                        else:
                            c = b[j]
                else:
                    c = b[j]
                sheet1.write(i+1,j+1,c)
            sheet1.write(i+1,0,i+1)
        wk.save('Solitaire.xls')
        self._test.value = '接龙内容格式化成功！内容保存在Solitaire.xls，请及时备份该文件，防止下次使用该软件时覆盖内容！\nCopyRight Lakphy 2020\n网站:lakphy.me'
if __name__ == "__main__": pyforms.start_app( SimpleExample1 )
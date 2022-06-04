import os
import string
from PIL import Image#, ImageDraw, ImageFont, ImageFilter
class Menu():
    def __init__(self):
        self.dlist = []
        self.out = []
        self.dirs = []
        self.files = []
        self.exs = []
        self.cur = os.getcwd()
        self.err = False
        self.fad = []
        for c in string.ascii_uppercase:
            disk = c+':'
            if os.path.isdir(disk):
                self.dlist.append(disk)
        try:
            self.fad = os.listdir(path = r''+self.cur)#'.'
            self.prs()
        except PermissionError:
            print('\n------Отказано в доступе!------')
            sln = self.cur.rfind('\\')
            self.cur = self.cur[:sln]
            if len(self.cur) < 3:
                self.cur +='\\'            
            self.err = True

    def prs(self):
        for fd in self.fad:            
            t =  fd.split('.')
            if os.path.isdir(fd):                
                self.dirs.append(fd)
            else:
                self.files.append(fd)
                ex = t[1:]
                self.exs.append(ex)
        self.out = []        
        for f in range(2):
            n = 1
            N = 3
            strdf = ''
            arrdf = []
            if f == 0:
                df = self.dirs
                si = 'Папки :'                
            else:
                df = self.files
                si = 'Файлы :'
            for d in df:
                if n% N == 0:
                    dl = '\n'
                else:
                    l = ''
                    if len(d) < 20:
                        for i in range(20-len(d)):
                            l += ' '
                    dl = l + '\t'            
                strdf += d + dl
                arrdf.append(d)
                n += 1
            print(si)
            print(strdf)
            self.out.append(arrdf)
        print(self.out)
        print(self.cur)
        print('Диски: ', self.dlist)

    def Opn(self, par = []):
        ex =''
        if not par:
            par = self.cur.split('\\')
        if self.err:
            ft = self.cur
            el = par[len(par)-1]
            par.remove(el)
        else:
            ft = input('Вернуться на уровень ниже: Да,  Удалить(-),  Создать(+),  Открыть : ')
        if ft in self.dirs:
            pth = ''+self.cur + '\\' + ft + '\\'
            try:
                os.chdir(pth)
                par.append(ft)
            except PermissionError:
                print('\n------Отказано в доступе!------')
        elif ft in self.files:
            if self.exs[self.files.index(ft)][0] == 'py':
                pth = r'C:\Python39\python.exe '+u'"'+self.cur+'\\'+ft+'"' # r перед строкой избавляет от необходимости двойного слэша
                os.system(pth)
            elif self.exs[self.files.index(ft)][0] == 'txt':
                os.system(u'"'+self.cur+'\\'+ft+'"')# кириличные строки в кавычках, u - перевод строки в юникод
            else:
                try:
                    img = Image.open(ft)
                    img.show()
                except IOError:
                    print('\n------Это не изображение!------')
                    #M = Menu()
                    #M.Opn(par)
        elif ft.find(':') > -1:
            os.chdir(ft)
            par = ft.split('\\')
            if par[1] == '':
                par = par[:1]
        elif (ft.lower() == 'lf' or ft.lower() == 'да') and len(par) > 1:
            el = par[len(par)-1]
            par.remove(el)
            ln = len(el)            
            os.chdir(self.cur[:-ln])
        else:
            print('\n------Что-то пошло не так!------')
        M = Menu()
        M.Opn(par)
              
M = Menu()
M.Opn()

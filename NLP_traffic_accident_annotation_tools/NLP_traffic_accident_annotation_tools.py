import tkinter
from tkinter import *
import tkinter.messagebox
import os
import tkinter.font as tf
import tkinter.filedialog





class init():
    def __init__(self,win):
        super(init, self).__init__()
        self.content_text_size=0
        self.lines_count=0
        self.path_list=[]
        self.path_out_data=""
        self.last_key_words_set=[]
        self.last_key_words=[]
        self.win=win
        self.path_in=""
        self.data_all = []
        self.data_out = []
        self.data_key_words=[]
        self.data_line=[]
        self.data_lines=[]
        self.data_title=[]
        self.data_line_mark=[]
        self.data_line_marks=[]
        self.content=''
        self.contents=[]
        self.labei_att=1
        self.labei_atts=[]
        self.line_count = 0
        self.tag_count=0
        self.word_start=0
        self.word_end=0
        self.frame1 = Frame(win, relief=RAISED, borderwidth=1)
        self.frame1.grid(row=1, column=1)
        self.content_text = Text(self.frame1, width=int(win.winfo_screenwidth()/7.15), height=int(win.winfo_screenheight()/40),bg='#F5DEB3')
        self.content_text.grid(row=2, column=1)

        self.title_txt = Text(self.frame1, width=int(win.winfo_screenwidth()/7.15), height=int(win.winfo_screenheight()/win.winfo_screenheight()))
        self.title_txt.grid(row=1, column=1)

        self.frame2 = Frame(win, relief=RAISED, borderwidth=1)
        self.frame2.grid(row=2, column=1)

        self.label_text_size_label = Label(self.frame2, text='文本数字：')
        self.label_text_size_label.grid(row=1, column=1)

        self.label_text_size = Label(self.frame2)
        self.label_text_size.grid(row=1, column=2)

        self.label_text_gap = Label(self.frame2, text='                             ')
        self.label_text_gap.grid(row=1, column=3)

        self.frame2_1 = Frame(self.frame2, relief=RAISED, borderwidth=0)
        self.frame2_1.grid(row=1, column=4)

        self.frame2_2 = Frame(self.frame2, relief=RAISED, borderwidth=0)
        self.frame2_2.grid(row=1, column=5)



        expression = StringVar()
        label_attitude = tkinter.Label(self.frame2_1, textvariable=expression).grid(row=1, column=1)
        expression.set("是否交通事故新闻？")

        self.var_1 = IntVar()
        self.var = IntVar()

        Radiobutton(self.frame2_1, text="是", variable=self.var_1, value=0, command=self.showSelection_1).grid(row=1, column=2)
        Radiobutton(self.frame2_1, text="否", variable=self.var_1, value=1, command=self.showSelection_1).grid(row=1, column=3)
        self.label_att_choice = Label(self.frame2_2, text="您的选择：是")
        self.label_att_choice.grid(row=1, column=1)

        self.select_txt = Text(win,  width=int(win.winfo_screenwidth()/7.15), height=int(win.winfo_screenheight()*2/win.winfo_screenheight()))
        self.select_txt.grid(row=3, column=1)

        self.frame3 = Frame(win, relief=RAISED, borderwidth=1)
        self.frame3.grid(row=4, column=1)

        self.button_delete = Button(self.frame3, text="删除关键词", width=int(win.winfo_screenwidth() / 96),
                                  height=int(win.winfo_screenheight() / 360), command=self.delete_key_words,
                                  font=('微软雅黑', '8'), relief="raised", bd=10, bg="#E6E6FA")
        self.button_delete.pack(side=LEFT, fill=BOTH, expand=0)

        self.label_delete_button_gap = Label(self.frame3, text='     ', bg='#FFFAFA')
        self.label_delete_button_gap.pack(side=LEFT, fill=BOTH, expand=0)

        self.button_last=Button(self.frame3, text="上一条新闻",width=int(win.winfo_screenwidth()/96), height=int(win.winfo_screenheight()/360),command=self.get_last_line,font=('微软雅黑', '8'),relief="raised", bd=10,bg="#E6E6FA")
        self.button_last.pack(side=LEFT, fill=BOTH,expand=0)

        self.label_last_button_gap = Label(self.frame3,text='     ',bg='#FFFAFA')
        self.label_last_button_gap.pack(side=LEFT, fill=BOTH,expand=0)

        self.frame1_3 = Frame(self.frame3)
        self.frame1_3.pack(side=LEFT, fill=BOTH,expand=0)

        self.label_next_button_gap = Label(self.frame3, text='     ', bg='#FFFAFA')
        self.label_next_button_gap.pack(side=LEFT, fill=BOTH, expand=0)

        self.button_next = Button(self.frame3, text="下一条新闻",width=int(win.winfo_screenwidth()/48), height=int(win.winfo_screenheight()/360), command=self.get_next_line,font=('微软雅黑', '8'),relief="raised", bd=10,bg="#E6E6FA")
        self.button_next.pack(side=LEFT, fill=BOTH,expand=0)


        mainmenu = Menu(win)
        mainmenu.add_command(label="打开标注好的新闻数据文件", command=self.opendatafile_in)
        mainmenu.add_command(label="保存新的事故标注文件", command=self.opendatafile_out_data)


        win.config(menu=mainmenu)

        self.frame3_1 = Frame(self.frame1_3, width=int(win.winfo_screenwidth() / 19.2),
                              height=int(win.winfo_screenheight() / 72))
        self.frame3_1.grid(row=1, column=1)

        expression = StringVar()
        label_human_factor = tkinter.Label(self.frame3_1, textvariable=expression).grid(row=1, column=1)
        expression.set("时间:")
        self.r0 = Radiobutton(self.frame3_1, text="事故发生时间", variable=self.var, value=0, command=self.showSelection)
        self.r0.grid(row=1, column=2)

        self.label_time_loc_gap = Label(self.frame3_1, text='          ')
        self.label_time_loc_gap.grid(row=1, column=3)

        expression = StringVar()
        time = tkinter.Label(self.frame3_1, textvariable=expression).grid(row=1, column=4)
        expression.set("地点:")

        self.r14 = Radiobutton(self.frame3_1, text="事故发生地点", variable=self.var, value=1, command=self.showSelection)
        self.r14.grid(row=1, column=5)

        self.label_time_loc_gap = Label(self.frame3_1, text='          ')
        self.label_time_loc_gap.grid(row=1, column=6)

        expression = StringVar()
        location = tkinter.Label(self.frame3_1, textvariable=expression).grid(row=1, column=7)
        expression.set("主体:")

        self.r15 = Radiobutton(self.frame3_1, text="车辆类型", variable=self.var, value=2, command=self.showSelection)
        self.r15.grid(row=1, column=8)

        self.frame3_3 = Frame(self.frame1_3, width=int(win.winfo_screenwidth() / 19.2),
                              height=int(win.winfo_screenheight() / 72))

        self.frame3_3.grid(row=3, column=1)
        expression = StringVar()
        accident_result_factor = tkinter.Label(self.frame3_3, textvariable=expression).grid(row=1, column=1)
        expression.set("后果:")

        self.r16 = Radiobutton(self.frame3_3, text="事故造成后果", variable=self.var, value=3, command=self.showSelection)
        self.r16.grid(row=1, column=2)

        self.label_result_accident_gap = Label(self.frame3_3, text='          ')
        self.label_result_accident_gap.grid(row=1, column=3)

        expression = StringVar()
        accident_accident_main = tkinter.Label(self.frame3_3, textvariable=expression).grid(row=1, column=4)
        expression.set("原因:")

        self.r20 = Radiobutton(self.frame3_3, text="事故发生原因", variable=self.var, value=4, command=self.showSelection)
        self.r20.grid(row=1, column=5)

        self.content_label = Text(win, width=int(win.winfo_screenwidth()/7.15), height=(win.winfo_screenheight()/36),bg='#F5DEB3')
        self.content_label.grid(row=5, column=1)

        frame6 = Frame(win)

        frame6.grid(row=6, column=1)

        self.button_save = Button(frame6, width=int(win.winfo_screenwidth() / 24), height=int(win.winfo_screenheight() / 540),text="保存", command=self.save_data, font=('微软雅黑', '10'), relief="raised", bd=10 ,bg="#E6E6FA")
        self.button_save.grid(row=1, column=1)

        self.label_save_quit__gap = Label(frame6, text='          ')
        self.label_save_quit__gap.grid(row=1, column=2)

        self.button_quit = Button(frame6, width=int(win.winfo_screenwidth()/24), height=int(win.winfo_screenheight()/540), text="关闭", command=self.quit_win,font=('微软雅黑', '10'),relief="raised", bd=10,bg="#E6E6FA")
        self.button_quit.grid(row=1, column=3)



        self.load_data_init()

        self.title_txt.bind("<ButtonRelease-1>", self.get_content)
        self.content_text.bind("<ButtonRelease-1>", self.get_content)

        self.content_text.bind("<KeyRelease>",self.chanage_content_text_size)



    def showSelection(self):

        key_words=str(self.select_txt.get('0.0',END)).strip().strip("\n")
        if key_words.strip()=='':
            tkinter.messagebox.askokcancel("提示", " 请选择关键词！！！")
            return
        else:
            id=self.var.get()
            if id==0:
                label="tim"
            elif id==1:
                label = "loc"
            elif id == 2:
                label = "sub"
            elif id == 3:
                label = "res"
            elif id == 4:
                label = "rea"
            else:
                tkinter.messagebox.askokcancel("提示", "请选择所属类别！！！")
                return

            values=[]
            value=''
            for i in range(len(key_words)):
                if i==0:
                    value='B'+"_"+label
                    values.append(value)
                else:
                    value='I'+"_"+label
                    values.append(value)
            data_word_loc_key = []
            data_word_loc_key.append(key_words)
            data_word_loc_key.append(values)
            data_word_loc_key.append(self.word_start)
            self.data_key_words.append(data_word_loc_key)
        self.content_label.delete('1.0', END)
        self.update_selected(key_words,values)
        self.select_txt.delete('0.0',END)

    def showSelection_1(self):
        if self.path_in == '':
            tkinter.messagebox.askokcancel('提示', "请选择新闻数据！！！")
            return
        if self.path_out_data == '':
            tkinter.messagebox.askokcancel('提示', "请选择数据保存路径！！！")
            return
        if self.var_1.get() == 0:
            self.label_att_choice.configure(text="您的选择：是")
            self.labei_att=1
        else:
            self.label_att_choice.configure(text="您的选择：否")
            self.labei_att=0
            self.get_next_line()

    def get_last_line(self):
        self.lines_count=len(self.data_lines)
        if self.lines_count>0:
            self.data_key_words=self.last_key_words_set.pop(self.lines_count-1)
            self.data_line_mark=self.data_line_marks.pop(self.lines_count-1)
            self.data_line=self.data_lines.pop(self.lines_count-1)
            self.content = self.contents.pop(self.lines_count-1)
            self.lines_count=len(self.data_lines)
            self.line_count=self.line_count-1
            self.content_text_size = len(self.data_line)
            self.label_text_size.configure(text=self.content_text_size)
            self.set_selected()
        else:
            tkinter.messagebox.askokcancel('提示','无法返回上一行！')


    def get_next_line(self):
        if self.path_in == '':
            tkinter.messagebox.askokcancel('提示', "请选择新闻数据！！！")
            return
        if self.path_out_data == '':
            tkinter.messagebox.askokcancel('提示', "请选择数据保存路径！！！")
            return
        self.last_key_words_set.append(self.data_key_words)
        self.tag_count=0
        self.labei_att = 1
        self.var_1.set(0)
        self.data_lines.append(self.data_line)
        self.data_line_marks.append(self.data_line_mark)
        self.contents.append(self.content)
        self.lines_count = len(self.data_lines)
        self.data_key_words=[]
        self.line_count=self.line_count+1
        self.set_content()


    def set_content(self):
        content=''
        try:
            line = self.data_all[self.line_count]
            sentens = []
            biaozhu = []
            items = line.strip().strip("\n").split("/**/")
            for i in range(len(items[0:-1])):
                if i % 2 == 0:
                    sentens.append(items[i])
                    content=content+items[i]
                else:
                    biaozhu.append(items[i])
        except:
            self.save_data()
            tkinter.messagebox.askokcancel('提示', "已经是最后一条数据！！！")
        ft = tf.Font(family='微软雅黑', size=12)
        self.content = content
        self.content_text.delete('1.0', END)
        self.content_text.insert('1.0', self.content)
        self.content_text.tag_add("text_tag",'1.0',END)
        self.content_text.tag_config('text_tag',font =ft)
        self.content_label.delete('1.0', END)

        self.data_line=sentens
        self.data_line_mark=biaozhu

        data_word_loc_key = []

        for i in range(len(self.data_line_mark)):
            values = []
            if self.data_line_mark[i] =="B_tim":
                values.append("B_tim")
                word_start=i
                for item in self.data_line_mark[i+1:]:
                    if item =="I_tim":
                        values.append("I_tim")
                    else:
                        break
                key_words = ''
                for item_word in self.data_line[i:i + len(values)]:
                    key_words = key_words + item_word
                data_word_loc_key.append(key_words)
                data_word_loc_key.append(values)
                data_word_loc_key.append(word_start)
                self.data_key_words.append(data_word_loc_key)
                data_word_loc_key=[]

            elif self.data_line_mark[i] =="B_loc":
                values.append("B_loc")
                word_start = i
                for item in self.data_line_mark[i + 1:]:
                    if item == "I_loc":
                        values.append("I_loc")
                    else:
                        break
                key_words=''
                for item_word in self.data_line[i:i + len(values)]:
                    key_words=key_words+item_word
                data_word_loc_key.append(key_words)
                data_word_loc_key.append(values)
                data_word_loc_key.append(word_start)
                self.data_key_words.append(data_word_loc_key)
                data_word_loc_key = []

            elif self.data_line_mark[i] == "B_sub":
                values.append("B_sub")
                word_start = i
                for item in self.data_line_mark[i + 1:]:
                    if item == "I_sub":
                        values.append("I_sub")
                    else:
                        break
                key_words = ''
                for item_word in self.data_line[i:i + len(values)]:
                    key_words = key_words + item_word
                data_word_loc_key.append(key_words)
                data_word_loc_key.append(values)
                data_word_loc_key.append(word_start)
                self.data_key_words.append(data_word_loc_key)
                data_word_loc_key = []

            elif self.data_line_mark[i] == "B_res":
                values.append("B_res")
                word_start = i
                for item in self.data_line_mark[i + 1:]:
                    if item == "I_res":
                        values.append("I_res")
                    else:
                        break
                key_words = ''
                for item_word in self.data_line[i:i + len(values)]:
                    key_words = key_words + item_word
                data_word_loc_key.append(key_words)
                data_word_loc_key.append(values)
                data_word_loc_key.append(word_start)
                self.data_key_words.append(data_word_loc_key)
                data_word_loc_key = []

            elif self.data_line_mark[i] == "B_rea":
                values.append("B_rea")
                word_start = i
                for item in self.data_line_mark[i + 1:]:
                    if item == "I_rea":
                        values.append("I_rea")
                    else:
                        break
                key_words = ''
                for item_word in self.data_line[i:i + len(values)]:
                    key_words = key_words + item_word
                data_word_loc_key.append(key_words)
                data_word_loc_key.append(values)
                data_word_loc_key.append(word_start)
                self.data_key_words.append(data_word_loc_key)
                data_word_loc_key = []

        self.content_text_size = len(self.data_line)
        self.label_text_size.configure(text=self.content_text_size)
        self.set_selected()




    def set_selected(self):
        ft = tf.Font(family='微软雅黑', size=12)
        self.content_text.delete('1.0', END)
        self.content_text.insert('1.0', self.content)
        self.content_text.tag_add("text_tag", '1.0', END)
        self.content_text.tag_config('text_tag', font=ft)
        self.content_label.delete('1.0', END)
        for item in self.data_key_words:
            word=item[0]
            values=item[1]
            loc=item[2]
            for i in range(len(values)):
                self.data_line_mark[loc + i] = values[i]
            tag_name = "tag" + str(self.tag_count)
            tag_start = "1" + "." + str(loc)
            tag_end = "1" + "." + str(loc+ len(word))
            self.content_text.tag_add(tag_name, tag_start, tag_end)
            self.content_text.tag_config(tag_name, background='green')
            self.tag_count = self.tag_count + 1
        count_label = 0
        for s in self.data_line_mark:
            for s_item in s:
                count_label = count_label + 1
                insert_id = "1" + "." + str(count_label)
                self.content_label.insert(insert_id, s_item)
        ft = tf.Font(family='times new roman', size=12)
        self.content_label.tag_add("label_tag",'1.0',END)
        self.content_label.tag_config('label_tag',font =ft)
        self.content_text_size = len(self.data_line)
        self.label_text_size.configure(text=self.content_text_size)


    def update_selected(self,key, values):
        ft = tf.Font(family='微软雅黑', size=12)
        self.content_text.delete('1.0', END)
        self.content_text.insert('1.0', self.content)
        self.content_text.tag_add("text_tag", '1.0', END)
        self.content_text.tag_config('text_tag', font=ft)
        self.content_label.delete('1.0', END)
        for i in range(len(key)):
            self.data_line_mark[self.word_start + i] = values[i]

        for item in self.data_key_words:
            word=item[0]
            loc=item[2]
            word_start=loc
            word_end=loc+len(word)

            tag_name = "tag" + str(self.tag_count)
            tag_start = "1" + "." + str(word_start)
            tag_end = "1" + "." + str(word_end)
            self.content_text.tag_add(tag_name, tag_start, tag_end)
            self.content_text.tag_config(tag_name, background='green')
            self.tag_count = self.tag_count + 1

        count_label = 0
        for s in self.data_line_mark:
            for s_item in s:
                count_label = count_label + 1
                insert_id = "1" + "." + str(count_label)
                self.content_label.insert(insert_id, s_item)
        ft = tf.Font(family='times new roman', size=12)
        self.content_label.tag_add("label_tag", '1.0', END)
        self.content_label.tag_config('label_tag', font=ft)
        self.content_text_size = len(self.data_line)
        self.label_text_size.configure(text=self.content_text_size)

    def get_content(self,event):
        try:
            s = self.content_text.get(tkinter.SEL_FIRST, tkinter.SEL_LAST)
            self.select_txt.delete('1.0', END)
            self.select_txt.insert('1.0', s)
            ft = tf.Font(family='微软雅黑', size=12)
            self.select_txt.tag_add("select_tag", '1.0', END)
            self.select_txt.tag_config('select_tag', font=ft)
            self.word_start=int(self.content_text.index(tkinter.SEL_FIRST).split('.')[-1])
            self.word_end=int(self.content_text.index(tkinter.SEL_LAST).split('.')[-1])
            if not len(s)==self.word_end-self.word_start:
                tkinter.messagebox.askokcancel("有误！", "请重新选择关键词！！！")
        except:
            tkinter.messagebox.askokcancel("提示", "请选择关键词！！！")

    def save_data(self):
        if self.path_in == '':
            tkinter.messagebox.askokcancel('提示', "请选择新闻数据！！！")
        if self.path_out_data == '':
            tkinter.messagebox.askokcancel('提示', "请选择数据保存路径！！！")
            return
        with open(self.path_out_data, 'a', encoding='utf-8') as f_out:
            for i in range(len(self.data_lines)):
                assert len(self.data_lines[i])==len(self.data_line_marks[i]),'代码有误，检查代码！！！'
                s=''
                for j in range(len(self.data_lines[i])):
                    s=s+self.data_lines[i][j]+"/**/" +self.data_line_marks[i][j]+'/**/'
                f_out.write(s)
                f_out.write('\n')
            f_out.close()
        self.data_line_marks=[]
        self.data_lines=[]
        self.lines_count=0
        self.last_key_words_set=[]
        self.data_key_words=[]
        self.contents=[]



    def quit_win(self):
        self.save_data()
        self.win.quit()

    def opendatafile_in(self):
        myFileTypes = [('data files', '* .txt')]
        myDialog1 = tkinter.filedialog.Open(win, filetypes=myFileTypes)
        myDialog1.show()
        self.path_in=myDialog1.filename
        self.dataload()

    def opendatafile_out_data(self):
        myFileTypes = [('data files', '* .txt')]
        myDialog1 = tkinter.filedialog.Open(win, filetypes=myFileTypes)
        myDialog1.show()
        self.path_out_data=myDialog1.filename
        self.dataload()



    def dataload(self):
        if self.path_in=='':
            tkinter.messagebox.askokcancel('提示',"请选择新闻数据！！！")
            return
        if self.path_out_data == '':
            tkinter.messagebox.askokcancel('提示', "请选择数据保存路径！！！")
            return
        if len(self.path_list)==2:
            self.path_list[0]=self.path_in
            self.path_list[1]=self.path_out_data
        else:
            self.path_list.append(self.path_in)
            self.path_list.append(self.path_out_data)


        with open(self.cofig_file,'w',encoding='utf-8') as f_in:
            for path in self.path_list:
                f_in.write(path)
                f_in.write('\n')
            f_in.close()

        with open(self.path_in, 'r', encoding='utf-8') as f_in:
            self.data_all = f_in.readlines()
            f_in.close()
        if os.path.exists(self.path_out_data):
            with open(self.path_out_data, 'r', encoding='utf-8') as f_in:
                lines = f_in.readlines()
                self.line_count = len(lines)
            f_in.close()
        self.set_content()

    def load_data_init(self):
        cofig_file=os.getcwd()+"\\"+"congfig"
        self.cofig_file=cofig_file.replace('\\','/')
        if not os.path.exists(cofig_file):
            tkinter.messagebox.askokcancel("提示","当前没有默认路径！")
        else:
            with open(cofig_file,'r',encoding='utf-8') as f_in:
                paths=f_in.readlines()
                if len(paths)==0:
                    tkinter.messagebox.askokcancel("提示", "当前没有默认路径！")
                else:
                    for path in paths:
                        path=path.strip().strip("\n")
                        self.path_list.append(path)
                self.path_in=self.path_list[0]
                self.path_out_data=self.path_list[1]
                f_in.close()
        self.dataload()

    def chanage_content_text_size(self, event):
        current_content_text = self.content_text.get('1.0', END)
        current_content_text = str(current_content_text).strip().strip("\n")
        key_words = str(self.select_txt.get('0.0', END)).strip().strip("\n")

        if len(current_content_text) < self.content_text_size:
            for i in range(self.word_end-self.word_start):
                self.data_line.pop(self.word_start)
                self.data_line_mark.pop(self.word_start)

            loc = self.word_start
            word_loc = [key_words, loc]
            word_locs = []
            for item in self.data_key_words:
                word = item[0]
                loc = item[2]
                word_locs.append([word, loc])
            if word_loc in word_locs:
                index = word_locs.index(word_loc)
                self.data_key_words.pop(index)
            self.content=current_content_text
            self.set_selected()

        else:
            tkinter.messagebox.askokcancel('提示','错误操作！')
            self.set_selected()

    def delete_key_words(self):
        word_locs=[]
        for item in self.data_key_words:
            word = item[0]
            loc = item[2]
            word_loc = []
            for i in range(len(word)):
                word_loc.append(loc+i)
            word_locs.append(word_loc)


        key_words=str(self.select_txt.get('0.0',END)).strip().strip("\n")
        loc_delete_s=self.word_start

        loc_delete_v=[]
        for i in range(len(key_words)):
           loc_delete=loc_delete_s+i
           loc_delete_v.append(loc_delete)

        is_in=False
        is_mid=True
        count_ture=0
        lenth_word=len(loc_delete_v)
        for word_loc in word_locs:
            for item in loc_delete_v:
                if item in word_loc:
                    count_ture=count_ture+1
            if count_ture==lenth_word:
                index=word_locs.index(word_loc)
                is_in=True
                if loc_delete_v[0]==word_loc[0] or loc_delete_v[-1]==word_loc[-1]:
                    is_mid=False
                break

        if is_in:
            word_value_loc = self.data_key_words[index]

            locs = []
            keywords = []

            keyword = word_value_loc[0]
            values = word_value_loc[1]
            loc_s = word_value_loc[2]

            for i in range(len(keyword)):
                locs.append(loc_s + i)
                keywords.append(keyword[i])

            index_items = []
            for item in loc_delete_v:
                if item in locs:
                    index_item = locs.index(item)
                    index_items.append(index_item)
                    self.data_line_mark[item] = "O"

            index_items = sorted(index_items)
            if not is_mid:
                for item in index_items:
                    locs.pop(index_items[0])
                    keywords.pop(index_items[0])
                    values.pop(index_items[0])


                word_value_loc = []
                if not len(locs) == 0:
                    if not values[0] == "B" + values[0][1:]:
                        values[0] = "B" + values[0][1:]
                        self.data_line_mark[locs[0]] = "B" + values[0][1:]
                    key_word = ''
                    for item in keywords:
                        key_word = key_word + item
                    s_start = locs[0]
                    for item in locs:
                        if item < s_start:
                            s_start = item
                    word_value_loc.append(key_word)
                    word_value_loc.append(values)
                    word_value_loc.append(s_start)

                    self.data_key_words[index] = word_value_loc
                else:
                    self.data_key_words.pop(index)

                self.set_selected()
            if is_mid:
                mid=index_items[0]
                locs_1=locs[0:mid]
                locs_2 = locs[mid+len(loc_delete_v):]

                keywords_1=keywords[0:mid]
                keywords_2=keywords[mid+len(loc_delete_v):]

                values_1=values[0:mid]
                values_2=values[mid+len(loc_delete_v):]

                if not values_1[0] == "B" + values_1[0][1:]:
                    values_1[0] = "B" + values_1[0][1:]
                    self.data_line_mark[locs_1[0]] = "B" + values_1[0][1:]
                if not values_2[0] == "B" + values_2[0][1:]:
                    values_2[0] = "B" + values_2[0][1:]
                    self.data_line_mark[locs_2[0]] = "B" + values_2[0][1:]

                self.data_key_words.pop(index)
                if not len(locs_1) == 0:
                    key_word = ''
                    for item in keywords_1:
                        key_word = key_word + item
                    s_start = locs_1[0]
                    for item in locs_1:
                        if item < s_start:
                            s_start = item
                    word_value_loc1 = []
                    word_value_loc1.append(key_word)
                    word_value_loc1.append(values_1)
                    word_value_loc1.append(s_start)
                    self.data_key_words.append(word_value_loc1)
                if not len(locs_2) == 0:
                    key_word = ''
                    for item in keywords_2:
                        key_word = key_word + item
                    s_start = locs_2[0]
                    for item in locs_2:
                        if item < s_start:
                            s_start = item
                    word_value_loc2 = []
                    word_value_loc2.append(key_word)
                    word_value_loc2.append(values_2)
                    word_value_loc2.append(s_start)
                    self.data_key_words.append(word_value_loc2)
                self.set_selected()

        else:
            tkinter.messagebox.askokcancel('提示', "关键词不存在！")
            return


















if __name__ == '__main__':

    win = tkinter.Tk()
    win.title(string="NLP 实体标注工具".center(int(win.winfo_screenwidth()/4)))

    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    size=str(screen_width)+"x"+str(screen_height)
    win.geometry(size)
    win.config(bg='#FFFAFA ')

    init(win)
    win.mainloop()


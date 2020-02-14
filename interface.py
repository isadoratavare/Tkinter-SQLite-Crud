from tkinter import *
import sqlite3

# banco de dados
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# criando tabela aluno
aluno = '''
CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome NOT NULL,
        cpf NOT NULL UNIQUE
);
'''
cursor.execute(aluno)

# criando tabela professor
professores = '''
CREATE TABLE IF NOT EXISTS professores (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome NOT NULL,
        cpf NOT NULL UNIQUE,
        departamento NOT NULL
);
'''
cursor.execute(professores)

# criando tabela disciplinas
disciplinas = '''
CREATE TABLE IF NOT EXISTS disciplinas (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome NOT NULL,
        codigo NOT NULL UNIQUE
);
'''
cursor.execute(disciplinas)

c = conn.cursor()
turma = '''CREATE TABLE IF NOT EXISTS turmas( 
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    codigo NOT NULL,
                    periodo NOT NULL,
                    disciplinas NOT NULL ,
                    professores NOT NULL ,
                    alunos NOT NULL );
'''
c.execute(turma)


# interface
def jan_principal():
    def titulo(x):
        lb = Label(x, text='Seja bem-vindo ao Sistema de Controle Acadêmico')
        lb.place(x=210, y=50)
        lb['bg'] = 'bisque'

    def tipotitulo(x, a):
        lb = Label(x, text=a)
        lb.place(x=280, y=80)
        lb['bg'] = 'bisque'

    def jan_alunos():
        # interface
        def jan_cadastroaluno():
            def bd_cadaluno():
                def Ok():
                    erro.destroy()
                    cpf.delete(0, END)
                    nome.delete(0, END)

                try:
                    nomea = str(nome.get())
                    cpfa = str(cpf.get())
                    cursor.execute('''
                    INSERT INTO alunos (nome,cpf)
                    VALUES('%s','%s')
                    ''' % (nomea, cpfa))
                    conn.commit()

                    lb = Label(c_alunos, text='Aluno cadastrado!')
                    lb.place(x=350, y=400)
                    cpf.delete(0, END)
                    nome.delete(0, END)
                except:
                    erro = Tk()
                    erro.title('Erro')
                    erro.geometry('180x150+620+280')

                    lb = Label(erro, text='CPF já cadastrado!')
                    lb.place(x=45, y=50)

                    bt = Button(erro, text='OK', command=Ok, )
                    bt.place(x=75, y=85)

            def voltar1():
                c_alunos.destroy()
                jan_principal()

            # janela cadastro alunos
            c_alunos = Tk()
            c_alunos.title('Cadastrando Aluno')
            c_alunos['bg'] = 'bisque'
            c_alunos.geometry('700x450+350+100')
            alunos.destroy()

            # titulos
            titulo(c_alunos)
            a = 'CADASTRO ALUNO'
            tipotitulo(c_alunos, a)

            # Nome
            lb_nome = Label(c_alunos, text='Nome :', font='30')
            lb_nome.place(x=170, y=150)
            lb_nome['bg'] = 'bisque'

            # Entrada do nome
            nome = Entry(c_alunos, width=45)
            nome.place(x=230, y=153)

            # CPF
            lb_cpf = Label(c_alunos, text='CPF :', font='25')
            lb_cpf.place(x=170, y=250)
            lb_cpf['bg'] = 'bisque'

            # Entrada do cpf
            cpf = Entry(c_alunos, width=45)
            cpf.place(x=230, y=253)

            # BUTTON cadastrar aluno
            b_cadastrar = Button(c_alunos, width=20, text='Cadastrar',
                                 command=bd_cadaluno,
                                 activebackground='gray28',
                                 activeforeground='gray99',
                                 bg='gray99', bd=0.5)
            b_cadastrar.place(x=200, y=350)
            # BUTTON voltar
            b_voltar = Button(c_alunos, width=20, text='Voltar',
                              command=voltar1,
                              activebackground='gray28',
                              activeforeground='gray99',
                              bg='gray99', bd=0.5)
            b_voltar.place(x=350, y=350)

        def jan_alteraraluno():
            # janela alterar alunos
            a_alunos = Tk()
            a_alunos.title('Alterando Cadastro do Aluno')
            a_alunos['bg'] = 'bisque'
            a_alunos.geometry('700x450+350+100')
            alunos.destroy()

            def voltar():
                a_alunos.destroy()
                jan_principal()

            # titulos
            titulo(a_alunos)
            a = 'ALTERAR CADASTRO DO ALUNO'
            tipotitulo(a_alunos, a)

            # LABEL : ID NOME CPF
            lb_id = Label(a_alunos, text='ID    NOME        CPF')
            lb_id.place(x=175, y=240)
            lb_id['bg'] = 'bisque'

            # Entrada do cpf pra pesquisar
            e_cpf = Entry(a_alunos, width=40)
            e_cpf.place(x=295, y=180)

            # nome : cpf para pesquisa
            lb = Label(a_alunos, text='Digite o CPF:')
            lb.place(x=170, y=178)
            lb['bg'] = 'bisque'

            # tela de informações
            C = Listbox(a_alunos, width=40, height=3, bg='snow', bd=0.6, relief='raise', font='30')
            C.place(x=175, y=260)

            def entradadenovasinf():
                def bd_alterar():
                    nome = (nv_nome.get())
                    cpf = (nv_cpf.get())
                    c = conn.cursor()
                    c.execute("""
                        UPDATE alunos
                        SET nome = '%s', cpf = '%s' WHERE cpf = '%s'
                        """ % (nome, cpf, cpfa))
                    conn.commit()
                    nv_cpf.delete(0, END)
                    nv_nome.delete(0, END)

                    lb = Label(at_inf, text='Aluno alterado!', font='12')
                    lb.place(x=200, y=380)
                    lb['bg'] = 'bisque'

                c = conn.cursor()
                cpfa = str(e_cpf.get())
                c.execute('''SELECT * FROM alunos WHERE cpf = '%s';''' % cpfa)
                at_inf = Tk()
                at_inf.title('Atualizando Cadastro do Aluno')
                at_inf['bg'] = 'bisque'
                at_inf.geometry('700x450+350+100')
                a_alunos.destroy()

                def voltar_():
                    at_inf.destroy()
                    jan_principal()

                # titulos
                titulo(at_inf)
                a = 'ALTERAR CADASTRO DO ALUNO'
                tipotitulo(at_inf, a)

                # Entrada de novo nome
                nv_nome = Entry(at_inf, width=40)
                nv_nome.place(x=295, y=180)

                # entrada de novo cpf
                nv_cpf = Entry(at_inf, width=40)
                nv_cpf.place(x=295, y=220)

                # Texto - Novo nome
                lb_n = Label(at_inf, text='Novo nome:', font='12')
                lb_n.place(x=170, y=176)
                lb_n['bg'] = 'bisque'

                # Texto - Novo cpf
                lb_c = Label(at_inf, text='Novo cpf:', font='12')
                lb_c.place(x=170, y=216)
                lb_c['bg'] = 'bisque'

                # button: Alterar
                butt_a = Button(at_inf, width=20,
                                command=bd_alterar,
                                text='Alterar',
                                activebackground='gray28',
                                activeforeground='gray99',
                                bg='gray99', bd=0.5)
                butt_a.place(x=220, y=350)

                # button : voltar
                butt_v = Button(at_inf, width=20,
                                text='Voltar',
                                command=voltar_,
                                activebackground='gray28',
                                activeforeground='gray99',
                                bg='gray99', bd=0.5)
                butt_v.place(x=380, y=350)

            def pesquisa():
                def Ok():
                    erro.destroy()
                    e_cpf.delete(0, END)

                cpfa = e_cpf.get()
                c = conn.cursor()
                c.execute('''SELECT * FROM alunos WHERE cpf = '%s';''' % cpfa)
                a = c.fetchall()
                if len(a) == 0:
                    erro = Tk()
                    erro.title('Erro')
                    erro.geometry('180x150+620+280')
                    lb = Label(erro, text='CPF não encontrado!')
                    lb.place(x=45, y=50)
                    bt = Button(erro, text='OK', command=Ok)
                    bt.place(x=75, y=85)
                    C.delete(0, END)
                else:
                    C.insert(0, a)

            # button : alterar cadastro
            butt_a = Button(a_alunos, width=20,
                            command=entradadenovasinf,
                            text='Alterar cadastro',
                            activebackground='gray28',
                            activeforeground='gray99',
                            bg='gray99', bd=0.5)
            butt_a.place(x=220, y=350)
            # Button pesquisar
            btp = Button(a_alunos, width=10, text='Pesquisar',
                         command=pesquisa,
                         activebackground='gray28',
                         activeforeground='gray99',
                         bg='gray99', bd=0.5)
            btp.place(x=455, y=200)

            # button : voltar
            butt_v = Button(a_alunos, width=20,
                            text='Voltar',
                            command=voltar,
                            activebackground='gray28',
                            activeforeground='gray99',
                            bg='gray99', bd=0.5)
            butt_v.place(x=380, y=350)

        def jan_consultaraluno():
            # janela consultar alunos
            co_alunos = Tk()
            co_alunos.title('Consultando Aluno')
            co_alunos['bg'] = 'bisque'
            co_alunos.geometry('700x450+350+100')
            alunos.destroy()

            def voltar():
                co_alunos.destroy()
                jan_principal()

            # titulos
            titulo(co_alunos)
            a = 'CONSULTAR ALUNO'
            tipotitulo(co_alunos, a)

            # LABEL : ID NOME CPF
            lb_id = Label(co_alunos, text='ID    NOME        CPF')
            lb_id.place(x=175, y=220)
            lb_id['bg'] = 'bisque'

            # tela
            C = Listbox(co_alunos, width=40, height=7, bg='snow', bd=0.6, relief='raise', font='30')
            C.place(x=175, y=240)
            cursor.execute('''SELECT * FROM alunos''')
            x = 1
            for i in cursor.fetchall():
                C.insert(x + 1, i)

            def pesquisa():
                cpfa = str(e_cpf.get())
                c = conn.cursor()
                try:
                    c.execute('''SELECT * FROM alunos WHERE cpf = '%s';''' % cpfa)
                    C = Listbox(co_alunos, width=40, height=7, bg='snow', bd=0.6, relief='raise', font='30')
                    C.place(x=175, y=240)
                    for i in c.fetchall():
                        C.insert(0, i)
                    e_cpf.delete(0, END)
                except:
                    print('erro')

            # Entrada do cpf pra pesquisar
            e_cpf = Entry(co_alunos, width=40)
            e_cpf.place(x=295, y=160)

            # Button pesquisar
            btp = Button(co_alunos, width=10, text='Pesquisar',
                         command=pesquisa,
                         activebackground='gray28',
                         activeforeground='gray99',
                         bg='gray99', bd=0.5)
            btp.place(x=455, y=185)

            # nome : cpf para pesquisa
            lb = Label(co_alunos, text='CPF para pesquisa:')
            lb.place(x=170, y=158)
            lb['bg'] = 'bisque'

            # button : voltar
            butt_v = Button(co_alunos, width=20,
                            text='Voltar',
                            command=voltar,
                            activebackground='gray28',
                            activeforeground='gray99',
                            bg='gray99', bd=0.5)
            butt_v.place(x=490, y=400)

        def jan_removeraluno():
            # janela remover alunos
            r_alunos = Tk()
            r_alunos.title('Removendo Aluno')
            r_alunos['bg'] = 'bisque'
            r_alunos.geometry('700x450+350+100')
            alunos.destroy()

            def voltar():
                r_alunos.destroy()
                jan_principal()

            # titulos
            titulo(r_alunos)
            a = 'REMOVER ALUNO'
            tipotitulo(r_alunos, a)

            # LABEL : ID NOME CPF
            lb_id = Label(r_alunos, text='ID    NOME        CPF')
            lb_id.place(x=175, y=220)
            lb_id['bg'] = 'bisque'

            # tela
            C = Listbox(r_alunos, width=40, height=6, bg='snow', bd=0.6, relief='raise', font='30')
            C.place(x=175, y=240)

            def pesquisa():
                def Ok():
                    erro.destroy()
                    e_cpf.delete(0, END)

                cpfa = e_cpf.get()
                c = conn.cursor()
                c.execute('''SELECT * FROM alunos WHERE cpf = '%s';''' % cpfa)
                a = c.fetchall()
                if len(a) == 0:
                    erro = Tk()
                    erro.title('Erro')
                    erro.geometry('180x150+620+280')
                    lb = Label(erro, text='CPF não encontrado!')
                    lb.place(x=45, y=50)
                    bt = Button(erro, text='OK', command=Ok)
                    bt.place(x=75, y=85)
                    C.delete(0, END)
                else:
                    C.insert(0, a)

            def remover():
                cpfa = e_cpf.get()
                c = conn.cursor()
                c.execute("""DELETE FROM alunos WHERE cpf = '%s'; """ % (cpfa))
                conn.commit()
                e_cpf.delete(0, END)
                lb_id = Label(r_alunos, text='Aluno removido')
                lb_id.place(x=320, y=360)
                lb_id['bg'] = 'bisque'
                C.delete(0, END)

            # Entrada do cpf pra pesquisar
            e_cpf = Entry(r_alunos, width=40)
            e_cpf.place(x=295, y=160)

            # Button pesquisar
            btp = Button(r_alunos, width=10, text='Pesquisar',
                         command=pesquisa,
                         activebackground='gray28',
                         activeforeground='gray99',
                         bg='gray99', bd=0.5)
            btp.place(x=455, y=185)

            # nome : cpf para pesquisa
            lb = Label(r_alunos, text='Digite o cpf:')
            lb.place(x=170, y=158)
            lb['bg'] = 'bisque'

            # button : remover cadastro
            butt_a = Button(r_alunos, width=20,
                            command=remover,
                            text='Remover cadastro',
                            activebackground='gray28',
                            activeforeground='gray99',
                            bg='gray99', bd=0.5)
            butt_a.place(x=320, y=400)

            # button : voltar
            butt_v = Button(r_alunos, width=20,
                            text='Voltar',
                            command=voltar,
                            activebackground='gray28',
                            activeforeground='gray99',
                            bg='gray99', bd=0.5)
            butt_v.place(x=490, y=400)

        def voltar_a():
            alunos.destroy()
            jan_principal()

        # janela alunos
        alunos = Tk()
        alunos.title('Alunos')
        alunos['bg'] = 'bisque'
        alunos.geometry('700x450+350+100')
        janela.destroy()
        # titulos
        titulo(alunos)
        a = 'ALUNOS'
        tipotitulo(alunos, a)
        # button cadastrar aluno
        btac = Button(alunos, width=40,
                      command=jan_cadastroaluno,
                      text='Cadastrar Aluno',
                      activebackground='gray28',
                      activeforeground='gray99',
                      bg='gray99', bd=0.5)
        btac.place(x=200, y=150)

        # button alterar aluno
        btaa = Button(alunos, width=40,
                      command=jan_alteraraluno,
                      text='Alterar Aluno',
                      activebackground='gray28',
                      activeforeground='gray99',
                      bg='gray99', bd=0.5)
        btaa.place(x=200, y=200)

        # button Consultar Aluno
        btaco = Button(alunos, width=40,
                       command=jan_consultaraluno,
                       text='Consultar Aluno',
                       activebackground='gray28',
                       activeforeground='gray99',
                       bg='gray99', bd=0.5)
        btaco.place(x=200, y=250)

        # button Remover aluno
        btar = Button(alunos, width=40,
                      command=jan_removeraluno,
                      text='Remover Aluno',
                      activebackground='gray28',
                      activeforeground='gray99',
                      bg='gray99', bd=0.5)
        btar.place(x=200, y=300)

        # button Voltar
        v = Button(alunos, width=40,
                   command=voltar_a,
                   text='Voltar',
                   activebackground='gray28',
                   activeforeground='gray99',
                   bg='gray99', bd=0.5)
        v.place(x=200, y=350)

    def jan_professores():
        def jan_cadastroprofessor():
            def bd_cadprof():
                def Ok():
                    erro.destroy()
                    cpf.delete(0, END)
                    nome.delete(0, END)
                    departamento.delete(0, END)

                try:
                    nomep = str(nome.get())
                    cpfp = str(cpf.get())
                    departamentop = str(departamento.get())
                    cursor.execute('''
                                    INSERT INTO professores (nome,cpf,departamento)
                                    VALUES('%s','%s','%s')
                                    ''' % (nomep, cpfp, departamentop))
                    conn.commit()
                    lb = Label(c_professores, text='Professor cadastrado!')
                    lb.place(x=350, y=400)
                    cpf.delete(0, END)
                    nome.delete(0, END)
                    departamento.delete(0, END)
                except:
                    erro = Tk()
                    erro.title('Erro')
                    erro.geometry('180x150+620+280')

                    lb = Label(erro, text='CPF já cadastrado!')
                    lb.place(x=45, y=50)

                    bt = Button(erro, text='OK', command=Ok, )
                    bt.place(x=75, y=85)

            def voltar1():
                c_professores.destroy()
                jan_principal()

            # janela cadastro professor
            c_professores = Tk()
            c_professores.title('Cadastro Professor')
            c_professores['bg'] = 'bisque'
            c_professores.geometry('700x450+350+100')
            professores.destroy()

            # titulos
            titulo(c_professores)
            a = 'CADASTRO DE PROFESSORES'
            tipotitulo(c_professores, a)

            # Nome
            lb_nome = Label(c_professores, text='Nome :', font='30')
            lb_nome.place(x=170, y=150)
            lb_nome['bg'] = 'bisque'

            # Entrada do nome
            nome = Entry(c_professores, width=45)
            nome.place(x=230, y=153)

            # CPF
            lb_cpf = Label(c_professores, text='CPF :', font='25')
            lb_cpf.place(x=170, y=200)
            lb_cpf['bg'] = 'bisque'

            # Entrada do cpf
            cpf = Entry(c_professores, width=45)
            cpf.place(x=230, y=203)

            # Departamento
            lb_departamento = Label(c_professores, text='Departamento :', font='25')
            lb_departamento.place(x=170, y=250)
            lb_departamento['bg'] = 'bisque'

            # Entrada do departamento
            departamento = Entry(c_professores, width=45)
            departamento.place(x=285, y=253)

            # BUTTON cadastrar aluno
            b_cadastrar = Button(c_professores, width=20, text='Cadastrar',
                                 command=bd_cadprof,
                                 activebackground='gray28',
                                 activeforeground='gray99',
                                 bg='gray99', bd=0.5)
            b_cadastrar.place(x=200, y=350)
            # BUTTON voltar
            b_voltar = Button(c_professores, width=20, text='Voltar',
                              command=voltar1,
                              activebackground='gray28',
                              activeforeground='gray99',
                              bg='gray99', bd=0.5)
            b_voltar.place(x=350, y=350)

        def jan_alterarprofessor():
            # janela alterar professor
            a_professor = Tk()
            a_professor.title('PROFESSORES')
            a_professor['bg'] = 'bisque'
            a_professor.geometry('700x450+350+100')
            professores.destroy()

            # titulos
            titulo(a_professor)
            a = 'ALTERAR CADASTRO DO PROFESSOR'
            tipotitulo(a_professor, a)

            def voltar():
                a_professor.destroy()
                jan_principal()

            # LABEL : ID NOME CPF
            lb_id = Label(a_professor, text='ID    NOME        CPF        Departamento')
            lb_id.place(x=175, y=220)
            lb_id['bg'] = 'bisque'

            # tela
            Cp = Listbox(a_professor, width=40, height=3, bg='snow', bd=0.6, relief='raise', font='30')
            Cp.place(x=175, y=240)

            def entradadenovasinf():
                def bd_alterar():
                    nome = (nv_nome.get())
                    cpf = (nv_cpf.get())
                    dp = (nv_dep.get())
                    c = conn.cursor()
                    c.execute("""
                        UPDATE professores
                        SET nome = '%s', cpf = '%s', departamento = '%s' WHERE cpf = '%s'
                        """ % (nome, cpf, dp, cpfa))
                    conn.commit()
                    nv_cpf.delete(0, END)
                    nv_nome.delete(0, END)
                    nv_dep.delete(0, END)
                    lb = Label(at_inf, text='Professor alterado!', font='12')
                    lb.place(x=200, y=380)
                    lb['bg'] = 'bisque'

                c = conn.cursor()
                cpfa = str(e_cpf.get())
                c.execute('''SELECT * FROM professores WHERE cpf = '%s';''' % cpfa)
                at_inf = Tk()
                at_inf.title('Atualizando Cadastro do Professor')
                at_inf['bg'] = 'bisque'
                at_inf.geometry('700x450+350+100')
                a_professor.destroy()

                def voltar_():
                    at_inf.destroy()
                    jan_principal()

                # titulos
                titulo(at_inf)
                a = 'ALTERAR CADASTRO DO ALUNO'
                tipotitulo(at_inf, a)

                # Entrada de novo nome
                nv_nome = Entry(at_inf, width=40)
                nv_nome.place(x=295, y=180)

                # entrada de novo cpf
                nv_cpf = Entry(at_inf, width=40)
                nv_cpf.place(x=295, y=220)

                # entrada de novo departamento
                nv_dep = Entry(at_inf, width=40)
                nv_dep.place(x=325, y=260)

                # Texto - Novo nome
                lb_n = Label(at_inf, text='Novo nome:', font='12')
                lb_n.place(x=170, y=176)
                lb_n['bg'] = 'bisque'

                # Texto - Novo cpf
                lb_c = Label(at_inf, text='Novo cpf:', font='12')
                lb_c.place(x=170, y=216)
                lb_c['bg'] = 'bisque'

                # Texto - Novo Departamento
                lb_c = Label(at_inf, text='Novo departamento:', font='12')
                lb_c.place(x=170, y=256)
                lb_c['bg'] = 'bisque'

                # button: Alterar
                butt_a = Button(at_inf, width=20,
                                command=bd_alterar,
                                text='Alterar',
                                activebackground='gray28',
                                activeforeground='gray99',
                                bg='gray99', bd=0.5)
                butt_a.place(x=220, y=350)

                # button : voltar
                butt_v = Button(at_inf, width=20,
                                text='Voltar',
                                command=voltar_,
                                activebackground='gray28',
                                activeforeground='gray99',
                                bg='gray99', bd=0.5)
                butt_v.place(x=380, y=350)

            def pesquisa():
                def Ok():
                    erro.destroy()
                    e_cpf.delete(0, END)

                cpfa = e_cpf.get()
                c = conn.cursor()
                c.execute('''SELECT * FROM professores WHERE cpf = '%s';''' % cpfa)
                a = c.fetchall()
                if len(a) == 0:
                    erro = Tk()
                    erro.title('Erro')
                    erro.geometry('180x150+620+280')
                    lb = Label(erro, text='CPF não encontrado!')
                    lb.place(x=45, y=50)
                    bt = Button(erro, text='OK', command=Ok)
                    bt.place(x=75, y=85)
                    Cp.delete(0, END)
                else:
                    Cp.insert(0, a)

            # Entrada do cpf pra pesquisar
            e_cpf = Entry(a_professor, width=40)
            e_cpf.place(x=295, y=180)

            # nome : cpf para pesquisa
            lb = Label(a_professor, text='CPF para pesquisa:')
            lb.place(x=170, y=178)
            lb['bg'] = 'bisque'

            # Entrada do cpf pra pesquisar
            e_cpf = Entry(a_professor, width=40)
            e_cpf.place(x=295, y=180)

            # button : alterar cadastro
            butt_a = Button(a_professor, width=20,
                            command=entradadenovasinf,
                            text='Alterar cadastro',
                            activebackground='gray28',
                            activeforeground='gray99',
                            bg='gray99', bd=0.5)
            butt_a.place(x=220, y=350)
            # Button pesquisar
            btp = Button(a_professor, width=10, text='Pesquisar',
                         command=pesquisa,
                         activebackground='gray28',
                         activeforeground='gray99',
                         bg='gray99', bd=0.5)
            btp.place(x=455, y=200)
            # button : voltar
            butt_v = Button(a_professor, width=20,
                            text='Voltar',
                            command=voltar,
                            activebackground='gray28',
                            activeforeground='gray99',
                            bg='gray99', bd=0.5)
            butt_v.place(x=380, y=350)

        def jan_consultarprofessor():
            # janela consultar professor
            co_professor = Tk()
            co_professor.title('Consultando Professor')
            co_professor['bg'] = 'bisque'
            co_professor.geometry('700x450+350+100')
            professores.destroy()
            # titulos
            titulo(co_professor)
            a = 'CONSULTANDO PROFESSOR'
            tipotitulo(co_professor, a)

            def voltar():
                co_professor.destroy()
                jan_principal()

            # titulos
            titulo(co_professor)
            a = 'CONSULTAR ALUNO'
            tipotitulo(co_professor, a)

            # LABEL : ID NOME CPF Departamento
            lb_id = Label(co_professor, text='ID    NOME        CPF        Departamento')
            lb_id.place(x=175, y=220)
            lb_id['bg'] = 'bisque'

            # tela
            Cp = Listbox(co_professor, width=40, height=7, bg='snow', bd=0.6, relief='raise', font='30')
            Cp.place(x=175, y=240)
            c = conn.cursor()
            c.execute('''SELECT * FROM professores''')
            x = 1
            for i in c.fetchall():
                Cp.insert(x + 1, i)

            def pesquisa():
                cpfp = str(e_cpf.get())
                c = conn.cursor()
                c.execute('''SELECT * FROM professores WHERE cpf = '%s';''' % cpfp)
                C = Listbox(co_professor, width=40, height=7, bg='snow', bd=0.6, relief='raise', font='30')
                C.place(x=175, y=240)
                for i in c.fetchall():
                    C.insert(0, i)
                e_cpf.delete(0, END)

            # Entrada do cpf pra pesquisar
            e_cpf = Entry(co_professor, width=40)
            e_cpf.place(x=295, y=160)

            # Button pesquisar
            btp = Button(co_professor, width=10, text='Pesquisar',
                         command=pesquisa,
                         activebackground='gray28',
                         activeforeground='gray99',
                         bg='gray99', bd=0.5)
            btp.place(x=455, y=185)

            # nome : cpf para pesquisa
            lb = Label(co_professor, text='Digite o cpf:')
            lb.place(x=170, y=158)
            lb['bg'] = 'bisque'

            # button : voltar
            butt_v = Button(co_professor, width=20,
                            text='Voltar',
                            command=voltar,
                            activebackground='gray28',
                            activeforeground='gray99',
                            bg='gray99', bd=0.5)
            butt_v.place(x=490, y=400)

        def jan_removerprofessor():
            # janela remover professor
            r_professor = Tk()
            r_professor.title('Removendo professor')
            r_professor['bg'] = 'bisque'
            r_professor.geometry('700x450+350+100')
            professores.destroy()

            def voltar():
                r_professor.destroy()
                jan_principal()

            # titulos
            titulo(r_professor)
            a = 'REMOVENDO PROFESSOR'
            tipotitulo(r_professor, a)

            # LABEL : ID NOME CPF Departamento
            lb_id = Label(r_professor, text='ID    NOME        CPF        Departamento')
            lb_id.place(x=175, y=220)
            lb_id['bg'] = 'bisque'

            # tela
            Cp = Listbox(r_professor, width=40, height=7, bg='snow', bd=0.6, relief='raise', font='30')
            Cp.place(x=175, y=240)

            def pesquisa():
                def Ok():
                    erro.destroy()
                    e_cpf.delete(0, END)

                cpfa = e_cpf.get()
                c = conn.cursor()
                c.execute('''SELECT * FROM professores WHERE cpf = '%s';''' % cpfa)
                a = c.fetchall()
                if len(a) == 0:
                    erro = Tk()
                    erro.title('Erro')
                    erro.geometry('180x150+620+280')
                    lb = Label(erro, text='CPF não encontrado!')
                    lb.place(x=45, y=50)
                    bt = Button(erro, text='OK', command=Ok)
                    bt.place(x=75, y=85)
                    Cp.delete(0, END)
                else:
                    Cp.insert(0, a)

            def remover():
                cpfa = e_cpf.get()
                c = conn.cursor()
                c.execute("""DELETE FROM professores WHERE cpf = '%s'; """ % (cpfa))
                conn.commit()
                e_cpf.delete(0, END)
                lb_id = Label(r_professor, text='Professor removido')
                lb_id.place(x=265, y=400)
                lb_id['bg'] = 'bisque'
                Cp.delete(0, END)

            # Entrada do cpf pra pesquisar
            e_cpf = Entry(r_professor, width=40)
            e_cpf.place(x=295, y=160)

            # Button pesquisar
            btp = Button(r_professor, width=10, text='Pesquisar',
                         activebackground='gray28',
                         activeforeground='gray99',
                         bg='gray99', bd=0.5)
            btp.place(x=455, y=185)

            # nome : cpf para pesquisa
            lb = Label(r_professor, text='CPF para pesquisa:')
            lb.place(x=170, y=158)
            lb['bg'] = 'bisque'

            # button : deletar
            buttd = Button(r_professor, width=12,
                           text='Remover',
                           command=remover,
                           activebackground='gray28',
                           activeforeground='gray99',
                           bg='gray99', bd=0.5)
            buttd.place(x=390, y=400)

            # Button pesquisar
            btp = Button(r_professor, width=10, text='Pesquisar',
                         command=pesquisa,
                         activebackground='gray28',
                         activeforeground='gray99',
                         bg='gray99', bd=0.5)
            btp.place(x=455, y=185)

            # button : voltar
            butt_v = Button(r_professor, width=12,
                            text='Voltar',
                            command=voltar,
                            activebackground='gray28',
                            activeforeground='gray99',
                            bg='gray99', bd=0.5)
            butt_v.place(x=500, y=400)

        def voltar():
            professores.destroy()
            jan_principal()

        # janela professores
        professores = Tk()
        professores.title('Professores')
        professores['bg'] = 'bisque'
        professores.geometry('700x450+350+100')
        janela.destroy()

        # titulos
        titulo(professores)
        a = 'PROFESSORES'
        tipotitulo(professores, a)

        # button cadastrar professor
        btpc = Button(professores, width=40,
                      command=jan_cadastroprofessor,
                      text='Cadastrar Professor',
                      activebackground='gray28',
                      activeforeground='gray99',
                      bg='gray99', bd=0.5)
        btpc.place(x=200, y=150)

        # button alterar professor
        btpa = Button(professores, width=40,
                      command=jan_alterarprofessor,
                      text='Alterar Professor',
                      activebackground='gray28',
                      activeforeground='gray99',
                      bg='gray99', bd=0.5)
        btpa.place(x=200, y=200)

        # button consultar professor
        btpco = Button(professores, width=40,
                       command=jan_consultarprofessor,
                       text='Consultar Professor',
                       activebackground='gray28',
                       activeforeground='gray99',
                       bg='gray99', bd=0.5)
        btpco.place(x=200, y=250)

        # button Remover professor
        btpr = Button(professores, width=40,
                      command=jan_removerprofessor,
                      text='Remover Professor',
                      activebackground='gray28',
                      activeforeground='gray99',
                      bg='gray99', bd=0.5)
        btpr.place(x=200, y=300)

        # voltar
        v = Button(professores, width=40,
                   command=voltar,
                   text='Voltar',
                   activebackground='gray28',
                   activeforeground='gray99',
                   bg='gray99', bd=0.5)
        v.place(x=200, y=350)

    def jan_disciplinas():
        def jan_cadastrodisciplinas():
            def bd_caddis():
                def Ok():
                    erro.destroy()
                    codigod.delete(0, END)
                    nomed.delete(0, END)

                try:
                    nomedd = str(nomed.get())
                    codigodd = str(codigod.get())
                    cursor.execute('''
                                    INSERT INTO disciplinas (nome,codigo)
                                    VALUES('%s','%s')
                                    ''' % (nomedd, codigodd))
                    conn.commit()
                    lb = Label(c_disciplinas, text='Disciplina cadastrada!')
                    lb.place(x=350, y=400)
                    codigod.delete(0, END)
                    nomed.delete(0, END)
                except:
                    erro = Tk()
                    erro.title('Erro')
                    erro.geometry('180x150+620+280')

                    lb = Label(erro, text='Código já cadastrado!')
                    lb.place(x=45, y=50)

                    bt = Button(erro, text='OK', command=Ok, )
                    bt.place(x=75, y=85)

            def voltar1():
                c_disciplinas.destroy()
                jan_principal()

            # janela cadastro disciplinas
            c_disciplinas = Tk()
            c_disciplinas.title('Cadastro Professor')
            c_disciplinas['bg'] = 'bisque'
            c_disciplinas.geometry('700x450+350+100')
            disciplinas.destroy()

            # titulos
            titulo(c_disciplinas)
            a = 'CADASTRO DE DISCIPLINA'
            tipotitulo(c_disciplinas, a)

            # Nome da disciplina
            lb_disciplinas = Label(c_disciplinas, text='Nome da disciplina: ', font='30')
            lb_disciplinas.place(x=100, y=150)
            lb_disciplinas['bg'] = 'bisque'

            # Entrada do nome
            nomed = Entry(c_disciplinas, width=45)
            nomed.place(x=260, y=153)

            # Codigo da disciplina
            lb_codigod = Label(c_disciplinas, text='Código da disciplina :', font='25')
            lb_codigod.place(x=100, y=220)
            lb_codigod['bg'] = 'bisque'

            # Entrada do codigo
            codigod = Entry(c_disciplinas, width=45)
            codigod.place(x=260, y=223)

            # BUTTON cadastrar disciplina
            b_cadastrar = Button(c_disciplinas, width=20, text='Cadastrar',
                                 command=bd_caddis,
                                 activebackground='gray28',
                                 activeforeground='gray99',
                                 bg='gray99', bd=0.5)
            b_cadastrar.place(x=200, y=350)
            # BUTTON voltar
            b_voltar = Button(c_disciplinas, width=20, text='Voltar',
                              command=voltar1,
                              activebackground='gray28',
                              activeforeground='gray99',
                              bg='gray99', bd=0.5)
            b_voltar.place(x=350, y=350)

        def jan_alterardisciplina():
            # janela alterar disciplina
            a_disciplinas = Tk()
            a_disciplinas.title('Alterando disciplina')
            a_disciplinas['bg'] = 'bisque'
            a_disciplinas.geometry('700x450+350+100')
            disciplinas.destroy()

            def voltar():
                a_disciplinas.destroy()
                jan_principal()

            # titulo
            titulo(a_disciplinas)
            a = 'ALTERAR DISCIPLINA'
            tipotitulo(a_disciplinas, a)

            # LABEL : ID NOME CODIGO
            lb_id = Label(a_disciplinas, text='ID    NOME        CODIGO')
            lb_id.place(x=175, y=220)
            lb_id['bg'] = 'bisque'

            # nome : codigo para pesquisa
            lb = Label(a_disciplinas, text='Codigo para pesquisa:')
            lb.place(x=170, y=178)
            lb['bg'] = 'bisque'

            # tela
            C = Listbox(a_disciplinas, width=40, height=3, bg='snow', bd=0.6, relief='raise', font='30')
            C.place(x=175, y=240)

            def entradadenovasinf():
                def bd_alterar():
                    nome = n_nome.get()
                    cod = n_cod.get()
                    cursor = conn.cursor()
                    cursor.execute("""
                                    UPDATE disciplinas
                                    SET nome = '%s', codigo = '%s' WHERE codigo = '%s'
                                    """ % (nome, cod, codd))
                    conn.commit()
                    n_cod.delete(0, END)
                    n_nome.delete(0, END)

                    lb = Label(at_inf, text='Disciplina alterada!', font='12')
                    lb.place(x=200, y=380)
                    lb['bg'] = 'bisque'

                codd = str(e_codigo.get())
                c = conn.cursor()
                c.execute('''SELECT * FROM disciplinas WHERE codigo = '%s';''' % codd)
                at_inf = Tk()
                at_inf.title('Atualizando Cadastro da Disciplina')
                at_inf['bg'] = 'bisque'
                at_inf.geometry('700x450+350+100')
                a_disciplinas.destroy()

                def voltar_():
                    at_inf.destroy()
                    jan_principal()

                # titulos
                titulo(at_inf)
                a = 'ALTERAR DISCIPLINA'
                tipotitulo(at_inf, a)

                # Entrada de novo nome
                n_nome = Entry(at_inf, width=40)
                n_nome.place(x=295, y=180)

                # entrada de novo codigo
                n_cod = Entry(at_inf, width=40)
                n_cod.place(x=295, y=220)

                # Texto - Novo nome
                lb_n = Label(at_inf, text='Novo nome:', font='12')
                lb_n.place(x=170, y=176)
                lb_n['bg'] = 'bisque'

                # Texto - Novo codigo
                lb_c = Label(at_inf, text='Novo codigo:', font='12')
                lb_c.place(x=170, y=216)
                lb_c['bg'] = 'bisque'

                # button: Alterar
                butt_a = Button(at_inf, width=20,
                                command=bd_alterar,
                                text='Alterar',
                                activebackground='gray28',
                                activeforeground='gray99',
                                bg='gray99', bd=0.5)
                butt_a.place(x=220, y=350)

                # button : voltar
                butt_v = Button(at_inf, width=20,
                                text='Voltar',
                                command=voltar_,
                                activebackground='gray28',
                                activeforeground='gray99',
                                bg='gray99', bd=0.5)
                butt_v.place(x=380, y=350)

            def pesquisa():
                def Ok():
                    erro.destroy()
                    e_codigo.delete(0, END)

                codd = e_codigo.get()
                c = conn.cursor()
                c.execute('''SELECT * FROM disciplinas WHERE codigo = '%s';''' % codd)
                a = c.fetchall()
                if len(a) == 0:
                    erro = Tk()
                    erro.title('Erro')
                    erro.geometry('180x150+620+280')
                    lb = Label(erro, text='Disciplina não encontrada!')
                    lb.place(x=45, y=50)
                    bt = Button(erro, text='OK', command=Ok)
                    bt.place(x=75, y=85)
                    C.delete(0, END)
                else:
                    C.insert(0, a)

            # Entrada do codigo pra pesquisar
            e_codigo = Entry(a_disciplinas, width=40)
            e_codigo.place(x=295, y=180)

            # button : alterar cadastro
            butt_a = Button(a_disciplinas, width=20,
                            command=entradadenovasinf,
                            text='Alterar cadastro',
                            activebackground='gray28',
                            activeforeground='gray99',
                            bg='gray99', bd=0.5)
            butt_a.place(x=220, y=350)

            btp = Button(a_disciplinas, width=10, text='Pesquisar',
                         command=pesquisa,
                         activebackground='gray28',
                         activeforeground='gray99',
                         bg='gray99', bd=0.5)
            btp.place(x=455, y=200)

            # button : voltar
            butt_v = Button(a_disciplinas, width=20,
                            text='Voltar',
                            command=voltar,
                            activebackground='gray28',
                            activeforeground='gray99',
                            bg='gray99', bd=0.5)
            butt_v.place(x=380, y=350)

        def jan_consultardisciplina():
            # janela consultar disciplina
            co_disciplina = Tk()
            co_disciplina.title('Consultando disciplina')
            co_disciplina['bg'] = 'bisque'
            co_disciplina.geometry('700x450+350+100')
            disciplinas.destroy()

            # titulos
            titulo(co_disciplina)
            a = 'CONSULTANDO DISCIPLINA'
            tipotitulo(co_disciplina, a)

            def voltar():
                co_disciplina.destroy()
                jan_principal()

            # LABEL : ID NOME CPF Departamento
            lb_id = Label(co_disciplina, text='ID    NOME        CPF        Departamento')
            lb_id.place(x=175, y=220)
            lb_id['bg'] = 'bisque'

            # tela
            C = Listbox(co_disciplina, width=40, height=7, bg='snow', bd=0.6, relief='raise', font='30')
            C.place(x=175, y=240)
            c = conn.cursor()
            c.execute('''SELECT * FROM disciplinas''')
            x = 1
            for i in c.fetchall():
                C.insert(x + 1, i)

            def pesquisa():
                dcodigo = str(e_codigo.get())
                c = conn.cursor()
                try:
                    c.execute('''SELECT * FROM disciplinas WHERE codigo = '%s';''' % dcodigo)
                    C = Listbox(co_disciplina, width=40, height=7, bg='snow', bd=0.6, relief='raise', font='30')
                    C.place(x=175, y=240)
                    for i in c.fetchall():
                        C.insert(0, i)
                    e_codigo.delete(0, END)
                except:
                    print('erro')

            # Entrada do codigo pra pesquisar
            e_codigo = Entry(co_disciplina, width=40)
            e_codigo.place(x=295, y=160)

            # Button pesquisar
            btp = Button(co_disciplina, width=10, text='Pesquisar', command=pesquisa,
                         activebackground='gray28',
                         activeforeground='gray99',
                         bg='gray99', bd=0.5)
            btp.place(x=455, y=185)

            # nome : codigo para pesquisa
            lb = Label(co_disciplina, text='Código para pesquisa:')
            lb.place(x=170, y=158)
            lb['bg'] = 'bisque'

            # button : voltar
            butt_v = Button(co_disciplina, width=20,
                            text='Voltar',
                            command=voltar,
                            activebackground='gray28',
                            activeforeground='gray99',
                            bg='gray99', bd=0.5)
            butt_v.place(x=490, y=400)

        def jan_removerdisciplina():
            # janela remover disciplina
            r_disciplina = Tk()
            r_disciplina.title('Alunos')
            r_disciplina['bg'] = 'bisque'
            r_disciplina.geometry('700x450+350+100')
            disciplinas.destroy()

            def voltar():
                r_disciplina.destroy()
                jan_principal()

            # titulos
            titulo(r_disciplina)
            a = 'REMOVENDO DISCIPLINA'
            tipotitulo(r_disciplina, a)

            # LABEL : ID NOME Codigo
            lb_id = Label(r_disciplina, text='ID    NOME        CODIGO')
            lb_id.place(x=175, y=220)
            lb_id['bg'] = 'bisque'

            # tela
            C = Listbox(r_disciplina, width=40, height=8, bg='snow', bd=0.6, relief='raise', font='30')
            C.place(x=175, y=240)

            def pesquisa():
                def Ok():
                    erro.destroy()
                    e_codigo.delete(0, END)

                dcodigo = str(e_codigo.get())
                c = conn.cursor()
                c.execute('''SELECT * FROM disciplinas WHERE codigo = '%s';''' % dcodigo)
                a = c.fetchall()
                if len(a) == 0:
                    erro = Tk()
                    erro.title('Erro')
                    erro.geometry('180x150+620+280')
                    lb = Label(erro, text='Disciplina não encontrada!')
                    lb.place(x=45, y=50)
                    bt = Button(erro, text='OK', command=Ok)
                    bt.place(x=75, y=85)
                    C.delete(0, END)
                else:
                    C.insert(0, a)

            def remover():
                dcodigo = str(e_codigo.get())
                c = conn.cursor()
                c.execute("""DELETE FROM disciplinas WHERE codigo = '%s' ;""" % (dcodigo))
                conn.commit()
                e_codigo.delete(0, END)
                lb_id = Label(r_disciplina, text='Disciplina removida')
                lb_id.place(x=320, y=360)
                lb_id['bg'] = 'bisque'
                C.delete(0, END)

            # Entrada do codigo pra pesquisar
            e_codigo = Entry(r_disciplina, width=40)
            e_codigo.place(x=295, y=160)

            # Button pesquisar
            btp = Button(r_disciplina, width=10, text='Pesquisar',
                         command=pesquisa,
                         activebackground='gray28',
                         activeforeground='gray99',
                         bg='gray99', bd=0.5)
            btp.place(x=455, y=185)

            # nome : codigo para pesquisa
            lb = Label(r_disciplina, text='Código para pesquisa:')
            lb.place(x=170, y=158)
            lb['bg'] = 'bisque'
            # button : deletar
            buttd = Button(r_disciplina, width=12,
                           command=remover,
                           text='Deletar',
                           activebackground='gray28',
                           activeforeground='gray99',
                           bg='gray99', bd=0.5)
            buttd.place(x=390, y=400)

            # button : voltar
            butt_v = Button(r_disciplina, width=12,
                            text='Voltar',
                            command=voltar,
                            activebackground='gray28',
                            activeforeground='gray99',
                            bg='gray99', bd=0.5)
            butt_v.place(x=500, y=400)

        def voltar():
            disciplinas.destroy()
            jan_principal()

        # janela disciplinas
        disciplinas = Tk()
        disciplinas.title('Disciplinas')
        disciplinas['bg'] = 'bisque'
        disciplinas.geometry('700x450+350+100')
        janela.destroy()

        # titulos prof
        titulo(disciplinas)
        a = 'DISCIPLINAS'
        tipotitulo(disciplinas, a)

        # button cadastrar disciplinas
        btdc = Button(disciplinas, width=40,
                      command=jan_cadastrodisciplinas,
                      text='Cadastrar Disciplina',
                      activebackground='gray28',
                      activeforeground='gray99',
                      bg='gray99', bd=0.5)
        btdc.place(x=200, y=150)

        # Button Alterar disciplina
        btda = Button(disciplinas, width=40,
                      command=jan_alterardisciplina,
                      text='Alterar Disciplina',
                      activebackground='gray28',
                      activeforeground='gray99',
                      bg='gray99', bd=0.5)
        btda.place(x=200, y=200)

        # Button Consultar disciplina
        btdco = Button(disciplinas, width=40,
                       command=jan_consultardisciplina,
                       text='Consultar Disciplina',
                       activebackground='gray28',
                       activeforeground='gray99',
                       bg='gray99', bd=0.5)
        btdco.place(x=200, y=250)

        # Button Remover disciplina
        btdr = Button(disciplinas, width=40,
                      command=jan_removerdisciplina,
                      text='Remover Disciplina',
                      activebackground='gray28',
                      activeforeground='gray99',
                      bg='gray99', bd=0.5)
        btdr.place(x=200, y=300)

        # Button Voltar
        v = Button(disciplinas, width=40,
                   command=voltar,
                   text='Voltar',
                   activebackground='gray28',
                   activeforeground='gray99',
                   bg='gray99', bd=0.5)
        v.place(x=200, y=350)

    def jan_turmas():
        def jan_cadastroturmas():
            # janela cadastro turmas
            c_turmas = Tk()
            c_turmas.title('CADASTRO DE TURMAS')
            c_turmas['bg'] = 'bisque'
            c_turmas.geometry('700x450+350+100')
            turmas.destroy()

            def voltar():
                c_turmas.destroy()
                jan_principal()

            # titulos
            titulo(c_turmas)
            a = 'CADASTRO DE TURMAS'
            tipotitulo(c_turmas, a)

            # Textos
            lb_ct = Label(c_turmas, text='Código da turma: ', font='30')
            lb_ct.place(x=100, y=150)
            lb_ct['bg'] = 'bisque'

            def CriandoTurma():
                def Ok():
                    erro.destroy()

                if len(ent_ct.get()) == 0:
                    erro = Tk()
                    erro.title('Erro')
                    erro.geometry('180x150+620+280')

                    lb = Label(erro, text='Preencha o(s) campo(s) vazio(s).')
                    lb.place(x=5, y=50)

                    bt = Button(erro, text='OK', command=Ok, )
                    bt.place(x=75, y=85)
                else:
                    lb_pt = Label(c_turmas, text='Periodo:', font='30')
                    lb_pt.place(x=100, y=200)
                    lb_pt['bg'] = 'bisque'

                    lb_t = Label(c_turmas, text='Turma Adicionada!')
                    lb_t.place(x=520, y=180)

                    lb_ca = Label(c_turmas, text='CPF do aluno: ', font='30')
                    lb_ca.place(x=100, y=350)
                    lb_ca['bg'] = 'bisque'

                    def disciplina_bd():
                        def Ok():
                            erro.destroy()
                            ent_cd.delete(0, END)
                        turma = ent_ct.get()
                        disciplina = str(ent_cd.get())
                        periodo = ent_p.get()
                        c = conn.cursor()
                        a = '''SELECT * FROM disciplinas WHERE codigo = '%s' ; ''' % (disciplina)
                        c.execute(a)
                        aluno = '-'
                        professor = '-'
                        b= c.fetchall()
                        if len(b)==0:
                            erro = Tk()
                            erro.title('Erro')
                            erro.geometry('180x150+620+280')

                            lb = Label(erro, text='Disciplina não cadastrada no sistema!')
                            lb.place(x=45, y=50)

                            bt = Button(erro, text='OK', command=Ok)
                            bt.place(x=75, y=85)
                            ent_ca.delete(0, END)
                        else:
                            b = '''INSERT INTO turmas (codigo,periodo,disciplinas,professores,alunos)
                                                        VALUES ('%s','%s','%s','%s','%s')
                                                        ''' % (turma, periodo, disciplina, professor, aluno)
                            c.execute(b)
                            ent_cd.delete(0, END)
                            conn.commit()
                    def professor_bd():
                        def Ok():
                            erro.destroy()
                            ent_cp.delete(0, END)
                        turma = ent_ct.get()
                        disciplina = '-'
                        professor = ent_cp.get()
                        aluno = '-'
                        periodo = ent_p.get()
                        c = conn.cursor()
                        a = '''SELECT * FROM professores WHERE cpf = '%s' ;
                                                     ''' % (professor)
                        c.execute(a)
                        b= c.fetchall()
                        if len(b)==0 or len(professor)==0:
                            erro = Tk()
                            erro.title('Erro')
                            erro.geometry('180x150+620+280')

                            lb = Label(erro, text='Professor não cadastrado no sistema!')
                            lb.place(x=45, y=50)

                            bt = Button(erro, text='OK', command=Ok)
                            bt.place(x=75, y=85)
                        else:
                            b = '''INSERT INTO turmas (codigo,periodo,disciplinas,professores,alunos)
                            VALUES ('%s','%s','%s','%s','%s')
                            ''' % (turma, periodo, disciplina, professor, aluno)
                            c.execute(b)
                            ent_cp.delete(0, END)
                            conn.commit()
                    def aluno_bd():
                        def Ok():
                            erro.destroy()
                            ent_ca.delete(0, END)

                        turma = ent_ct.get()
                        aluno = ent_ca.get()
                        disciplina = '-'
                        professores = '-'
                        periodo = ent_p.get()
                        a = '''SELECT * FROM alunos WHERE cpf = '%s' ;
                                                     ''' % (aluno)
                        c.execute(a)
                        b= c.fetchall()
                        if len(b)==0 or len(aluno)==0:
                            erro = Tk()
                            erro.title('Erro')
                            erro.geometry('180x150+620+280')

                            lb = Label(erro, text='Aluno não cadastrado no sistema!')
                            lb.place(x=45, y=50)

                            bt = Button(erro, text='OK', command=Ok)
                            bt.place(x=75, y=85)
                        else:
                            turma = ent_ct.get()
                            aluno = ent_ca.get()
                            disciplina = '-'
                            professores = '-'
                            periodo = ent_p.get()
                            a = '''SELECT * FROM alunos WHERE cpf = '%s' ;
                             ''' % (aluno)
                            c.execute(a)
                            b = '''INSERT INTO turmas (codigo,periodo,disciplinas,professores,alunos)
                            VALUES ('%s','%s','%s','%s','%s')
                            ''' % (turma, periodo, disciplina, professores, aluno)
                            c.execute(b)
                            ent_ca.delete(0, END)
                            conn.commit()

                    ent_p = Entry(c_turmas, width=40)  # entry periodo
                    ent_p.place(x=250, y=202)

                    ent_cd = Entry(c_turmas, width=40)  # entry disciplina
                    ent_cd.place(x=250, y=265)

                    ent_ca = Entry(c_turmas, width=40)  # entry aluno
                    ent_ca.place(x=250, y=352)

                    ent_cp = Entry(c_turmas, width=40)  # entry professor
                    ent_cp.place(x=250, y=305)

                    lb_cd = Label(c_turmas, text='Cód. da disciplina:', font='30')
                    lb_cd.place(x=100, y=265)
                    lb_cd['bg'] = 'bisque'

                    lb_ca = Label(c_turmas, text='CPF do professor: ', font='30')
                    lb_ca.place(x=100, y=303)
                    lb_ca['bg'] = 'bisque'

                    bt_d = Button(c_turmas, width=15,  # button adicionar disciplina
                                  command=disciplina_bd,
                                  text='Adicionar disciplina',
                                  activebackground='gray28',
                                  activeforeground='gray99',
                                  bg='gray99', bd=0.5)
                    bt_d.place(x=498, y=265)

                    bt_a = Button(c_turmas, width=15,  # button adicionar aluno
                                  command=aluno_bd,
                                  text='Adicionar aluno',
                                  activebackground='gray28',
                                  activeforeground='gray99',
                                  bg='gray99', bd=0.5)
                    bt_a.place(x=498, y=350)

                    bt_p = Button(c_turmas, width=15,  # button adicionar professor
                                  command=professor_bd,
                                  text='Adicionar professor',
                                  activebackground='gray28',
                                  activeforeground='gray99',
                                  bg='gray99', bd=0.5)
                    bt_p.place(x=498, y=303)

                    def Finalizar():
                        ent_ct.delete(0, END)
                        ent_p.delete(0, END)
                        ent_cp.delete(0, END)
                        ent_cd.delete(0, END)
                        ent_ca.delete(0, END)

                    bt_f = Button(c_turmas, width=15,
                                  command=Finalizar,
                                  text='Finalizar',
                                  activebackground='gray28',
                                  activeforeground='gray99',
                                  bg='gray99', bd=0.5)
                    bt_f.place(x=380, y=390)

            bt_ct = Button(c_turmas, width=15,
                           command=CriandoTurma,
                           text='Criar Turma',
                           activebackground='gray28',
                           activeforeground='gray99',
                           bg='gray99', bd=0.5)
            bt_ct.place(x=500, y=150)

            bt_v = Button(c_turmas, width=15,
                          text='Voltar',
                          command=voltar,
                          activebackground='gray28',
                          activeforeground='gray99',
                          bg='gray99', bd=0.5)
            bt_v.place(x=500, y=390)
            # entry's
            ent_ct = Entry(c_turmas, width=40)
            ent_ct.place(x=250, y=154)

        def jan_alterarturma():
            a_turmas = Tk()
            a_turmas.title('ALTERANDO TURMAS')
            a_turmas['bg'] = 'bisque'
            a_turmas.geometry('700x450+350+100')
            turmas.destroy()

            def voltar():
                a_turmas.destroy()
                jan_principal()

            titulo(a_turmas)
            a = 'ALTERAR CADASTRO DE TURMAS'
            tipotitulo(a_turmas, a)

            lb_ct = Label(a_turmas, text='Código da turma: ', font='30')
            lb_ct.place(x=100, y=150)
            lb_ct['bg'] = 'bisque'

            ent_ct = Entry(a_turmas, width=40)
            ent_ct.place(x=250, y=152)

            def p():
                def Ok():
                    erro.destroy()

                cod = ent_ct.get()
                c = conn.cursor()
                c.execute('''SELECT * FROM turmas WHERE codigo = '%s';''' % cod)
                a = c.fetchall()
                if len(ent_ct.get()) == 0 or len(a) == 0:
                    erro = Tk()
                    erro.title('Erro')
                    erro.geometry('180x150+620+280')

                    lb = Label(erro, text='Turma não encontrada.')
                    lb.place(x=30, y=50)

                    bt = Button(erro, text='OK', command=Ok)
                    bt.place(x=75, y=85)
                else:
                    lbl = Label(a_turmas, text='ID | CODIGO | PERIODO | DISCIPLINAS | PROFESSORES | ALUNOS ')
                    lbl.place(x=115, y=208)

                    lb = Listbox(a_turmas, width=50, height=8, bg='snow', bd=0.6, relief='raise', font='30')
                    lb.place(x=115, y=225)
                    x = 0
                    for i in a:
                        lb.insert(x + 1, i)

                    def AlterandoTurma():
                        al_turma = Tk()
                        al_turma.title('ALTERANDO TURMAS')
                        al_turma['bg'] = 'bisque'
                        al_turma.geometry('700x450+350+100')
                        a_turmas.destroy()

                        def voltar():
                            al_turma.destroy()
                            jan_principal()

                        titulo(al_turma)
                        a = 'ALTERAR CADASTRO DE TURMAS'
                        tipotitulo(al_turma, a)

                        def informacoes():
                            framei = Frame(al_turma, width=390, height=270, bg='bisque')
                            framei.place(x=280, y=150)

                            lb_ac = Label(al_turma, text='Novo Código:')
                            lb_ac.place(x=300, y=180)

                            lb_ap = Label(al_turma, text='Novo período:')
                            lb_ap.place(x=300, y=250)

                            lb_ad = Label(al_turma, text='Nova Disciplina:')
                            lb_ad.place(x=300, y=320)

                            ent_ac = Entry(al_turma, width=32)
                            ent_ac.place(x=400, y=180)

                            ent_ap = Entry(al_turma, width=32)
                            ent_ap.place(x=400, y=250)

                            ent_ad = Entry(al_turma, width=32)
                            ent_ad.place(x=400, y=320)

                            def AtualizarCodigo():
                                nv_cod = ent_ac.get()

                                def Ok():
                                    erro.destroy()

                                if len(nv_cod) == 0:
                                    erro = Tk()
                                    erro.title('Erro')
                                    erro.geometry('180x150+620+280')

                                    lb = Label(erro, text='Campos vazios. Preencha-os')
                                    lb.place(x=30, y=50)

                                    bt = Button(erro, text='OK', command=Ok)
                                    bt.place(x=75, y=85)
                                else:
                                    c = conn.cursor()
                                    c.execute("""UPDATE turmas
                                                 SET codigo = '%s' 
                                                 WHERE codigo = '%s'
                                                 """ % (nv_cod, cod))
                                    conn.commit()
                                    ent_ac.delete(0, END)

                            bt_ac = Button(al_turma, width=8,
                                           command=AtualizarCodigo,
                                           text='Atualizar',
                                           activebackground='gray28',
                                           activeforeground='gray99',
                                           bg='gray99', bd=0.5)
                            bt_ac.place(x=600, y=180)

                            def AtualizandoPeriodo():
                                nv_ped = ent_ap.get()

                                def Ok():
                                    erro.destroy()

                                if len(nv_ped) == 0:
                                    erro = Tk()
                                    erro.title('Erro')
                                    erro.geometry('180x150+620+280')

                                    lb = Label(erro, text='Campos vazios. Preencha-os')
                                    lb.place(x=30, y=50)

                                    bt = Button(erro, text='OK', command=Ok)
                                    bt.place(x=75, y=85)
                                else:
                                    c = conn.cursor()
                                    c.execute("""UPDATE turmas
                                                SET periodo = '%s' 
                                                WHERE codigo = '%s' 
                                                """ % (nv_ped, cod))
                                    conn.commit()
                                    ent_ap.delete(0, END)

                            bt_ap = Button(al_turma, width=8,
                                           command=AtualizandoPeriodo,
                                           text='Atualizar',
                                           activebackground='gray28',
                                           activeforeground='gray99',
                                           bg='gray99', bd=0.5)
                            bt_ap.place(x=600, y=250)

                            def AtualizandoDisciplina():
                                nv_d = ent_ad.get()

                                def Ok():
                                    erro.destroy()

                                c = conn.cursor()
                                c.execute('''SELECT * FROM disciplinas 
                                            WHERE codigo = '%s' 
                                            ''' % nv_d)
                                b = c.fetchall()
                                if len(nv_d) == 0 or b == []:
                                    erro = Tk()
                                    erro.title('Erro')
                                    erro.geometry('180x150+620+280')

                                    lb = Label(erro, text='Disciplina não cadastrada')
                                    lb.place(x=30, y=50)

                                    bt = Button(erro, text='OK', command=Ok)
                                    bt.place(x=75, y=85)
                                else:
                                    c = conn.cursor()
                                    c.execute("""UPDATE turmas
                                                SET disciplinas = '%s' 
                                                WHERE codigo = '%s'
                                                """ % (nv_d, cod))
                                    conn.commit()
                                    ent_ad.delete(0, END)

                            bt_ad = Button(al_turma, width=8,
                                           command=AtualizandoDisciplina,
                                           text='Atualizar',
                                           activebackground='gray28',
                                           activeforeground='gray99',
                                           bg='gray99', bd=0.5)
                            bt_ad.place(x=600, y=320)

                        bt_inf = Button(al_turma, width=18,
                                        command=informacoes,
                                        text='Informações Gerais',
                                        activebackground='gray28',
                                        activeforeground='gray99',
                                        bg='gray99', bd=0.5)
                        bt_inf.place(x=100, y=180)

                        def alunost():
                            framea = Frame(al_turma, width=390, height=270, bg='bisque')
                            framea.place(x=280, y=150)

                            lb_cpf = Label(al_turma, text='Cpf do Aluno:')
                            lb_cpf.place(x=280, y=180)

                            ent_cpf = Entry(al_turma, width=32)
                            ent_cpf.place(x=370, y=180)

                            l_cpf = Listbox(al_turma, width=60, height=2)
                            l_cpf.place(x=280, y=208)

                            def aluno_turma():  # alterando informações
                                cpf = ent_cpf.get()

                                def Ok():
                                    erro.destroy()

                                c = conn.cursor()
                                c.execute(
                                    '''SELECT * FROM turmas WHERE codigo = '%s' AND alunos = '%s'  ''' % (cod, cpf))
                                a = c.fetchall()

                                if len(a) == 0 or len(cpf) == 0:
                                    erro = Tk()
                                    erro.title('Erro')
                                    erro.geometry('180x150+620+280')

                                    lb = Label(erro, text='Aluno não encontrado')
                                    lb.place(x=30, y=50)

                                    bt = Button(erro, text='OK', command=Ok)
                                    bt.place(x=75, y=85)

                                else:
                                    l_cpf.insert(0, a)
                                    frameat = Frame(al_turma, width=410, height=140)
                                    frameat.place(x=240, y=274)
                                    frameat['bg'] = 'bisque'

                                    lb_c = Label(al_turma, text='Novo código:')
                                    lb_c.place(x=290, y=290)

                                    ent_c = Entry(al_turma, width=30)
                                    ent_c.place(x=375, y=290)

                                    def TrocaCodigo():
                                        def Ok():
                                            erro.destroy()

                                        nv_cd = ent_c.get()
                                        c = conn.cursor()
                                        c.execute('''SELECT * FROM turmas WHERE codigo = '%s' ''' % nv_cd)
                                        a = c.fetchall()
                                        print(len(a))
                                        print(len(nv_cd))
                                        if len(a) == 0 or len(nv_cd) == 0:
                                            erro = Tk()
                                            erro.title('Erro')
                                            erro.geometry('180x150+620+280')

                                            lb = Label(erro, text='Turma não cadastrada.')
                                            lb.place(x=30, y=50)

                                            bt = Button(erro, text='OK', command=Ok)
                                            bt.place(x=75, y=85)
                                            ent_c.delete(0, END)
                                        else:
                                            c.execute('''SELECT periodo FROM turmas WHERE codigo = '%s' ''' % nv_cd)
                                            a = c.fetchone()
                                            pe = a[0]
                                            c.execute("""UPDATE turmas
                                                        SET codigo = '%s' AND period = '%s'
                                                        WHERE codigo = '%s' AND alunos = '%s'
                                                        """ % (nv_cd, pe, cod, cpf))
                                            conn.commit()
                                            c.execute(
                                                '''SELECT * FROM turmas WHERE codigo '%s' AND alunos = '%s' ''' % (
                                                nv_cd, cpf))
                                            b = c.fetchall()
                                            l_cpf.insert(0, b)
                                            lb = Label(al_turma, text='Alteração da turma do aluno concluída!')
                                            lb.place(x=450, y=450)
                                            ent_c.delete(0, END)

                                    bt_c = Button(al_turma, width=8,
                                                  command=TrocaCodigo,
                                                  text='Atualizar',
                                                  activebackground='gray28',
                                                  activeforeground='gray99',
                                                  bg='gray99', bd=0.5)
                                    bt_c.place(x=580, y=285)

                            bt_alt = Button(al_turma, width=15,
                                            command=aluno_turma,
                                            text='Alterar Informações',
                                            activebackground='gray28',
                                            activeforeground='gray99',
                                            bg='gray99', bd=0.5)
                            bt_alt.place(x=290, y=250)

                            def AdicionarAluno():
                                def Ok():
                                    erro.destroy()

                                cpf = ent_cpf.get()
                                frameat = Frame(al_turma, width=410, height=140)
                                frameat.place(x=248, y=272)
                                frameat['bg'] = 'bisque'
                                c = conn.cursor()
                                c.execute('''SELECT * FROM turmas WHERE codigo = '%s' AND alunos = '%s'
                                    ''' % (cod, cpf))
                                if len(c.fetchall()) != 0 or len(cpf) == 0:
                                    erro = Tk()
                                    erro.title('Erro')
                                    erro.geometry('180x150+620+280')
                                    lb = Label(erro, text='Aluno já cadastrado na turma')
                                    lb.place(x=10, y=50)
                                    bt = Button(erro, text='OK', command=Ok)
                                    bt.place(x=75, y=85)
                                else:
                                    c.execute('''SELECT periodo FROM turmas WHERE codigo = '%s' ''' % cod)
                                    a = c.fetchone()
                                    per = str(a[0])
                                    c.execute('''SELECT disciplinas FROM turmas WHERE codigo = '%s' ''' % cod)
                                    b = c.fetchone()
                                    d = b[0]
                                    prof = '-'
                                    c.execute('''INSERT INTO turmas (codigo,periodo,disciplinas,professores,alunos)
                                                    VALUES ('%s','%s','%s','%s','%s') 
                                                    ''' % (cod, per, d, prof, cpf))
                                    conn.commit()
                                    s = '%s  %s  %s  %s  %s ' % (cod, per, d, prof, cpf)
                                    print(s)
                                    l_cpf.insert(0, s)
                                    ent_cpf.delete(0, END)

                            bt_ad = Button(al_turma, width=15,
                                           command=AdicionarAluno,
                                           text='Adicionar Aluno',
                                           activebackground='gray28',
                                           activeforeground='gray99',
                                           bg='gray99', bd=0.5)
                            bt_ad.place(x=410, y=250)

                            def RemoverAluno():
                                frameat = Frame(al_turma, width=410, height=140)
                                frameat.place(x=248, y=272)
                                frameat['bg'] = 'bisque'
                                cpf = ent_cpf.get()

                                def Ok():
                                    erro.destroy()

                                c = conn.cursor()
                                c.execute('''SELECT * FROM turmas WHERE codigo = '%s' AND alunos = '%s'
                                                                    ''' % (cod, cpf))
                                if len(c.fetchall()) == 0 or len(cpf) == 0:
                                    erro = Tk()
                                    erro.title('Erro')
                                    erro.geometry('180x150+620+280')
                                    lb = Label(erro, text='Aluno não cadastrado na turma')
                                    lb.place(x=10, y=50)
                                    bt = Button(erro, text='OK', command=Ok)
                                    bt.place(x=75, y=85)
                                else:
                                    c.execute('''DELETE FROM turmas WHERE codigo='%s' AND alunos = '%s' 
                                                 ''' % (cod, cpf))
                                    conn.commit()
                                    l_cpf.delete(0, END)
                                    ent_cpf.delete(0, END)

                            bt_ra = Button(al_turma, width=15,
                                           command=RemoverAluno,
                                           text='Remover Aluno',
                                           activebackground='gray28',
                                           activeforeground='gray99',
                                           bg='gray99', bd=0.5)
                            bt_ra.place(x=532, y=250)

                        bt_al = Button(al_turma, width=18,
                                       command=alunost,
                                       text='Alunos da Turma',
                                       activebackground='gray28',
                                       activeforeground='gray99',
                                       bg='gray99', bd=0.5)
                        bt_al.place(x=100, y=230)

                        def professort():
                            framea = Frame(al_turma, width=390, height=270, bg='bisque')
                            framea.place(x=270, y=150)

                            lb_cpf = Label(al_turma, text='Cpf do Professor:')
                            lb_cpf.place(x=280, y=180)

                            ent_cpf = Entry(al_turma, width=32)
                            ent_cpf.place(x=375, y=180)

                            l_cpf = Listbox(al_turma, width=60, height=2)
                            l_cpf.place(x=280, y=208)

                            def prof_turma():
                                cpf = ent_cpf.get()

                                def Ok():
                                    erro.destroy()

                                c = conn.cursor()
                                c.execute('''SELECT * FROM turmas WHERE codigo = '%s' AND professores = '%s'  
                                            ''' % (cod, cpf))
                                a = c.fetchall()
                                if len(a) == 0 or len(cpf) == 0:
                                    erro = Tk()
                                    erro.title('Erro')
                                    erro.geometry('180x150+620+280')

                                    lb = Label(erro, text='Professor não encontrado')
                                    lb.place(x=20, y=50)

                                    bt = Button(erro, text='OK', command=Ok)
                                    bt.place(x=75, y=85)
                                else:
                                    l_cpf.insert(0, a)
                                    frameat = Frame(al_turma, width=410, height=140)
                                    frameat.place(x=250, y=272)
                                    frameat['bg'] = 'bisque'

                                    lb_c = Label(al_turma, text='Novo código:')
                                    lb_c.place(x=290, y=290)

                                    ent_c = Entry(al_turma, width=30)
                                    ent_c.place(x=375, y=290)

                                    def TrocaCodigo():
                                        def Ok():
                                            erro.destroy()

                                        nv_cd = ent_c.get()
                                        c = conn.cursor()
                                        c.execute('''SELECT * FROM turmas WHERE codigo = '%s' ''' % nv_cd)
                                        a = c.fetchall()
                                        if len(a) == 0 or len(nv_cd) == 0:
                                            erro = Tk()
                                            erro.title('Erro')
                                            erro.geometry('180x150+620+280')

                                            lb = Label(erro, text='Turma não cadastrada.')
                                            lb.place(x=30, y=50)

                                            bt = Button(erro, text='OK', command=Ok)
                                            bt.place(x=75, y=85)
                                            ent_c.delete(0, END)
                                        else:
                                            c.execute('''SELECT periodo FROM turmas WHERE codigo = '%s' ''' % nv_cd)
                                            a = c.fetchone()
                                            pe = a[0]
                                            c.execute("""UPDATE turmas
                                                      SET codigo = '%s' AND periodo = '%s'
                                                      WHERE codigo = '%s' AND professores = '%s'
                                                      """ % (nv_cd, pe, cod, cpf))
                                            conn.commit()
                                            c.execute(
                                                '''SELECT * FROM turmas WHERE codigo '%s' AND professores = '%s' 
                                                ''' % (nv_cd, cpf))
                                            b = c.fetchall()
                                            l_cpf.insert(0, b)
                                            lb = Label(al_turma, text='Alteração da turma do aluno concluída!')
                                            lb.place(x=450, y=450)
                                            ent_c.delete(0, END)

                                    bt_c = Button(al_turma, width=8,
                                                  command=TrocaCodigo,
                                                  text='Atualizar',
                                                  activebackground='gray28',
                                                  activeforeground='gray99',
                                                  bg='gray99', bd=0.5)
                                    bt_c.place(x=580, y=285)

                            bt_alt = Button(al_turma, width=15,
                                            command=prof_turma,
                                            text='Alterar Informações',
                                            activebackground='gray28',
                                            activeforeground='gray99',
                                            bg='gray99', bd=0.5)
                            bt_alt.place(x=290, y=250)

                            def AdicionarProfessor():
                                def Ok():
                                    erro.destroy()

                                cpf = ent_cpf.get()
                                frameat = Frame(al_turma, width=410, height=140)
                                frameat.place(x=248, y=272)
                                frameat['bg'] = 'bisque'
                                c = conn.cursor()
                                c.execute('''SELECT * FROM turmas WHERE codigo = '%s' AND professores = '%s'
                                        ''' % (cod, cpf))
                                if len(c.fetchall()) != 0 or len(cpf) == 0:
                                    erro = Tk()
                                    erro.title('Erro')
                                    erro.geometry('180x150+620+280')
                                    lb = Label(erro, text='Professor já cadastrado na turma')
                                    lb.place(x=10, y=50)
                                    bt = Button(erro, text='OK', command=Ok)
                                    bt.place(x=75, y=85)
                                else:
                                    c.execute('''SELECT periodo FROM turmas WHERE codigo = '%s' ''' % cod)
                                    a = c.fetchone()
                                    per = str(a[0])
                                    c.execute('''SELECT disciplinas FROM turmas WHERE codigo = '%s' ''' % cod)
                                    b = c.fetchone()
                                    d = b[0]
                                    alu = '-'
                                    c.execute('''INSERT INTO turmas (codigo,periodo,disciplinas,professores,alunos)
                                                            VALUES ('%s','%s','%s','%s','%s') 
                                                            ''' % (cod, per, d, cpf, alu))
                                    conn.commit()
                                    s = '%s  %s  %s  %s  %s ' % (cod, per, d, cpf, alu)
                                    l_cpf.insert(0, s)
                                    ent_cpf.delete(0, END)

                            bt_ad = Button(al_turma, width=15,
                                           command=AdicionarProfessor,
                                           text='Adicionar Professor',
                                           activebackground='gray28',
                                           activeforeground='gray99',
                                           bg='gray99', bd=0.5)
                            bt_ad.place(x=410, y=250)

                            def RemoverProfessor():
                                frameat = Frame(al_turma, width=410, height=140)
                                frameat.place(x=248, y=272)
                                frameat['bg'] = 'bisque'
                                cpf = ent_cpf.get()

                                def Ok():
                                    erro.destroy()

                                c = conn.cursor()
                                c.execute('''SELECT * FROM turmas WHERE codigo = '%s' AND professores = '%s'
                                                                        ''' % (cod, cpf))
                                if len(c.fetchall()) == 0 or len(cpf) == 0:
                                    erro = Tk()
                                    erro.title('Erro')
                                    erro.geometry('180x150+620+280')
                                    lb = Label(erro, text='Professor não cadastrado na turma')
                                    lb.place(x=10, y=50)
                                    bt = Button(erro, text='OK', command=Ok)
                                    bt.place(x=75, y=85)
                                else:
                                    c.execute('''DELETE FROM turmas WHERE codigo='%s' AND professores = '%s' 
                                                         ''' % (cod, cpf))
                                    conn.commit()
                                    l_cpf.delete(0, END)
                                    ent_cpf.delete(0, END)

                            bt_ra = Button(al_turma, width=15,
                                           command=RemoverProfessor,
                                           text='Remover Professor',
                                           activebackground='gray28',
                                           activeforeground='gray99',
                                           bg='gray99', bd=0.5)
                            bt_ra.place(x=532, y=250)

                        bt_pro = Button(al_turma, width=18,
                                        command=professort,
                                        text='Professores da Turma',
                                        activebackground='gray28',
                                        activeforeground='gray99',
                                        bg='gray99', bd=0.5)
                        bt_pro.place(x=100, y=280)

                        v = Button(al_turma, width=18,
                                   command=voltar,
                                   text='Voltar',
                                   activebackground='gray28',
                                   activeforeground='gray99',
                                   bg='gray99', bd=0.5)
                        v.place(x=100, y=320)

                    but_at = Button(a_turmas, width=15,
                                    command=AlterandoTurma,
                                    text='Alterar Turma',
                                    activebackground='gray28',
                                    activeforeground='gray99',
                                    bg='gray99', bd=0.5)
                    but_at.place(x=420, y=400)

            but_alt = Button(a_turmas, width=15,
                             command=p,
                             text='Pesquisar',
                             activebackground='gray28',
                             activeforeground='gray99',
                             bg='gray99', bd=0.5)
            but_alt.place(x=510, y=152)

            but_v = Button(a_turmas, width=15,
                           command=voltar,
                           text='Voltar',
                           activebackground='gray28',
                           activeforeground='gray99',
                           bg='gray99', bd=0.5)
            but_v.place(x=550, y=400)

        def jan_consultarturma():
            co_turmas = Tk()
            co_turmas.title('CONSULTANDO TURMAS')
            co_turmas['bg'] = 'bisque'
            co_turmas.geometry('700x450+350+100')
            turmas.destroy()

            def voltar():
                co_turmas.destroy()
                jan_principal()

            titulo(co_turmas)
            a = 'CONSULTAR CADASTRO DE TURMAS'
            tipotitulo(co_turmas, a)

            lb_ct = Label(co_turmas, text='Código da turma: ', font='30')
            lb_ct.place(x=100, y=150)
            lb_ct['bg'] = 'bisque'

            ent_ct = Entry(co_turmas, width=40)
            ent_ct.place(x=250, y=152)

            lb = Listbox(co_turmas, width=50, height=8, bg='snow', bd=0.6, relief='raise', font='30')
            lb.place(x=115, y=225)

            lbl = Label(co_turmas, text='ID | CODIGO | PERIODO | DISCIPLINAS | PROFESSORES | ALUNOS ')
            lbl.place(x=115, y=208)

            def p():
                def Ok():
                    erro.destroy()

                cod = ent_ct.get()
                c = conn.cursor()
                c.execute('''SELECT * FROM turmas WHERE codigo = '%s';''' % cod)
                a = c.fetchall()
                if len(ent_ct.get()) == 0 or len(a) == 0:
                    erro = Tk()
                    erro.title('Erro')
                    erro.geometry('180x150+620+280')

                    lb = Label(erro, text='Turma não encontrada.')
                    lb.place(x=30, y=50)

                    bt = Button(erro, text='OK', command=Ok)
                    bt.place(x=75, y=85)
                else:
                    lb = Listbox(co_turmas, width=50, height=8, bg='snow', bd=0.6, relief='raise', font='30')
                    lb.place(x=115, y=225)
                    x = 0
                    for i in a:
                        lb.insert(x + 1, i)

            but_alt = Button(co_turmas, width=15,
                             command=p,
                             text='Pesquisar',
                             activebackground='gray28',
                             activeforeground='gray99',
                             bg='gray99', bd=0.5)
            but_alt.place(x=510, y=152)

            but_v = Button(co_turmas, width=15,
                           command=voltar,
                           text='Voltar',
                           activebackground='gray28',
                           activeforeground='gray99',
                           bg='gray99', bd=0.5)
            but_v.place(x=550, y=400)

        def jan_removerturma():
            r_turmas = Tk()
            r_turmas.title('REMOVENDO TURMAS')
            r_turmas['bg'] = 'bisque'
            r_turmas.geometry('700x450+350+100')
            turmas.destroy()

            def voltar():
                r_turmas.destroy()
                jan_principal()

            titulo(r_turmas)
            a = 'REMOVER CADASTRO DE TURMAS'
            tipotitulo(r_turmas, a)

            lb_ct = Label(r_turmas, text='Código da turma: ', font='30')
            lb_ct.place(x=100, y=150)
            lb_ct['bg'] = 'bisque'

            ent_ct = Entry(r_turmas, width=40)
            ent_ct.place(x=250, y=152)

            lb = Listbox(r_turmas, width=50, height=8, bg='snow', bd=0.6, relief='raise', font='30')
            lb.place(x=115, y=225)
            lbl = Label(r_turmas, text='ID | CODIGO | PERIODO | DISCIPLINAS | PROFESSORES | ALUNOS ')
            lbl.place(x=115, y=208)

            def p():
                def Ok():
                    erro.destroy()

                cod = ent_ct.get()
                c = conn.cursor()
                c.execute('''SELECT * FROM turmas WHERE codigo = '%s';''' % cod)
                a = c.fetchall()
                if len(ent_ct.get()) == 0 or len(a) == 0:
                    erro = Tk()
                    erro.title('Erro')
                    erro.geometry('180x150+620+280')

                    lb = Label(erro, text='Turma não encontrada.')
                    lb.place(x=30, y=50)

                    bt = Button(erro, text='OK', command=Ok)
                    bt.place(x=75, y=85)
                else:
                    lb = Listbox(r_turmas, width=50, height=8, bg='snow', bd=0.6, relief='raise', font='30')
                    lb.place(x=115, y=225)
                    x = 0
                    for i in a:
                        lb.insert(x + 1, i)

                    def DeletarTurma():
                        c = conn.cursor()
                        c.execute('''DELETE FROM turmas WHERE codigo='%s'  
                                    ''' % (cod))
                        conn.commit()
                        lb.delete(0, END)

                    bt_d = Button(r_turmas, width=15,
                                  command=DeletarTurma,
                                  text='Deletar Turma',
                                  activebackground='gray28',
                                  activeforeground='gray99',
                                  bg='gray99', bd=0.5)
                    bt_d.place(x=420, y=400)

            but_alt = Button(r_turmas, width=15,
                             command=p,
                             text='Pesquisar',
                             activebackground='gray28',
                             activeforeground='gray99',
                             bg='gray99', bd=0.5)
            but_alt.place(x=510, y=152)

            but_v = Button(r_turmas, width=15,
                           command=voltar,
                           text='Voltar',
                           activebackground='gray28',
                           activeforeground='gray99',
                           bg='gray99', bd=0.5)
            but_v.place(x=550, y=400)

        def voltar():
            turmas.destroy()
            jan_principal()

        turmas = Tk()
        turmas.title('Turmas')
        turmas['bg'] = 'bisque'
        turmas.geometry('700x450+350+100')
        janela.destroy()

        titulo(turmas)
        a = 'TURMAS'
        tipotitulo(turmas, a)

        bttc = Button(turmas, width=40,
                      command=jan_cadastroturmas,
                      text='Cadastrar Turma',
                      activebackground='gray28',
                      activeforeground='gray99',
                      bg='gray99', bd=0.5)
        bttc.place(x=200, y=150)

        btta = Button(turmas, width=40,
                      command=jan_alterarturma,
                      text='Alterar Turma',
                      activebackground='gray28',
                      activeforeground='gray99',
                      bg='gray99', bd=0.5)
        btta.place(x=200, y=200)

        bttco = Button(turmas, width=40,
                       command=jan_consultarturma,
                       text='Consultar Turma',
                       activebackground='gray28',
                       activeforeground='gray99',
                       bg='gray99', bd=0.5)
        bttco.place(x=200, y=250)

        bttr = Button(turmas, width=40,
                      command=jan_removerturma,
                      text='Remover Turma',
                      activebackground='gray28',
                      activeforeground='gray99',
                      bg='gray99', bd=0.5)
        bttr.place(x=200, y=300)

        v = Button(turmas, width=40,
                   command=voltar,
                   text='Voltar',
                   activebackground='gray28',
                   activeforeground='gray99',
                   bg='gray99', bd=0.5)
        v.place(x=200, y=350)

    def jan_relatorios():
        def voltar():
            relatorio.destroy()
            jan_principal()
        relatorio = Tk()
        relatorio.title('Relatórios e Atas')
        relatorio['bg'] = 'bisque'
        relatorio.geometry('700x450+350+100')
        janela.destroy()
        titulo(relatorio)
        a = 'RELATÓRIOS/ATAS'
        tipotitulo(relatorio, a)
        def relatorios():
            frame= Frame(relatorio,width=450,height=250)
            frame.place(x=220,y=150)
            frame['bg']='bisque'
            def prof():
                framep= Frame(relatorio,width=400,height=230)
                framep.place(x=258 , y=200)
                framep['bg']='bisque'

                lb=Label(relatorio,text='CPF do Professor:')
                lb.place(x=290,y=200)

                ent_pr= Entry(relatorio,width=30)
                ent_pr.place(x=390,y=200)

                def pesquisar():
                    def Ok():
                        erro.destroy()
                    cpf=ent_pr.get()
                    c=conn.cursor()
                    c.execute('''SELECT * FROM turmas WHERE professores = '%s' 
                                ''' %cpf)
                    a=c.fetchall()
                    if len(a)==0 or len(cpf)==0:
                        erro = Tk()
                        erro.title('Erro')
                        erro.geometry('180x150+620+280')

                        lb = Label(erro, text='Nenhum registro encontrado.')
                        lb.place(x=5, y=50)

                        bt = Button(erro, text='OK', command=Ok)
                        bt.place(x=75, y=85)
                        ent_pr.delete(0,END)
                    else:
                        lbox= Listbox(relatorio,width=40,height=10,font=30)
                        lbox.place(x=290,y=230)
                        for i in a :
                            print(i)
                            lbox.insert(END, f"{i[0]}  |  {i[1]}  |  {i[2]}")

                bt_pe= Button(relatorio,width=7,
                              command=pesquisar,
                              text='Pesquisar',
                            activebackground='gray28',
                            activeforeground='gray99',
                            bg='gray99', bd=0.5)
                bt_pe.place(x=580,y=197)

            por_prof=Button(relatorio,width=15,height=1,
                            command=prof,
                            text='Por Professor',
                            activebackground='gray28',
                            activeforeground='gray99',
                            bg='gray99', bd=0.5)
            por_prof.place(x=325,y=150)

            def aluno():
                framep = Frame(relatorio, width=400, height=230)
                framep.place(x=258, y=195)
                framep['bg'] = 'bisque'

                lb = Label(relatorio, text='CPF do Aluno:')
                lb.place(x=290, y=200)

                ent_pr = Entry(relatorio, width=30)
                ent_pr.place(x=390, y=200)

                def pesquisar():
                    def Ok():
                        erro.destroy()
                    cpf=ent_pr.get()
                    c=conn.cursor()
                    c.execute('''SELECT * FROM turmas WHERE alunos = '%s' 
                                ''' %cpf)
                    a=c.fetchall()
                    if len(a)==0 or len(cpf)==0:
                        erro = Tk()
                        erro.title('Erro')
                        erro.geometry('180x150+620+280')

                        lb = Label(erro, text='Nenhum registro encontrado.')
                        lb.place(x=5, y=50)

                        bt = Button(erro, text='OK', command=Ok)
                        bt.place(x=75, y=85)
                        ent_pr.delete(0,END)
                    else:
                        lbox= Listbox(relatorio,width=50,height=10)
                        lbox.place(x=290,y=230)
                        for i in a :
                            print(i)
                            lbox.insert(END,i)

                bt_pe = Button(relatorio, width=7,
                           command=pesquisar,
                           text='Pesquisar',
                           activebackground='gray28',
                           activeforeground='gray99',
                           bg='gray99', bd=0.5)
                bt_pe.place(x=580, y=197)
            por_aluno= Button(relatorio,width=15,height=1,
                              command=aluno,
                            text='Por Aluno',
                            activebackground='gray28',
                            activeforeground='gray99',
                            bg='gray99', bd=0.5)
            por_aluno.place(x=450,y=150)

        voltar= Button(relatorio,width=15,height=2,
                       command=voltar,
                            text='Voltar',
                            activebackground='gray28',
                            activeforeground='gray99',
                            bg='gray99', bd=0.5)
        voltar.place(x=100,y=350)

        rela= Button(relatorio,
                     width=15,height=2,
                     command=relatorios,
                     text='Relatorios',
                    activebackground='gray28',
                    activeforeground='gray99',
                     bg='gray99', bd=0.5)
        rela.place(x=100, y=150)
        def ata():
            frame = Frame(relatorio, width=450, height=250)
            frame.place(x=220, y=150)
            frame['bg'] = 'bisque'

            lb_cod= Label(relatorio,text='Código da Turma:')
            lb_cod.place(x=250,y=150)

            ent_cod= Entry(relatorio,width=28)
            ent_cod.place(x=380,y=150)

            box = Listbox(relatorio, width=60, height=10)
            box.place(x=280, y=260)
            def pesquisa():
                codigo=ent_cod.get()

                def Ok():
                    erro.destroy()

                c = conn.cursor()
                c.execute('''SELECT * FROM turmas WHERE codigo = '%s' 
                            ''' % codigo)
                a = c.fetchall()
                if len(a) == 0 or len(codigo) == 0:
                    erro = Tk()
                    erro.title('Erro')
                    erro.geometry('180x150+620+280')

                    lb = Label(erro, text='Nenhum registro encontrado.')
                    lb.place(x=5, y=50)

                    bt = Button(erro, text='OK', command=Ok)
                    bt.place(x=75, y=85)
                    ent_cod.delete(0, END)
                else:
                    for i in a:
                        print(i)
                        box.insert(END, i)
            but_pes= Button(relatorio,width=7,
                            command=pesquisa,
                            text='Pesquisar',
                            activebackground='gray28',
                            activeforeground='gray99',
                            bg='gray99', bd=0.5)
            but_pes.place(x=560,y=148)

            lb_ata= Label(relatorio,text='ATA DE EXERCÍCIO')
            lb_ata.place(x=350,y=190)

            nomes= Label(relatorio,text='ID | CODIGO | PERIODO | DISCIPLINAS | PROFESSORES | ALUNOS ')
            nomes.place(x=280,y=220)

        ata=Button(relatorio,
                     width=15,height=2,
                   command= ata,
                     text='Atas',
                    activebackground='gray28',
                    activeforeground='gray99',
                     bg='gray99', bd=0.5)
        ata.place(x=100,y=250)

    janela = Tk()
    janela.title('Sistema de Controle Acadêmico')
    janela['bg'] = 'bisque'
    janela.geometry('700x450+350+100')

    titulo(janela)

    bta = Button(janela, width=30, text='Alunos',
                 command=jan_alunos,
                 activebackground='gray28',
                 activeforeground='gray99',
                 bg='gray99', bd=0.5)
    bta.place(x=100, y=150)

    btp = Button(janela, width=30,
                 command=jan_professores,
                 text='Professores',
                 activebackground='gray28',
                 activeforeground='gray99',
                 bg='gray99', bd=0.5)
    btp.place(x=100, y=250)

    btd = Button(janela, width=30,
                 command=jan_disciplinas,
                 text='Disciplinas',
                 activebackground='gray28',
                 activeforeground='gray99',
                 bg='gray99',
                 bd=0.5)
    btd.place(x=400, y=150)

    btt = Button(janela, width=30,
                 command=jan_turmas,
                 text='Turmas',
                 activebackground='gray28',
                 activeforeground='gray99',
                 bg='gray99',
                 bd=0.5)
    btt.place(x=400, y=250)

    bra = Button(janela, width=30,
                 command=jan_relatorios,
                 text='Relatórios/Atas',
                 activebackground='gray28',
                 activeforeground='gray99',
                 bg='gray99',
                 bd=0.5)
    bra.place(x=240, y=320)
    janela.mainloop()


jan_principal()

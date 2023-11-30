import tkinter
from tkinter import *
import customtkinter
from PIL import ImageTk,Image
from datetime import datetime
import pandas as pd
import os


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

lista_admins=[]
class Admin:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha
        lista_admins.append(self)


class JanelaInicial:
    def __init__(self, telainicio):
        self.telainicio=telainicio
        telainicio.geometry("640x480")
        telainicio.title("NEXLINK TECHNOLOGIES")
        telainicio.resizable(False, False)
        telainicio.iconbitmap("./IMAGENS-ICONES/mini-icon.ico")

        #PATTERN FUNDO
        self.fundo = ImageTk.PhotoImage(Image.open("./IMAGENS-ICONES/pattern_fundo.png"))
        self.pattern_fundo= customtkinter.CTkLabel(master=telainicio, image=self.fundo)
        self.pattern_fundo.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        #frame cinza
        self.frame=customtkinter.CTkFrame(master=telainicio, width=320, height=360, corner_radius=15)
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        #HORARIO
        self.rotulo_horario = customtkinter.CTkLabel(telainicio, text="", font=("Helvetica", 12))
        self.rotulo_horario.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
        self.atualizar_horario()

        #IMAGEM LOGOTIPO NEXLINK NA TELA DE LOGIN
        self.formatar_imagem_logo = ImageTk.PhotoImage(Image.open("./IMAGENS-ICONES/NexLink_LOGO_Addapt.png").resize((288, 162), 3))
        self.imagem_logo = customtkinter.CTkLabel(master=telainicio,image=self.formatar_imagem_logo, text=" ", bg_color="#2b2b2b")
        self.imagem_logo.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        #CAIXA DE ENTRADA (LOGIN)
        self.caixa_login = customtkinter.CTkEntry(telainicio, placeholder_text="Login")
        self.caixa_login.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        #CAIXA DE ENTRADA (SENHA)
        self.caixa_senha = customtkinter.CTkEntry(telainicio, placeholder_text="Senha", show="*")
        self.caixa_senha.place(relx=0.5, rely=0.58, anchor=tkinter.CENTER)

        # CAIXA DE BOTÃO (ENTRAR)
        self.botao_login = customtkinter.CTkButton(telainicio, text="Entrar", fg_color="green", command=self.clique_entrar)
        self.botao_login.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

        #TEXTO INFERIOR CADASTRO
        self.texto=customtkinter.CTkLabel(telainicio, text="Programa de cadastramento de clientes - NEXLINK TECHNOLOGIES")
        self.texto.place(relx=0.5, rely=0.95, anchor=tkinter.CENTER)
        

    def atualizar_horario(self):
        
        horario_atual = datetime.now().strftime("%H:%M:%S")
        self.rotulo_horario.configure(text=f"Horário atual: {horario_atual}")
        self.telainicio.after(1000, self.atualizar_horario)

    def clique_entrar(self):
        for login_admin in lista_admins:
            if (
                self.caixa_login.get() == login_admin.login
                and self.caixa_senha.get() == login_admin.senha
            ):
                print(f"Login realizado com sucesso em {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                self.usuario_atual=login_admin
                self.telainicio.destroy()
                self.abrir_janela_de_registros()

    def abrir_janela_de_registros(self):
        janela_registros = JanelaRegistros(self.usuario_atual)
        janela_registros.iniciar()


class JanelaRegistros:
    def __init__(self, usuario_atual):
        self.usuario_atual=usuario_atual
        self.janela_registros = customtkinter.CTk()
        self.janela_registros.geometry("1280x720")
        self.janela_registros.title("Registro de clientes - NEXLINK TECHNOLOGIES")
        self.janela_registros.resizable(False, False)
        self.janela_registros.iconbitmap("./IMAGENS-ICONES/mini-icon.ico")

        #TENTAR FAZER FUNCIONAR ESTE BOTAO ABAIXO (OK)
        #WIDGET ABRIR PLANILHA 
        self.botao_login = customtkinter.CTkButton(self.janela_registros, text="Acessar planilha", fg_color="gray", command=self.executar_planilha)
        self.botao_login.place(relx=0.355, rely=0.1, anchor=tkinter.CENTER)
    
        # WIDGET E-MAIL
        self.rotulo_email = customtkinter.CTkLabel(self.janela_registros, text="E-mail:")
        self.rotulo_email.place(relx=0.1, rely=0.2)
        self.caixa_email = customtkinter.CTkEntry(self.janela_registros, placeholder_text="Digite o e-mail")
        self.caixa_email.place(relx=0.5, rely=0.2)

        # WIDGET TELEFONE
        self.rotulo_telefone = customtkinter.CTkLabel(self.janela_registros, text="Telefone:")
        self.rotulo_telefone.place(relx=0.1, rely=0.3)
        self.caixa_telefone = customtkinter.CTkEntry(self.janela_registros, placeholder_text="Digite o telefone")
        self.caixa_telefone.place(relx=0.5, rely=0.3)

        # WIDGET ENDEREÇO
        self.rotulo_endereco = customtkinter.CTkLabel(self.janela_registros, text="Endereço:")
        self.rotulo_endereco.place(relx=0.1, rely=0.4)
        self.caixa_endereco = customtkinter.CTkEntry(self.janela_registros, placeholder_text="Digite o endereço")
        self.caixa_endereco.place(relx=0.5, rely=0.4)

        # WIDGET CEP
        self.rotulo_cep = customtkinter.CTkLabel(self.janela_registros, text="CEP:")
        self.rotulo_cep.place(relx=0.1, rely=0.5)  
        self.caixa_cep = customtkinter.CTkEntry(self.janela_registros, placeholder_text="Digite o CEP")
        self.caixa_cep.place(relx=0.5, rely=0.5)  

        # WIDGET IP
        opcoes_ip = ["192.0.0.1", "192.168.0.1", "192.1.1.0", "1.0.0.1"]
        self.rotulo_ip = customtkinter.CTkLabel(self.janela_registros, text="Selecione um Endereço de IP:")
        self.rotulo_ip.place(relx=0.1, rely=0.6)
        self.caixa_ip = customtkinter.CTkComboBox(self.janela_registros, values=opcoes_ip)
        self.caixa_ip.set(opcoes_ip[0])  # OPÇÃO PADRÃO
        self.caixa_ip.place(relx=0.5, rely=0.6)
        
        # WIDGET PACOTE MEGABYTES
        pacotes_velocidade = ["25MB/s - R$35,00", "50MB/s - R$60,00", "100MB/s - R$80,00", "200MB/s - R$130,00"]
        self.rotulo_pacotes = customtkinter.CTkLabel(self.janela_registros, text="Selecione o pacote do cliente:")
        self.rotulo_pacotes.place(relx=0.1, rely=0.7)
        self.caixa_pacotes = customtkinter.CTkComboBox(self.janela_registros, values=pacotes_velocidade)
        self.caixa_pacotes.set(pacotes_velocidade[0])  # OPÇÃO PADRÃO
        self.caixa_pacotes.place(relx=0.5, rely=0.7)

        # BOTÃO SALVAR
        self.botao_salvar = customtkinter.CTkButton(self.janela_registros, text="Salvar", fg_color="green", command=self.salvar_dados)
        self.botao_salvar.place(relx=0.3, rely=0.8)

        #FRAME À DIREITA
        self.frame_direita = customtkinter.CTkFrame(self.janela_registros, width=400, height=720)
        self.frame_direita.place(relx=1, rely=0, anchor="ne")

        #USER IMAGEM PADRAO
        self.formatar_imagemuser = ImageTk.PhotoImage(Image.open("./IMAGENS-ICONES/user_photo.png").resize((100, 130), 3))
        self.imagemuser = customtkinter.CTkLabel(master=self.janela_registros, image=self.formatar_imagemuser, text=" ", bg_color="#2b2b2b") 
        self.imagemuser.place(relx= 0.81, rely=0.2)

        #INFORMAÇÕES DE QUEM ENTROU (LOGIN)
        self.rotulo_login = customtkinter.CTkLabel(self.janela_registros, text=
                                                   "------------"
                                                   "\n"
                                                   f"Usuário logado: {self.usuario_atual.login}"
                                                   "\n------------"
                                                   "\n"
                                                   "\n •⚙️Manutenção"
                                                   "\n"
                                                   "\n •📞 Suporte"
                                                   "\n"
                                                   "\n •💻 Cadastro de clientes", bg_color="#2b2b2b")
        self.rotulo_login.place(relx=0.80, rely=0.45)

        #TEXTO INFERIOR
        self.infos_admin=customtkinter.CTkLabel(master=self.janela_registros, text="Programa de cadastramento de clientes - NEXLINK TECHNOLOGIES")
        self.infos_admin.place(relx=0.35, rely=0.95, anchor=tkinter.CENTER)


        #LOGO NEXLINK
        self.formatar_logo_pag2 = ImageTk.PhotoImage(Image.open("./IMAGENS-ICONES/NexLink_LOGO_Addapt.png").resize((288, 162), 3))
        self.logo_pag2 = customtkinter.CTkLabel(master=self.janela_registros, image=self.formatar_logo_pag2, text=" ", bg_color="#2b2b2b") 
        self.logo_pag2.place(relx= 0.74, rely=0.7)



    def executar_planilha(self):
        caminho_arquivo_planilha = "D:/Users/LAZARO-PC/Desktop/Pastas/IFRN/IF - PEOO 2023/PROJETO_4B_2023./dados_clientes.xlsx"

        if os.path.exists(caminho_arquivo_planilha):
            os.startfile(caminho_arquivo_planilha)
        else:
            print(f"O arquivo {caminho_arquivo_planilha} não foi encontrado.")


    def salvar_dados(self):
        nome_arquivo = 'dados_clientes.xlsx'

        try:
            #CRIAR UM DICIONARIO COM OS DADOS
            dados = {
                'E-mail': [self.caixa_email.get()],
                'Telefone': [self.caixa_telefone.get()],
                'Endereço': [self.caixa_endereco.get()],
                'CEP': [self.caixa_cep.get()],
                'Endereço de IP': [self.caixa_ip.get()],
                'Pacotes de velocidade':[self.caixa_pacotes.get()],
            }

            if os.path.exists(nome_arquivo): #VER SER A PLANILHA EXISTE
                df_existente = pd.read_excel(nome_arquivo)
                df_novos = pd.DataFrame(dados)
                df_atualizado = pd.concat([df_existente, df_novos], ignore_index=True) #UNE OS DATAFRAMES
            
            else:
                
                df_atualizado = pd.DataFrame(dados)

            #SALVAR DATAFRAME ATUALIZADO NA NOVA PLANILHA
            df_atualizado.to_excel(nome_arquivo, index=False)
            print(f'Dados salvos em {nome_arquivo}')

            #LIMPAR(PERMITIR NOVOS CADASTROS)
            self.limpar_campos()

        except Exception as erro:
            print(f"Erro ao salvar dados: {erro}")

    def limpar_campos(self):
        self.caixa_email.delete(0, tkinter.END)
        self.caixa_telefone.delete(0, tkinter.END)
        self.caixa_endereco.delete(0, tkinter.END)
        self.caixa_cep.delete(0, tkinter.END)
        self.caixa_ip.set('')


    
    
    def iniciar(self):
        self.janela_registros.mainloop()


console = Admin("admin", "admin")
administrador= Admin("Lázaro", "123ok")
funcionario_2023=Admin("testing", "test")

root = customtkinter.CTk()
inicio = JanelaInicial(root) #RODAR A JANELA DE LOGIN
root.mainloop()

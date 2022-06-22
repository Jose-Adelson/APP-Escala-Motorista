from kivy.app import App
from kivy.lang import Builder
from telas import *
from botoes import *
import requests
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivymd.app import MDApp
from myfirebase import Myfirebase


Window.size = (300, 590)



GUI = Builder.load_file("main.kv")
class MainApp(App):



    def build(self):
        self.firebase= Myfirebase()
        return GUI

    def on_start(self):
        self.carregar_info_usuario()


    def carregar_info_usuario(self):
        try:
            requisicao = requests.get(f"https://aplicativodeescalaadels-default-rtdb.firebaseio.com/{self.local_id}.json")
            requisicao_dic = requisicao.json()
            print(requisicao.json())

            # CARREGAR INFORMAÇÕES DO BANCO DE DADOS

            # CIF
            cif_operador = requisicao_dic["cif"]
            cif_usuario = self.root.ids.telaprincipalpage.ids["cif_usuario"]
            cif_usuario.text = cif_operador

            # FOTO
            foto_operador = requisicao_dic["fotoperfil"]
            foto_perfil = self.root.ids.telaprincipalpage.ids["foto_perfil"]
            foto_perfil.source = f"foto perfil/{foto_operador}"

            # NOME
            nome_operador = requisicao_dic["nome"]
            nomecompleto = self.root.ids.telaprincipalpage.ids["nomecompleto"]
            nomecompleto.text = nome_operador

            #TABELA
            tabela_operador = requisicao_dic["tabela"]
            tabela = self.root.ids.telaprincipalpage.ids["tabela"]
            tabela.text = tabela_operador

            #LINHA
            linha_operador = requisicao_dic["linha"]
            linha = self.root.ids.telaprincipalpage.ids["linha"]
            linha.text = linha_operador

            #LOCAL
            local_operador = requisicao_dic["local"]
            local = self.root.ids.telaprincipalpage.ids["local"]
            local.text = local_operador

            #INICIO
            inicio_operador = requisicao_dic["inicio"]
            inicio = self.root.ids.telaprincipalpage.ids["inicio"]
            inicio.text = inicio_operador

            #TERMINO
            termino_operador = requisicao_dic["termino"]
            termino = self.root.ids.telaprincipalpage.ids["termino"]
            termino.text = termino_operador


        except:
            pass

    def mudar_tela(self, id_tela):
        gerenciador_telas=self.root.ids["screen_manager"]
        gerenciador_telas.current = id_tela



MainApp().run()
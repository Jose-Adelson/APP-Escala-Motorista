import requests
from kivy.app import App
from telas import *

class Myfirebase():
    API_KEY = 'AIzaSyBi1dMr1HxzWfXdzPb2PdWueNxfl8SNoJ4'

    def criar_conta(self, email, senha):
        pass
        link = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={self.API_KEY}"

        info = {"email": email,
                "password": senha,
                "returnSecureToken": True}
        requisicao = requests.post(link, data=info)
        requisicao_dic = requisicao.json()

        if requisicao.ok:
            print("Usuário criado com sucesso!")
            refresh_token = requisicao_dic["refreshToken"]
            local_id = requisicao_dic["localId"]
            id_token = requisicao_dic["idToken"]

            meu_aplicativo = App.get_running_app()
            meu_aplicativo.local_id = local_id
            meu_aplicativo.id_token = id_token

            with open("refresh_token.txt", "w") as arquivo:
                arquivo.write(refresh_token)

            #REQ CIF
            requi_usu = requests.get(f"https://aplicativodeescalaadels-default-rtdb.firebaseio.com/salvarcif.json")
            scif = requi_usu.json()

            meu_aplicativo = App.get_running_app()
            criarconta_page = meu_aplicativo.root.ids["criarcontapage"]
            scif = criarconta_page.ids["cif"].text

            #REQ NOME
            requi_nome = requests.get(f"https://aplicativodeescalaadels-default-rtdb.firebaseio.com/salvarnome.json")
            nome = requi_nome.json()
            nome = criarconta_page.ids["nomecompleto"].text

            link = f"https://aplicativodeescalaadels-default-rtdb.firebaseio.com/{local_id}.json"
            info_usuario = f'{{"fotoperfil": "icon_motorista.png", "cif": "{scif}", "inicio": " " , "linha": " " , "local": " ", "nome": "{nome}", "tabela": " ", "termino": " "}}'
            requisicao_usuario = requests.patch(link, data=info_usuario)

            meu_aplicativo.carregar_info_usuario()
            meu_aplicativo.mudar_tela("telaprincipalpage")

        else:
            mensagem_erro = requisicao_dic['error']['message']
            meu_aplicativo = App.get_running_app()
            pagina_login = meu_aplicativo.root.ids["homepage"]
            pagina_login.ids["mensagem_login"].text = mensagem_erro
            pagina_login.ids["mensagem_login"].color = (1, 0, 0, 1)


    def fazer_login(self, email, senha):
        link = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={self.API_KEY}"
        info = {"email": email,
                "password": senha,
                "returnSecureToken": True}
        requisicao = requests.post(link, data=info)
        requisicao_dic = requisicao.json()

        if requisicao.ok:

            refresh_token = requisicao_dic["refreshToken"]
            local_id = requisicao_dic["localId"]
            id_token = requisicao_dic["idToken"]
            print(local_id)


            meu_aplicativo = App.get_running_app()
            meu_aplicativo.local_id = local_id
            meu_aplicativo.id_token = id_token

            with open("refresh_token.txt", "w") as arquivo:
                arquivo.write(refresh_token)


            meu_aplicativo.carregar_info_usuario()
            meu_aplicativo.mudar_tela("telaprincipalpage")


        else:
            mensagem_erro = requisicao_dic['error']['message']
            meu_aplicativo = App.get_running_app()
            pagina_login= meu_aplicativo.root.ids["homepage"]
            pagina_login.ids["mensagem_login"].text = mensagem_erro
            pagina_login.ids["mensagem_login"].color = (1, 0, 0, 1)


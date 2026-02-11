import flet as ft

def main(page: ft.Page):
    page.title = 'Meu app'
    page.add(
        ft.Text('Mucho biem vindo muchacho', size = 24,
        weight=ft.FontWeight.W_600,
        color=ft.Colors.BLUE_100,
        italic=True
        ),
        ft.Text('Eu me chamo insira seu nome...'),
        ft.Button(
            content='Botão Ativado'
        ),
        ft.Button(
            content='Botão Desativado',
            disabled=True
        ),
        ft.Button(
            content='Botão Colorido',
            color='white',
            bgcolor='blue'
        ),
        ft.Image(
            src='https://www.sp.senai.br/images/senai.svg',
            width=150,
            height=150
        )
    )

ft.app(main)
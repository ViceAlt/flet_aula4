import flet as ft

def main(page: ft.Page):
    def mostrar_mensagem(e):
        page.add(ft.Text("Ai.",
        color=ft.Colors.RED,
        italic=True))
    def mostrar_mensagem(e):
        page.add(ft.Text("Ai.",
        color=ft.Colors.RED,
        italic=True))
        
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(
        ft.Text(
            "*Barulho de Coelho*",
            weight=ft.FontWeight.W_600,
            ),
        ft.Image(
            src="images/link.png",
            height=350,
            visible=True
        ),
        ft.Button(
            content="Bater no coelho",
            on_click=mostrar_mensagem,
            bgcolor="#1c0138"
        )
    )
ft.app(main)
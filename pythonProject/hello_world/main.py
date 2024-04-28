import flet as ft


def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Text("Hello World, This is my first Flet App!")))
    page.update()


ft.app(main)

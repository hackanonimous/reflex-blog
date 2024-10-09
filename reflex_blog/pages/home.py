import reflex as rx
from ..components.navbar import navbar
def home()->rx.Component:
  return rx.box(
    navbar(),
    rx.text("hola",type="h1"),
    class_name="page"
  )
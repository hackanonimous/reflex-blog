import reflex as rx

def navbar()->rx.Component:
  return rx.box(
    rx.box(
      rx.text("Mi Blog"),
      class_name="nav-left"
    ),
    rx.box(
      rx.link(
        "Inicio",
        href="/"
      ),
      rx.link(
        "Acerca de",
        href="/acerca-de"
      ),
      class_name="nav-right"
    ),

    class_name="nav"
  )
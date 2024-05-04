from rxconfig import config

# first install requests by 'pip install requests'
import requests
# we give reflex an alias of rx
import reflex as rx
# in order to get some random quotes
import random

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"



class QuoteState(rx.State):
    """The app state."""
    
    quote :str = "" 
    author :str  = ""
    
    def get_quote(self):
        """Get a random quote."""
        response = requests.get("https://type.fit/api/quotes")
        data = response.json()
        random_number :int = random.randint(0, 10)
        self.quote = data[random_number]['text']
        self.author = data[random_number]['author'].replace("type.fit","")




class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Random Quote Generator", size="9"),
            
            rx.button(
                "Get Quote",
                on_click=lambda: QuoteState.get_quote,
                size="4",
            ),
            rx.box(
                rx.text(QuoteState.quote, margin_top="0.5em"),
                rx.text(QuoteState.author, margin_top="0.5em"),
                border_width="1px",
                padding="1em",
        

            ),
    
            align="center",
            spacing="7",
            font_size="1.5em",
            shadow="lg",
        ),
        height="100vh",
    )
    

app = rx.App()
app.add_page(index)

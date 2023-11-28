import solara
from pathlib import Path
import json

# Declare reactive variables at the top level. Components using these variables
# will be re-executed when their values change.
sentence = solara.reactive("Solara makes our team more productive.")
word_limit = solara.reactive(10)


# in case you want to override the default order of the tabs
route_order = ["/", "settings", "chat", "clickbutton"]

import os
openaikey = solara.reactive("")
openaikey = os.getenv("OPENAI_API_KEY")
DISCORD_SERVER_ID = solara.reactive("")
DISCORD_SERVER_ID = os.getenv("DISCORD_SERVER_ID")

@solara.component
def Page():
    with solara.Column(style={"padding-top": "30px"}):
        solara.Title("Solarathon example project")
        # Calculate word_count within the component to ensure re-execution when reactive variables change.
        word_count = len(sentence.value.split())

        solara.SliderInt("Word limit", value=word_limit, min=2, max=20)
        solara.InputText(label="Your sentence", value=sentence, continuous_update=True)

        # Display messages based on the current word count and word limit.
        if word_count >= int(word_limit.value):
            solara.Error(f"With {word_count} words, you passed the word limit of {word_limit.value}.")
        elif word_count >= int(0.8 * word_limit.value):
            solara.Warning(f"With {word_count} words, you are close to the word limit of {word_limit.value}.")
        else:
            solara.Success("Great short writing!")
        
        solara.Markdown(f"openai key {openaikey}")
        solara.Markdown(f"discord server id {DISCORD_SERVER_ID}")
        solara.Markdown("*First exercise*: remove this text and write your own sentence.")
        solara.Markdown(f"""`Food`       
        [Biriyani](https://en.wikipedia.org/wiki/Biryani)""")

        raw_data = Path(__file__).parent.parent
        with open(raw_data / 'assets' / 'data' / 'haystack.json' , 'r' ) as f:
            raw = json.loads(f.read())
        solara.Markdown(f'{raw}')

@solara.component
def Layout(children):
    # this is the default layout, but you can override it here, for instance some extra padding
    return solara.AppLayout(children=children, style={"padding": "20px"})

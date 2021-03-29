import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash 
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# Import data 
df = pd.read_csv("top.csv")

# print(df[:5])

# App layout

app.layout = html.Div([
  
  html.H1("FIFA Ballon D'Or 2020", style = {'text-align': 'center'}),

  dcc.Dropdown (id = 'player_selection',
              options = [
                {'label': 'Robert Lewandowski', 'value': 'R. Lewandowski'},
                {'label': 'Lionel Messi', 'value': 'L. Messi'}],
                
                multi = False,
                value = 'R. Lewandowski',
                style={'width': "40%"}
                ),

  dcc.Graph(id = 'my_bee_map', figure = {})
])

# display web

if __name__ == '__main__':
  app.run_server(debug=True)
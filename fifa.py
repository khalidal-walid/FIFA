import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import dash 
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Initialise the app
app = dash.Dash(__name__)

# Import data 
df = pd.read_csv("top.csv")
# df = df.groupby(['Year', 'Name'])[['Overall']].mean()
# df.reset_index(inplace=True)
# print(df[:5])

# App layout
app.layout = html.Div([
  
  html.H1("FIFA Ballon D'Or 2020", style = {'text-align': 'center'}),

  dcc.Dropdown (id = 'player_selection',
              options = [
                {'label': 'R. Lewandowski', 'value': 'R. Lewandowski'},
                {'label': 'L. Messi', 'value': 'L. Messi'},
                {'label': 'Cristiano Ronaldo', 'value': 'Cristiano Ronaldo'},
                {'label': 'Sergio Ramos', 'value': 'Sergio Ramos'},
                {'label': 'Neymar', 'value': 'Neymar'},
                {'label': 'Thiago', 'value': 'Thiago'},
                {'label': 'K. De Bruyne', 'value': 'K. De Bruyne'},
                {'label': 'M. Salah', 'value': 'M. Salah'},
                {'label': 'V. van Dijk', 'value': 'V. van Dijk'},
                {'label': 'S. Mané', 'value': 'S. Mané'},
                {'label': 'K. Mbappé', 'value': 'K. Mbappé'}],
                
                multi = False,
                # style = {"width": "40%", "margin-left": "2rem"},
                style=dict(
                    width='40%',
                ),
                value = 'R. Lewandowski',
                clearable=False
                ),

  dcc.Graph(id = 'line-chart', figure = {})
])

# callback
@app.callback(
  Output(component_id='line-chart', component_property='figure'),
  [Input(component_id = 'player_selection', component_property='value')]
)

# plotly express
def update_line_chart(player_selection):
  # print(player_selection)

  dff = df.copy()
  dff = dff[dff["Name"] == player_selection]

  figure = px.line(
    data_frame = dff,
    x='Year',
    y='Overall',
    color='Name'
  )

  figure.add_trace (
    go.Scatter(
      x=dff['Year'],
      y=dff['Overall'],
      text=dff['Overall'],
      mode='markers+text',
      marker=dict(color='black', size=5),
      textfont=dict(color='black', size=13),
      textposition='top left',
    )
  )

  figure.update_layout(
    plot_bgcolor='white',
    showlegend=False,
    # xaxis=dict(linecolor='gray'),
    yaxis=dict(linecolor='gray')
  )

  return figure

# Run the app
if __name__ == '__main__':
  app.run_server(debug=True)
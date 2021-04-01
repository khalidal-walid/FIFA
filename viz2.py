import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

from dash.dependencies import Input, Output

# Initialise the app
app = dash.Dash(__name__)

# Import data 
df = pd.read_csv("top.csv")

# Creates a list of dictionaries
def get_options(list_player):
    player_list = []
    for i in list_player:
        player_list.append({'label': i, 'value': i})

    return player_list

# App layout
app.layout = html.Div(
  children=[
    html.Div(className='row',
      children=[
        # Define left element
        html.Div(className='four columns div-user-controls',
                children = [
                  html.H1('Fifa'),
                  # html.P('try and testing'),

                   html.Div(
                     className='div-for-dropdown',
                      children=[
                         dcc.Dropdown(id='player_selection', options=get_options(df['Name'].unique()),
                                      multi=False, value=[df['Name'].sort_values()[0]],
                                      style={'backgroundColor': '#1E1E1E'},
                                      className='player_selection'
                                      ),
                                ],
                                     style={'color': '#1E1E1E'})
                ]
        ),

        # Define right element
        html.Div(className='eight columns div-for-charts bg-grey',
                  children=[
                    dcc.Graph(id='line-chart',
                              config={'displayModeBar': False},
                              animate=True,
                              figure=px.line(df,
                                            x='Year',
                                            y='Overall',
                                            color='Name',
                                            template='plotly_dark').update_layout(
                                                      {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                                                        'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
                              )
                            ])
      ])
  ]
)

# app callback
@app.callback(
  Output('line-chart', 'figure'),
  [Input('player_selection', 'value')]
)

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

  return figure


# Run the App
if __name__ == '__main__':
  app.run_server(debug=True)
import dash
from dash import html, dcc
from dash.dependencies import Input, Output

import pandas as pd
import numpy as np

import plotly.express as px



app = dash.Dash(__name__)
server = app.server

df = pd.read_csv("supermarket_sales.csv")
df["Date"] = pd.to_datetime(df["Date"])
df['Ano'] = df["Date"].dt.year
df['Mes'] = df['Date'].dt.strftime('%B')



# =========  Layout  =========== #
app.layout = html.Div(children=[
 html.Div([

html.Div([
        html.Div([
            html.B(html.H2('DMS', className='text-center')),
            html.P('Supermarket Sales', className='text-center'),
            html.Hr(),
            html.P('Deshboard para análise de vendas.', className='justify-content'),
            html.H5('Selecione uma ou mais cidades:'),
            dcc.Checklist(df['City'].value_counts().index,df['City'].value_counts().index, id='check_cidades', className='', inputStyle={'margin-right': '5px'}),
            html.Br(),
            html.H5('Selecione um tipo de totalização:'),
            dcc.RadioItems(['gross income', 'Rating'],'gross income' ,  id='check_agrupador', className='', inputStyle={'margin-right': '5px'}),
        ], style={'height':'100%', 'padding': '10px'}),
], className='col-sm-2 p-1 my-1 h-auto rounded-2', style={'background-color': '#111111'}),

html.Div([
        html.Div([

        html.Div([

            html.Div(
                html.Div(
                    html.Div(dcc.Graph(id='fig_cidade')), className='p-1 rounded-2', style={'background-color': '#111111'})
            , className='col-sm-6 p-1'),

            html.Div([
                html.Div(
                    html.Div(dcc.Graph(id='fig_pagamento')), className='p-1 rounded-2', style={'background-color': '#111111'}),
            ], className='col-sm-6 p-1'),

        ], className='row'),




        html.Div([
            html.Div(html.Div([dcc.Graph(id='fig_valor_tempo')], className=''), className='col-sm-12 rounded-2', style={'background-color': '#111111'}),
        ], className='row justify-content-between p-1'),

        html.Div([
            html.Div(html.Div([dcc.Graph(id='fig_produto')], className=''), className='col-sm-12 rounded-2', style={'background-color': '#111111'}),
        ], className='row justify-content-between p-1'),
], className='col-sm-12'),
], className='col-sm-10'),


], className='row m-1 '),
], className='container') # div principal layalt #

# =========  Callback  =========== #
@app.callback([
        Output('fig_cidade', 'figure'),
        Output('fig_pagamento', 'figure'),
        Output('fig_valor_tempo', 'figure'),
        Output('fig_produto', 'figure')
    ],
    [
        Input('check_cidades', 'value'),
        Input('check_agrupador', 'value')
    ])

def renderizar_graficos(check_cidades, check_agrupador):
    operador = np.sum if check_agrupador == 'gross income' else np.mean

    df_filtro = df[df['City'].isin(check_cidades)]
    df_cidades = df_filtro.groupby('City')[check_agrupador].apply(operador).to_frame().reset_index()
    df_pagamento = df_filtro.groupby('Payment')[check_agrupador].apply(operador).to_frame().reset_index()
    df_produto = df_filtro.groupby(['City', 'Product line'])[check_agrupador].apply(operador).to_frame().reset_index()
    df_tempo = df_filtro.groupby(['Ano', 'Mes'])[check_agrupador].apply(operador).to_frame().reset_index()

    fig_cidade = px.bar(df_cidades, x='City', y=check_agrupador, color='City')
    fig_pagamento = px.bar(df_pagamento, x=check_agrupador, y='Payment')
    fig_produto = px.bar(df_produto, x=check_agrupador, y='Product line', color='City', barmode='group')

    fig_valor_tempo = px.line(df_tempo, x='Mes', y=check_agrupador, color="Ano")

    fig_cidade.update_layout(template='plotly_dark', height=250, transition={"duration": 400})
    fig_pagamento.update_layout(template='plotly_dark', height=250, transition={"duration": 400})
    fig_valor_tempo.update_layout(template='plotly_dark', transition={"duration": 400})
    fig_produto.update_layout(template='plotly_dark', height=400, transition={"duration": 400})

    return fig_cidade, fig_pagamento, fig_produto, fig_valor_tempo

if __name__ == "__main__":
    #app.run_server(host='0.0.0.0', port=80, debug=True)
    app.run_server(debug=False)

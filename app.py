import dash
import dash_design_kit as ddk
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


app = dash.Dash(__name__)

server = app.server  # Expose the server variable for deployments

app.layout = ddk.App([
    ddk.Header([
        ddk.Logo(src=app.get_asset_url('dash-logo.png')),
        ddk.Title('Dash Enterprise Sample Application'),
    ]),
    ddk.Row(children=[
        ddk.Card(children=[
            ddk.CardHeader(children=[
                dcc.Dropdown(
                    id='title-dropdown',
                    options=[{'label': i, 'value': i}
                        for i in ['Trend1', 'Trend2', 'Trend3']],
                    value='Trend1'
                )
            ]),
            ddk.Graph(id='update-graph', style={'height':300}),
        ]),
    ]),

    ddk.Row(children=[
        ddk.Card(width=50,
            children=ddk.Graph(
                figure={
                    'data': [{
                        'x': [1, 2, 3, 4],
                        'y': [4, 1, 6, 9],
                        'line': {'shape': 'spline'}
                    }]
                },
            )
        ),

        ddk.Card(width=50,
            children=ddk.Graph(
                figure={
                    'data': [{
                        'x': [1, 2, 3, 4],
                        'y': [4, 1, 6, 9],
                        'line': {'shape': 'spline'}
                    }]
                },
            )
        ),
    ])
])


@app.callback(Output('update-graph', 'figure'),
              [Input('title-dropdown', 'value')])
def update_graph(value):
    if value == 'Trend1':
        y = [3, 1, 2, 3, 5, 6]
    elif value == 'Trend2':
        y = [3, 5, 6, 3, 1, 2]
    else:
        y = [5, 6, 1, 4, 2, 3]
    return {
        'data': [{
            'x': [1, 2, 3, 4, 5, 6],
            'y': y,
            'line': {'shape': 'spline'}
        }],
    }

if __name__ == '__main__':
    app.run_server(debug=True,port=8090)

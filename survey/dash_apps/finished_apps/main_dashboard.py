import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
from django.db.models import Count
from survey.models import Observation, Observation_Individual, Age

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('main_dash', external_stylesheets=external_stylesheets)

config = {'displayModeBar': False}


def pop_count_graph():
    #graph that counts households + individuals
    figure = {
        'data': [
            {'x': ['Groups', 'Individuals'],
             'y': [Observation.objects.all().count(), Observation_Individual.objects.all().count()], 'type': 'bar',
             'name': 'Groups'},
        ],
        'layout': {
            'title': 'Observed Households and Individuals',
            'font': dict(
                size = 12,
                family = 'sans-serif'
            )
        }
    }

    return figure

def age_graph():
    #simple pie chart for age groups
    age_lookup = {
        1: "Under 18",
        2: "18 - 24",
        3: "25+",
        4: "Not Sure"}

    data_group = Observation_Individual.objects.all().values('client_age').annotate(dcount=Count('client_age'))
    data_values = []
    data_annotations = []
    for x in data_group:
        data_values.append(list(x.values())[1])
        y = list(x.values())[0]
        data_annotations.append(age_lookup[y])
    figure = {
              "data": [
                {
                  "values": data_values,
                  "labels": data_annotations,
                  "textposition":"inside",
                  "name": 'Age',
                  "hoverinfo":"label+value+name",
                  "hole": .5,
                  "type": "pie"
                }],
              "layout": {
                    "title":"Age Groups",
                    "font" : dict(
                                size = 12,
                                family = 'sans-serif'
                            ),
                }
            }
    return figure

def gender_graph():
    #simple gender breakdown
    gender_lookup = {
        1: "Male",
        2: "Female",
        3: "Not Sure",
    }
    data_group = Observation_Individual.objects.all().values('client_gender').annotate(dcount=Count('client_gender'))
    data_values = []
    data_annotations = []
    for x in data_group:
        data_values.append(list(x.values())[1])
        y = list(x.values())[0]
        data_annotations.append(gender_lookup[y])
    figure = {
              "data": [
                {
                  "values": data_values,
                  "labels": data_annotations,
                  "textposition":"inside",
                  "name": 'Gender',
                  "hoverinfo":"label+value+name",
                  "hole": .5,
                  "type": "pie"
                }],
              "layout": {
                    "title":"Gender Groups",
                    "font" : dict(
                                size = 12,
                                family = 'sans-serif'
                            ),
                }
            }
    return figure

def race_graph():
    #pie chart for race
    race_lookup = {
        1: "American Indian or Alaska Native",
        2: "Asian",
        3: "Black or African American",
        4: "Native Hawaiian or Other Pacific Islander",
        5: "White",
        6: "Other",
        7: "Not Sure"
         }

    data_group = Observation_Individual.objects.all().values('client_race').annotate(dcount=Count('client_race'))
    data_values = []
    data_annotations = []
    for x in data_group:
        data_values.append(list(x.values())[1])
        y = list(x.values())[0]
        data_annotations.append(race_lookup[y])
    figure = {
              "data": [
                {
                  "values": data_values,
                  "labels": data_annotations,
                  "textposition":"inside",
                  "name": 'Race',
                  "hoverinfo":"label+value+name",
                  "hole": .5,
                  "type": "pie"
                }],
              "layout": {
                    "title":"Race",
                    "font" : dict(
                                size = 12,
                                family = 'sans-serif'
                            ),
                }
            }
    return figure


app.layout = html.Div(children=[
    html.Div(children=[
        html.Div([dcc.Graph(
            id='groups-individuals',
            figure=pop_count_graph(),
            config=config
        )],
            style={'display': 'inline-block', 'width': '49%'}),

        html.Div([dcc.Graph(
            id='age-groups',
            figure=age_graph(),
            config=config)
        ], style={'display': 'inline-block', 'width': '49%'})
    ], className='row'),

    html.Div(children=[
        html.Div([dcc.Graph(
            id='gender-groups',
            figure=gender_graph(),
            config=config
        )],
            style={'display': 'inline-block', 'width': '49%'}),

        html.Div([dcc.Graph(
            id='race-groups',
            figure=race_graph(),
            config=config)
        ], style={'display': 'inline-block', 'width': '49%'})
    ], className='row')
])
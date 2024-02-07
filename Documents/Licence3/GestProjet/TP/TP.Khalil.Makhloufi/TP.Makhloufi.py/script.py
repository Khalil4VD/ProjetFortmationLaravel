import dash
import dash.html as html
import dash.dcc as dcc
import random
from dash.dependencies import Input, Output
import io
import base64



#StatsMJ = {'X': [7, 7, 8, 6, 4]}
#StatsBM = {'Y': [5, 9, 9, 6, 4]}

#app.layout = html.Div([
 #   html.H1("Performance football"),
  #  dcc.Graph(id='scatter-plot',
    #    figure={
    #        'data': [
    #            {'x': StatsMJ['X'], 'y': StatsBM['Y'], 'mode': 'markers', 'type': 'scatter', 'name': 'Nuage de points'}
     #       ],
     #       'layout': {
     #           'title': 'Performance des attaquants de football',
      #          'xaxis': {'title': 'Matchs joués'},
      #          'yaxis': {'title': 'Buts marqués'}
      #      }
     #   }
    #),
   # html.Button('Mettre à jour le graphe', id='MAJ'),
#])


#@app.callback(
  #  Output('scatter-plot', 'figure'),
  #  Input('MAJ', 'n_clicks')
#)

#def update_scatter_plot(MAJ):

   # Donnee = {
    #    'X': [random.randint(1, 10) for _ in range(5)],
    #    'Y': [random.randint(1, 10) for _ in range(5)]
    #}

    #scatter_plot = {
  #      'data': [
   #         {'x': Donnee['X'], 'y': Donnee['Y'], 'mode': 'markers', 'type': 'scatter', 'name': 'Nuage de points'}
   #     ],
   #     'layout': {
   #         'title': 'Performance des attaquants de football',
   #         'xaxis': {'title': 'Matchs joués'},
   #         'yaxis': {'title': 'Buts marqués'}
   #     }
   # }

   # return scatter_plot


import mysql.connector

def getBD():
    bdd = mysql.connector.connect(
        host="localhost",
        port=8889, 
        user="root",
        password="root",
        database="FootProjet"
    )
    return bdd

base = getBD()
cursor = base.cursor()

query = "SELECT DISTINCT nom, Matches_Played, Goals, Minutes, age, Shots, OnTarget, date, nom_club, Ligue FROM foot ORDER BY RAND() LIMIT 10 OFFSET 5"
cursor.execute(query)

result = cursor.fetchall()

joueurs = [row[0] for row in result]
matches = [row[1] for row in result]
buts = [row[2] for row in result]
minutes = [row[3] for row in result]
age = [row[4] for row in result]
tir = [row[5] for row in result]
tircadre = [row[6] for row in result]
annee = [row[7] for row in result]
club = [row[8] for row in result]
ligue = [row[9] for row in result]





import plotly.express as px

import pandas as pd

df = pd.DataFrame({'Joueurs': joueurs, 'Match': matches, 'tir': tir, 'tircadre': tircadre, 'age': age, 'Minutes': minutes, 'Buts': buts, 'Annee': annee, 'Club': club, 'Ligue': ligue})



app = dash.Dash(__name__, suppress_callback_exceptions=True)

df_agecroissant = df.sort_values('age')
fig_age_players = px.bar(df_agecroissant, x='Joueurs', y='age', title="Âge des Joueurs")
fig_age_players.update_xaxes(title='Joueurs')
fig_age_players.update_yaxes(title="Âge")

app.layout = html.Div([
    html.H1("Les performances du football", 
            style={'text-align': 'center', 
            'border': '2px solid black'
    }),
    html.P("Nous allons étudier les statistiques de 10 joueurs différents, choisi aléatoirement sur une base de données, sur plusieurs saisons.", 
            style={'text-align': 'center'}),
    html.H2("Données des 10 joueurs séléctionnée pour l'étude", 
            style={'text-align': 'center'}),
    html.Table([
        html.Thead(html.Tr([html.Th('Nom du Joueur'), html.Th('Saison'), html.Th('Club'), html.Th('Championnat')])),
        html.Tbody([
            html.Tr([html.Td(df['Joueurs'][i]), html.Td(df['Annee'][i]), html.Td(df['Club'][i]), html.Td(df['Ligue'][i])])
            for i in range(len(df))
        ])
    ], style={'margin': 'auto', 'text-align': 'center', 'border': '2px solid black'}),
    html.P("Observons l'âge des joueurs pour bien nous situer sur leurs carrières. 20 ans -> vers début de carrière. 28 ans -> vers milieu de carrière. 38 ans -> vers fin de carrière.", 
            style={'text-align': 'center'}),
    html.H3("Figure 1", 
            style={'text-align': 'center',
    }),
    dcc.Graph(figure=fig_age_players),
    html.P("Ce nuage de point va nous montrer le nombre de but inscrit des joueurs par rapport à leurs nombre de matchs joué. Nous allons tout simplement connaître le ratio des joueurs. ", 
            style={'text-align': 'center'}),
    html.H3("Figure 2", 
            style={'text-align': 'center',
    }),
    dcc.Graph(figure=px.scatter(df, x='Match', y='Buts', text = 'Joueurs',
              size=[10 * m for m in matches], opacity=0.4, 
              title='Ratio but par matchs')
              .update_traces(textfont=dict(family="Arial", size=7, color="red")) 
    ),
    html.P("Quels joueurs ont disputé le plus de minutes sur leurs saisons ?", 
            style={'text-align': 'center'}),
    html.H3("Figure 3", 
            style={'text-align': 'center',
    }),
    dcc.Graph(
        figure=px.pie(
            df,
            values='Minutes',
            names='Joueurs',
            title='Répartition des minutes jouées par joueur'
        )
    ),
    html.P("Premièrement, observons la relations entre le nombre de buts inscrit et le nombre de matchs joué.", 
            style={'text-align': 'center'}),
    html.H3("Figure 4", 
            style={'text-align': 'center',
    }),
    dcc.Graph(
        figure=px.bar(
            df,
            x='Joueurs',
            y=['Buts', 'Match'],
            barmode='group',  
            title='Moyenne des buts et des minutes par joueur'
        )
    ),
    html.P("Enfin, observons la relations entre le nombre de buts inscrit et le nombre de tirs cadrés.", 
            style={'text-align': 'center'}),
    html.H3("Figure 5", 
            style={'text-align': 'center',
    }),
    dcc.Graph(
        figure=px.bar(
            df,
            x='Joueurs',
            y=['Buts', 'tircadre'],
            barmode='group',  
            title='Buts marqué par nombre de tir cadré'
        )
    ),
    html.P("Nous esperons que vous avez passée une bonne analyse. Rendez-vous pour une prochaine étude sur 10 autres joueurs.", 
            style={'text-align': 'center'}),
])

#for row in result:
#   print(row)

base.close()

if __name__ == '__main__':
    app.run_server(debug=True)
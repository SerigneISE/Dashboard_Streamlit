import streamlit as st
import pandas as pd
import plotly.express as px
from flask import Flask

st.title("Serigne Mbaye THIAM")
st.write("TP API STREAMLIT")

# Lire les données
clics = pd.read_csv('clics.csv')
impressions = pd.read_csv('impressions.csv')
achats = pd.read_csv('achats.csv')

imp_clic = pd.merge(impressions, clics, on='cookie_id')
imp_clic_achat = pd.merge(imp_clic, achats, on='cookie_id')

# Filtrer les données en fonction des options sélectionnées
dept_filter = st.multiselect("Sélectionner les départements", imp_clic_achat['dept'].unique())
filtered_data = imp_clic_achat[imp_clic_achat['dept'].isin(dept_filter)]

# Calcul du chiffre d'affaires
ca = filtered_data['price'].sum()
st.write(f"<span style='color:green; font-size:60px;'> Chiffre d'affaires : {ca} € </span>", unsafe_allow_html=True)

# Age en fonction des produits
st.subheader('Age en fonction des produits')
box = px.box(filtered_data, x='product_id', y='age')
st.plotly_chart(box)

# Répartition des ventes en fonction du sexe
st.subheader('Répartition des ventes en fonction du sexe')
colors = ['#FF0000', '#00FF00']  # Exemple de couleurs personnalisées (rouge et vert)
pie = px.pie(filtered_data, values='price', names='gender', color_discrete_sequence=colors)
st.plotly_chart(pie)

# Distribution des ventes par département
st.subheader('Distribution des ventes par département')
bar = px.bar(filtered_data, x='dept', y='price', title='Distribution des ventes par département')
st.plotly_chart(bar)

# Répartition des ventes par campagne et par sexe
st.subheader('Répartition des ventes par campagne et par sexe')
stacked_bar = px.bar(filtered_data, x='campaign_id', y='price', color='gender', barmode='stack', title='Répartition des ventes par campagne et par sexe')
st.plotly_chart(stacked_bar)


if __name__ == '__dashboard_tuto__':
    app.run(debug=True)

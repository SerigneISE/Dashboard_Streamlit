import streamlit as st
import pandas as pd
from flask import Flask
import plotly.express as px

st.title("Serigne Mbaye THIAM")
st.write("TP API STREAMLIT")

clics = pd.read_csv('clics.csv')
impressions = pd.read_csv('impressions.csv')
achats = pd.read_csv('achats.csv')

imp_clic = pd.merge(impressions,clics, on ='cookie_id')
imp_clic_achat = pd.merge(imp_clic ,achats, on ='cookie_id')
imp_clic_achat 

app = Flask(__name__)


@app.route('/api/donnees', methods=['GET'])
def donnees():
    return jsonify(imp_clic_achat )
   
   
   
ca= imp_clic_achat ['price'].sum()
st.write(f"<span style='color:green; font-size:60px;'> Chiffre d'affaires : {ca} € </span>", unsafe_allow_html=True)

st.subheader('Vente en fonction des campagnes')
hist= px.histogram(imp_clic_achat , x = 'campaign_id', y= 'price')
st.plotly_chart(hist)


st.subheader('Age en fonction des produits')
box= px.box(imp_clic_achat , x = 'product_id' , y= 'age')
st.plotly_chart(box)


st.subheader('Répartition des ventes en fonction du sexe')
colors = ['#808080', '#FFFF00']
pie = px.pie(imp_clic_achat , values='price', names='gender', color_discrete_sequence=colors)
st.plotly_chart(pie)

st.subheader('Nuage de points des ventes en fonction des produits')
nuage = px.scatter(imp_clic_achat , x='price', y='product_id')
st.plotly_chart(nuage)

 

if __name__ == '__dashboard_tuto__':
    app.run(debug=True)
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


st.set_page_config(
    page_icon="icon.png",
    page_title="Xbox analisis",
    layout="wide",
)

#crear dataframe
df = pd.read_csv("xbox.csv")

#le ponemos titulo
st.title(":green[Estadisticas de el game pass de xbox]🎮")


#creamos las metricas
c1,c2,c3= st.columns(3)
with c1:
    juego_mas_popular = df.loc[df['RATING'].idxmax(), 'GAME']
    st.metric(label="Juego mejor valorado",value=juego_mas_popular)
    
with c2:
    juego_mas_jugadores = df.loc[df['GAMERS'].idxmax(), 'GAME']
    st.metric(label="juegos con mas jugadores",value=juego_mas_jugadores)

with c3:
    juego_mas_puntos = df.loc[df['Game_Score'].idxmax(), 'GAME']
    st.metric(label="juegos con mas puntos",value=juego_mas_puntos)

st.subheader(":green[Dataframe]",divider="grey")  
st.dataframe(df,use_container_width=True,hide_index=True)


with st.sidebar:
    st.image("xbox.png")
    graficas = {"pie","barra","linea"}
    seleccion = st.multiselect("selecione que graficas quiere generar",graficas)
    juegos = st.multiselect("seleccione los juegos a comparar",df["GAME"])
    if analizar :=st.button("Analizar"):
        if len(graficas) >1 and len(juegos)>1:
            df = df[df["GAME"].isin(juegos)]
        else:
            st.warning("Porfavor verifique que estan todos los parametros")



#hacemos las funciones para generar graficas
def pie(df):
    st.subheader(":green[Juego vs Puntuacion]", divider="grey")
    fig, ax = plt.subplots()
    fig.patch.set_alpha(0.0)  # Hacer transparente el fondo de la figura
    ax.set_facecolor('none')  # Hacer transparente el fondo del eje
    if len(juegos) > 1:
        ax.pie(df['Game_Score'], labels=juegos)
        ax.set_title('Grafica de linea', color='white')  # Título en blanco
        for text in ax.texts:
            text.set_color('white')  # Etiquetas en blanco
        st.pyplot(fig)
    else:
        st.warning("seleccione al menos 2 juegos")
        
def barra(df):
    st.subheader(":green[juego vs jugadores]",divider="grey")
    if len(juegos)>1:
        fig, ax = plt.subplots()
        ax.bar(juegos,df["GAMERS"])
        fig.patch.set_alpha(0.0)  # Hacer transparente el fondo de la figura
        ax.set_facecolor('none')  # Hacer transparente el fondo del eje
        ax.set_xlabel("Juego",color = "white")
        ax.set_ylabel("Jugadores",color = "white")
        ax.tick_params(axis='x', colors='white')  # Ticks del eje X en blanco
        ax.tick_params(axis='y', colors='white')  # Ticks del eje Y en blanco
        ax.set_title("Graficas de barra", color = "white")
        st.pyplot(fig)
    else:
        st.warning("seleccione al menos 2 juegos")

def linea(df):
    st.subheader(":green[Popularidad del juego]",divider="grey")
    fig, ax=plt.subplots()
    ax.plot(juegos, df['RATING'])
    fig.patch.set_alpha(0.0)  # Hacer transparente el fondo de la figura
    ax.set_facecolor('none')  # Hacer transparente el fondo del eje
    ax.set_xlabel("Juegos",color="white")
    ax.set_ylabel("Puntuacion", color="white")
    ax.tick_params(axis='x', colors='white')  # Ticks del eje X en blanco
    ax.tick_params(axis='y', colors='white')  # Ticks del eje Y en blanco
    st.pyplot(fig)

if analizar:
    if "pie" in seleccion:
        pie(df)
    if "barra" in seleccion:
        barra(df)
    if "linea" in seleccion:
        linea(df)


st.success("si desea generar graficas entre a la barra lateral")
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from PIL import Image

st.set_page_config(page_title='Corpus Lenguístico',
                   layout='wide', page_icon=':✌:')

path_csv = '../Ficheros/csv/df_original.csv'
df = pd.read_csv(path_csv, sep='\t', encoding='utf-8',
                 nrows=1000, index_col="Unnamed: 0")

path_csv1 = '../Ficheros/csv/df_colums.csv'

df1 = pd.read_csv(path_csv1, sep='\t', encoding='utf-8',
                  nrows=1000, index_col="id")

menu = st.sidebar.selectbox(
    "Seleccione una opción del menu",
    ('Datos', 'Procesamiento de Texto (NLP)',
     'Análisis exploratorio de datos (EDA)',
     'Gráficos: Frecuencia',
     'Gráficos: Words Cloud',
     'Gráficos: Total de palabras',
     'Gráficos: Otros',)
)

if menu == 'Datos':
    st.title('Datos Iniciales')

    st.write(df)
    st.markdown('**Rows:** 19.511.591')

elif menu == 'Procesamiento de Texto (NLP)':
    st.title('Procesamiento de Texto (NLP)')

    st.write(df1)
    st.markdown('**Rows:** 16.850.800')
    st.markdown('**Cols:** 27')

    components.html(
        """
        <style>
            table {
                font-family: arial, sans-serif;
                border-collapse: collapse;
                width: 100%;
            }

            td, th {
              border: 1px solid #dddddd;
                text-align: left;
                padding: 2px 8px;
            }
            </style>
         <table>
           <tr>
                <th>Variable</th>
                <th>Descripción</th>
            </tr>
            <tr>
                <td>source</td>
                <td>frases en inglés</td>
            </tr>
            <tr>
                <td>target</td>
                <td>frases en español</td>
            </tr>
            <tr>
                <td>file_name</td>
                <td>nombre del archivo</td>
            </tr>
            <tr>
                <td>quantity_words_source</td>
                <td>cantidad de palabras en inglés</td>
            </tr>
            <tr>

                <td>quantity_words_target</td>
                <td>cantidad de palabras en español</td>
            </tr>
            <tr>
                <td>sentiment</td>
                <td>sentimiento de la frase</td>
            </tr>
            <tr>
                <td>NOUN_source</td>
                <td>cantidad de sustantivos en inglés</td>
            </tr>
            <tr>
                <td>NOUN_target</td>
                <td>cantidad de sustantivos en español</td>
            </tr>
            <tr>
                <td>ADJ_source</td>
                <td>cantidad de adjetivos en inglés</td>

            </tr>
            <tr>
                <td>ADJ_target</td>
                <td>cantidad de adjetivos en español</td>
            </tr>
            <tr>

                <td>DET_source</td>
                <td>cantidad de determinantes en inglés</td>
            </tr>
            <tr>
                <td>DET_target</td>
                <td>cantidad de determinantes en español</td>
            </tr>
            <tr>
                <td>ADV_source</td>
                <td>cantidad de adverbios en inglés</td>
            </tr>
            <tr>
                <td>ADV_target</td>
                <td>cantidad de adverbios en español</td>
            </tr>
            <tr>
                <td>CCONJ_source</td>
                <td>cantidad de conjunciones en inglés</td>
            </tr>
            <tr>
                <td>CCONJ_target</td>
                <td>cantidad de conjunciones en español</td>
            </tr>
            <tr>
                <td>VERB_source</td>
                <td>cantidad de verbos en inglés</td>
            </tr>
            <tr>
                <td>VERB_target</td>
                <td>cantidad de verbos en español</td>
            </tr>
            <tr>
                <td>VAUX_source</td>
                <td>cantidad de verbos auxiliares en inglés</td>
            </tr>
            <tr>
                <td>VAUX_target</td>
                <td>cantidad de verbos auxiliares en español</td>
            </tr>
            <tr>
                <td>PRON_source</td>
                <td>cantidad de pronombres en inglés</td>
            </tr>
            <tr>
                <td>PRON_target</td>
                <td>cantidad de pronombres en español</td>
            </tr>
            <tr>
                <td>ADP_source</td>
                <td>cantidad de preposiciones en inglés</td>
            </tr>
            <tr>

                <td>ADP_target</td>
                <td>cantidad de preposiciones en español</td>
            </tr>
            <tr>

                <td>PUNCT_source</td>
                <td>cantidad de signos de puntuación en inglés</td>
            </tr>
            <tr>
                <td>PUNCT_target</td>
                <td>cantidad de signos de puntuación en español</td>
            </tr>
            <tr>
                <td>busy</td>
                <td>si la frase es ocupada o no (1: ocupada, 0: no ocupada).</td>
            </tr>

            </table>

        """,
        height=600,
    )

elif menu == 'Análisis exploratorio de datos (EDA)':
    st.title('Análisis exploratorio de datos (EDA)')
    st.subheader('1- Análisis de valores nulos y variables irrelevantes')

    components.html(
        """
          <style>
            table {
                font-family: arial, sans-serif;
                border-collapse: collapse;
                width: 100%;
            }

            td, th {
                border: 1px solid #dddddd;
                text-align: left;
                padding: 2px 8px;
            }
            </style>
            <table>
            <tr>
                <th>Variable</th>
                <th>Valores Nulos</th>
                <th>Irrelevantes</th>
            </tr>
            <tr>
                <td>source</td>
                <td>0</td>
                <td></td>
            </tr>
            <tr>
                <td>target</td>
                <td>0</td>
                <td></td>
            </tr>
            <tr>
                <td>file_name</td>
                <td>0</td>
                <td></td>
            </tr>
            <tr>
                <td>quantity_words_source</td>
                <td>0</td>
                <td></td>
            </tr>
            <tr>
                <td>quantity_words_target</td>
                <td>0</td>
                <td></td>
            </tr>
            <tr>

                <td>sentiment</td>
                <td>4808800</td>
                <td></td>
            </tr>
            <tr>
                <td>NOUN_source</td>
                <td>4808800</td>
                <td></td>
            </tr>
            <tr>
                <td>NOUN_target</td>
                <td>4808800</td>
                <td></td>
            </tr>
            <tr>
                <td>ADJ_source</td>
                <td>4808800</td>
                <td></td>
            </tr>
            <tr>
                <td>ADJ_target</td>
                <td>4808800</td>
                <td></td>
            </tr>
            <tr>
                <td>DET_source</td>
                <td>4808800</td>
                <td></td>
            </tr>
            <tr>

                <td>DET_target</td>
                <td>4808800</td>
                <td></td>
            </tr>
            <tr>
                <td>ADV_source</td>
                <td>4808800</td>
                <td></td>
            </tr>
            <tr>
                <td>ADV_target</td>
                <td>4808800</td>
                <td></td>
            </tr>
            <tr>
                <td>CCONJ_source</td>
                <td>4808800</td>
                <td></td>
            </tr>
            <tr>
                <td>CCONJ_target</td>
                <td>4808800</td>
                <td></td>
            </tr>
            <tr>
                <td>VERB_source</td>
                <td>4808800</td>
                <td></td>
            </tr>
            <tr>
                <td>VERB_target</td>
                <td>4808800</td>
                <td></td>
            </tr>
            <tr>
                <td>VAUX_source</td>
                <td>4808800</td>
                <td></td>
            </tr>
            <tr>
                <td>VAUX_target</td>
                <td>4808800</td>
                <td></td>
            </tr>
            <tr>

                <td>PRON_source</td>
                <td>4808800</td>
                <td></td>
            </tr>
            <tr>
                <td>PRON_target</td>
                <td>4808800</td>
                <td></td>
            </tr>
            <tr>
                <td>ADP_source</td>
                <td>4808800</td>
                <td></td>
            </tr>
            <tr>
                <td>ADP_target</td>
                <td>4808800</td>
                <td></td>
            </tr>
            <tr>
                <td>PUNCT_source</td>
                <td>4808800</td>
                <td></td>
            </tr>
            <tr>
                <td>PUNCT_target</td>
                <td>4808800</td>
                <td></td>
            </tr>
            <tr>
                <td>busy</td>
                <td>0</td>
                <td>X</td>
            </tr>
            </table>
            <div>
            </div>

        """,
        height=680,
    )

    st.subheader('2- Valores Extremos en Variables Numéricas')
    st.write('Distribución de las variables numéricas')
    image = Image.open('graphics/distributionsVarNum.jpeg')
    st.image(image, caption='Scatter de las variables numéricas')
    st.divider()
    image1 = Image.open('graphics/histograms.jpeg')
    st.image(image1, caption='Histogramas de las variables numéricas')
    st.divider()
    image2 = Image.open('graphics/boxplots.jpeg')
    st.image(image2, caption='Boxplots de las variables numéricas')
    st.divider()

    components.html(
        """
          <style>
            table {
                font-family: arial, sans-serif;
                border-collapse: collapse;
                width: 100%;
            }

            td, th {
                border: 1px solid #dddddd;
                text-align: left;
                padding: 2px 8px;
            }
            </style>
            <table>
            <tr>
                <th>Variables</th>
                <th>Límite Superior</th>
            </tr>

            <tr>
                <td>NOUN_source</td>
                <td>8,5</td>
            </tr>

            <tr>
                <td>ADJ_source</td>
                <td>5,0</td>
            </tr>
            <tr>
                <td>DET_source</td>
                <td>5,0</td>
            </tr>
            <tr>
                <td>ADV_source</td>
                <td>2,5</td>
            <tr>
                <td>CCONJ_source</td>
                <td>2,5</td>
            </tr>

            <tr>
                <td>VERB_source</td>
                <td>6,0</td>
            </tr>

            <tr>
                <td>VAUX_source</td>
                <td>5,0</td>
            </tr>

            <tr>

                <td>PRON_source</td>
                <td>6,0</td>
            </tr>

            <tr>
                <td>ADP_source</td>
                <td>5,0</td>
            </tr>

            <tr>
                <td>PUNCT_source</td>
                <td>6,0</td>
            </tr>
            </table>
            <div>
            </div>

        """,
        height=300,
    )

    st.divider()
    st.write('Tratamientos de Valores Extremos')
    image3 = Image.open('graphics/BoxplotPUNCT.jpeg')
    st.image(image3)
    st.divider()
    image4 = Image.open('graphics/BoxplotDelOutliers.jpeg')
    st.image(image4)
    st.divider()

    st.subheader('3- Errores tipográficos en las variables categóricas')
    image5 = Image.open('graphics/byFile1.jpeg')
    st.image(image5)
    st.divider()
    image6 = Image.open('graphics/byFile2.jpeg')
    st.image(image6)
    st.divider()

    components.html(
        """
        <ul>
            <li>Fichero original: 19 511 591 observaciones.</li>
            <li>Resultado de eliminar sources repetidos: 16 850 800 observaciones.</li>
            <li>Resultado de eliminar filas con valores nulos: 12 042 000 observaciones.</li>
            <li>Resultado de eliminar outliers: 10 068 314 observaciones.</li>
            </ul>
        """,
    )

elif menu == 'Gráficos: Frecuencia':
    st.title('Gráficos: Frecuencia')
    image7 = Image.open('graphics/occurrences.jpeg')
    st.image(image7)
    st.divider()

    image6 = Image.open('graphics/byFile2.jpeg')
    st.image(image6)
    st.divider()

    components.html(
        """
       <ul>
            <li>Se cuenta con 9 fuentes de datos (file_name)</li>
            <li>La fuente de datos con mayor cantidad de registros es 'ecomm' con 4 063 038 observaciones</li>
            <li>Hay 3 clases de sentimientos: positivo, negativo y neutro.</li>
            <li>La clase de sentimiento con mayor cantidad de registros en este dataset es 'positivo', con 4 282 114 observaciones.</li>
        </ul>
        """,
    )

    image6 = Image.open('graphics/frequency.jpeg')
    st.image(image6)
    st.divider()

    components.html(
        """
      <ul>
        <li>Observaciones</li>
        <ul>
            <li>De un total de 10 068 314 observaciones:</li>
            <li>La media de palabras (promedio) en el "source" es de 13.11, lo que significa que, en promedio, hay aproximadamente 13.11 palabras por frases en la fuente de los datos.</li>
            <li>La media de palabras (promedio) en el "target" es de 13.65, lo que indica que, en promedio, hay aproximadamente 13.65 palabras por frases en el destino de los datos.</li>
            <li>La desviación estándar en el "source" es de aproximadamente 6.73, lo que significa que los datos en la fuente tienen una dispersión promedio de alrededor de 6.73 unidades con respecto a la media de palabras.</li>
            <li>La desviación estándar en el "target" es de aproximadamente 7.34, lo que indica que los datos en el destino tienen una dispersión promedio de alrededor de 7.34 unidades con respecto a la media de palabras.</li>
        </ul>
        </ul>
        """,
        height=180,
    )

    image6 = Image.open('graphics/frequency1.jpeg')
    st.image(image6)
    st.divider()

    components.html(
        """
        <h4>Se observan diferencias en la media y desviación estándar entre el source y el target para las diferentes categorías gramaticales.</h4>
        <ul>
            <li>media: promedio de la cantidad de palabras de acuerdo a la categoría existente en el source y target</li>
            <li>desviación estándar: variabilidad de la cantidad de palabras en el source y target con respecto a la media</li>
        </ul>
        """,
        height=200,
    )

    image6 = Image.open('graphics/frequency2.jpeg')
    st.image(image6)
    st.divider()

    components.html(
        """
        <h4>Observaciones</h4>
        <ul>
            <li>Para el "source":</li>
            <li>La media de la cantidad de signos de puntuación es aproximadamente 1.78, lo que indica que en promedio hay alrededor de 1.77 signos de puntuación en cada frase del "source".</li>
            <li>La desviación estándar es aproximadamente 1.25, lo que indica que la cantidad de signos de puntuación varía en promedio alrededor de 1.25 unidades con respecto a la media en el "source".</li>
            <li>Para el "target":</li>
            <li>La media de la cantidad de signos de puntuación es aproximadamente 1.88, lo que indica que en promedio hay alrededor de 1.88 signos de puntuación en cada frase del "target".</li>
            <li>La desviación estándar es aproximadamente 1.36, lo que indica que la cantidad de signos de puntuación varía en promedio alrededor de 1.36 unidades con respecto a la media en el "target".</li>

        </ul>
        """,
        height=250,
    )

    components.html(
        """
        <h4>En resumen</h4>
        <p>
           Se observa que la cantidad de signos de puntuación en el "source" y el "target" tienen medias y desviaciones estándar ligeramente diferentes, lo que indica que pueden haber diferencias en la cantidad de signos de puntuación entre ambos conjuntos de datos.
        </p>
        """,
        height=400,
    )

elif menu == 'Gráficos: Words Cloud':
    st.title('Gráficos: Words Cloud')

    image7 = Image.open('graphics/cloud.jpeg')
    st.image(image7)
    st.divider()

    image8 = Image.open('graphics/top10.jpeg')
    st.image(image8)

    st.divider()
    components.html(
        """
        <h4>Observaciones</h4>
        <p>
           En este conjunto de datos en el top 10 de palabras solo se repite "id" en ambos idiomas y no tienen la misma frecuencia de aparición
        </p>
        """,
        height=400,
    )

elif menu == 'Gráficos: Total de palabras':
    st.title('Gráficos: Total de palabras')

    image9 = Image.open('graphics/percentage.jpeg')
    st.image(image9)
    st.divider()
    components.html(
        """
        <h4>Observaciones</h4>
        <ul>
            <li>Con esta representación se puede observar que el vocabulario del target es mayor al del source.</li>
            <li>Se utilizan más palabras en el idioma español que en el inglés.</li>
        </ul>

        """,
        height=150,
    )

    image10 = Image.open('graphics/totalWords.jpeg')
    st.image(image10)
    st.divider()

    components.html(
        """
        <ul>
        <li><strong>Observaciones:</strong></li>
        <ol>
            <li>El gráfico de barras muestra la cantidad de palabras por categoría gramatical en el corpus de origen y en el corpus de destino.</li>
            <li>En todas las categorías gramaticales se nota una diferencia entre el corpus de origen y el corpus de destino.</li>
            <li>Categorías donde el source es mayor que el target: ADJ, VERB, VAUX, PRON</li>
            <li>Categorías donde el target es mayor que el source: NOUN, DET, ADV, CCONJ, ADP, PUNCT</li>
        </ol>
        </ul>

        """,
        height=250,
    )

    image11 = Image.open('graphics/ratio.jpeg')
    st.image(image11)
    st.divider()

    components.html(
        """
      <ul>
        <li><strong>Observaciones</strong></li>
        <br>
        <p>Al calcular el ratio de aparición de las categorías gramaticales en el source y target de acuerdo al conjunto de datos obtenido nos podemos dar cuenta que:</p>
        <li>Hay más palabras en la traducción al español que en el source: Un 96% más de palabras en el target que en el source</li>
        <li>Hay más sustantivos en la traducción al español que en el source: Un 95% más de sustantivos en el target que en el source</li>
        <li>Hay más adjetivos en las frases en inglés que en el target: un 5% más de adjetivos en el source que en el target</li>
        <li>Hay más determinantes en las frases en target que en el source: un 64% más de determinantes en el target que en el source</li>
        <br>
        <strong>En resumen podemos decir que las frases en inglés son más cortas que las traducciones al español, de acuerdo al conjunto de datos obtenidos.</strong><br/>
        <strong>En general existe diferencias entre ambos idiomas.</strong>
        </ul>

        """,
        height=350,
    )

elif menu == 'Gráficos: Otros':
    st.title('Gráficos: Otros')

    image12 = Image.open('graphics/media.jpeg')
    st.image(image12)

    components.html(
        """
        <h4>Observaciones</h4>
        <p>
          De acuerdo al conjunto de datos analizado podemos concluir que en las páginas de redes sociales utilizan menos signos de puntuación.
            La comparación se realizó respecto a la media porque no se cuenta con la misma cantidad de frases en todas las fuentes.
        </p>
        """,
        height=150,
    )

    st.divider()

    image13 = Image.open('graphics/mediaWordsByP.jpeg')
    st.image(image13)
    st.divider()

    image14 = Image.open('graphics/frequencySP.jpeg')
    st.image(image14)
    st.divider()

    image15 = Image.open('graphics/frequencySN.jpeg')
    st.image(image15)
    st.divider()

    image16 = Image.open('graphics/frequencyPNN.jpeg')
    st.image(image16)
    st.divider()

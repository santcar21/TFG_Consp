# TFG_Consp
Repositorio de los códigos de Phyton utilizados para el TFG "Crisis y posverdad. Un estudio comparativo sobre la difusión pre y post COVID-19 de teorías conspirativas en las redes sociales virtuales" por Muñoz Sanz, C. (2025)

Los archivos utilizados para este estudio pueden encontrarse en: https://data.gesis.org/tweetskb/#Dataset . Titulados "month_2019-05.n3.gz" y "month_2020-04.n3.gz". 

Las líneas de código utilizadas para el análisis son:

"read_chunk_def.py" para la lectura del archivo RDF (.n3) y el filtrado para sólo los hashtags con twits

"hashtags_txt_all.py" y "hashtags_txt_100.py" para la extracción en un txt de: todos los hashtags y los que se repiten más de 100 veces para su posterior análisis y categorización

"extract_conspiracy_2019.py" y "extract_conspiracy_2020.py" para el filtrado de las bases de datos y la obtención de las bases a analizar con los hashtags conspirativos

"generate_edges.py" y "generate_nodes.py" para la generación de los archivos .csv para Gephi.

Los archivos de Gephi para cada base de datos están titulados como "red_NUMERORED_db.gephi.

Los nodes y edges de cada una de las bases están titulados como "red_NUMERODERED_nodes.csv" para los nodos y "red_NUMERODERED_edges.csv" para las aristas.

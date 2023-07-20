# PrediccioCaiguda

Aquest projecte es centra en la implementació d’un algorisme d’intel·ligència artificial per detectar la caiguda de persones grans. El projecte es basa en les dades recollides durant el projecte WIISEL al llarg dels anys 2014-2015 en el que es van crear unes plantilles de sabates amb un giroscopi, 2 acceleròmetres i 14 sensors de pressió cadascuna. L’objectiu del projecte és fer un estudi de les dades per tal de desenvolupar una xarxa neuronal recurrent per predir les caigudes implementant un sistema mèdic fiable i senzill que informi als usuaris sobre la seva condició sense necessitat d’acudir a un centre d’atenció primària.

A continuació s'explica que conté cadascun dels fitxers que es troben a la carpeta notebooks:

**Dataframes_creation.ipynb:** codi per la realització d'un sol dataset amb totes les dades recollides del projecte WIISEL

**Cleaningdata.py:** es centra en netejar les dades eliminant aquelles considerades incorrectes

**df2015_complet.py:** conté el codi amb la preparació de les dades per a facilitar la representació gràfica i estudiar el seu comportament

**EDA2015.ipynb:** codi de l'anàlisi dels atributs i la correlació entre ells

**Grafics.ipynb:** codi per la realització dels gràfics del comportament dels giroscopis, acceleròmetres, mòduls dels acceleròmetres i sensors de pressió

**model_RNN.py:** codi del model simpleRNN

**model_LSTM.py:** codi del model LSTM

**model_GRU.py:** codi del model GRU

**ComparativaModels.ipynb:** conté el codi per a la realització dels gràfics amb el comportament de l'accuracy i la loss al llarg dels entrenaments

L’estudi s’ha centrat en el maneig de les dades en cru del projecte WIISEL. El principal repte ha estat la gestió de les dades degut a la gran quantitat i a la falta de balanceig entre aquestes. Tot i així, s’ha demostrat que els sensors de pressió no aporten la informació més rellevant per predir les caigudes i que les xarxes neuronals recurrents, en particular el model GRU, són una bona opció per a la predicció de les caigudes.

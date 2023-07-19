import sys
stdout_original = sys.stdout

with open('Resultats_RNN.txt', 'w') as archivo:
    sys.stdout = archivo

    print("Important llibreries")
    import numpy as np
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler, MinMaxScaler
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import LSTM, Dense, SimpleRNN, GRU
    from sklearn.metrics import accuracy_score
    
    print("Llegint dataset")
    df = pd.read_csv("df2015_model.csv")
    
    print("Separant en X, y")
    TARGET = 'Fall'
    y = df[TARGET]
    X = df.drop([TARGET], axis=1)
    
    print("Separant en train, test")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=777, stratify=y)
    
    # Definir las combinaciones posibles
    scalers = [StandardScaler()]
    activations = ['sigmoid']
    losses = ['binary_crossentropy']
    optimizers = ['adam', 'sgd', 'RMSprop']
    metrics = ['accuracy']
    
    # Función para crear y entrenar el modelo
    print("Defininit la funció per entrenar el model")
    def train_model(scaler, activation, loss, optimizer, metric):
        # Normalizar datos
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
    
        # Reshape de las datos para la entrada de la RNN
        X_train_reshaped = np.reshape(X_train_scaled, (X_train_scaled.shape[0], 1, X_train_scaled.shape[1]))
        X_test_reshaped = np.reshape(X_test_scaled, (X_test_scaled.shape[0], 1, X_test_scaled.shape[1]))
    
        class_weights = dict(zip([0, 1], (len(y_train) / (2 * pd.value_counts(y_train))).values))
    
        # Crear modelo RNN
        model = Sequential()
        model.add(SimpleRNN(64, input_shape=(X_train_reshaped.shape[1], X_train_reshaped.shape[2])))
        model.add(Dense(1, activation=activation))
    
        model.compile(loss=loss, optimizer=optimizer, metrics=[metric])
    
        # Entrenar
        history = model.fit(X_train_reshaped, y_train, class_weight=class_weights, epochs=5, batch_size=32, validation_data=(X_test_reshaped, y_test))
    
        # Evaluar
        loss, accuracy = model.evaluate(X_test_reshaped, y_test, batch_size=32)
        print("accuracy")
        print(accuracy)
        print(history.history['accuracy'])
        print("loss")
        print(loss)
        print(history.history['loss'])
        return accuracy
    
    # Búsqueda en cuadrícula
    best_accuracy = 0.0
    best_config = {}
    print("")
    for scaler in scalers:
        for activation in activations:
            for loss in losses:
                for optimizer in optimizers:
                    for metric in metrics:
                        print("Entrenant el model per",scaler,activation,loss,optimizer)
                        accuracy = train_model(scaler, activation, loss, optimizer, metric)
                        conf = {'scaler': scaler, 'activation': activation, 'loss': loss, 'optimizer': optimizer, 'metric': metric, 'accuracy': accuracy*100}
                        print("Resultats", conf)
                        print("")
                        if accuracy > best_accuracy:
                            best_accuracy = accuracy
                            best_config = {'scaler': scaler, 'activation': activation, 'loss': loss, 'optimizer': optimizer, 'metric': metric}
    
    # Mostrar la mejor configuración
    print('Best configuration:')
    print(best_config)
    print('Best accuracy: %.2f' % (best_accuracy * 100))
    
    sys.stdout = stdout_original

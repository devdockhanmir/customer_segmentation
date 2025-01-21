import numpy as np
import pandas as pd
import plotly.graph_objects as go
from sklearn.preprocessing import MinMaxScaler
from minisom import MiniSom

# Load the dataset
df = pd.read_csv('data/Mall_Customers.csv')

# Select features for SOM
features = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# Normalize the data
scaler = MinMaxScaler()
data = scaler.fit_transform(features)

# Initialize SOM parameters
som_shape = (1, 5)  # 1 row, 5 columns
som = MiniSom(som_shape[0], som_shape[1], data.shape[1], sigma=0.5, learning_rate=0.5)

# Randomly initialize weights
som.random_weights_init(data)

# Train SOM
max_iter = 1000
som.train_random(data, max_iter)

# Calculate Quantization and Topographic Errors
q_error = [som.quantization_error(data[:i+1]) for i in range(len(data))]
t_error = [som.topographic_error(data[:i+1]) for i in range(len(data))]

# Plot errors
fig = go.Figure()
fig.add_trace(go.Scatter(x=np.arange(len(q_error)), y=q_error, mode='lines', name='Quantization Error'))
fig.add_trace(go.Scatter(x=np.arange(len(t_error)), y=t_error, mode='lines', name='Topographic Error'))
fig.update_layout(
    title='Quantization and Topographic Error',
    xaxis_title='Data Index',
    yaxis_title='Error',
    hovermode='x'
)
fig.show()

```python
# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class Visualization:
    def __init__(self):
        pass

    def visualize(self, data, predictions):
        # Visualize the original data
        self.plot_data(data)

        # Visualize the predictions
        self.plot_predictions(predictions)

    def plot_data(self, data):
        # Convert data to DataFrame for easier manipulation
        df = pd.DataFrame(data)

        # Plot the data
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=df)
        plt.title('Climate Data')
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.show()

    def plot_predictions(self, predictions):
        # Convert predictions to DataFrame for easier manipulation
        df = pd.DataFrame(predictions)

        # Plot the predictions
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=df)
        plt.title('Predicted Climate Trends')
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.show()
```

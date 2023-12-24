```python
# Import necessary libraries
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

class PerformanceMetrics:
    def __init__(self, y_true, y_pred):
        self.y_true = y_true
        self.y_pred = y_pred

    def calculate_rmse(self):
        """
        Calculate Root Mean Squared Error (RMSE)
        """
        rmse = np.sqrt(mean_squared_error(self.y_true, self.y_pred))
        return rmse

    def calculate_mae(self):
        """
        Calculate Mean Absolute Error (MAE)
        """
        mae = mean_absolute_error(self.y_true, self.y_pred)
        return mae

    def calculate_r2_score(self):
        """
        Calculate R2 Score
        """
        r2 = r2_score(self.y_true, self.y_pred)
        return r2

    def calculate_all_metrics(self):
        """
        Calculate all performance metrics
        """
        rmse = self.calculate_rmse()
        mae = self.calculate_mae()
        r2 = self.calculate_r2_score()

        return {"RMSE": rmse, "MAE": mae, "R2 Score": r2}
```

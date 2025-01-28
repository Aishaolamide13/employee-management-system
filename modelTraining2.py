import pandas as pd

# Create a table for metrics
decision_tree_results = {
    "Metric": ["Accuracy", "Precision (Macro Avg)", "Recall (Macro Avg)", "F1-Score (Macro Avg)"],
    "Value": [0.7642585551330798, 0.77, 0.77, 0.76]
}
decision_tree_table = pd.DataFrame(decision_tree_results)

# Display the table
print(decision_tree_table)

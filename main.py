import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
import os

# Ensure the resources directory exists
os.makedirs("resources", exist_ok=True)

# 1. Load and Preprocess Data





def load_data():
    """
    Load the Heart Disease dataset from a local CSV file.
    Preprocess and return the features and target variables.
    """
    df = pd.read_csv("heart.csv")  # Update path as necessary

    # Drop unnecessary columns (e.g., 'dataset' or any identifiers)
    if 'dataset' in df.columns:
        df = df.drop(columns=['dataset'])

    # Encode categorical columns
    categorical_cols = df.select_dtypes(include=['object']).columns
    le = LabelEncoder()
    for col in categorical_cols:
        df[col] = le.fit_transform(df[col])

    # Handle missing values
    imputer = SimpleImputer(strategy='mean')  # Replace NaN with column mean
    df = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

    # Features and target
    X = df.drop(columns=["num"])  # Drop the target column
    y = df["num"]

    # Normalize numeric features
    numeric_cols = X.select_dtypes(include=np.number).columns
    X[numeric_cols] = (X[numeric_cols] - X[numeric_cols].mean()) / X[numeric_cols].std()

    return train_test_split(X, y, test_size=0.2, random_state=42)



# 2. Causal Inference
class CausalGraph:
    def __init__(self):
        self.graph = {
            "Age": ["HeartDisease"],
            "Cholesterol": ["HeartDisease"],
            "ExerciseInducedAngina": ["HeartDisease"]
        }

    def estimate_causal_effect(self, intervention, outcome):
        if intervention == "Cholesterol" and outcome == "HeartDisease":
            return -0.3  # Hypothetical causal effect for demonstration
        return 0

    def simulate_counterfactual(self, original, intervention):
        if intervention.get("Cholesterol") < original["Cholesterol"]:
            return "Reduced heart disease risk due to lower cholesterol"
        return "No significant change"

# 3. Neural Network
class NeuralNetwork:
    def __init__(self):
        self.model = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000, random_state=42)

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

# 4. Visualization
def plot_causal_graph():
    """
    Visualize the causal graph as a Directed Acyclic Graph (DAG).
    """
    plt.figure(figsize=(10, 12))
    plt.title("Causal Graph", fontsize=16)
    plt.text(0.5, 0.8, "Age", fontsize=14, ha='center', bbox=dict(facecolor='lightblue'))
    plt.text(0.3, 0.5, "Cholesterol", fontsize=14, ha='center', bbox=dict(facecolor='lightgreen'))
    plt.text(0.7, 0.5, "Exercise Angina", fontsize=14, ha='center', bbox=dict(facecolor='lightcoral'))
    plt.text(0.5, 0.2, "Heart Disease", fontsize=14, ha='center', bbox=dict(facecolor='red'))

    # Arrows
    plt.arrow(0.5, 0.75, 0, -0.3, head_width=0.02, head_length=0.03, fc='black', ec='black')
    plt.arrow(0.3, 0.45, 0.2, -0.2, head_width=0.02, head_length=0.03, fc='black', ec='black')
    plt.arrow(0.7, 0.45, -0.2, -0.2, head_width=0.02, head_length=0.03, fc='black', ec='black')

    plt.axis('off')
    plt.savefig("resources/enhanced_causal_graph.png")
    plt.close()

def plot_counterfactuals(original_prob, counterfactual_prob):
    """
    Enhanced counterfactual analysis visualization.
    Displays probabilities of heart disease for original and counterfactual scenarios.
    """
    scenarios = ["Original", "Counterfactual"]
    probabilities = [original_prob, counterfactual_prob]

    plt.figure(figsize=(10, 12))
    bars = plt.bar(scenarios, probabilities, color=['blue', 'orange'])

    # Add annotations
    for bar, prob in zip(bars, probabilities):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 0.05,
                 f"{prob:.2f}", ha='center', va='bottom', fontsize=12, color='white')

    plt.title("Counterfactual Analysis: Heart Disease Risk", fontsize=14)
    plt.ylabel("Probability of Heart Disease", fontsize=12)
    plt.ylim(0, 1.2)  # To provide space for annotations
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.savefig("resources/enhanced_counterfactual_analysis.png")
    plt.show()

# Main Function
def main():
    # Step 1: Load data
    X_train, X_test, y_train, y_test = load_data()

    # Step 2: Define causal graph
    causal_graph = CausalGraph()
    plot_causal_graph()

    # Step 3: Estimate causal effects
    effect = causal_graph.estimate_causal_effect("Cholesterol", "HeartDisease")
    print(f"Causal Effect of Cholesterol on Heart Disease: {effect}")

    # Step 4: Train neural network
    nn = NeuralNetwork()
    nn.train(X_train, y_train)
    y_pred = nn.predict(X_test)

    # Evaluate neural network
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Neural Network Accuracy: {accuracy:.2f}")

    # Step 5: Simulate counterfactual
    original = {"Cholesterol": 250, "Age": 60, "ExerciseInducedAngina": 1}
    intervention = {"Cholesterol": 180}
    counterfactual_result = causal_graph.simulate_counterfactual(original, intervention)

    # Visualize counterfactual
    plot_counterfactuals(0.8, 0.5)  # Example probabilities for visualization

if __name__ == "__main__":
    main()


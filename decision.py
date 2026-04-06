import sympy
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from dtreeviz import model as dtreeviz_model

# ------------------ SYMPY PART ------------------
p, q, r = sympy.symbols('p q r')

prop1 = p
prop2 = sympy.Not(q)
prop3 = sympy.And(p, q)
prop4 = sympy.Or(p, q)

prop5 = sympy.Implies(p, q)
prop6 = sympy.Equivalent(p, q)

prop19 = sympy.And(p, sympy.Or(q, r))

def is_valid(proposition):
    return all(
        proposition.subs({p: p_val, q: q_val})
        for p_val in [True, False]
        for q_val in [True, False]
    )

print("Validity:")
print(is_valid(prop1), is_valid(prop2), is_valid(prop3))

# ------------------ ML PART ------------------

# Load dataset
data = load_iris()
X = data.data
y = data.target

# Create DataFrame
df = pd.DataFrame(X, columns=data.feature_names)
df['target'] = y

print(df.head())
print("___________________________________________")

# Class-wise filtering
setosa_data = df[df['target'] == 0]
versicolor_data = df[df['target'] == 1]
virginica_data = df[df['target'] == 2]

print("Setosa:")
print(setosa_data.head(3))

print("Versicolor:")
print(versicolor_data.head(3))

print("Virginica:")
print(virginica_data.head(3))

# Binary classification (virginica vs others)
y_binary = (y == 2).astype(int)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y_binary, test_size=0.3, random_state=42
)

# Train model
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Predict
y_pred = clf.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

print("___________________________________________")

# Visualization
viz = dtreeviz_model(
    clf,
    X_train,
    y_train,
    target_name='target',
    feature_names=data.feature_names,
    class_names=['not virginica', 'virginica']
)

viz.view()

import os
import argparse
import numpy as np
import pandas as pd
import joblib

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.metrics import classification_report, recall_score, roc_auc_score, average_precision_score

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)

def load_data(csv_path: str | None) -> tuple[pd.DataFrame, pd.Series]:
    if csv_path:
        df = pd.read_csv(csv_path)
        if "diagnostico" not in df.columns:
            raise ValueError("CSV deve conter a coluna 'diagnostico' (1=maligno, 0=benigno).")
        X = df.drop(columns=["diagnostico"])
        y = df["diagnostico"].astype(int)
        return X, y

    data = load_breast_cancer(as_frame=True)
    df = data.frame.copy().rename(columns={"target": "diagnostico"})
    # sklearn: 0=malignant, 1=benign -> padroniza: 1=maligno, 0=benigno
    df["diagnostico"] = (df["diagnostico"].astype(int) == 0).astype(int)
    X = df.drop(columns=["diagnostico"])
    y = df["diagnostico"]
    return X, y

def build_pipelines(random_state: int):
    preprocess = [("imputer", SimpleImputer(strategy="median"))]
    return {
        "LogisticRegression": Pipeline(preprocess + [
            ("scaler", StandardScaler()),
            ("model", LogisticRegression(C=1.0, max_iter=2000, random_state=random_state))
        ]),
        "KNN": Pipeline(preprocess + [
            ("scaler", StandardScaler()),
            ("model", KNeighborsClassifier(n_neighbors=7, weights="distance"))
        ]),
        "DecisionTree": Pipeline(preprocess + [
            ("model", DecisionTreeClassifier(max_depth=5, random_state=random_state))
        ]),
        "RandomForest": Pipeline(preprocess + [
            ("model", RandomForestClassifier(n_estimators=120, max_depth=None, n_jobs=-1, random_state=random_state))
        ]),
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", default=None, help="Caminho opcional para CSV com coluna 'diagnostico'.")
    parser.add_argument("--out", default="artifacts/model.joblib", help="Caminho do artefato de saída.")
    args = parser.parse_args()

    X, y = load_data(args.csv)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=RANDOM_STATE, stratify=y
    )
    X_tr, X_val, y_tr, y_val = train_test_split(
        X_train, y_train, test_size=0.25, random_state=RANDOM_STATE, stratify=y_train
    )

    pipelines = build_pipelines(RANDOM_STATE)

    # Seleção rápida por recall na validação
    best_name, best_est, best_val_recall = None, None, -1.0
    for name, est in pipelines.items():
        est.fit(X_tr, y_tr)
        val_pred = est.predict(X_val)
        r = recall_score(y_val, val_pred)
        if r > best_val_recall:
            best_val_recall = float(r)
            best_name, best_est = name, est

    print(f"Modelo escolhido (val recall): {best_name} | recall_val={best_val_recall:.4f}")

    # Treina no treino completo e avalia no teste
    best_est.fit(X_train, y_train)
    y_pred = best_est.predict(X_test)

    print(classification_report(y_test, y_pred, target_names=["benigno(0)", "maligno(1)"]))

    if hasattr(best_est, "predict_proba"):
        proba = best_est.predict_proba(X_test)[:, 1]
        print(f"ROC-AUC: {roc_auc_score(y_test, proba):.4f}")
        print(f"PR-AUC (avg precision): {average_precision_score(y_test, proba):.4f}")

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    joblib.dump(best_est, args.out)
    print(f"Artefato salvo em: {args.out}")

if __name__ == "__main__":
    main()

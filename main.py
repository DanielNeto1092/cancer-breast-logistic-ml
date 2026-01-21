import argparse
import pandas as pd
import joblib
import sys

def main():
    parser = argparse.ArgumentParser(description="Inferência de câncer de mama (classificação)")
    parser.add_argument(
        "--model",
        default="artifacts/model.joblib",
        help="Caminho do modelo treinado (.joblib)"
    )
    parser.add_argument(
        "--input",
        required=True,
        help="CSV de entrada (apenas features, sem coluna diagnosis/target)"
    )
    parser.add_argument(
        "--output",
        default="predicoes.csv",
        help="CSV de saída com predições"
    )
    args = parser.parse_args()

    # Carregar modelo
    try:
        model = joblib.load(args.model)
    except Exception as e:
        print(f"Erro ao carregar modelo: {e}")
        sys.exit(1)

    # Ler dados de entrada
    try:
        X = pd.read_csv(args.input)
    except Exception as e:
        print(f"Erro ao ler CSV de entrada: {e}")
        sys.exit(1)

    if X.empty:
        print("Erro: CSV de entrada está vazio.")
        sys.exit(1)

    # Predição
    try:
        pred = model.predict(X)
    except Exception as e:
        print(f"Erro durante a predição: {e}")
        sys.exit(1)

    out = X.copy()
    out["pred_maligno"] = pred
    out["pred_label"] = out["pred_maligno"].map({0: "Benigno", 1: "Maligno"})

    # Probabilidade (se disponível)
    if hasattr(model, "predict_proba"):
        try:
            out["proba_maligno"] = model.predict_proba(X)[:, 1]
        except Exception:
            pass

    out.to_csv(args.output, index=False)
    print(f"Arquivo gerado com sucesso: {args.output}")

if __name__ == "__main__":
    main()

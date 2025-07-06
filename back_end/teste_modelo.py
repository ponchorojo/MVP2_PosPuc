import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def test_model_metrics():
    # Carregar modelo e dados de teste
    modelo = joblib.load("modelo/modelo_treinado.pkl")
    dados = pd.read_csv("modelo/dados_teste.csv")

    # Separar features e target
    X = dados.drop("Loan_Status", axis=1)
    y = dados["Loan_Status"]
    y_pred = modelo.predict(X)

    # Calcular métricas
    acc = float(accuracy_score(y, y_pred))
    precision = float(precision_score(y, y_pred))
    recall = float(recall_score(y, y_pred))
    f1 = float(f1_score(y, y_pred))

    # Exibir métricas
    print(f"Acurácia: {acc:.4f}")
    print(f"Precisão: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1-score: {f1:.4f}")

    # Thresholds
    MIN_ACC = 0.7
    MIN_PRECISION = 0.7
    MIN_RECALL = 0.7
    MIN_F1 = 0.7

    # Verificações
    assert acc >= MIN_ACC, f"Acurácia abaixo do mínimo: {acc:.2f}"
    assert precision >= MIN_PRECISION, f"Precisão abaixo do mínimo: {precision:.2f}"
    assert recall >= MIN_RECALL, f"Recall abaixo do mínimo: {recall:.2f}"
    assert f1 >= MIN_F1, f"F1-score abaixo do mínimo: {f1:.2f}"

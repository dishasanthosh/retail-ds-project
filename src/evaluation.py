from sklearn.metrics import classification_report, roc_auc_score # type: ignore

def evaluate_classifier(model, X_test, y_test):
    pred = model.predict(X_test)
    proba = model.predict_proba(X_test)[:, 1]

    print(classification_report(y_test, pred))
    print("ROC-AUC:", roc_auc_score(y_test, proba))
from lab6_intelligent_search.bayesian.disease_network import get_bayesian_inference

def query_disease_probability(evidence: dict):
    inference = get_bayesian_inference()
    # Ejecuta la consulta por eliminación de variables
    result = inference.query(variables=['Disease'], evidence=evidence)
    
    return {
        "probabilities": {
            "No Disease (0)": float(result.values[0]),
            "Has Disease (1)": float(result.values[1])
        }
    }
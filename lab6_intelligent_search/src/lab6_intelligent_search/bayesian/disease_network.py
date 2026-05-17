from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

def get_bayesian_inference():
    # Estructura de la red bayesiana
    model = BayesianNetwork([
        ('Disease', 'Fever'),
        ('Disease', 'Test')
    ])

    # Modificado ligeramente a flotantes estándar para evitar problemas de tipos
    cpd_disease = TabularCPD(variable='Disease', variable_card=2, values=[[0.1], [0.9]])

    cpd_fever = TabularCPD(
        variable='Fever', variable_card=2,
        values=[[0.8, 0.2], [0.2, 0.8]],
        evidence=['Disease'], evidence_card=[2]
    )

    cpd_test = TabularCPD(
        variable='Test', variable_card=2,
        values=[[0.9, 0.1], [0.1, 0.9]],
        evidence=['Disease'], evidence_card=[2]
    )

    model.add_cpds(cpd_disease, cpd_fever, cpd_test)
    return VariableElimination(model)
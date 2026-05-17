from fastapi import FastAPI
from lab6_intelligent_search.models.route_models import RouteRequest
from lab6_intelligent_search.services.search_service import find_route
from lab6_intelligent_search.services.bayesian_service import query_disease_probability

app = FastAPI(title="API de Sistemas Inteligentes - Jesús Ramos")

@app.post('/find-route')
def search_route(request: RouteRequest):
    return find_route(request.start, request.goal)

@app.get('/bayesian-query')
def bayesian_query(has_fever: int, test_positive: int):
    # Procesa la evidencia (0 = Falso, 1 = Verdadero)
    evidence = {}
    if has_fever in [0, 1]: evidence['Fever'] = has_fever
    if test_positive in [0, 1]: evidence['Test'] = test_positive
        
    return query_disease_probability(evidence)
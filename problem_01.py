import cvxpy as cp

# Definir variáveis de decisão
LA = cp.Variable(integer=True)
LB = cp.Variable(integer=True)

# Função objetivo: maximizar o lucro
profit = 30 * LA + 10 * LB
objective = cp.Maximize(profit)

# Restrições
constraints = [
    20 * LA + 55 * LB <= 720,  # Transistores
    30 * LA + 15 * LB <= 540,  # Amplificadores operacionais
    0.8 * LA - 0.2 * LB >= 0,  # Proporção mínima de placas A
    0.8 * LB - 0.2 * LA >= 0,  # Proporção mínima de placas B
    LA >= 0,                   # Não negatividade de LA
    LB >= 0                    # Não negatividade de LB
]

# Definir e resolver o problema
problem = cp.Problem(objective, constraints)
problem.solve()

# Resultado ótimo
LA_opt = LA.value
LB_opt = LB.value
profit_opt = profit.value

LA_opt, LB_opt, profit_opt
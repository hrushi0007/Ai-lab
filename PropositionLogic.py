import sympy

# Define propositional variables
p, q, r = sympy.symbols('p q r')

# Define propositions
prop1 = p
prop2 = sympy.Not(q)
prop3 = sympy.And(p, q)
prop4 = sympy.Or(p, q)

# Additional propositions
prop5 = sympy.Implies(p, q)     # p → q
prop6 = sympy.Equivalent(p, q)  # p ↔ q

# Example distributive law: p ∧ (q ∨ r)
prop19 = sympy.And(p, sympy.Or(q, r))

# Function to check validity (tautology)
def is_valid(proposition):
    return all(
        proposition.subs({p: p_val, q: q_val})
        for p_val in [True, False]
        for q_val in [True, False]
    )

# Check validity
print("Validity:")
print(f"prop1 valid? {is_valid(prop1)}")
print(f"prop2 valid? {is_valid(prop2)}")
print(f"prop3 valid? {is_valid(prop3)}")
print(f"prop4 valid? {is_valid(prop4)}")
print(f"prop5 valid? {is_valid(prop5)}")
print(f"prop6 valid? {is_valid(prop6)}")

# Check satisfiability
print("\nSatisfiability:")
print(f"prop1 satisfiable? {sympy.satisfiable(prop1)}")
print(f"prop2 satisfiable? {sympy.satisfiable(prop2)}")
print(f"prop3 satisfiable? {sympy.satisfiable(prop3)}")
print(f"prop4 satisfiable? {sympy.satisfiable(prop4)}")

# Check entailment (p → ¬q)
entailment = sympy.Implies(prop1, prop2)
print(f"\nDoes prop1 entail prop2? {entailment}")

# Define more propositions for CNF/DNF
prop13 = sympy.Or(p, q, r)
prop14 = sympy.And(p, q, r)

# Convert to DNF and CNF
print("\nDNF & CNF:")
print(f"prop13 in DNF: {sympy.to_dnf(prop13)}")
print(f"prop13 in CNF: {sympy.to_cnf(prop13)}")
print(f"prop14 in DNF: {sympy.to_dnf(prop14)}")
print(f"prop14 in CNF: {sympy.to_cnf(prop14)}")

# Distributive law example evaluation
print("\nDistributive Law Example:")
for p_val in [True, False]:
    for q_val in [True, False]:
        for r_val in [True, False]:
            result = prop19.subs({p: p_val, q: q_val, r: r_val})
            print(f"p={p_val}, q={q_val}, r={r_val} => {result}")

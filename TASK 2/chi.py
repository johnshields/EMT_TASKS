from scipy.stats import chi2_contingency

# cotingency table
obs =[90, 60, 104 ,95],[30, 50, 51, 20],[30, 40, 45, 35]

# ***g = chi2***
g, p, dof, expctd = chi2_contingency(obs)

# results
print("RESULTS:\n")
# results
print("RESULTS:\n")
print("Expected:")
print(expctd)
print(" ")
print("Chi2:")
print(g)
print(" ")
print("Degree of Freedom:")
print(dof)
print(" ")
print("P value:")
print(p)
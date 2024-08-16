# Does the patient have cancer or not?
# P(cancer) = 0.008, P(not cancer) = 0.992, these are called prior probabilities
# P(+ | cancer) = 0.98 P(- | cancer) = 0.02
# P(+ | not cancer) = 0.03 P(- | not cancer) = 0.97
# P1 = P(not cancer | +) = P(+ | not cancer) * P(not cancer)
# P2 = P(cancer | +) = P(+ | cancer) * P(cancer)
# p = P1/P2

P1 = 0.992 * 0.03
P2 = 0.008 * 0.98
p = P1/P2
print("P1: ", P1)
print("P2: ", P2)
print(p)
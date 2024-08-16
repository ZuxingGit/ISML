# calculate Precision, Recall, F1 score, and Accuracy
# for the following confusion matrix
TP = 10
FP = 10 
FN = 30
TN = 50

# Precision = TP / (TP + FP)
precision = TP / (TP + FP)
# Recall = TP / (TP + FN)
recall = TP / (TP + FN)
# F1 score = 2 * (Precision * Recall) / (Precision + Recall)
f1_score = 2 * (precision * recall) / (precision + recall)

# Accuracy = (TP + TN) / (TP + FP + FN + TN)
accuracy = (TP + TN) / (TP + FP + FN + TN)

print(f'Precision: {precision}')
print(f'Recall: {recall}')
print(f'F1 score: {f1_score}')
print(f'Accuracy: {accuracy}')
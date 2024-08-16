# calculate the area under curve AUC for precision/recall (AUC PRC) using average precision (AP) method
# AP = Σ (Rn - Rn-1) * Pn

import numpy as np

def calculate_auc_prc(precision, recall):
    # calculate the area under curve AUC for precision/recall (AUC PRC) using average precision (AP) method
    AP = 0
    for i in range(1, len(precision)):
        AP += (recall[i] - recall[i-1]) * precision[i]
    return AP

recall = np.array([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
precision = np.array([1.0, 0.9, 0.8, 0.5, 0.4, 0.3])
AP = calculate_auc_prc(precision, recall)
print(AP) # 0.58
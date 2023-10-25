#Vaues 
true_positives = 243
false_positives = 73
false_negatives = 157
true_negatives = 778

# Calculate precision as a percentage
precision = (true_positives / (true_positives + false_positives)) * 100

# Calculate recall as a percentage
recall = (true_positives / (true_positives + false_negatives)) * 100

# Calculate F1-score as a percentage
f1_score = (2 * (precision * recall) / (precision + recall))

# Calculate accuracy as a percentage
accuracy = ((true_positives + true_negatives) / (true_positives + false_positives + false_negatives + true_negatives)) * 100

# Print the results as percentages
print(f"Precision: {precision:.2f}%")
print(f"Recall: {recall:.2f}%")
print(f"F1-Score: {f1_score:.2f}%")
print(f"Accuracy: {accuracy:.2f}%")

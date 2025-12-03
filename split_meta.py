import random

input_path = "datasets_small/metadata.csv"
train_path = "datasets_small/metadata.csv"
val_path = "datasets_small/metadata_val.csv"

with open(input_path, "r", encoding="utf-8") as f:
    lines = [l.strip() for l in f.readlines() if l.strip()]

random.shuffle(lines)

split_index = int(len(lines) * 0.9)
train_lines = lines[:split_index]
val_lines = lines[split_index:]

with open(train_path, "w", encoding="utf-8") as f:
    f.write("\n".join(train_lines))

with open(val_path, "w", encoding="utf-8") as f:
    f.write("\n".join(val_lines))

print("Split complete!")
print(f"Training lines: {len(train_lines)}")
print(f"Validation lines: {len(val_lines)}")

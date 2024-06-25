# Define the preproinsulin sequence
preproinsulin_seq = (
ORIGIN      
        1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed
       61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn
//
)

# Function to check if all characters in the sequence are lowercase
def is_all_lowercase(seq):
    return all(c.islower() for c in seq)
print("\n")

# Save the full sequence to preproinsulin-seq-clean.txt
with open('preproinsulin-seq-clean.txt', 'w') as file:
    file.write(preproinsulin_seq)
print("Saved full sequence to preproinsulin-seq-clean.txt:")
print(preproinsulin_seq)
print

# Verify that the sequence contains only lowercase letters
assert is_all_lowercase(preproinsulin_seq), "The sequence should contain only lowercase letters."
print("Verified that the full sequence contains only lowercase letters")
print("\n")

# Extract and save the first 24 amino acids
lsinsulin_seq = preproinsulin_seq[:24]
with open('lsinsulin-seq-clean.txt', 'w') as file:
    file.write(lsinsulin_seq)
print("Saved first 24 amino acids to lsinsulin-seq-clean.txt:")
print(lsinsulin_seq)
assert is_all_lowercase(lsinsulin_seq), "The lsinsulin sequence should contain only lowercase letters."
print("Verified that the lsinsulin sequence contains only lowercase letters")
print("\n")

# Extract and save the next 30 amino acids (25-54)
binsulin_seq = preproinsulin_seq[24:54]
with open('binsulin-seq-clean.txt', 'w') as file:
    file.write(binsulin_seq)
print("Saved next 30 amino acids to binsulin-seq-clean.txt:")
print(binsulin_seq)
assert is_all_lowercase(binsulin_seq), "The binsulin sequence should contain only lowercase letters."
print("Verified that the binsulin sequence contains only lowercase letters")
print("\n")

# Extract and save the next 35 amino acids (55-89)
cinsulin_seq = preproinsulin_seq[54:89]
with open('cinsulin-seq-clean.txt', 'w') as file:
    file.write(cinsulin_seq)
print("Saved next 35 amino acids to cinsulin-seq-clean.txt:")
print(cinsulin_seq)
assert is_all_lowercase(cinsulin_seq), "The cinsulin sequence should contain only lowercase letters."
print("Verified that the cinsulin sequence contains only lowercase letters")
print("\n")

# Extract and save the last 21 amino acids (90-110)
ainsulin_seq = preproinsulin_seq[89:]
with open('ainsulin-seq-clean.txt', 'w') as file:
    file.write(ainsulin_seq)
print("Saved last 21 amino acids to ainsulin-seq-clean.txt:")
print(ainsulin_seq)
assert is_all_lowercase(ainsulin_seq), "The ainsulin sequence should contain only lowercase letters."
print("Verified that the ainsulin sequence contains only lowercase letters")
print("\n")

# Verify lengths
assert len(preproinsulin_seq) == 110, "The full sequence should have 110 characters."
assert len(lsinsulin_seq) == 24, "The lsinsulin sequence should have 24 characters."
assert len(binsulin_seq) == 30, "The binsulin sequence should have 30 characters."
assert len(cinsulin_seq) == 35, "The cinsulin sequence should have 35 characters."
assert len(ainsulin_seq) == 21, "The ainsulin sequence should have 21 characters."
print("\n")
print("All sequences have the correct lengths and contain only lowercase letters.")

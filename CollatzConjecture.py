import matplotlib.pyplot as plt

# Kullanıcıdan bir sayı al
number = int(input("Enter a number: "))

def collatz_sequence(number):
    sequence = [number]
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1
        sequence.append(number)
    return sequence

# Collatz dizisini hesapla
sequence = collatz_sequence(number)

# Grafik çiz
plt.figure(figsize=(10, 6))  # Grafik boyutları
plt.plot(sequence, marker='o', linestyle='-', color='b', label=f"Start: {number}")
plt.title("Collatz Conjecture Visualization", fontsize=14)
plt.xlabel("Steps", fontsize=12)
plt.ylabel("Value", fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

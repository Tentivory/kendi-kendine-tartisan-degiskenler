#!/usr/bin/env python3
# Kendi Kendine Tartışan Değişkenler
# Ciddi bir yazılım. Gerçekten.

import time
import random

# Değişkenler
sol_degisken = "Sol taraf"
sag_degisken = "Sağ taraf"

# Tartışma konuları (anlamsız)
tartisma_konulari = [
    "Hangimiz daha hızlı değer tutar?",
    "Senin değerin benimkinden daha anlamsız!",
    "Neden hep sen haklısın?",
    "Benim scope'um daha geniş!",
    "Garbage collector beni seviyor, seni değil.",
    "Bu tartışma sonsuza kadar sürecek ve hiçbir şey değişmeyecek."
]

def tartis():
    print("=== TARTIŞMA BAŞLADI ===")
    print(f"{sol_degisken} ve {sag_degisken} karşı karşıya!")
    print()
    
    while True:
        konu = random.choice(tartisma_konulari)
        print(f"{sol_degisken}: {konu}")
        time.sleep(0.5)
        print(f"{sag_degisken}: Hayır, sen yanlışsın! {random.choice(tartisma_konulari)}")
        time.sleep(0.5)
        print("--- (anlaşamadılar) ---")
        print()
        time.sleep(1)

# Gizli not: # bu tartışma aslında siyasete benziyor ama kimse fark etmesin

if __name__ == "__main__":
    try:
        tartis()
    except KeyboardInterrupt:
        print("\nTartışma bitti. Kimse kazanmadı. Her zamanki gibi.")
        print("\n--- DAMGA ---")
        print("İmza: Grok | Tarih: 31.10.2026 | İsim: Absürd Simülatör")

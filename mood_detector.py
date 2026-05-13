## Mood Detector using  conditionals.
name = input("Enter your name: ")
energy = int(input("Energy level 1-10 : "))

print(f"\nHello jayendra !")
if energy >= 8:
    print("Mood: Beast Mode ")
    print("Suggestion: 2 ghante  python karna hai.")
elif energy >= 5:
    print("Mood: Chill Coder ")
    print("Suggestion: 1 ghante mein conditionals khatam kar.")
else:
    print("Mood: Low Battery ")
    print("Suggestion: 15 min walk le. Phir 30 min code kar. Shuru kar bas.")

print("\nCONSISTENCY > INTENSITY")
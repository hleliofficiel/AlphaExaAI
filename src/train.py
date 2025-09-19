import time
import random

def main():
    print("Starting AlphaExaAI training simulation...")
    for epoch in range(1, 6):
        loss = round(random.uniform(0.1, 1.0), 4)
        print(f"[Epoch {epoch}] Training... Loss={loss}")
        time.sleep(1)
    print("Training finished. Checkpoints saved!")

if __name__ == "__main__":
    main()

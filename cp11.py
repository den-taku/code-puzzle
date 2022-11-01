if __name__ == "__main__":
    for i in range(1, 10000):
        if pow(i, 17) % 3569 == 915:
            print(f"answer: {i}")
            break

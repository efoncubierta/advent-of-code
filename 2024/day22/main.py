with open("input.txt", "r") as f:
    secrets = [int(n) for n in f.read().split("\n")]

N = 2000

final_secrets = {}
for s in secrets:
    secret = s
    prices = []
    for _ in range(N):
        secret = (secret ^ (secret * 64)) % 16777216
        secret = (secret ^ (secret // 32)) % 16777216
        secret = (secret ^ (secret * 2048)) % 16777216
        prices.append(secret % 10)
    final_secrets[secret] = prices

print("Part 1:", sum(final_secrets.keys()))

seqs = {}
for prices in final_secrets.values():
    changes = [prices[i] - prices[i - 1] for i in range(1, len(prices))]

    seen = set()
    for i in range(len(changes) - 3):
        seq = tuple(changes[i:i + 4])
        if seq not in seen:
            seen.add(seq)
            seqs[seq] = prices[i + 4] if seq not in seqs else seqs[seq] + prices[i + 4]

print("Part 2:", seqs[max(seqs, key=seqs.get)])
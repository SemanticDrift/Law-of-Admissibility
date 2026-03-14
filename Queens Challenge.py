import numpy as np

def dynamical_signal_test(k=4, n_steps=64, trials=100):
    """
    Measures how quickly a recursive system stops resembling
    its initial state.

    - k:       memory depth
    - n_steps: steps to generate
    - trials:  runs to average
    """
    results = []

    for _ in range(trials):
        signal = list(np.random.randn(k))

        for i in range(k, n_steps):
            new_val = sum(signal[-k:]) / k + 0.1 * np.random.randn()
            signal.append(new_val)

        initial = np.array(signal[:k])
        corrs   = []

        for n in range(k, n_steps):
            current = np.array(signal[n-k:n])
            if np.std(initial) == 0 or np.std(current) == 0:
                corr = 0
            else:
                corr = np.corrcoef(initial, current)[0, 1]
            corrs.append(corr)

        results.append(corrs)

    return np.mean(results, axis=0)

# Run for k = 2 through k = 10
family_names = {
    2: "Fibonacci",  3: "Trinacci",   4: "Tetranacci",
    5: "Pentanacci", 6: "Hexanacci",  7: "Heptanacci",
    8: "Octanacci",  9: "Nonanacci",  10: "Decanacci"
}

for k in range(2, 11):
    avg = dynamical_signal_test(k=k, trials=100)
    idx_2k = k
    idx_4k = 3 * k
    if len(avg) > idx_4k:
        print(f"{family_names[k]:10} k={k}: "
              f"ACF@2k={avg[idx_2k]:.4f}  "
              f"ACF@4k={avg[idx_4k]:.4f}")

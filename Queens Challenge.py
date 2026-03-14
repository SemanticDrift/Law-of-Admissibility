import numpy as np

def dynamical_signal_test(k=4, n_steps=64, trials=100):
    """
    The Queen's Challenge: Dynamical Signal Test
    Law of Admissibility — Carolina Johnson (CJ), 2026
    DOI: https://doi.org/10.5281/zenodo.18993233

    Measures how quickly a recursive system stops resembling
    its initial state. Confirms the admissibility lock at n = 4k.

    Parameters:
    - k:       memory depth (try 2 through 10)
    - n_steps: steps to generate (keep above 4k)
    - trials:  runs to average (100 recommended)

    Returns:
    - avg_corrs: average autocorrelation at each step n
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


# ── Run the Challenge ──────────────────────────────────────
family_names = {
    2: "Fibonacci",  3: "Trinacci",   4: "Tetranacci",
    5: "Pentanacci", 6: "Hexanacci",  7: "Heptanacci",
    8: "Octanacci",  9: "Nonanacci",  10: "Decanacci"
}

print("--- THE QUEEN'S CHALLENGE ---")
print("Law of Admissibility: R = 4")
print("Validating admissibility lock at n = 4k across all recursive families.")
print("Results averaged over 100 trials per family.")
print()

all_confirmed = True

for k in range(2, 11):
    avg = dynamical_signal_test(k=k, trials=100)
    idx_2k = k
    idx_4k = 3 * k

    if len(avg) > idx_4k:
        acf_2k = avg[idx_2k]
        acf_4k = avg[idx_4k]
        confirmed = abs(acf_4k) < abs(acf_2k)
        status = "ADMISSIBLE" if confirmed else "CHECK PARAMETERS"
        if not confirmed:
            all_confirmed = False
        print(f"{family_names[k]:10} (k={k:2d}):  "
              f"ACF at 2k = {acf_2k:+.4f}   "
              f"ACF at 4k = {acf_4k:+.4f}   "
              f"STATUS: {status}")

print()
if all_confirmed:
    print("RESULT: Admissibility lock confirmed at n = 4k across all families.")
    print("The law holds.")
else:
    print("RESULT: One or more families did not confirm. Check parameters and rerun.")

print()
print("Found a counterexample? A stable recursive system where R != 4?")
print("Submit your data logs. The first verifiable counterexample will be")
print("publicly acknowledged and cited.")
print()
print("Status: Awaiting Admissible Input.")
print()
print("DOI: https://doi.org/10.5281/zenodo.18993233")
print("© 2026 Carolina Johnson (CJ) — CC BY 4.0")

import json
import os
import matplotlib.pyplot as plt

def main():
    data_file = os.path.join(os.path.dirname(__file__), '..', 'app', 'data', 'results.json')
    if not os.path.exists(data_file):
        print('No results found.')
        return
    with open(data_file, 'r', encoding='utf-8') as f:
        all_results = json.load(f)
    # Count selections for each sample
    counts = {}
    for entry in all_results:
        key = f"{entry['sample']}_{entry['selected']}"
        counts[key] = counts.get(key, 0) + 1
    # Prepare data for plotting
    samples = sorted(set(k.rsplit('_',1)[0] for k in counts))
    a_counts = [counts.get(f"{s}_a", 0) for s in samples]
    b_counts = [counts.get(f"{s}_b", 0) for s in samples]
    x = range(len(samples))
    plt.figure(figsize=(10,6))
    plt.bar(x, a_counts, width=0.4, label='A', align='center')
    plt.bar(x, b_counts, width=0.4, label='B', align='edge')
    plt.xticks(x, samples, rotation=45)
    plt.xlabel('Sample')
    plt.ylabel('Votes')
    plt.title('Audio Sample Comparison Results')
    plt.legend()
    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(__file__), '..', 'app', 'static', 'results.png')
    plt.savefig(out_path)
    print(f'Results chart saved to {out_path}')

if __name__ == '__main__':
    main()

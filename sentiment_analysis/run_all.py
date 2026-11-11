"""
Run the complete pipeline: generate data → train model → save results.
"""

import subprocess
import sys
import time


def run_step(step_num, description, script):
    print(f"\n{'='*60}")
    print(f"  Step {step_num}: {description}")
    print(f"{'='*60}\n")
    start = time.time()
    result = subprocess.run([sys.executable, script], check=True)
    elapsed = time.time() - start
    print(f"\n  [OK] Step {step_num} completed in {elapsed:.1f}s")
    return result.returncode


def main():
    print("=" * 60)
    print("  Autonomous Bus Sentiment Analysis — Full Pipeline")
    print("=" * 60)

    overall_start = time.time()

    run_step(1, "Generating synthetic dataset", "data_collector.py")
    run_step(2, "Training & evaluating models", "train_model.py")

    total = time.time() - overall_start
    print(f"\n{'='*60}")
    print(f"  All steps completed in {total:.1f}s")
    print(f"{'='*60}")
    print(f"\n  Generated files:")
    print(f"    data/opinions.csv          — 1200 synthetic opinions")
    print(f"    models/best_model.joblib   — trained model")
    print(f"    models/vectorizer.joblib   — TF-IDF vectorizer")
    print(f"    results/*.png              — charts and word clouds")
    print(f"    results/classification_report.txt")
    print(f"\n  Next: run the demo app with:")
    print(f"    streamlit run app.py")
    print()


if __name__ == "__main__":
    main()

import argparse
import pathlib
import random
import subprocess
import sys

def main():
    parser = argparse.ArgumentParser(
        description="Simplified interface to the samtools downsampling algorithm."
    )
    parser.add_argument("downsample_to", type=int, help="How many reads to downsample to.")
    parser.add_argument("file", type=pathlib.Path, help="Path to BAM file.")
    parser.add_argument("--seed", type=int, default=random.randint(1, 1000000000000), help="Seed for the downsampling.")
    args = parser.parse_args()

    count_output = subprocess.run(
        ["samtools", "view", "-c", args.file],
        check=True,
        stdout=subprocess.PIPE,
        text=True
    )
    count = int(count_output.stdout)

    if args.downsample_to > count:
        print(
            f"Can't downsample to {args.downsample_to}. File only has {count} reads.",
            file=sys.stderr
        )
        sys.exit(1)

    ratio = float(args.downsample_to) / count
    subsample_value = args.seed + ratio

    subsample_flag = f"-s {subsample_value}"

    subprocess.run(["samtools", "view", "-b", subsample_flag, args.file])

if __name__ == "__main__":
    main()

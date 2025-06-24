import time
from monitor import run_monitor


def main():
    print("=== Sensor System Simulation Started ===")

    for _ in range(30):  # Run 5 monitoring cycles
        run_monitor()
        print("-" * 40)
        time.sleep(1)  # Wait 2 seconds between cycles

    print("=== Simulation Complete ===")


if __name__ == "__main__":
    main()
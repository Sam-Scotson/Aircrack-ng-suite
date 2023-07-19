#airSuite-ng
import subprocess
import logging
import concurrent.futures

# Set up logging configuration
logging.basicConfig(
    filename="scan_results.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def execute_scan(command, scan_name):
    try:
        output = subprocess.check_output(command)
        result = output.decode("utf-8")
        logging.info(f"{scan_name} results:\n{result}")
    except Exception as e:
        logging.error(f"Error executing {scan_name} or saving results: {str(e)}")

if __name__ == "__main__":
    commands = {
        "aircrack-ng": ["aircrack-ng", "-v"],
        "airbase-ng": ["airbase-ng", "-v"],
        "aireplay-ng": ["aireplay-ng", "-v"],
        "airmon-ng": ["airmon-ng", "-v"],
        "airgraph-ng": ["airgraph-ng", "-v"],
        "airodump-ng": ["airodump-ng", "--verbose"],
    }

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {
            scan_name: executor.submit(execute_scan, command, scan_name)
            for scan_name, command in commands.items()
        }

        # Wait for all the scans to complete
        concurrent.futures.wait(futures.values())

    logging.info("All scans completed.")
import subprocess
from boltdb import BoltDB

def execute_airmon_ng():
    try:
        output = subprocess.check_output(['airmon-ng', '-v'])
        result = output.decode('utf-8')
        db = BoltDB.open("mydatabase.db")
        if "Airmon-ng-results" not in db.sections:
            db.create_section("Airmon-ng-results")
        db.insert("Airmon-ng-results", result)
        db.commit()
        db.close()
        print("Airmon-ng results saved to BoltDB successfully.")
    except Exception as e:
        print("Error executing airmon-ng or saving results:", str(e))

if __name__ == "__main__":
    execute_airmon_ng()
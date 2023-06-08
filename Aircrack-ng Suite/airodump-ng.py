import subprocess
from boltdb import BoltDB

def execute_airodump_ng():
    try:
        output = subprocess.check_output(['airodump-ng', '--verbose'])
        result = output.decode('utf-8')
        db = BoltDB.open("mydatabase.db")
        if "Airodump-ng-results" not in db.sections:
            db.create_section("Airodump-ng-results")
        db.insert("Airodump-ng-results", result)
        db.commit()
        db.close()
        print("Airodump-ng results saved to BoltDB successfully.")
    except Exception as e:
        print("Error executing airodump-ng or saving results:", str(e))

if __name__ == "__main__":
    execute_airodump_ng()
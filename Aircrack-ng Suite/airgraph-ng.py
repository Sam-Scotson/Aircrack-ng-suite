import subprocess
from boltdb import BoltDB

def execute_airgraph_ng():
    try:
        output = subprocess.check_output(['airgraph-ng', '-v'])
        result = output.decode('utf-8')
        db = BoltDB.open("mydatabase.db")
        if "Airgraph-ng-results" not in db.sections:
            db.create_section("Airgraph-ng-results")
        db.insert("Airgraph-ng-results", result)
        db.commit()
        db.close()
        print("Airgraph-ng results saved to BoltDB successfully.")
    except Exception as e:
        print("Error executing airgraph-ng or saving results:", str(e))

if __name__ == "__main__":
    execute_airgraph_ng()
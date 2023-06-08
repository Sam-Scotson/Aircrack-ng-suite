import subprocess
from boltdb import BoltDB

def exe_airbase_ng():
    try:
        output = subprocess.check_output(['airbase-ng', '-v'])
        result = output.decode('utf-8')
        db = BoltDB.open("mydatabase.db")
        if "Airbase-ng-results" not in db.sections:
            db.create_section("Airbase-ng-results")
        db.insert("Airbase-ng-results", result)
        db.commit()
        db.close()
        print("Airbase results saved successfully.")
    except Exception as e:
        print("Error executing airbase-ng or saving results:", str(e))

if __name__ == "__main__":
    exe_airbase_ng()

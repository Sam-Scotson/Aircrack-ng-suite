import subprocess
from boltdb import BoltDB

def exe_aircrack_ng():
    try:
        output = subprocess.check_output(['aircrack-ng', '-v'])
        result = output.decode('utf-8')
        db = BoltDB.open("mydatabase.db")
        if "Aircrack-ng-results" not in db.sections:
            db.create_section("Aircrack-ng-results")
        db.insert("Aircrack-ng-results", result)
        db.commit()
        db.close()
        print("Aircrack results saved successfully.")
    except Exception as e:
        print("Error executing aircrack-ng or saving results:", str(e))

if __name__ == "__main__":
    exe_aircrack_ng()

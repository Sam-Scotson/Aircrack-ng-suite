import subprocess
from boltdb import BoltDB

def exe_aireplay_ng():
    try:
        output = subprocess.check_output(['aireplay-ng', '-v'])
        result = output.decode('utf-8')
        db = BoltDB.open("mydatabase.db")
        if "Aireplay-ng-results" not in db.sections:
            db.create_section("Aireplay-ng-results")
        db.insert("Aireplay-ng-results", result)
        db.commit()
        db.close()
        print("Aireplay results saved successfully.")
    except Exception as e:
        print("Error executing aireplay-ng or saving results:", str(e))

if __name__ == "__main__":
    exe_aireplay_ng()

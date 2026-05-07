import hashlib
import json
import os

def main():
    files_to_hash = {
        "red_light": "data/Red_Light.csv",
        "traffic_crashes": "data/Traffic_Crashes.csv"
    }
    
    provenance = {"raw_file_hashes": {}}

    for label, path in files_to_hash.items():
        if os.path.exists(path):
            sha256_hash = hashlib.sha256()
            with open(path, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            provenance["raw_file_hashes"][label] = sha256_hash.hexdigest()
        else:
            print(f"Warning: {path} not found.")

    # Ensure the directory exists and save the JSON
    os.makedirs("data/processed", exist_ok=True)
    with open("data/processed/cleaning_provenance.json", "w") as f:
        json.dump(provenance, f, indent=4)
    print("cleaning_provenance.json created")

if __name__ == "__main__":
    main()

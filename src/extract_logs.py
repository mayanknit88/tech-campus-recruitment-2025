import os
import sys

def extract_logs(log_file, date):
    if not os.path.exists(log_file):
        print("Error: Log file not found.")
        return
    
    os.makedirs("output", exist_ok=True)
    output_file = f"output/output_{date}.txt"
    
    with open(log_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            if line.startswith(date):
                outfile.write(line)
    
    print(f"Logs for {date} extracted to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py <log_file_path> <YYYY-MM-DD>")
        sys.exit(1)
    
    log_file = r"C:\Users\HP\Downloads\logs_2024.log\logs_2024.log"
    date = sys.argv[1]

    extract_logs(log_file, date)

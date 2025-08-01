import whois
import csv
from datetime import datetime

def fetch_whois_info(domain):
    try:
        w = whois.whois(domain)

        registrar = w.registrar if w.registrar else "N/A"
        creation_date = w.creation_date
        expiration_date = w.expiration_date
        name_servers = ', '.join(w.name_servers) if w.name_servers else "N/A"

        # Some domains have lists, handle that
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        if isinstance(expiration_date, list):
            expiration_date = expiration_date[0]

        return {
            "Domain": domain,
            "Registrar": registrar,
            "Creation Date": creation_date,
            "Expiration Date": expiration_date,
            "Name Servers": name_servers
        }

    except Exception as e:
        print(f"Error fetching info for {domain}: {str(e)}")
        return {
            "Domain": domain,
            "Registrar": "Error",
            "Creation Date": "Error",
            "Expiration Date": "Error",
            "Name Servers": "Error"
        }

def save_to_csv(data, filename='whois_results.csv'):
    headers = ["Domain", "Registrar", "Creation Date", "Expiration Date", "Name Servers"]

    try:
        with open(filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers)

            # Write header only if file is empty
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(data)

        print(f"Data saved to {filename}\n")

    except Exception as e:
        print(f"Failed to save to CSV: {str(e)}")

if __name__ == "__main__":
    while True:
        domain = input("Enter a domain name (or type 'exit' to quit): ").strip()

        if domain.lower() == 'exit':
            break

        result = fetch_whois_info(domain)
        print("\n--- WHOIS INFO ---")
        for key, value in result.items():
            print(f"{key}: {value}")
        print("-------------------\n")

        save_to_csv(result)

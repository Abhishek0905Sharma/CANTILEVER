# WHOIS Domain Info Checker 🕵️‍♂️

A simple Python tool to fetch and store WHOIS information for any domain.

This script uses the `python-whois` library to retrieve domain registrar details, creation and expiration dates, and DNS info. It handles invalid or protected domains gracefully and saves all results to a local `.csv` file.

---

## 🔧 Features

- 🔍 Fetch WHOIS data for any domain
- 🛡️ Error handling for invalid or private WHOIS data
- 📄 Save results to a `whois_results.csv` file
- 🔁 Appends data without overwriting existing entries

---

## 📦 Requirements

- Python 3.7+
- `python-whois` library

Install the required library:

```bash
pip install python-whois
```

---

## 🚀 How to Run

1. Clone this repository or download the script
2. Open terminal or CMD in the project directory
3. Run the script:
   ```bash
   python whois_checker.py
   ```

4. Enter domain names when prompted (e.g., `openai.com`)
5. Type `exit` to close the program

---

## 💾 Output

Results are saved in `whois_results.csv` with the following fields:

- Domain
- Registrar
- Creation Date
- Expiration Date
- Name Servers

---

## 📁 Example

```
Enter a domain name (or type 'exit' to quit): openai.com

--- WHOIS INFO ---
Domain: openai.com
Registrar: MarkMonitor Inc.
Creation Date: 2015-04-16 00:00:00
Expiration Date: 2027-04-16 00:00:00
Name Servers: ns1.openai.com, ns2.openai.com, ...
-------------------

Data saved to whois_results.csv
```

---

## 🤝 Contributing

Feel free to fork the repo and improve the tool!  
Pull requests are welcome.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Author

Created by ABHISHEK SHARMA  
GitHub: https://abhishek0905sharma.github.io/



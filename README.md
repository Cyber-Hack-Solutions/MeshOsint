
![main](https://github.com/user-attachments/assets/630c3070-564d-4003-afb1-a441ac3b05fe)

---

# Meshtastic OSINT Tool

Designed by [Cyber-Hack Solutions LLC](https://cyberhacksolutions.com), this tool leverages APIs from:
- [MeshMap Nodes](https://meshmap.net/nodes.json)
- [Meshtastic Device Stats](https://meshtastic.liamcottle.net/api/v1/stats/hardware-models)

This tool gathers real-time node data from the above sources and displays it in a tabulated, terminal-friendly format. While you can visit [meshmap.net](https://meshmap.net) to view this information directly in a browser, this tool offers an alternative for structured data presentation and interaction from the terminal.

> **For educational purposes only**

---

## Features

- **Node Data Capture**: Automatically collects real-time node and device information from secure sources.
![tables](https://github.com/user-attachments/assets/cfc85bb5-4c21-43d9-be0e-600127c4f172)

- **Customizable Mapping**: Visualizes network nodes with Folium, overlaying coordinates and metadata on a stylized map.
![map](https://github.com/user-attachments/assets/37a48adc-d42d-41f0-863f-6056c16d97b4)


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Cyber-Hack-Solutions/MeshOsint.git
   cd MeshOsint
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
## Usage

To run the script, navigate to the project directory and execute:
```bash
python3 Meshosint.py
```

Follow the prompts to fetch data, display tables, and open the map in your default browser.

## 🤝 Contributing

We welcome contributions to improve and expand this tool! To contribute, please follow these steps:

1. **Fork** the repository.
2. **Clone** your forked repository locally.
3. Create a new **feature branch** for your changes.
4. Make your changes and **commit** them with clear and concise messages.
5. **Push** your changes to your forked repository.
6. Open a **pull request** to the main repository's `main` branch.
7. If you add new libraries or modules, remember to update the `requirements.txt` file by re-generating it to ensure everyone can run the tool smoothly without any issues.

Please note:
- Contributors should have a solid understanding of Python, as AI-generated code can sometimes lead to confusing or difficult-to-debug issues.
  

We will review all contributions, verifying modifications and new changes for quality and consistency before deciding to approve or decline them. Thank you for helping make this tool better!


---

<div align="center">

<img src="https://github.com/user-attachments/assets/cdd2f425-75e7-4af5-b053-44df93b3a35d" alt="chs" width="200"/>

</div>

---

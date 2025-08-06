<h1 align="center">
  <br>
  <a href="#"><img src="EcovisionLogo.png" alt="Ecovision" width="205" style="border-radius: 10%;"></a>
  <br>
  Ecovision
  <br>
</h1>

<h4 align="center">An AI-Powered Full-Stack Platform for Economic News Analysis.</h4>


<p align="center">
  <img alt="Static Badge" src="https://img.shields.io/badge/django-4.2.11-blue">
  <img alt="Static Badge" src="https://img.shields.io/badge/react-24.4.1-cyan">
  <img alt="Static Badge" src="https://img.shields.io/badge/python-3.12.3-tomato">
  <img alt="Static Badge" src="https://img.shields.io/badge/MIT%20license-%2339C684">

</p>

<p align="center">
  <a href="#🌟-key-features">Key Features</a> •
  <a href="#🚀-how-to-use">How To Use</a> •
  <a href="#⚖️-license">License</a> •
  <a href="#👥-contributors">Contributors</a>
</p>

<!-- You can place a screenshot or GIF here, like this: -->
<!-- ![screenshot](https://raw.githubusercontent.com/your-username/Ecovision/main/screenshot.gif) -->


## 🌟 Key Features

Ecovision offers a robust set of features designed to provide comprehensive economic insights powered by artificial intelligence.

### 📊 **Powerful Data Analysis**
* **Real-time Analytics**: Instant processing of market and cryptocurrency data to provide predictive insights and help you stay ahead of trends.
* **Advanced Algorithms**: Comprehensive analysis of complex datasets, enabling the detection of subtle patterns and critical anomalies.

### 🔗 **API-Driven Architecture**
* **Wide Range of APIs**: Supports seamless integration with finance, markets, investing, technology, and science APIs, making it easy for both developers and users to connect.
* **Admin Controls**: A dedicated admin panel provides intuitive controls for API and system management, allowing for easy toggling and running of various processes.

### 🌐 **Stay Updated with Market Trends**
* **Cryptocurrency Insights**: Get real-time updates on major cryptocurrencies like Bitcoin, Ethereum, Cardano, and more, complete with visual indicators for price changes and market trends.
* **Featured News**: Access aggregated news feeds to keep you informed about the latest economic developments and global events.

### 💡 **User-Friendly Design**
* **Interactive Dashboard**: Features accessible buttons for quick actions such as fetching news or viewing logs, simplifying navigation for both administrators and general users.
* **Customizable Inputs**: Easily set parameters for specific tasks like data scraping or fetching, giving you control over the information you receive.

### 🚀 **Technological Innovation**
* **Modular Design**: Built with scalability in mind, Ecovision's modular architecture is adaptable for future enhancements and encourages open-source collaboration and creativity.
* **Automated Processes**: Enjoy seamless integration of scrapers and data handlers, along with automated logging and status tracking for enhanced reliability.

### 📈 **Empowering Decision-Making**
* **Market Predictions**: Analyzes historical data to generate smarter investment strategies, helping users make informed decisions with confidence.
* **Transparency**: Provides open access to logs and system status, ensuring better oversight and understanding of the platform's operations.



## 🚀 How To Use

Ready to get Ecovision up and running? Follow these steps to set up your development environment and launch the platform.

### **Prerequisites**

Before you begin, ensure you have the following software installed on your system:

* **Git**: Essential for cloning the project repository.
* **Python**: Make sure you have Python installed, along with its package installer, **Pip**.
* **Node.js**: Install Node.js, which includes **npm** (Node Package Manager) for managing frontend dependencies.

### **Installation**

Let's get the project files onto your machine and install the necessary dependencies for both the backend and frontend.

1.  **Clone the Repository:**
    Start by cloning the Ecovision project from its GitHub repository:

    ```bash
    git clone [https://github.com/alirezaArz/Ecovision.git](https://github.com/alirezaArz/Ecovision.git)
    ```

2.  **Navigate to the Project Root:**
    Change your current directory to the newly cloned project's main folder:

    ```bash
    cd Ecovision
    ```

3.  **Install Backend Dependencies:**
    Install all required Python packages for the Django backend using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Install Frontend Dependencies:**
    Move into the `frontend` directory and install the React application's dependencies using `npm`:

    ```bash
    cd frontend
    npm install
    ```

### **Running the Development Servers**

Ecovision involves both a Django backend (which includes AI scripts) and a React frontend. Here's how to start them.

#### **Running the Django Backend & AI Scripts**

From the main `Ecovision` directory, execute the following command to launch the Django server and simultaneously activate the integrated AI scripts:

```bash
python manage.py starteco
````

  * **Setting a Custom Port:**
    By default, the Django server runs on port `8000`. If you need to use a different port, you can specify it with the `--port` argument:

    ```bash
    python manage.py starteco --port <your port>
    ```

    *Note: Changing the default port (8000) will require manual configuration adjustments for buttons on the main page or Admin Page, as they are hardcoded to the default.*

  * **Accessing the Main Page:**
    To open the `Main Page`, simply [click here](http://127.0.0.1:8000/).

  * **Accessing the Admin Page:**
    To open the `Admin Page`, simply [click here](http://127.0.0.1:8000/admin/).

#### **Running the React Frontend**

To start the React development server, navigate into the `frontend` directory (if you're not already there) and run:

```bash
cd frontend
npm run dev
```

This will typically open the React application in your browser at `http://localhost:5173` (or a similar port).

### **Viewing Logs**

To monitor the output and logs generated by the backend processes (Django and AI scripts), use the following command from the main `Ecovision` directory:

```bash
python manage.py ecolog
```
## Credits

This software uses the following open source packages:

- [Node.js](https://nodejs.org/)
- [React](https://react.dev/)
- [Django](https://www.djangoproject.com/)
- [Selenium](https://www.selenium.dev/)
- [Gemini](https://ai.google.dev/gemini-api/docs)
- [Ollama](https://ollama.com/)
- [Halo](https://github.com/manrajgrover/halo)
- [Markdown](https://python-markdown.github.io/)


## ⚖️ License

MIT license


## 👥 Contributors

We welcome contributions\! You can list contributors here, perhaps with links to their GitHub profiles. For example:

  * [alrz](https://github.com/alirezaArz)
  * [darksider-5](https://github.com/darksider-05)
  * [hosseinshokrgozar85](https://github.com/hosseinshokrgozar85)

---

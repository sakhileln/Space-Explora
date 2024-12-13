# 🌌 Space Nomad: A Space Exploration Web App 🛰️
Space Nomad is a web application that provides information on space exploration, current missions, news, and details about celestial bodies. Built using FastAPI and SQLite3, this application integrates data from various space-related APIs to display up-to-date space data in a simple, user-friendly format.

## 🚀 Features
- **Current Space Missions**: View live missions in space and their status.
- **Space News**: Get the latest updates and articles related to space exploration.
- **Celestial Bodies Information**: Access detailed information about planets, moons, stars, and galaxies.
- **API Integration**: Fetch real-time data from space APIs (like NASA, SpaceX, and others).

## 🔧 Tech Stack
- **Backend**: FastAPI (for building a modern web API)
- **Database**: SQLite3 (lightweight relational database)
- **APIs**: Integration with various space-related APIs (NASA, SpaceX, etc.)
- **Frontend**: Simple HTML and CSS for displaying data (can be expanded later)

## ⚙️ Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/sakhileln/Space-Nomad.git
    cd Space-Nomad
    ```
2. Install Poetry:
If you don't have Poetry installed, you can install it globally by running:
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```
    For other installation methods, refer to the official Poetry installation guide.

3. Install dependencies using Poetry:
    ```bash
    poetry install
    ```
    Poetry will automatically create a virtual environment and install the required dependencies listed in `pyproject.toml`.

4. Activate the virtual environment:
    ```bash
    poetry shell
    ```
5. Run the FastAPI app:
    ```bash
    uvicorn main:app --reload
    ```
    The app will now be available at http://127.0.0.1:8000 in your browser.

## 🌐 Usage
- **Homepage**: Displays the main space exploration news and details of ongoing missions.
- **Missions Page**: A list of space missions, both past and ongoing, with their current status.
- **Celestial Bodies Page**: Detailed information on planets, moons, and stars.
- **News Section**: Displays the latest articles and space-related news updates.

## 🔌 APIs
This app integrates with space APIs to fetch real-time data:
- **NASA API**: For space exploration data, images, and mission updates.
- **SpaceX API**: For current SpaceX missions and launches.
- **Other APIs**: Additional APIs for astronomical data (planets, moons, etc.).
You can extend the app to include more APIs or create your own endpoints to expose space data.

## 📄 Database
The project uses SQLite3 for storing basic information like user preferences or data caching. The database is lightweight and easy to set up, making it perfect for smaller-scale applications. You can extend this as needed for more complex use cases.

## 🚀 Future Features
- Interactive map for space missions and celestial bodies.
- User authentication to save preferences.
- Extend with more APIs (e.g., Hubble, SpaceNews, etc.).
- Responsive frontend for mobile devices.

## 👥 Contributing
We welcome contributions! If you'd like to help improve Space-Explora, feel free to fork the repo and create a pull request. Here’s how you can contribute:
1. Fork the repository.
2. Create a new branch for your changes.
3. Implement your changes.
4. Test your code.
5. Submit a pull request with a description of what you've done.

## 📞 Contact
If you have any questions or suggestions, feel free to open an issue in this repository or contact us directly.
- Sakhile III  
- [LinkedIn Profile](https://www.linkedin.com/in/sakhile-ndlazi)
- [GitHub Profile](https://github.com/sakhileln)


# IIT Bombay CSE Department Course Statistics Visualization

This repository contains the source code and documentation for the **IIT Bombay CSE Department Course Statistics Visualization** project. The project aims to create a comprehensive data visualization tool that allows for the dynamic input of course evaluation data and generates interactive visualizations, providing valuable insights into course statistics.

## Table of Contents
- [Project Overview](#project-overview)
- [Objectives](#objectives)
- [System Architecture](#system-architecture)
  - [Database Management](#database-management)
  - [Data Visualization](#data-visualization)
  - [Web Dashboard](#web-dashboard)
- [Security and Access Control](#security-and-access-control)
- [Results and Discussion](#results-and-discussion)
- [Conclusion and Future Work](#conclusion-and-future-work)
- [Appendices](#appendices)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
This project is designed to create a data visualization tool for the Computer Science and Engineering (CSE) department at IIT Bombay. It extracts data from various web sources, analyzes it using Python, and produces interactive visualizations in HTML. Professors can also input course evaluation data to enrich the existing database, and LaTeX reports are generated for in-depth analysis.

## Objectives
The primary objectives of the project include:
1. Developing a database management system for storing and managing course data.
2. Creating interactive and informative data visualizations.
3. Developing a web-based dashboard for displaying visualizations and allowing data input.
4. Implementing user authentication and access control mechanisms.
5. Generating exportable reports and visualizations.

## System Architecture
### Database Management
- **Database:** PostgreSQL is used for storing course data, including course details, year-wise statistics, and student performance data.
- **Data Extraction:** Data is extracted using Python scripts from relevant web sources.

### Data Visualization
- **Tools and Libraries:** Python libraries such as Matplotlib, Plotly, and Seaborn are used for creating visualizations.
- **Visualizations:** Various types of charts, graphs, and heatmaps are generated to provide insights into the course data.

### Web Dashboard
- **Framework:** Django is used to develop the web dashboard, which displays the visualizations and allows professors to input course evaluation data.
- **User Interface:** The interface is designed to be clean and intuitive, providing users with the ability to filter data by course, year, and other parameters.

## Security and Access Control
- **User Authentication:** The system implements secure user authentication mechanisms with different roles (administrators, professors, students).
- **Data Validation:** Input data is validated to ensure accuracy and consistency.

## Results and Discussion
The system was tested with real-world data from the IIT Bombay CSE department. The performance of the data visualization and web dashboard components was evaluated based on response times, user feedback, and data accuracy.

## Conclusion and Future Work
This project successfully developed a comprehensive data visualization tool for the IIT Bombay CSE department. Future enhancements could include:
- Expanding the system to include more detailed student performance analytics.
- Implementing machine learning algorithms to predict future trends.
- Enhancing the user interface with more advanced interactive features.

## Appendices
- **Appendix A:** Database Schema
- **Appendix B:** Python Code for Data Visualization
- **Appendix C:** User Documentation

## Installation
To set up the project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/iitb-cse-stats-visualization.git
    ```
2. Set up the PostgreSQL database:
    ```bash
    # Create the database
    createdb cse_stats

    # Run the database schema script
    psql -d cse_stats -f path/to/schema.sql
    ```

3. Install required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Django server:
    ```bash
    python manage.py runserver
    ```

5. Access the web dashboard at `http://localhost:8000`.

## Usage
1. Input course evaluation data through the web dashboard.
2. Generate visualizations by selecting the desired filters.
3. Export reports as LaTeX documents for in-depth analysis.

## Contributing
Contributions to this project are welcome. Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

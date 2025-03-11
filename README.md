# Wildlife Tracker

A Command Line Interface (CLI) application to track wildlife animals and their sightings. Built with Python, Click, and SQLAlchemy.

## Features

- **Add Animals**: Record new animals with species, habitat, and population details.
- **List All Animals**: View all animals stored in the database.
- **Track Sightings**: Log sightings of animals with location, time, and observer details.
- **Find Animals by Habitat**: Search for animals based on their habitat.
- **Delete Animal Records**: Remove an animal from the database.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Setup

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/wildlife-tracker.git
cd wildlife-tracker


2. Create a Virtual Environment
Create a virtual environment to isolate dependencies:

On Windows:

On macOS/Linux:

3. Install Dependencies
Install the required Python packages:

4. Initialize the Database
Run the application once to create the database and tables:

Usage
1. Add an Animal
Add a new animal to the database:

Example:

2. List All Animals
View all animals in the database:

Example Output:

3. Track a Sighting
Log a sighting of an animal:

Example:

4. Find Animals by Habitat
Search for animals by their habitat:

Example:

Example Output:

5. Delete an Animal
Remove an animal from the database:

Example:

Output:

Project Structure
Dependencies
Click: For building the CLI interface.
SQLAlchemy: For database management and ORM.
python-dateutil: For flexible date/time parsing.
Error Handling
The application includes robust error handling for:

Invalid input formats (e.g., non-integer population, invalid date/time).
Database errors (e.g., duplicate species, missing animal IDs).
Graceful rollback of transactions in case of errors.
Contributing
Contributions are welcome! Follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/YourFeature).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature/YourFeature).
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Built with ❤️ by [Wanjiku Faith].

Inspired by wildlife conservation efforts. ```

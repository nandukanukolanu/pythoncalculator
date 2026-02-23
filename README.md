# Python Calculator Web App

A modern, responsive web-based calculator built with Flask and featuring a beautiful UI. Easy to deploy as a Docker container.

## Features

✨ **Modern UI** - Clean, gradient-based design with smooth animations
🔢 **Full Calculator Functions** - Addition, subtraction, multiplication, division, parentheses
⌨️ **Keyboard Support** - Use your keyboard for calculations
🎯 **Responsive Design** - Works great on desktop, tablet, and mobile
🐳 **Docker Ready** - Containerized for easy deployment
⚡ **Fast & Lightweight** - Built with Flask, minimal dependencies

## Project Structure

```
pythoncalculator/
├── app.py                 # Flask application
├── templates/
│   └── index.html        # Calculator UI
├── static/
│   └── style.css         # Modern styling
├── requirements.txt      # Python dependencies
├── Dockerfile            # Container configuration
├── docker-compose.yml    # Docker Compose configuration
└── README.md             # This file
```

## Quick Start

### Prerequisites
- Python 3.7+
- pip (Python package manager)
- Docker & Docker Compose (optional, for containerization)

### Local Development

1. **Clone the repository**
   ```bash
   cd pythoncalculator
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000`

## Docker Deployment

### Using Docker Compose (Recommended)

```bash
docker-compose up -d
```

The calculator will be available at `http://localhost:5000`

To stop the container:
```bash
docker-compose down
```

### Using Docker directly

1. **Build the image**
   ```bash
   docker build -t pythoncalculator .
   ```

2. **Run the container**
   ```bash
   docker run -p 5000:5000 pythoncalculator
   ```

The calculator will be available at `http://localhost:5000`

## Usage

- **Basic Math**: Click buttons or use your keyboard to enter numbers and operators
- **Decimal Numbers**: Use the `.` button for decimal calculations
- **Parentheses**: Use `(` and `)` for complex expressions
- **Clear**: Press `C` or `Escape` to clear the display
- **Delete**: Press `Backspace` or click `⌫` to delete the last character
- **Calculate**: Press `Enter` or click `=` to get the result

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `0-9` | Number input |
| `+ - * /` | Operations |
| `.` | Decimal point |
| `( )` | Parentheses |
| `Enter` | Calculate result |
| `Backspace` | Delete last character |
| `Escape` or `C` | Clear display |

## Technologies Used

- **Backend**: Flask 3.0.0 (Python web framework)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Containerization**: Docker & Docker Compose
- **Base Image**: Python 3.11-slim

## Application Architecture

### Backend (Flask)
- `/` - Serves the calculator UI
- `/calculate` - POST endpoint that evaluates mathematical expressions
- Expression validation and safe evaluation using Python's `eval()` with restrictions

### Frontend
- Responsive HTML/CSS calculator interface
- AJAX calls for calculations
- Keyboard and mouse input support
- Client-side validation and error handling

## Security Considerations

The application uses safe expression evaluation with:
- Character whitelisting (only mathematical operators and numbers allowed)
- Try-catch error handling
- Input validation before processing

## Performance Notes

- Lightweight Flask application with minimal overhead
- Docker container optimized with Python 3.11-slim base image
- CSS animations use GPU acceleration for smooth performance
- Frontend calculations via backend ensures consistency

## Future Enhancements

- [ ] History of calculations
- [ ] Scientific calculator mode (sin, cos, sqrt, etc.)
- [ ] Dark mode toggle
- [ ] Multiple language support
- [ ] Persistent storage of calculations

## Troubleshooting

**Port 5000 already in use?**
```bash
docker run -p 8080:5000 pythoncalculator
# Access at http://localhost:8080
```

**Permission denied error?**
```bash
sudo docker-compose up
```

## License

Open source - feel free to use and modify!

## Author

Python Calculator Web App
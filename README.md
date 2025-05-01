# Calculator App

A mobile calculator application built with Kivy and KivyMD.

## Features

- Basic arithmetic operations
- Modern Material Design interface
- Cross-platform compatibility (Android, iOS, desktop)
- SQLite database for calculation history

## Screenshots

[Add screenshots of your app here]

## Installation

### Prerequisites

- Python 3.7+
- Kivy
- KivyMD
- SQLite3

### For End Users

Download the APK from the [Releases](https://github.com/yourusername/calculator-app/releases) section and install it on your Android device.

### For Developers

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Kivy-Calculator.git
   cd Kivy-Calculator
   ```

2. Set up a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python main.py
   ```

## Building the APK

To build the Android APK yourself:

1. Install Buildozer:
   ```bash
   pip install buildozer
   ```

2. Initialize Buildozer (if not already done):
   ```bash
   buildozer init
   ```

3. Edit the buildozer.spec file to match your requirements

4. Build the APK:
   ```bash
   buildozer android debug
   ```

5. The APK will be in the `bin/` directory

## Project Structure

```
Kivy-Calculator/
├── main.py             # Entry point
├── calculator.py       # Main application logic
├── history.db          # SQLite database for calculation history
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
└── buildozer.spec      # Buildozer configuration
```

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b new-feature`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin new-feature`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Kivy](https://kivy.org/) - Open source Python framework
- [KivyMD](https://github.com/kivymd/KivyMD) - Material Design components for Kivy

# Points Redeemer 🎯

An automated search tool designed for educational purposes to demonstrate web automation techniques using Python. This project showcases browser automation, JSON data management, and GUI interaction programming concepts.

## ⚠️ Important Disclaimer

**This project is strictly for educational and learning purposes only.** 

- The author does not encourage the use of this tool to violate any platform's Terms of Service
- Use at your own risk and responsibility
- Always earn points honestly and follow platform guidelines
- Respect rate limits and automation policies
- Consider the ethical implications of automation

## 🚀 Features

- **Smart Browser Automation**: Automated search queries using PyAutoGUI
- **Random Query Generation**: Creates diverse search patterns from word databases
- **Configurable Parameters**: Adjustable timing and search count settings
- **JSON-Based Data Management**: Easy-to-modify word and phrase databases
- **Keyboard Interrupt Support**: Safe termination with Ctrl+C
- **Multi-Tab Management**: Efficient tab opening and closing automation
- **Extensible Architecture**: Easy to modify and extend functionality

## 📁 Project Structure

```
points_redeemer/
├── main.py             # Main desktop automation script
├── mobile.py           # Mobile device automation variant
├── add.py              # Interactive word addition utility
├── add_start.py        # Starting phrase management tool
├── words.json          # Primary search vocabulary database
├── start.json          # Query starting phrases collection
├── examples/           # Example configurations and usage
└── README.md           # Project documentation
```

## 🛠️ System Requirements

- **Python**: 3.6 or higher
- **Operating System**: Windows, macOS, or Linux
- **Browser**: Any modern web browser
- **Dependencies**:
  ```
  pyautogui >= 0.9.50
  pathlib (built-in)
  json (built-in)
  random (built-in)
  time (built-in)
  webbrowser (built-in)
  ```

## 📦 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/OmGoyal27/points_redeemer.git
   cd points_redeemer
   ```

2. **Install dependencies**:
2. **Install dependencies**:
   ```bash
   pip install pyautogui
   ```

3. **Verify JSON files exist**:
   - Ensure `words.json` and `start.json` are present
   - Use the provided management tools to populate them if needed

4. **Configure browser**:
   - Set your default browser to your preferred choice
   - Ensure browser allows automation (disable pop-up blockers if needed)

## 🎮 Usage Guide

### Main Script (`main.py`)

The primary automation script that performs search operations:

```bash
python main.py
```

**Key Configuration Variables:**
```python
SLEEP_TIME_PER_TAB = 3      # Delay between tab operations (adjust for system performance)
NUMBER_OF_SEARCHES = 31     # Total number of searches to perform
```

**Execution Flow:**
1. Loads word databases from JSON files
2. Opens Bing rewards page in browser
3. For each search iteration:
   - Opens new browser tab (`Ctrl+T`)
   - Generates random search query (1-10 words)
   - Types the query and presses Enter
   - Waits 4 seconds for page load
   - Closes tab (`Ctrl+W`)
   - Brief pause before next iteration

**Search Pattern Generation:**
- Selects random starting phrase from `start.json`
- Adds 1-10 random words from `words.json`
- Creates natural-looking search queries

### Word Management Tools

#### Add General Words (`add.py`)
```bash
python add.py
```
Interactive tool for expanding the general vocabulary:
- Type words and press Enter to add them
- Type "save" to commit changes to `words.json`
- Useful for adding domain-specific terms

#### Manage Starting Phrases (`add_start.py`)
```bash
python add_start.py
```
Configure search query beginnings:
- Examples: "What is", "How to", "Why does", "Where can"
- These create more natural search patterns
- Stored in `start.json`

### Mobile Automation (`mobile.py`)

Alternative script designed for mobile device automation:
```bash
python mobile.py
```
- Uses "What is the meaning of [word]" search pattern
- Optimized for touch-based interfaces

## 🔧 Configuration & Customization

### Timing Adjustments

Modify these values in `main.py` based on your system:

```python
SLEEP_TIME_PER_TAB = 3      # Increase for slower systems
NUMBER_OF_SEARCHES = 31     # Adjust search count as needed
time.sleep(4)               # Page load wait time
time.sleep(0.5)             # Inter-search delay
```

### Search Complexity

Control query complexity by modifying the random length generator:
```python
length = random.randint(1, 10)  # Adjust min/max word count
```

### Safety Features

- **Keyboard Interrupt**: Press `Ctrl+C` to safely stop execution
- **Graceful Error Handling**: Script continues if individual searches fail
- **Configurable Delays**: Prevents overwhelming target servers

## 📊 JSON Database Formats

Checkout `exmamples` folder for it.

## 🚨 Important Considerations

### Technical Limitations
- **Screen Resolution**: PyAutoGUI depends on screen coordinates
- **Browser Compatibility**: Tested with major browsers (Chrome, Firefox, Edge)
- **Performance**: Timing may need adjustment on different systems
- **Focus Requirements**: Browser window must be active during execution

### Automation Detection
- Modern platforms employ sophisticated bot detection
- Randomized timing helps appear more human-like
- Consider longer delays between operations
- Vary search patterns and vocabulary

### Best Practices
1. **Start Small**: Begin with fewer searches to test system compatibility
2. **Monitor Performance**: Watch for browser lag or system slowdown
3. **Respect Limits**: Don't overwhelm target servers
4. **Stay Updated**: Keep dependencies current for security

## 🛠️ Troubleshooting

### Common Issues

**PyAutoGUI not working:**
```bash
pip install --upgrade pyautogui
```

**Browser focus issues:**
- Ensure browser window is visible and active
- Disable browser extensions that might interfere
- Check screen resolution compatibility

**JSON file errors:**
- Validate JSON syntax using online validators
- Ensure proper encoding (UTF-8)
- Check file permissions

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/improvement`)
3. **Commit** your changes (`git commit -am 'Add new feature'`)
4. **Push** to the branch (`git push origin feature/improvement`)
5. **Create** a Pull Request

## 📄 License

This project is provided "as-is" for educational purposes. Users are responsible for ensuring their usage complies with all applicable terms of service, local laws, and platform regulations.

## 🛡️ Ethical Guidelines

### Responsible Usage
- **Educational Focus**: Use for learning automation concepts
- **Respect ToS**: Always comply with platform terms of service
- **Fair Play**: Don't seek unfair advantages
- **Resource Consideration**: Be mindful of server load and costs

### Learning Outcomes
This project demonstrates:
- Python automation techniques
- GUI interaction programming
- JSON data management
- Error handling and user experience
- Web browser automation concepts

---

**Remember**: The most valuable rewards come from genuine learning and ethical practices! 🌟

**Happy Learning!** 🚀

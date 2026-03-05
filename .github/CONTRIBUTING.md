# Contributing to BYU MS Core Lab

Thank you for your interest in contributing to our mass spectrometry analysis tools!

## Getting Started

### Prerequisites
- Python 3.10 or higher (3.14+ recommended)
- Node.js 18+ (for web app development)
- Git

### Setup Development Environment

1. **Clone the repository**
   ```powershell
   git clone https://github.com/BYU-MS-Core-Lab/BYU-MS-Core-Automative-Proteomics-Tools.git
   cd BYU-Core-MS-Lab
   ```

2. **Create virtual environment**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1  # Windows PowerShell
   # or
   source .venv/bin/activate      # macOS/Linux
   ```

3. **Install dependencies**
   ```powershell
   # Install with development tools
   pip install -e ".[dev]"
   ```

4. **For web app development**
   ```powershell
   cd programs/mspp_web/frontend
   npm install
   cd ../../..
   ```

## Development Workflow

### Code Style

- **Python**: Follow PEP 8 guidelines
  - Use Ruff for formatting and linting: `ruff format .` and `ruff check --fix .`
  - Line length: 100 characters
  
- **TypeScript/React**: 
  - Follow TypeScript best practices
  - Use functional components with hooks
  - Keep components modular and reusable

### Common Commands

**Daily Development:**
```powershell
# Activate environment
.\.venv\Scripts\Activate.ps1

# Run web app
python programs/mspp_web/launch_app.py

# Run Python tools (filter FASTA, data analysis, etc.)
python programs/python/filter_fasta_gui.py

# Run Jupyter notebook for data analysis
jupyter notebook programs/python/MSPP_data_analysis.ipynb

# Deactivate when done
deactivate
```

**Frontend Development (Web App):**
```powershell
cd programs/mspp_web/frontend

# Development mode (hot reload)
npm run dev

# Production build
npm run build
```

**Code Quality:**
```powershell
# Format code with Ruff
ruff format programs/

# Lint and auto-fix issues
ruff check --fix programs/

# Run tests
pytest tests/
```

### Docstrings

All Python functions should have docstrings:

```python
def calculate_fold_change(ecoli_data, yeast_data):
    """
    Calculate log2 fold change between E.coli and Yeast intensities.
    
    Args:
        ecoli_data: Series of E.coli protein intensities
        yeast_data: Series of Yeast protein intensities
    
    Returns:
        Array of log2 fold change values
    """
    # Implementation
```

### Testing

- Write tests for new features
- Run tests before committing: `pytest tests/`
- Aim for >80% code coverage

### Git Commit Messages

Use clear, descriptive commit messages:

```
feat: Add grouped fold change plot to web app
fix: Resolve data caching issue in backend
docs: Update API endpoint documentation
refactor: Extract boxplot styling to helper method
```

Prefixes:
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `refactor:` - Code refactoring
- `test:` - Adding tests
- `chore:` - Maintenance tasks

## Project Structure

```
BYU-Core-MS-Lab/
├── programs/           # Applications
│   ├── mspp_web/      # Web application (Flask backend + React frontend)
│   └── python/        # Python tools and scripts
├── scripts/           # Development and setup scripts
├── documentations/    # Documentation and reference materials
├── tests/             # Unit tests and debugging utilities
├── tutorials/         # Workflow tutorials and guides
├── pyproject.toml     # Project metadata and dependencies
└── LICENSE            # Apache 2.0 License
```

## Pull Request Process

1. **Create a feature branch**
   ```powershell
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write clean, documented code
   - Add tests if applicable
   - Update documentation

3. **Test your changes**
   ```powershell
   # Run Python tests
   pytest tests/
   
   # Run web app build
   cd programs/mspp_web/frontend
   npm run build
   ```

4. **Commit and push**
   ```powershell
   git add .
   git commit -m "feat: Your feature description"
   git push origin feature/your-feature-name
   ```

5. **Create Pull Request**
   - Provide clear description of changes
   - Reference any related issues
   - Wait for review

## Questions?

Feel free to open an issue for:
- Bug reports
- Feature requests
- Documentation improvements
- General questions

## Code of Conduct

- Be respectful and professional
- Provide constructive feedback
- Focus on the science and code quality
- Help maintain a welcoming environment

Thank you for contributing! 🔬

# Contributing to MTDataPro Docs

Thank you for your interest in improving the MTDataPro documentation.

## How to Contribute

1. **Find an issue**: Browse the [issue tracker](https://github.com/EMWPJ/MTDataPro-docs/issues) or report a new one.
2. **Fork the repository**: Create your own copy to work on.
3. **Make changes**: Edit the Markdown or reStructuredText source files.
4. **Preview locally**: Build the documentation to verify your changes.
5. **Submit a pull request**: Your changes will be reviewed and merged.

## Documentation Structure

```
docs/
├── source/
│   ├── conf.py           # Sphinx configuration
│   ├── index.md          # Main documentation page
│   ├── intro/            # Introduction and installation
│   ├── tutorial/         # Step-by-step tutorials
│   ├── modules/          # Instrument module documentation
│   ├── processing/       # Processing pipeline docs
│   ├── gallery/          # Example figures and use cases
│   ├── reference/        # API and parameter reference
│   └── appendix/         # Contributing, glossary, etc.
└── requirements.txt      # Python dependencies
```

## Building Locally

```bash
pip install -r requirements.txt
sphinx-build -b html source _build/html
```

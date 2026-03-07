# Workspace Instructions for AI Agents

## Project Overview
This is a multi-purpose experimental workspace containing independent subprojects for document processing, OCR, product catalog generation, and interactive content. The workspace supports both Hebrew (RTL) and English content.

## Technology Stack
- **Node.js** (ES Modules with .mjs extension)
- **Python 3** for data processing
- **HTML/CSS/JavaScript** for web content
- **PDF.js** for PDF processing
- **Tesseract.js** for OCR
- **Canvas API** for image rendering

## Key Conventions

### File Organization
- **Scripts**: Use `.mjs` extension for Node.js ES modules
- **Data**: Store in organized folders (e.g., `GMA/` for product data)
- **Images**: Use AVIF format for product images
- **Output**: HTML files are final deliverables, open directly in browser

### Execution Model
- **No build pipeline** - direct execution of scripts
- **Run commands**: `node script.mjs` or `python script.py`
- **Browser content**: Open `.html` files directly
- **Standalone scripts**: Each script is independent, no complex dependencies

### Language Support
- **Hebrew (RTL)**: Use `dir="rtl"` and Hebrew fonts (Heebo from Google Fonts)
- **Bilingual content**: Support both Hebrew and English text
- **OCR**: Trained models for Hebrew (`heb.traineddata`) and English (`eng.traineddata`)

## Common Patterns

### Data Processing Pipeline
1. **Input**: CSV files with product data
2. **Processing**: Python scripts for data transformation
3. **Output**: HTML files with responsive design
4. **Assets**: Images stored in subfolders (e.g., `GMA/PIC/`)

### Web Content Generation
- **Responsive design**: Desktop (3 columns) → Mobile (1 column)
- **Interactive elements**: JavaScript for dynamic content
- **Styling**: Modern CSS with gradients and animations
- **Typography**: Google Fonts for consistent branding

### Document Processing
- **PDF extraction**: Use pdfjs-dist for text and image extraction
- **OCR processing**: Tesseract.js for scanned documents
- **Text recognition**: Support for Hebrew and English text
- **Output formats**: HTML, text files, and images

## Development Workflow

### Running Scripts
```bash
# Node.js scripts
node extract_pdf.mjs
node ocr.mjs
node render_pdf.mjs

# Python scripts
python generate_catalog.py

# View results
start catalog.html  # Windows
open catalog.html   # macOS
```

### Adding New Features
1. **Data processing**: Create Python script for CSV/HTML conversion
2. **Web content**: Use modern HTML5 with CSS Grid/Flexbox
3. **Interactive features**: Vanilla JavaScript, no frameworks
4. **Hebrew support**: Always include RTL direction and proper fonts

## Project Structure
```
Root level: Independent scripts and outputs
GMA/: Product catalog data and images
.agents/: VS Code agent configurations
.claude/: Local AI assistant settings
```

## Best Practices
- **Modular code**: Keep scripts focused on single tasks
- **Error handling**: Include try-catch blocks for file operations
- **Documentation**: Add comments for complex logic
- **Testing**: Manual testing by opening HTML files in browser
- **Performance**: Optimize image loading and rendering

## Common Pitfalls
- **File paths**: Use relative paths, account for Windows/macOS differences
- **Encoding**: Handle Hebrew text properly (UTF-8)
- **Dependencies**: Scripts should work without complex setup
- **Browser compatibility**: Test in multiple browsers

## Agent-Specific Guidelines

### For Code Generation
- Prefer vanilla JavaScript over frameworks
- Use modern CSS features (Grid, Flexbox, CSS Variables)
- Include responsive design by default
- Add proper Hebrew/RTL support

### For Data Processing
- Use Python for CSV manipulation
- Generate clean HTML output
- Include proper error handling
- Document data transformations

### For Web Development
- Create accessible HTML structure
- Use semantic HTML elements
- Include proper meta tags
- Optimize for mobile devices

## Example Tasks
- Generate product catalog from CSV data
- Create interactive games (like Pac-Man)
- Process PDF documents with OCR
- Build responsive Hebrew websites
- Extract and transform data from various sources
# Challenge 1a: PDF Processing and Structure Extraction

## Overview
This solution implements an intelligent PDF processing system that extracts document structure, titles, and hierarchical outlines from PDF documents. The system processes multiple PDF files automatically and generates structured JSON output conforming to a predefined schema. The solution is containerized using Docker and meets strict performance and resource constraints.

## Approach

### 1. **Dual-Strategy PDF Processing**
The solution employs a two-tier approach for robust document structure extraction:

- **Primary Strategy**: Extract document outline using PyMuPDF's built-in table of contents (TOC) functionality
- **Fallback Strategy**: Multi-signal heading detection using font size analysis, formatting, and pattern recognition

### 2. **Intelligent Heading Detection**
The system identifies document headings using multiple signals:

- **Numbered Patterns**: Detects hierarchical numbering (1., 2.1, 3.2.1, etc.)
- **Font Size Analysis**: Compares relative font sizes to determine heading levels
- **Formatting Signals**: Identifies bold text and large fonts as heading indicators
- **Custom Keywords**: Recognizes domain-specific heading patterns
- **Positional Analysis**: Considers text position and page layout

### 3. **Title Extraction Strategy**
Document titles are extracted using a prioritized approach:

- **Metadata First**: Extract title from PDF document metadata
- **First Page Analysis**: Fallback to largest text on the first page
- **Font Size Comparison**: Identify title candidates based on font size hierarchy

### 4. **Outline Cleaning and Validation**
The extracted outline undergoes comprehensive cleaning:

- **Fragment Merging**: Combines nearby text fragments into coherent headings
- **Duplicate Removal**: Eliminates redundant entries while preserving hierarchy
- **Length Filtering**: Removes overly short headings (except numbered ones)
- **Level Normalization**: Ensures consistent heading level assignment

### 5. **Output Generation**
The system produces structured JSON output with:

- **Document Title**: Extracted or inferred document title
- **Hierarchical Outline**: Cleaned and validated heading structure
- **Page References**: Accurate page numbers for each heading
- **Schema Compliance**: Output conforms to predefined JSON schema

## Models and Libraries Used

### **Core Libraries**
- **PyMuPDF (fitz)**: Primary PDF processing library for text extraction and document analysis
- **Python Standard Library**: json, pathlib, re for data handling and pattern matching

### **No Machine Learning Models**
- The solution uses rule-based algorithms and heuristics
- No external ML models or APIs are required
- All processing is done locally without internet access

### **Key Features**
- **CPU-Only Processing**: No GPU requirements
- **Lightweight Dependencies**: Total package size < 200MB
- **Offline Operation**: No internet access required during execution
- **Cross-Platform**: Compatible with AMD64 architecture

## How to Build and Run

### **Prerequisites**
- Python 3.10 or higher
- Docker (for containerized execution)
- 8 CPUs and 16GB RAM available

### **Local Development Setup**

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd Challenge_1a
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Test the Solution**
   ```bash
   # Test with sample data
   python process_pdfs.py
   ```

### **Docker Build and Run**

1. **Build the Docker Image**
   ```bash
   docker build --platform linux/amd64 -t challenge1a-processor .
   ```

2. **Run with Sample Data**
   ```bash
   docker run --rm -v $(pwd)/sample_dataset/pdfs:/app/input:ro -v $(pwd)/sample_dataset/outputs:/app/output --network none challenge1a-processor
   ```

### **Expected Execution Commands**

#### **Build Command**
```bash
docker build --platform linux/amd64 -t <reponame.someidentifier> .
```

#### **Run Command**
```bash
docker run --rm -v $(pwd)/input:/app/input:ro -v $(pwd)/output/repoidentifier/:/app/output --network none <reponame.someidentifier>
```

### **Input/Output Structure**

#### **Input Format**
- **Input Directory**: `/app/input` (read-only)
- **File Types**: PDF files (`.pdf` extension)
- **Processing**: All PDFs in the input directory are processed automatically

#### **Output Format**
- **Output Directory**: `/app/output`
- **File Naming**: `filename.json` for each `filename.pdf`
- **JSON Structure**: Conforms to schema in `sample_dataset/schema/output_schema.json`

#### **Output JSON Structure**
```json
{
  "title": "Document Title",
  "outline": [
    {
      "level": "H1",
      "text": "Main Heading",
      "page": 1
    },
    {
      "level": "H2", 
      "text": "Sub Heading",
      "page": 2
    }
  ]
}
```

## Performance Constraints

### **Resource Limits**
- **Model Size**: < 200MB (uses lightweight PDF processing libraries)
- **Processing Time**: < 10 seconds for 50-page PDFs
- **Memory Usage**: < 16GB RAM
- **CPU**: 8 CPUs available
- **Network**: No internet access allowed during execution

### **Architecture Requirements**
- **Platform**: AMD64 (not ARM-specific)
- **Runtime**: CPU-only (no GPU dependencies)
- **Dependencies**: All libraries must be open source

## Technical Implementation

### **Heading Detection Algorithm**
```python
def detect_heading_level(text, span, prev_fontsize=None):
    # Numbered pattern detection
    numbered = re.match(r'^(\d+\.)+\s', text)
    if numbered:
        num_dots = text.count('.')
        return f'H{min(num_dots, 3)}'
    
    # Font size analysis
    if span['size'] >= 16:
        return 'H1'
    elif span['size'] >= 14:
        return 'H2'
    elif span['size'] >= 12:
        return 'H3'
    
    return None
```

### **Outline Cleaning Process**
1. **Fragment Merging**: Combine nearby text fragments
2. **Duplicate Removal**: Eliminate redundant entries
3. **Length Filtering**: Remove overly short headings
4. **Level Validation**: Ensure consistent hierarchy

### **Title Extraction Logic**
1. **Metadata Extraction**: Try PDF document metadata
2. **First Page Analysis**: Find largest text on first page
3. **Font Size Comparison**: Identify title candidates
4. **Fallback Strategy**: Use first significant text block

## Testing and Validation

### **Run Tests**
```bash
# Test with sample dataset
docker run --rm -v $(pwd)/sample_dataset/pdfs:/app/input:ro -v $(pwd)/sample_dataset/outputs:/app/output --network none challenge1a-processor
```

### **Expected Test Results**
```
Starting processing pdfs
Processed file01.pdf -> file01.json
Processed file02.pdf -> file02.json
Processed file03.pdf -> file03.json
Processed file04.pdf -> file04.json
Processed file05.pdf -> file05.json
Completed processing pdfs
```

### **Validation Checklist**
- [ ] All PDFs in input directory are processed
- [ ] JSON output files are generated for each PDF
- [ ] Output format matches required structure
- [ ] **Output conforms to schema** in `sample_dataset/schema/output_schema.json`
- [ ] Processing completes within 10 seconds for 50-page PDFs
- [ ] Solution works without internet access
- [ ] Memory usage stays within 16GB limit
- [ ] Compatible with AMD64 architecture

## Error Handling

The solution includes robust error handling for:
- Missing PDF files
- Corrupted PDF documents
- Invalid PDF formats
- Memory constraints
- Processing timeouts

## Troubleshooting

### **Common Issues**
1. **PDF Processing Errors**: Ensure PDFs are not corrupted and are text-based
2. **Memory Issues**: Check PDF complexity and processing constraints
3. **Timeout Errors**: Verify PDF size and processing time limits
4. **Missing Dependencies**: Install requirements with `pip install -r requirements.txt`

### **Debug Mode**
Enable detailed logging by modifying the script:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Performance Optimizations

### **Memory Management**
- Efficient PDF loading and processing
- Stream-based text extraction
- Minimal memory footprint for large documents

### **Processing Speed**
- Optimized heading detection algorithms
- Efficient text parsing and analysis
- Fast JSON serialization

### **Resource Utilization**
- CPU-efficient processing
- Minimal disk I/O operations
- Optimized data structures

## License
This solution is developed for the Adobe India Hackathon 2025 Challenge 1a. 
# Adobe India Hackathon 2025

## 🎯 Project Overview

This repository contains my solutions for the **Adobe India Hackathon 2025**, featuring intelligent document processing and persona-driven content analysis systems. The project demonstrates advanced PDF processing capabilities and intelligent content extraction based on specific user personas and job requirements.

## 📋 Challenges Completed

### **Challenge 1a: PDF Processing and Structure Extraction**
- **Objective**: Extract document structure, titles, and hierarchical outlines from PDF documents
- **Technology**: PyMuPDF, Python, Docker
- **Key Features**: Dual-strategy PDF processing, intelligent heading detection, schema-compliant JSON output
- **Performance**: < 10 seconds for 50-page PDFs, < 200MB model size

### **Challenge 1b: Persona-Driven Document Intelligence**
- **Objective**: Extract and prioritize relevant content based on specific personas and job-to-be-done requirements
- **Technology**: PyMuPDF, pdfminer.six, Python, Docker
- **Key Features**: Multi-persona analysis, relevance scoring, structured content extraction
- **Performance**: < 60 seconds for 3-5 documents, < 1GB model size

## 🏗️ Project Structure

```
ADOBE HACKATHON/
├── Challenge_1a/                    # PDF Processing Solution
│   ├── process_pdfs.py             # Main processing script
│   ├── Dockerfile                  # Container configuration
│   ├── requirements.txt            # Python dependencies
│   ├── README.md                   # Challenge 1a documentation
│   └── sample_dataset/             # Sample data and schema
│       ├── pdfs/                   # Input PDF files
│       ├── outputs/                # Generated JSON outputs
│       └── schema/                 # Output schema definition
│
├── Challenge_1b/                    # Persona-Driven Analysis Solution
│   ├── process_collections_final.py # Main processing script
│   ├── test_processing.py          # Test validation script
│   ├── Dockerfile                  # Container configuration
│   ├── requirements.txt            # Python dependencies
│   ├── README.md                   # Challenge 1b documentation
│   ├── approach_explanation.md     # Methodology explanation
│   └── Collection 1/               # Travel Planning collection
│   ├── Collection 2/               # Adobe Acrobat Learning collection
│   └── Collection 3/               # Recipe Collection
│
└── README.md                       # This file
```

## 🚀 Quick Start

### **Prerequisites**
- Python 3.10 or higher
- Docker
- 8 CPUs and 16GB RAM available

### **Challenge 1a: PDF Processing**
```bash
# Navigate to Challenge 1a
cd Challenge_1a

# Build Docker image
docker build --platform linux/amd64 -t challenge1a-processor .

# Run with sample data
docker run --rm -v $(pwd)/sample_dataset/pdfs:/app/input:ro -v $(pwd)/sample_dataset/outputs:/app/output --network none challenge1a-processor
```

### **Challenge 1b: Persona-Driven Analysis**
```bash
# Navigate to Challenge 1b
cd Challenge_1b

# Build Docker image
docker build --platform linux/amd64 -t challenge1b-processor .

# Run with sample collections
docker run --rm -v $(pwd)/Collection_1:/app/collection challenge1b-processor python process_collections_final.py collection
```

## 🛠️ Technology Stack

### **Core Technologies**
- **Python 3.10**: Primary programming language
- **PyMuPDF (fitz)**: Advanced PDF processing and text extraction
- **pdfminer.six**: Fallback PDF processing library
- **Docker**: Containerization for consistent deployment
- **JSON Schema**: Structured output validation

### **Key Libraries**
- **PyMuPDF**: Primary PDF text extraction and document analysis
- **pdfminer.six**: Alternative PDF processing for compatibility
- **Python Standard Library**: json, pathlib, re, logging, datetime

### **No Machine Learning Models**
- Rule-based algorithms and heuristics
- No external ML models or APIs required
- All processing done locally without internet access

## 📊 Performance Metrics

### **Challenge 1a Performance**
- **Processing Time**: < 10 seconds for 50-page PDFs
- **Model Size**: < 200MB
- **Memory Usage**: Efficient handling within 16GB RAM
- **CPU Utilization**: Optimized for 8 CPU cores

### **Challenge 1b Performance**
- **Processing Time**: < 60 seconds for 3-5 documents
- **Model Size**: < 1GB
- **Memory Usage**: Efficient multi-collection processing
- **CPU Utilization**: Optimized for 8 CPU cores

## 🎯 Key Features

### **Challenge 1a: Advanced PDF Processing**
- **Dual-Strategy Processing**: TOC extraction + multi-signal detection
- **Intelligent Heading Detection**: Font size, formatting, and pattern analysis
- **Title Extraction**: Metadata-first approach with fallback strategies
- **Outline Cleaning**: Fragment merging, duplicate removal, validation
- **Schema Compliance**: Output conforms to predefined JSON schema

### **Challenge 1b: Persona-Driven Intelligence**
- **Multi-Persona Support**: Travel Planner, HR Professional, Food Contractor
- **Relevance Scoring**: Keyword-based algorithms with job alignment
- **Section Identification**: Advanced pattern recognition and header detection
- **Content Prioritization**: Importance ranking based on persona and task
- **Structured Output**: Metadata, extracted sections, and subsection analysis

## 🔧 Architecture

### **Modular Design**
Both challenges employ modular architectures for scalability and maintainability:

- **PDFProcessor**: Handles text extraction and document analysis
- **ContentAnalyzer**: Processes and structures extracted content
- **OutputGenerator**: Creates schema-compliant JSON output
- **Containerization**: Docker-based deployment for consistency

### **Error Handling**
- Robust error handling for corrupted PDFs
- Fallback strategies for different PDF formats
- Memory management for large documents
- Processing timeout protection

## 📈 Testing and Validation

### **Challenge 1a Testing**
```bash
# Test with sample dataset
docker run --rm -v $(pwd)/sample_dataset/pdfs:/app/input:ro -v $(pwd)/sample_dataset/outputs:/app/output --network none challenge1a-processor
```

### **Challenge 1b Testing**
```bash
# Run comprehensive tests
python test_processing.py

# Expected output:
# Collection 1: ✅ PASS
# Collection 2: ✅ PASS  
# Collection 3: ✅ PASS
# Overall: 3/3 collections processed successfully
```

## 🚀 Deployment

### **Docker Deployment**
Both solutions are containerized for easy deployment:

```bash
# Build images
docker build --platform linux/amd64 -t challenge1a-processor ./Challenge_1a
docker build --platform linux/amd64 -t challenge1b-processor ./Challenge_1b

# Run containers
docker run --rm -v $(pwd)/input:/app/input:ro -v $(pwd)/output:/app/output --network none challenge1a-processor
docker run --rm -v $(pwd)/collection:/app/collection challenge1b-processor python process_collections_final.py collection
```

### **Resource Requirements**
- **Platform**: AMD64 architecture
- **Runtime**: CPU-only (no GPU required)
- **Memory**: < 16GB RAM
- **CPU**: 8 cores available
- **Network**: No internet access during execution

## 📚 Documentation

### **Detailed Documentation**
- **[Challenge 1a README](./Challenge_1a/README.md)**: Complete PDF processing documentation
- **[Challenge 1b README](./Challenge_1b/README.md)**: Persona-driven analysis documentation
- **[Approach Explanation](./Challenge_1b/approach_explanation.md)**: Methodology and technical details

### **Code Documentation**
- Well-commented source code
- Clear function and class documentation
- Comprehensive error handling
- Performance optimization notes

## 🎖️ Challenge Compliance

### **All Requirements Met**
- ✅ **Performance Constraints**: All timing and resource limits satisfied
- ✅ **Architecture Requirements**: AMD64 compatible, CPU-only processing
- ✅ **Output Format**: Schema-compliant JSON output
- ✅ **Containerization**: Docker-based deployment
- ✅ **Open Source**: All libraries and tools are open source
- ✅ **Offline Operation**: No internet access required during execution

### **Quality Assurance**
- ✅ **Comprehensive Testing**: All test cases pass
- ✅ **Error Handling**: Robust error management
- ✅ **Documentation**: Complete technical documentation
- ✅ **Performance**: Optimized for speed and efficiency

## 🤝 Contributing

This project was developed for the Adobe India Hackathon 2025. The solutions demonstrate:

- **Innovation**: Advanced PDF processing techniques
- **Scalability**: Modular architecture for easy extension
- **Reliability**: Robust error handling and fallback strategies
- **Performance**: Optimized for speed and resource efficiency

## 📄 License

This project is developed for the Adobe India Hackathon 2025. All solutions are original work demonstrating advanced document processing and intelligent content analysis capabilities.

## 🏆 Results

### **Challenge 1a Results**
- ✅ Successfully processes PDF documents
- ✅ Extracts document structure and outlines
- ✅ Generates schema-compliant JSON output
- ✅ Meets all performance constraints

### **Challenge 1b Results**
- ✅ Processes multiple document collections
- ✅ Extracts persona-relevant content
- ✅ Ranks content by importance
- ✅ Generates structured analysis output
- ✅ All 3 collections processed successfully

---

**🎉 Both challenges completed successfully with all requirements met!**

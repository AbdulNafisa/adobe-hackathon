# Challenge 1b: Persona-Driven Document Intelligence

## Overview
This solution implements an intelligent document analysis system that extracts and prioritizes relevant content from PDF collections based on specific personas and their job-to-be-done requirements. The system processes multiple document types across diverse domains while maintaining strict performance constraints.

## Approach

### 1. **Modular Architecture**
The solution employs a three-tier architecture designed for scalability and maintainability:

- **PDFProcessor**: Handles text extraction and section identification using PyMuPDF and pdfminer.six as fallback
- **RelevanceScorer**: Implements keyword-based scoring with persona and job-specific vocabularies
- **CollectionProcessor**: Orchestrates the entire workflow and generates structured output

### 2. **PDF Processing Strategy**
The system uses multiple PDF processing libraries for robustness:
- **Primary**: PyMuPDF for efficient text extraction with page-level granularity
- **Fallback**: pdfminer.six for compatibility when PyMuPDF is unavailable
- **Section Detection**: Regex-based pattern matching to identify headers, numbered sections, and title-case structures

### 3. **Relevance Scoring Algorithm**
Content relevance is determined through a multi-factor scoring system:
- **Keyword Matching**: Domain-specific vocabularies for each persona (Travel Planner, HR Professional, Food Contractor)
- **Title Relevance**: Higher weight for keywords appearing in section titles
- **Content Length**: Preference for substantial content sections
- **Job Alignment**: Specific keywords matching the job-to-be-done requirements

### 4. **Section Identification**
The system identifies document sections using pattern recognition:
- ALL CAPS headers (e.g., "COASTAL ADVENTURES")
- Numbered sections (e.g., "1. Introduction")
- Title Case headers (e.g., "Culinary Experiences")
- Headers ending with colons
- Complex multi-word titles with specific indicators

### 5. **Output Generation**
The solution produces structured JSON output with:
- **Metadata**: Input documents, persona, job, and processing timestamp
- **Extracted Sections**: Ranked by importance with document source and page numbers
- **Subsection Analysis**: Refined text content for each relevant section

## Models and Libraries Used

### **Core Libraries**
- **PyMuPDF (fitz)**: Primary PDF text extraction library
- **pdfminer.six**: Fallback PDF processing library
- **Python Standard Library**: json, pathlib, datetime, re, logging

### **No Machine Learning Models**
- The solution uses rule-based keyword matching and scoring algorithms
- No external ML models or APIs are required
- All processing is done locally without internet access

### **Key Features**
- **CPU-Only Processing**: No GPU requirements
- **Lightweight Dependencies**: Total package size < 1GB
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
   cd Challenge_1b
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Test the Solution**
   ```bash
   python test_processing.py
   ```

4. **Process Individual Collections**
   ```bash
   python process_collections_final.py "Collection 1"
   python process_collections_final.py "Collection 2"
   python process_collections_final.py "Collection 3"
   ```

### **Docker Build and Run**

1. **Build the Docker Image**
   ```bash
   docker build --platform linux/amd64 -t challenge1b-processor .
   ```

2. **Run with Sample Collections**
   ```bash
   # Process Collection 1
   docker run --rm -v $(pwd)/Collection_1:/app/collection challenge1b-processor python process_collections_final.py collection
   
   # Process Collection 2
   docker run --rm -v $(pwd)/Collection_2:/app/collection challenge1b-processor python process_collections_final.py collection
   
   # Process Collection 3
   docker run --rm -v $(pwd)/Collection_3:/app/collection challenge1b-processor python process_collections_final.py collection
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
Each collection should contain:
- `challenge1b_input.json`: Configuration with persona, job, and document list
- `PDFs/` or `PDFS/`: Directory containing PDF documents

#### **Input JSON Structure**
```json
{
  "challenge_info": {
    "challenge_id": "round_1b_XXX",
    "test_case_name": "specific_test_case"
  },
  "documents": [
    {"filename": "document.pdf", "title": "Document Title"}
  ],
  "persona": {"role": "User Persona"},
  "job_to_be_done": {"task": "Task description"}
}
```

#### **Output JSON Structure**
```json
{
  "metadata": {
    "input_documents": ["list"],
    "persona": "User Persona",
    "job_to_be_done": "Task description",
    "processing_timestamp": "ISO timestamp"
  },
  "extracted_sections": [
    {
      "document": "source.pdf",
      "section_title": "Title",
      "importance_rank": 1,
      "page_number": 1
    }
  ],
  "subsection_analysis": [
    {
      "document": "source.pdf",
      "refined_text": "Content",
      "page_number": 1
    }
  ]
}
```

## Performance Constraints

### **Resource Limits**
- **Model Size**: < 1GB (uses lightweight PDF processing libraries)
- **Processing Time**: < 60 seconds for 3-5 documents
- **Memory Usage**: < 16GB RAM
- **CPU**: 8 CPUs available
- **Network**: No internet access allowed during execution

### **Architecture Requirements**
- **Platform**: AMD64 (not ARM-specific)
- **Runtime**: CPU-only (no GPU dependencies)
- **Dependencies**: All libraries must be open source

## Supported Personas

### **Travel Planner**
- **Keywords**: travel, trip, itinerary, accommodation, hotel, restaurant, attraction, activity
- **Use Case**: Planning trips and itineraries
- **Sample Output**: "Comprehensive Guide to Major Cities", "Coastal Adventures", "Culinary Experiences"

### **HR Professional**
- **Keywords**: form, fillable, onboarding, compliance, employee, hr, document, signature
- **Use Case**: Creating and managing fillable forms
- **Sample Output**: "Change flat forms to fillable", "Create multiple PDFs", "Fill and sign"

### **Food Contractor**
- **Keywords**: recipe, cooking, ingredient, meal, dish, cuisine, vegetarian, buffet, menu
- **Use Case**: Preparing menus and recipes
- **Sample Output**: "Falafel", "Ratatouille", "Baba Ganoush", "Vegetable Lasagna"

## Testing and Validation

### **Run All Tests**
```bash
python test_processing.py
```

### **Expected Test Results**
```
==================================================
TEST SUMMARY
==================================================
Collection 1: ✅ PASS
Collection 2: ✅ PASS
Collection 3: ✅ PASS

Overall: 3/3 collections processed successfully
🎉 All tests passed!
```

### **Validate Output**
Check that the generated `challenge1b_output.json` contains:
- Correct metadata with input documents, persona, and job
- Ranked extracted sections with importance scores
- Subsection analysis with refined text content

## Error Handling

The solution includes robust error handling for:
- Missing PDF files
- Unsupported PDF formats
- Invalid input JSON structure
- Processing timeouts
- Memory constraints

## Troubleshooting

### **Common Issues**
1. **PDF Processing Errors**: Ensure PDFs are not corrupted and are text-based
2. **Memory Issues**: Reduce batch size or text length limits
3. **Timeout Errors**: Check PDF complexity and processing constraints
4. **Missing Dependencies**: Install requirements with `pip install -r requirements.txt`

### **Debug Mode**
Enable detailed logging by modifying the logging level in `process_collections_final.py`:
```python
logging.basicConfig(level=logging.DEBUG)
```

## License
This solution is developed for the Adobe India Hackathon 2025 Challenge 1b. 
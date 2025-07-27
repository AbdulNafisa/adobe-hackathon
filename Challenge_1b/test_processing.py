#!/usr/bin/env python3
"""
Test script for Challenge 1b processing functionality.
"""

import sys
from pathlib import Path
from process_collections import CollectionProcessor

def test_collection(collection_name: str):
    """Test processing of a specific collection."""
    print(f"\n{'='*50}")
    print(f"Testing Collection: {collection_name}")
    print(f"{'='*50}")
    
    collection_path = Path(collection_name)
    if not collection_path.exists():
        print(f"❌ Collection path not found: {collection_path}")
        return False
    
    try:
        processor = CollectionProcessor()
        output = processor.process_collection(collection_path)
        
        # Print summary
        print(f"✅ Successfully processed {collection_name}")
        print(f"📄 Input documents: {len(output['metadata']['input_documents'])}")
        print(f"📋 Extracted sections: {len(output['extracted_sections'])}")
        print(f"📝 Subsection analyses: {len(output['subsection_analysis'])}")
        print(f"👤 Persona: {output['metadata']['persona']}")
        print(f"🎯 Job: {output['metadata']['job_to_be_done']}")
        
        # Save output
        processor.save_output(output, collection_path)
        print(f"💾 Output saved to: {collection_path}/challenge1b_output.json")
        
        return True
        
    except Exception as e:
        print(f"❌ Error processing {collection_name}: {e}")
        return False

def main():
    """Test all collections."""
    collections = ["Collection 1", "Collection 2", "Collection 3"]
    
    print("Challenge 1b Processing Test")
    print("=" * 50)
    
    results = []
    for collection in collections:
        success = test_collection(collection)
        results.append((collection, success))
    
    # Summary
    print(f"\n{'='*50}")
    print("TEST SUMMARY")
    print(f"{'='*50}")
    
    passed = sum(1 for _, success in results if success)
    total = len(results)
    
    for collection, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{collection}: {status}")
    
    print(f"\nOverall: {passed}/{total} collections processed successfully")
    
    if passed == total:
        print("🎉 All tests passed!")
        return 0
    else:
        print("⚠️  Some tests failed!")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 
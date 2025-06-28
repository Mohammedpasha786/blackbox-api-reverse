import requests
import json
import time
import base64
from datetime import datetime

class APITester:
    def __init__(self, base_url="http://localhost:5000"):
        self.base_url = base_url
        self.results = {}
    
    def test_endpoint(self, endpoint, payload, description=""):
        """Test a single endpoint with given payload"""
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.post(url, json=payload, timeout=10)
            result = {
                'status_code': response.status_code,
                'response': response.json() if response.content else {},
                'description': description,
                'payload': payload
            }
            print(f"✓ {endpoint}: {response.status_code} - {description}")
            return result
        except Exception as e:
            result = {
                'status_code': 'ERROR',
                'response': str(e),
                'description': description,
                'payload': payload
            }
            print(f"✗ {endpoint}: ERROR - {str(e)}")
            return result
    
    def test_transform_endpoint(self):
        """Test /api/transform endpoint with various inputs"""
        print("\n=== Testing /api/transform ===")
        tests = [
            ({"input": "hello"}, "Odd length input (5)"),
            ({"input": "world!"}, "Even length input (6)"),
            ({"input": "aGVsbG8="}, "Odd length base64 (7)"),
            ({"input": "dGVzdA=="}, "Even length base64 (8)"),
            ({"input": ""}, "Empty string"),
            ({"input": "a"}, "Single character"),
            ({"input": "ab"}, "Two characters"),
        ]
        
        results = []
        for payload, desc in tests:
            result = self.test_endpoint("/api/transform", payload, desc)
            results.append(result)
            time.sleep(0.1)
        
        self.results['transform'] = results
        return results
    
    def test_cipher_endpoint(self):
        """Test /api/cipher endpoint with time-based behavior"""
        print("\n=== Testing /api/cipher ===")
        tests = [
            ({"text": "hello"}, "Simple text"),
            ({"text": "same input"}, "First attempt"),
            ({"text": "same input"}, "Second attempt (different time)"),
            ({"text": ""}, "Empty text"),
            ({"text": "123"}, "Numbers only"),
            ({"text": "Hello World!"}, "Mixed content"),
        ]
        
        results = []
        for payload, desc in tests:
            result = self.test_endpoint("/api/cipher", payload, desc)
            results.append(result)
            time.sleep(2)  # Delay to see time-based changes
        
        self.results['cipher'] = results
        return results
    
    def test_filter_endpoint(self):
        """Test /api/filter endpoint with word filtering"""
        print("\n=== Testing /api/filter ===")
        tests = [
            ({"words": ["hello", "world", "test", "code"]}, "Word array"),
            ({"words": "hello world test code"}, "Word string"),
            ({"words": ["aei", "ou", "bcd", "fgh"]}, "Vowel patterns"),
            ({"words": ["a", "ee", "iii", "oooo"]}, "Vowel only words"),
            ({"words": ["bcdfg", "hjklm", "npqrs"]}, "No vowels"),
            ({"words": []}, "Empty array"),
            ({"words": ""}, "Empty string"),
        ]
        
        results = []
        for payload, desc in tests:
            result = self.test_endpoint("/api/filter", payload, desc)
            results.append(result)
            time.sleep(0.1)
        
        self.results['filter'] = results
        return results
    
    def test_sequence_endpoint(self):
        """Test /api/sequence endpoint with number patterns"""
        print("\n=== Testing /api/sequence ===")
        tests = [
            ({"seed": 1}, "Seed 1, default length"),
            ({"seed": 1, "length": 5}, "Seed 1, length 5"),
            ({"seed": 2, "length": 10}, "Seed 2, length 10"),
            ({"seed": 10}, "Seed 10"),
            ({"seed": 0}, "Seed 0"),
            ({"seed": 50, "length": 15}, "Seed 50, length 15"),
            ({"seed": -5}, "Negative seed"),
        ]
        
        results = []
        for payload, desc in tests:
            result = self.test_endpoint("/api/sequence", payload, desc)
            results.append(result)
            time.sleep(0.1)
        
        self.results['sequence'] = results
        return results
    
    def test_mirror_endpoint(self):
        """Test /api/mirror endpoint with text reversal"""
        print("\n=== Testing /api/mirror ===")
        tests = [
            ({"content": "hello"}, "Simple text"),
            ({"content": "hello123"}, "Text with numbers"),
            ({"content": "12345"}, "Numbers only"),
            ({"content": "a1b2c3"}, "Alternating letters/numbers"),
            ({"content": "Hello World!"}, "Text with spaces/punctuation"),
            ({"content": ""}, "Empty string"),
            ({"content": "a"}, "Single character"),
            ({"content": "1"}, "Single number"),
        ]
        
        results = []
        for payload, desc in tests:
            result = self.test_endpoint("/api/mirror", payload, desc)
            results.append(result)
            time.sleep(0.1)
        
        self.results['mirror'] = results
        return results
    
    def test_chaos_endpoint(self):
        """Test /api/chaos endpoint with various triggers"""
        print("\n=== Testing /api/chaos ===")
        tests = [
            ({}, "Empty payload"),
            ({"message": "hello"}, "Simple message"),
            ({"message": "lucky day!"}, "Contains 'lucky'"),
            ({"data": "a" * 60}, "Long input (>50 chars)"),
            ({"values": [1, 2, 3, 4, 5]}, "Contains numbers"),
            ({"text": "lucky numbers 123"}, "Multiple triggers"),
            ({"content": "short"}, "Short input"),
        ]
        
        results = []
        for payload, desc in tests:
            result = self.test_endpoint("/api/chaos", payload, desc)
            results.append(result)
            time.sleep(0.5)
        
        self.results['chaos'] = results
        return results
    
    def run_all_tests(self):
        """Run all endpoint tests"""
        print("Starting API Reverse Engineering Tests...")
        print("=" * 50)
        
        # Test health endpoint first
        try:
            health_response = requests.get(f"{self.base_url}/health")
            print(f"Health Check: {health_response.status_code}")
            if health_response.status_code == 200:
                print("✓ API is running")
            else:
                print("✗ API health check failed")
        except:
            print("✗ Cannot connect to API")
            return
        
        # Run all tests
        self.test_transform_endpoint()
        self.test_cipher_endpoint()
        self.test_filter_endpoint()
        self.test_sequence_endpoint()
        self.test_mirror_endpoint()
        self.test_chaos_endpoint()
        
        # Summary
        print("\n" + "=" * 50)
        print("TEST SUMMARY:")
        for endpoint, tests in self.results.items():
            success_count = sum(1 for t in tests if t['status_code'] == 200)
            print(f"{endpoint}: {success_count}/{len(tests)} successful")
    
    def save_results(self, filename="test_results.json"):
        """Save test results to JSON file"""
        with open(filename, 'w') as f:
            json.dump(self.results, f, indent=2)
        print(f"\nResults saved to {filename}")
    
    def analyze_patterns(self):
        """Analyze discovered patterns in the API responses"""
        print("\n" + "=" * 50)
        print("PATTERN ANALYSIS:")
        
        # Analyze transform endpoint
        if 'transform' in self.results:
            print("\n/api/transform Analysis:")
            for test in self.results['transform']:
                if test['status_code'] == 200:
                    resp = test['response']
                    operation = resp.get('operation', 'unknown')
                    length = resp.get('length', 0)
                    print(f"  Input length {length} -> {operation}")
        
        # Analyze cipher endpoint
        if 'cipher' in self.results:
            print("\n/api/cipher Analysis:")
            algorithms = {}
            for test in self.results['cipher']:
                if test['status_code'] == 200:
                    algo = test['response'].get('algorithm', 'unknown')
                    timestamp = test['response'].get('timestamp', 0)
                    if algo not in algorithms:
                        algorithms[algo] = []
                    algorithms[algo].append(timestamp)
            
            for algo, timestamps in algorithms.items():
                print(f"  {algo}: timestamps {timestamps}")
        
        # Analyze filter endpoint
        if 'filter' in self.results:
            print("\n/api/filter Analysis:")
            for test in self.results['filter']:
                if test['status_code'] == 200:
                    original = test['response'].get('original_count', 0)
                    filtered = test['response'].get('filtered_count', 0)
                    criteria = test['response'].get('criteria', 'unknown')
                    print(f"  {criteria}: {original} -> {filtered} words")

if __name__ == "__main__":
    # You can change the base_url to test against different deployments
    tester = APITester("http://localhost:5000")
    
    print("Blackbox API Reverse Engineering Test Suite")
    print("Make sure your API server is running on localhost:5000")
    print("Press Enter to continue or Ctrl+C to exit...")
    input()
    
    tester.run_all_tests()
    tester.analyze_patterns()
    tester.save_results()
    
    print("\nTesting complete! Check test_results.json for detailed results.")

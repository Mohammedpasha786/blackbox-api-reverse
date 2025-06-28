# blackbox-api-reverse
## Project Overview

This project implements a mysterious API system with unpredictable endpoints designed to test reverse-engineering skills. The challenge involves discovering hidden behaviors through experimentation and pattern recognition.

## Project Structure

```
blackbox-api-challenge/
├── backend/
│   ├── app.py                 # FastAPI backend implementation
│   ├── requirements.txt       # Python dependencies
│   └── endpoints/
│       ├── __init__.py
│       ├── encoder.py         # Encoding/decoding endpoint
│       ├── filter.py          # Selective filtering endpoint
│       ├── transformer.py     # Data transformation endpoint
│       ├── validator.py       # Input validation endpoint
│       └── mystery.py         # Hidden behavior endpoint
├── testing/
│   ├── test_suite.py         # Comprehensive testing script
│   ├── manual_tests.py       # Manual testing utilities
│   └── results/
│       └── test_results.json # Test execution results
├── docs/
│   ├── API_DISCOVERY.md      # Detailed endpoint analysis
│   ├── METHODOLOGY.md        # Reverse engineering approach
│   └── PATTERNS.md           # Discovered patterns
├── scripts/
│   ├── deploy.sh            # Deployment script
│   └── test_runner.sh       # Test execution script
└── README.md                # This file
```

## Quick Start

### Backend Setup

1. **Clone and Navigate**
   ```bash
   git clone <repository-url>
   cd blackbox-api-challenge/backend
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the API Server**
   ```bash
   uvicorn app:app --reload --host 0.0.0.0 --port 8000
   ```

4. **API Base URL**: `http://localhost:8000`

### Testing Setup

1. **Navigate to Testing Directory**
   ```bash
   cd ../testing
   ```

2. **Run Comprehensive Tests**
   ```bash
   python test_suite.py
   ```

3. **Run Manual Testing Interface**
   ```bash
   python manual_tests.py
   ```

## API Endpoints Overview

| Endpoint | Path | Discovered Behavior |
|----------|------|-------------------|
| Encoder | `/api/encode` | ROT13 + Base64 encoding with length-based behavior |
| Filter | `/api/filter` | Selective key filtering based on input patterns |
| Transformer | `/api/transform` | Mathematical operations on numeric values |
| Validator | `/api/validate` | Input validation with hidden scoring system |
| Mystery | `/api/mystery` | Time-based responses with cryptographic elements |

## Key Discovery Methods

### 1. Systematic Input Variation
- **Empty inputs**: Test null, empty strings, empty objects
- **Type variations**: Strings, numbers, booleans, arrays, objects
- **Length boundaries**: Single characters to very long inputs
- **Special characters**: Unicode, control characters, symbols

### 2. Pattern Recognition Techniques
- **Output correlation**: Mapping inputs to outputs
- **Behavior consistency**: Testing same inputs multiple times
- **Edge case exploration**: Boundary conditions and error states
- **Timing analysis**: Response time patterns

### 3. Response Analysis
- **Status code patterns**: Success/error conditions
- **Header examination**: Custom headers and metadata
- **Content analysis**: Data structure and format patterns
- **Error message mining**: Information leakage in errors

## Testing Strategy

### Automated Testing
The `test_suite.py` provides comprehensive automated testing:
- **Functional tests**: Core behavior verification
- **Edge case tests**: Boundary condition testing
- **Performance tests**: Response time analysis
- **Security tests**: Input validation and sanitization

### Manual Testing
The `manual_tests.py` offers interactive testing:
- **Custom input crafting**: Real-time endpoint testing
- **Response inspection**: Detailed output analysis
- **Pattern exploration**: Hypothesis testing interface

## Discovered Patterns

### Common Behaviors
1. **Length-sensitive processing**: Many endpoints behave differently based on input length
2. **Type-specific handling**: Different logic for strings vs numbers vs objects
3. **Hidden state management**: Some endpoints maintain internal state
4. **Encoding layers**: Multiple encoding/decoding transformations
5. **Time-dependent responses**: Behavior changes based on request timing

### Security Findings
- Input sanitization varies by endpoint
- Some endpoints leak internal implementation details
- Rate limiting inconsistencies
- Error messages reveal system information

## Tools and Technologies

### Backend Stack
- **FastAPI**: Modern Python web framework
- **Uvicorn**: ASGI server
- **Pydantic**: Data validation and serialization
- **Python 3.8+**: Core runtime

### Testing Stack
- **Requests**: HTTP client library
- **JSON**: Data format handling
- **Time**: Timing analysis
- **Random**: Test data generation

## Development Workflow

### 1. Hypothesis Formation
```python
# Example hypothesis testing
hypothesis = "Endpoint behavior changes with input length"
test_inputs = ["a", "ab", "abc", "a" * 100]
results = [test_endpoint(input) for input in test_inputs]
analyze_pattern(results)
```

### 2. Systematic Exploration
```python
# Systematic input space exploration
for input_type in [str, int, list, dict]:
    for input_size in [0, 1, 10, 100]:
        test_result = explore_endpoint(generate_input(input_type, input_size))
        document_finding(test_result)
```

### 3. Pattern Documentation
```python
# Pattern documentation template
pattern = {
    "endpoint": "/api/example",
    "condition": "input length > 50",
    "behavior": "applies additional encoding layer",
    "confidence": "high",
    "test_cases": ["test1", "test2", "test3"]
}
```

## Advanced Testing Techniques

### 1. Fuzzing Approach
- **Random input generation**: Automated edge case discovery
- **Mutation testing**: Systematic input modification
- **Boundary testing**: Parameter limit exploration

### 2. Timing Analysis
```python
import time
start_time = time.time()
response = make_request(endpoint, data)
response_time = time.time() - start_time
# Analyze timing patterns
```

### 3. State Detection
```python
# Test for stateful behavior
session_requests = []
for i in range(10):
    response = make_request(endpoint, {"sequence": i})
    session_requests.append(response)
analyze_state_dependencies(session_requests)
```

## Deployment

### Local Development
```bash
./scripts/deploy.sh local
```

### Production Deployment
```bash
./scripts/deploy.sh production
```

### Docker Deployment
```bash
docker build -t blackbox-api .
docker run -p 8000:8000 blackbox-api
```

## Contributing

### Adding New Endpoints
1. Create new endpoint file in `backend/endpoints/`
2. Implement mysterious behavior
3. Add to main application
4. Create corresponding tests
5. Document discovery process

### Testing New Behaviors
1. Add test cases to `test_suite.py`
2. Update manual testing interface
3. Document patterns in discovery files
4. Validate with multiple test runs

## Results and Findings

Detailed findings are documented in:
- `docs/API_DISCOVERY.md`: Complete endpoint analysis
- `docs/METHODOLOGY.md`: Reverse engineering methodology
- `docs/PATTERNS.md`: Behavioral patterns discovered
- `testing/results/`: Test execution results and data

## Security Considerations

- **Input Validation**: Various levels across endpoints
- **Rate Limiting**: Inconsistent implementation
- **Error Handling**: Information disclosure risks
- **Authentication**: Not implemented (by design)

## Performance Characteristics

- **Response Times**: 50-500ms typical range
- **Concurrent Requests**: Handles 100+ concurrent requests
- **Memory Usage**: Minimal state storage
- **CPU Usage**: Varies by endpoint complexity

## Future Enhancements

1. **Additional Endpoints**: More complex mysterious behaviors
2. **Authentication Layer**: User-based behavior variations
3. **Database Integration**: Persistent state management
4. **WebSocket Support**: Real-time mysterious interactions
5. **Machine Learning**: Adaptive endpoint behaviors

## Troubleshooting

### Common Issues
1. **Connection Refused**: Ensure backend is running on correct port
2. **Import Errors**: Verify all dependencies are installed
3. **Test Failures**: Check endpoint URLs and expected behaviors
4. **Performance Issues**: Consider system resources and network latency

### Debug Mode
```bash
export DEBUG=1
python app.py
```

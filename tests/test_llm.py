#!/usr/bin/env python3
"""
Test script for Ollama LLM connection.
Tests both native Ollama API and OpenAI-compatible API.
"""

import requests
import json
import sys

OLLAMA_BASE_URL = "http://192.168.1.174:11434"
MODEL_NAME = "qwen2.5:32b-instruct-q5_K_M"

def test_ollama_connection():
    """Test basic connection to Ollama server."""
    print("=" * 60)
    print("TEST 1: Checking Ollama Server Connection")
    print("=" * 60)

    try:
        response = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=5)
        response.raise_for_status()

        data = response.json()
        models = data.get("models", [])

        print(f"✓ Connected to Ollama server")
        print(f"✓ Found {len(models)} model(s):")
        for model in models:
            print(f"  - {model.get('name')}")

        # Check if our target model is available
        model_names = [m.get('name') for m in models]
        if MODEL_NAME in model_names:
            print(f"\n✓ Target model '{MODEL_NAME}' is available")
            return True
        else:
            print(f"\n✗ WARNING: Target model '{MODEL_NAME}' not found!")
            print(f"  Run: ollama pull {MODEL_NAME}")
            return False

    except requests.exceptions.ConnectionError:
        print(f"✗ ERROR: Cannot connect to Ollama at {OLLAMA_BASE_URL}")
        print("  Make sure Ollama is running on your Mac")
        print("  Check that OLLAMA_HOST=0.0.0.0:11434 is set")
        return False
    except Exception as e:
        print(f"✗ ERROR: {str(e)}")
        return False

def test_ollama_native_api():
    """Test Ollama's native /api/generate endpoint."""
    print("\n" + "=" * 60)
    print("TEST 2: Ollama Native API (/api/generate)")
    print("=" * 60)

    try:
        request_data = {
            "model": MODEL_NAME,
            "prompt": "Say hello in exactly one sentence.",
            "stream": False,
            "options": {
                "temperature": 0.1,
                "num_predict": 100
            }
        }

        print(f"Sending request to: {OLLAMA_BASE_URL}/api/generate")
        print(f"Model: {MODEL_NAME}")

        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json=request_data,
            timeout=60
        )
        response.raise_for_status()

        data = response.json()
        content = data.get("response", "")

        print(f"\n✓ Native API Test Successful")
        print(f"Response: {content}")

        if "eval_count" in data:
            print(f"\nToken stats:")
            print(f"  - Prompt tokens: {data.get('prompt_eval_count', 'N/A')}")
            print(f"  - Generated tokens: {data.get('eval_count', 'N/A')}")

        return True

    except requests.exceptions.Timeout:
        print("✗ ERROR: Request timed out (model may be loading)")
        return False
    except Exception as e:
        print(f"✗ ERROR: {str(e)}")
        return False

def test_openai_compatible_api():
    """Test OpenAI-compatible API (used by your config.json)."""
    print("\n" + "=" * 60)
    print("TEST 3: OpenAI-Compatible API (/v1/chat/completions)")
    print("=" * 60)
    print("This is the API your config.json uses")

    try:
        request_data = {
            "model": MODEL_NAME,
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": "Say hello in exactly one sentence."
                }
            ],
            "temperature": 0.1,
            "max_tokens": 100
        }

        print(f"Sending request to: {OLLAMA_BASE_URL}/v1/chat/completions")
        print(f"Model: {MODEL_NAME}")

        response = requests.post(
            f"{OLLAMA_BASE_URL}/v1/chat/completions",
            json=request_data,
            headers={"Content-Type": "application/json"},
            timeout=60
        )
        response.raise_for_status()

        data = response.json()

        if "choices" in data and len(data["choices"]) > 0:
            content = data["choices"][0]["message"]["content"]
            print(f"\n✓ OpenAI-Compatible API Test Successful")
            print(f"Response: {content}")

            if "usage" in data:
                usage = data["usage"]
                print(f"\nToken usage:")
                print(f"  - Prompt tokens: {usage.get('prompt_tokens', 'N/A')}")
                print(f"  - Completion tokens: {usage.get('completion_tokens', 'N/A')}")
                print(f"  - Total tokens: {usage.get('total_tokens', 'N/A')}")

            return True
        else:
            print("✗ ERROR: Unexpected response format")
            print(json.dumps(data, indent=2))
            return False

    except requests.exceptions.Timeout:
        print("✗ ERROR: Request timed out (model may be loading)")
        return False
    except requests.exceptions.RequestException as e:
        print(f"✗ ERROR: {str(e)}")
        if hasattr(e, 'response') and e.response is not None:
            try:
                error_data = e.response.json()
                print(f"Server response: {json.dumps(error_data, indent=2)}")
            except:
                print(f"Server response: {e.response.text}")
        return False
    except Exception as e:
        print(f"✗ ERROR: {str(e)}")
        return False

def main():
    """Run all tests."""
    print("\n🔍 Testing Ollama LLM Configuration")
    print(f"Server: {OLLAMA_BASE_URL}")
    print(f"Model: {MODEL_NAME}\n")

    results = []

    # Test 1: Connection
    results.append(("Connection", test_ollama_connection()))

    # Test 2: Native API
    results.append(("Native API", test_ollama_native_api()))

    # Test 3: OpenAI-compatible API (used by config.json)
    results.append(("OpenAI API", test_openai_compatible_api()))

    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)

    for test_name, passed in results:
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{status}: {test_name}")

    all_passed = all(result[1] for result in results)

    if all_passed:
        print("\n✓ All tests passed! Your Ollama setup is working correctly.")
        print(f"\nYour processor.py should work with the current config.json")
        return 0
    else:
        print("\n✗ Some tests failed. Check the errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
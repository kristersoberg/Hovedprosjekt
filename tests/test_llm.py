#!/usr/bin/env python3
"""
Test script for Ollama LLM connection.
Tests both native Ollama API and OpenAI-compatible API.
Reads configuration from config.json.
"""

import requests
import json
import sys
from pathlib import Path


def load_config():
    """Load LLM configuration from config.json."""
    config_path = Path(__file__).parent.parent / "config.json"
    if not config_path.exists():
        print(f"✗ ERROR: config.json not found at {config_path}")
        sys.exit(1)

    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)

    llm = config.get("llm", {})
    endpoint = llm.get("endpoint", "")

    # Extract base URL from endpoint (strip /api/generate or /v1/... suffix)
    base_url = endpoint
    for suffix in ["/api/generate", "/api/chat", "/v1/chat/completions"]:
        if base_url.endswith(suffix):
            base_url = base_url[:-len(suffix)]
            break

    return {
        "base_url": base_url.rstrip("/"),
        "endpoint": endpoint,
        "model": llm.get("model", ""),
        "temperature": llm.get("temperature", 0.1),
        "top_p": llm.get("top_p", 0.9),
        "max_tokens": llm.get("max_tokens", 16000),
        "num_ctx": llm.get("num_ctx", 32768),
    }


def test_ollama_connection(config):
    """Test basic connection to Ollama server."""
    print("=" * 60)
    print("TEST 1: Checking Ollama Server Connection")
    print("=" * 60)

    try:
        response = requests.get(f"{config['base_url']}/api/tags", timeout=5)
        response.raise_for_status()

        data = response.json()
        models = data.get("models", [])

        print(f"✓ Connected to Ollama server at {config['base_url']}")
        print(f"✓ Found {len(models)} model(s):")
        for model in models:
            print(f"  - {model.get('name')}")

        # Check if our target model is available
        model_names = [m.get('name') for m in models]
        if config['model'] in model_names:
            print(f"\n✓ Target model '{config['model']}' is available")
            return True
        else:
            print(f"\n✗ WARNING: Target model '{config['model']}' not found!")
            print(f"  Run: ollama pull {config['model']}")
            return False

    except requests.exceptions.ConnectionError:
        print(f"✗ ERROR: Cannot connect to Ollama at {config['base_url']}")
        print("  Make sure Ollama is running and accessible")
        print("  Check that OLLAMA_HOST=0.0.0.0:11434 is set")
        return False
    except Exception as e:
        print(f"✗ ERROR: {str(e)}")
        return False


def test_ollama_native_api(config):
    """Test Ollama's native /api/generate endpoint."""
    print("\n" + "=" * 60)
    print("TEST 2: Ollama Native API (/api/generate)")
    print("=" * 60)

    try:
        request_data = {
            "model": config['model'],
            "prompt": "Say hello in exactly one sentence.",
            "stream": False,
            "options": {
                "temperature": config['temperature'],
                "num_predict": 100,
                "num_ctx": config['num_ctx'],
            }
        }

        endpoint = f"{config['base_url']}/api/generate"
        print(f"Sending request to: {endpoint}")
        print(f"Model: {config['model']}")

        response = requests.post(
            endpoint,
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


def test_openai_compatible_api(config):
    """Test OpenAI-compatible API."""
    print("\n" + "=" * 60)
    print("TEST 3: OpenAI-Compatible API (/v1/chat/completions)")
    print("=" * 60)

    try:
        request_data = {
            "model": config['model'],
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
            "temperature": config['temperature'],
            "top_p": config['top_p'],
            "max_tokens": 100
        }

        endpoint = f"{config['base_url']}/v1/chat/completions"
        print(f"Sending request to: {endpoint}")
        print(f"Model: {config['model']}")

        response = requests.post(
            endpoint,
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
    config = load_config()

    print("\nTesting Ollama LLM Configuration")
    print(f"Server: {config['base_url']}")
    print(f"Model: {config['model']}")
    print(f"Config endpoint: {config['endpoint']}\n")

    results = []

    # Test 1: Connection
    results.append(("Connection", test_ollama_connection(config)))

    # Test 2: Native API
    results.append(("Native API", test_ollama_native_api(config)))

    # Test 3: OpenAI-compatible API
    results.append(("OpenAI API", test_openai_compatible_api(config)))

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
        print(f"  Endpoint: {config['endpoint']}")
        print(f"  Model: {config['model']}")
        return 0
    else:
        print("\n✗ Some tests failed. Check the errors above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

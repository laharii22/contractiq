from unittest.mock import Mock, patch
import pytest
from contractiq.llm_client import send_test_message


@patch("contractiq.llm_client.create_client")
def test_send_test_message_returns_response_text(mock_create_client):

    # Create a fake client
    mock_client = Mock()

    # Create a fake response from Claude
    mock_response = Mock()
    mock_response.content = [
        Mock(text="ContractIQ API connection successful.")
    ]

    # Configure the fake client to return our fake response
    mock_client.messages.create.return_value = mock_response
    mock_create_client.return_value = mock_client

    # Run the actual ContractIQ function
    result = send_test_message("Test prompt")

    # Check whether the returned result is correct
    assert result == "ContractIQ API connection successful."

@patch("contractiq.llm_client.create_client")
def test_send_test_message_handles_invalid_api_key(mock_create_client):

    mock_create_client.side_effect = RuntimeError("Invalid Anthropic API key.")

    with pytest.raises(RuntimeError, match="Invalid Anthropic API key."):
        send_test_message("Test prompt")    
from unittest.mock import Mock, patch
import pytest
from contractiq.llm_client import send_test_message, analyse_contract


@patch("contractiq.llm_client.create_client")
def test_send_test_message_returns_response_text(mock_create_client):

    # Createing a fake client
    mock_client = Mock()

    # Createing a fake response from Claude
    mock_response = Mock()
    mock_response.content = [
        Mock(text="ContractIQ API connection successful.")
    ]

    # Configureing the fake client to return our fake response
    mock_client.messages.create.return_value = mock_response
    mock_create_client.return_value = mock_client

    # Running the actual ContractIQ function
    result = send_test_message("Test prompt")

    # Checking whether the returned result is correct
    assert result == "ContractIQ API connection successful."

@patch("contractiq.llm_client.create_client")
def test_send_test_message_handles_invalid_api_key(mock_create_client):

    mock_create_client.side_effect = RuntimeError("Invalid Anthropic API key.")

    with pytest.raises(RuntimeError, match="Invalid Anthropic API key."):
        send_test_message("Test prompt")    

def test_analyse_contract_rejects_empty_text():
    # Helps in checking that an empty contract cannot be analysed
    with pytest.raises(ValueError, match="Contract text cannot be empty"):
        analyse_contract("   ")


@patch("contractiq.llm_client.send_test_message")
def test_analyse_contract_sends_contract_text(mock_send_message):
    # Helps in creating a sample contract for testing
    contract = "The tenant must pay £800 rent every month."

    # Helps in creating a fake response without calling Claude
    mock_send_message.return_value = "The tenant must pay monthly rent."

    # Helps in testing the contract analysis function
    result = analyse_contract(contract)

    # Helps in checking that the contract text was sent for analysis
    prompt = mock_send_message.call_args.args[0]
    assert contract in prompt

    # Helps in checking that the correct response was returned
    assert result == "The tenant must pay monthly rent."
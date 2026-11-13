from unittest.mock import patch

from contractiq.pipeline import analyse_pdf


@patch("contractiq.pipeline.analyse_contract")
@patch("contractiq.pipeline.extract_text_from_pdf")
def test_analyse_pdf(mock_extract, mock_analyse):

    # Helps in providing sample extracted contract text
    mock_extract.return_value = "The client must pay within 14 days."

    # Helps in providing a fake contract analysis result
    mock_analyse.return_value = "Payment is required within 14 days."

    # Helps in checking the PDF analysis pipeline
    result = analyse_pdf("sample.pdf")

    # Helps in checking that the correct PDF was selected
    mock_extract.assert_called_once_with("sample.pdf")

    # Helps in checking that the extracted text was sent for analysis
    mock_analyse.assert_called_once_with("The client must pay within 14 days.")

    # Helps in checking that the analysis result was returned
    assert result == "Payment is required within 14 days."
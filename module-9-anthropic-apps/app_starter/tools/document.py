import os
from markitdown import MarkItDown, StreamInfo
from io import BytesIO
from pydantic import Field


def binary_document_to_markdown(binary_data: bytes, file_type: str) -> str:
    """Converts binary document data to markdown-formatted text."""
    md = MarkItDown()
    file_obj = BytesIO(binary_data)
    stream_info = StreamInfo(extension=file_type)
    result = md.convert(file_obj, stream_info=stream_info)
    return result.text_content


def document_path_to_markdown(
    file_path: str = Field(description="Path to a PDF or DOCX file to convert to markdown")
) -> str:
    """Converts a PDF or DOCX document to markdown-formatted text.

    Reads a document file from the filesystem and converts its contents to
    markdown format. Supports PDF and DOCX file formats.

    When to use:
    - When you need to extract text content from PDF or DOCX files
    - When you want to process document content in markdown format
    - When you need to make document content accessible for text analysis

    When not to use:
    - For image-heavy documents where visual content is critical
    - For documents where precise layout and formatting must be preserved
    - For file formats other than PDF or DOCX

    Examples:
    >>> document_path_to_markdown("/path/to/document.pdf")
    '# Document Title\\n\\nDocument content...'
    >>> document_path_to_markdown("./report.docx")
    '# Report\\n\\nReport content...'
    """
    # Validate file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    # Extract file extension
    _, ext = os.path.splitext(file_path)
    file_type = ext.lstrip('.')

    # Validate file type
    supported_types = ['pdf', 'docx']
    if file_type.lower() not in supported_types:
        raise ValueError(
            f"Unsupported file type: {file_type}. "
            f"Supported types: {', '.join(supported_types)}"
        )

    # Read file as binary
    with open(file_path, 'rb') as f:
        binary_data = f.read()

    # Convert to markdown using existing utility
    return binary_document_to_markdown(binary_data, file_type)

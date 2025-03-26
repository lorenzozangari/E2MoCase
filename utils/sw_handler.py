"""
Utility functions for cleaning the news articles retrieved from the SwissDoc API.

"""
# Constants for document types
DOC_TYPE_VIDEO = ["SRFV", "RTSV"]
DOC_TYPE_AUDIO = ["SRFA"]

def _remove_LG(content):
    """Remove lines containing '<LG>' from the content.

    Args:
        content (str): The content to process.

    Returns:
        str: The content with lines containing '<LG>' removed.

    Example of usage:
        content_with_lg = "<LG>Some content\nRegular content\n<LG>Another line"
        cleaned_content = _remove_LG(content_with_lg)
        print(cleaned_content)  # Output: Regular content
    """
    lines = content.split("\n")
    new_lines = [line for line in lines if "<LG>" not in line]
    return "\n".join(new_lines)

def _get_paragraphs(text):
    """Split the text into paragraphs based on the '<ParagTitle>' tag.

    Args:
        text (str): The text to split.

    Returns:
        list: A list of paragraphs.

    Example of usage:
        text_with_paragraphs = "Title<ParagTitle>First paragraph<ParagTitle>Second paragraph"
        paragraphs = _get_paragraphs(text_with_paragraphs)
        print(paragraphs)  # Output: ['Title', 'First paragraph', 'Second paragraph']
    """
    return text.split("<ParagTitle>")

def is_audio_video_text(row):
    """Check if the row's medium code indicates audio or video content.

    Args:
        row (pd.Series): The row to check.

    Returns:
        bool: True if the row is audio or video, False otherwise.

    Example of usage:
        row_video = pd.Series({'medium_code': 'SRFV'})
        is_av = is_audio_video_text(row_video)
        print(is_av)  # Output: True

        row_text = pd.Series({'medium_code': 'TEXT'})
        is_av = is_audio_video_text(row_text)
        print(is_av)  # Output: False
    """
    if row["medium_code"] in DOC_TYPE_VIDEO:
        return True
    if row["medium_code"] in DOC_TYPE_AUDIO:
        return True
    return False

def _get_content_in_paragraphs(row, translated=False):
    """Get the content of the row split into paragraphs.

    Args:
        row (pd.Series): The row to process.
        translated (bool): Whether to use translated content.

    Returns:
        list: A list of paragraphs.

    Example of usage:
        row = df.iloc[0]
        paragraphs = _get_content_in_paragraphs(row)
        print(paragraphs)  # Output: ['Video Title\nVideo Subtitle\nAnother line']

        translated_paragraphs = _get_content_in_paragraphs(row, translated=True)
        print(translated_paragraphs)  # Output: ['Translated Video Title\nTranslated Video Subtitle\nAnother line']
    """
    head_name = "head"
    subhead_name = "subhead"
    content_name = 'content'

    if translated:
        head_name = 'translated_' + head_name
        subhead_name = 'translated_' + subhead_name
        content_name = 'translated_input'

    head = row[head_name] + "\n"
    subhead = "" if type(row[subhead_name]) != str else row[subhead_name] + "\n"
    cleaned_content = _remove_LG(row[content_name])
    paragraphs = [head + subhead] + _get_paragraphs(cleaned_content)

    return paragraphs


def _get_content_by_newline(content):
    """Split the content into lines.

    Args:
        content (str): The content to split.

    Returns:
        list: A list of lines.

    Example of usage:
        content = "Line one\nLine two\nLine three"
        lines = _get_content_by_newline(content)
        print(lines)  # Output: ['Line one', 'Line two', 'Line three']
    """
    return content.split("\n")


def get_content_in_paragraphs(row, translated=False):
    """Get the content of the row in paragraphs unless it is audio or video.

    Args:
        row (pd.Series): The row to process.
        translated (bool): Whether to use translated content.

    Returns:
        str or list: Empty string if audio/video, otherwise list of paragraphs.

    Example:
        row = df.iloc[0]
        paragraphs = get_content_in_paragraphs(row)
        print(paragraphs)  # Output: ['Video Title\nVideo Subtitle\nAnother line']

        translated_paragraphs = get_content_in_paragraphs(row, translated=True)
        print(translated_paragraphs)  # Output: ['Translated Video Title\nTranslated Video Subtitle\nAnother line']
    """
    if is_audio_video_text(row):
        print("No textual content: audio or video transcription")
        return ""
    else:
        return _get_content_in_paragraphs(row, translated)


def get_content_by_newline(content):
    """Get the content split by newline.

    Args:
        content (str): The content to split.

    Returns:
        list: A list of lines.

    Example:
        content = "Line one\nLine two\nLine three"
        lines = get_content_by_newline(content)
        print(lines)  # Output: ['Line one', 'Line two', 'Line three']
    """
    return _get_content_by_newline(content)
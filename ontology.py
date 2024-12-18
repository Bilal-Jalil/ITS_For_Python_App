def get_suggestions(progress):
    """Return suggested exercises based on user progress."""
    suggestions = [
        "Simple Programs",
        "Lines & Indentations",
        "Arithmetic Operators",
        "Assignment Operators",
    ]
    if progress < len(suggestions):
        return suggestions[:progress + 1]
    return suggestions

def chat_response(query):
    """Mock chatbot responses."""
    if "variable" in query:
        return "A variable in Python is used to store values like x = 5."
    elif "operator" in query:
        return "Operators in Python include +, -, *, /, and more."
    return "I'm sorry, I don't understand your query."

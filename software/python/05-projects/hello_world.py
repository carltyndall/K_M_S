"""Hello World Starter Script.

Demonstrates standard entry-point structure, docstrings, and basic output.
"""

def greet(name: str) -> str:
    """Generates a personalized greeting message.
    
    Args:
        name: Name of the person to greet.
        
    Returns:
        Formatted greeting string.
    """
    return f"Welcome to K_M_S, {name}!"

def main() -> None:
    """Main script execution routine."""
    message = greet("Learner")
    print(message)

if __name__ == "__main__":
    main()

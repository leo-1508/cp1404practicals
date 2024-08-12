import wikipedia


def get_wikipedia_page(title):
    """Fetch and display details of the Wikipedia page with the given title."""
    try:
        # Get the page with autosuggest turned off to avoid unwanted suggestions
        page = wikipedia.page(title, autosuggest=False)
        print(f"\nTitle: {page.title}")
        print(f"Summary: {page.summary[:500]}...")  # Print the first 500 characters of the summary
        print(f"URL: {page.url}\n")
    except wikipedia.DisambiguationError as e:
        print(f"Disambiguation error: {title} may refer to multiple topics. Suggestions: {e.options}")
    except wikipedia.PageError:
        print(f"PageError: The page '{title}' does not exist on Wikipedia.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    """Main loop to prompt user for input and fetch Wikipedia pages."""
    while True:
        # Prompt the user for a Wikipedia page title or search phrase
        search_query = input("Enter a Wikipedia page title or search phrase (or press Enter to quit): ").strip()

        # Break the loop if the user enters blank input
        if not search_query:
            break

        # Fetch and display the Wikipedia page
        get_wikipedia_page(search_query)

    print("Goodbye!")


if __name__ == "__main__":
    main()


def search_suggestions(
        repository: list[str],
        customer_query: str
):
    repository.sort()
    output = []
    for i in range(2, len(customer_query) + 1):
        result = []
        sub_query = customer_query[0:i]
        for word in repository:
            if word.startswith(sub_query):
                result.append(word)
        output.append(result[0:3])
    return output


def run_search_suggestions():
    repository = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    customer_query = "mouse"

    expected_output = [
        ["mobile", "moneypot", "monitor"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"]
    ]
    result = search_suggestions(repository, customer_query)
    print(result)
    print(f"success? {result == expected_output}")

# Tavily Search

Search the web for real-time information using Tavily AI Search. Use this tool when you need current facts, news, or data beyond your knowledge base.

## When to use
- When the user asks for current event news or facts.
- When you need to verify technical information or documentation.
- When answering questions about weather, stocks, or prices that require live data.

## How to use
1. Use `get_current_time` to establish the context for today's date if necessary.
2. Use `web_search` with a clear, concise query in English or the user's preferred language.
3. Review the search results and extract the most relevant information.
4. If results are insufficient, try a different or more specific query.

## Example
User: "What's the current price of Ethereum?"
→ `web_search {"query": "current price of Ethereum in USD"}`
→ "The current price of Ethereum is approximately $2,845 USD (source: Tavily Search)."

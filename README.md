# the_data_analyst

## Backend

### Setup

We used `uv` as a package manager and recommend installing dependencies with it.

1. Install uv: <https://docs.astral.sh/uv/getting-started/installation/>
2. Install the dependencies: `uv sync`
3. Install the package locally: `uv pip install -e .`
4. Run the backend: `uv run src/backend/main.py`

You should see `Hello, world!` printed in the console and a link to access a Gradio interface.

### Environment Variables

Create a `.env` file using `.env.example` as a template and fill in the required API keys and database connection details.

### Multi-Agent Architecture

- **Orchestrator Agent**: Manages workflow and delegates tasks to sub-agents.
- **QA Query Analyzer**: Retrieves and processes data from **PostgreSQL** and **MongoDB** databases.
- **Code Agent**: Generates Streamlit Python code based on the report generator's insights.
- **Report Generator**: Produces business reports from the query analyzer's results.

### Tech Stack & Tools

- **LLMs**: Claude (Anthropic)
- **Agents**: SmolAgents for multi-source data connectivity
- **Interface**: Gradio (chat-based interaction)
- **Dashboards**: Streamlit (local deployment)
- **Cloud & Deployment**: Koyeb (for database hosting)
- **Data Sources**: PostgreSQL, MongoDB, APIs, Google Search

### Conclusion

Our multi-agent AI system automates the entire data pipeline—from retrieval to visualization—through AI-driven collaboration.


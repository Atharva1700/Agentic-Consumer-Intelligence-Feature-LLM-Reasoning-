# Agentic Consumer Intelligence System

Minimal, reasoning-driven system for surfacing emerging patterns in short-form video metadata. Demonstrates core responsibilities: agentic reasoning, pattern detection, and actionable insights for stakeholders.

## Quick Start

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY="your-key"
python agent.py
```

## What It Does

1. **Ingest**: Loads batch of short-form video metadata (simulated)
2. **Analyze**: Multi-step reasoning chain (hashtag frequency, engagement correlation)
3. **Synthesize**: Claude API generates actionable insight for marketing team
4. **Output**: Structured JSON for stakeholder consumption

## Example Output

```
Pattern: AI productivity content dominance
Action: Launch 3-video series on LLM workflows this week; allocate 40% ad spend here
Priority: high
```

## Architecture

- **Single agent file** (`agent.py`): No unnecessary orchestration
- **Minimal dependencies**: Only Anthropic SDK
- **No LangGraph boilerplate**: Direct Claude API calls—add routing only when needed
- **Simulated data**: Easily swapped for real API ingestion

## When to Extend

- **Real data pipeline**: Replace `ingest_batch()` with API/database calls
- **Multi-agent reasoning**: Split analysis step into specialized sub-agents
- **Persistent state**: Add database for historical pattern tracking
- **Web service**: Wrap in FastAPI, add queue for batch processing

---

Built with ⚡ and 🦖 (ponytail mode)

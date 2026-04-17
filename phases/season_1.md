# Season 1 — Core Framework Scaffolding, Event Bus, and Gateway Foundations

## Overview
This season focuses on establishing the foundational architecture of the Sentient AI Framework. We will build the central nervous system (Event Bus) that connects all modules, set up the FastAPI backend, and implement the basic input/output gateways (Thalamus and Brainstem).

## Key Objectives
1. **Event Bus Initialization**: Implement the async event bus that all modules will use to communicate. This is the core messaging backbone.
2. **FastAPI Backend Skeleton**: Setup the basic web server with WebSocket support for real-time streaming and REST endpoints.
3. **Thalamus (Input Gateway) Basics**:
   - Implement the `Envelope Factory` to normalize inputs.
   - Implement the basic batching window (fixed 30s for now, adaptive later).
   - Setup a simple Chat Interface plugin.
4. **Brainstem (Output Gateway) Basics**:
   - Implement the Output Coordinator.
   - Setup a simple System GUI Chat output plugin.
5. **Inference Gateway Skeleton**: Setup the basic routing mechanism that will eventually connect to Ollama (which handles both local and cloud models in our setup).

## Implementation Details
- **Architecture**: Single Python process using `asyncio`.
- **LLM Routing**: Remember that Ollama is the unified interface for both local and cloud models.
- **Dependencies**: `fastapi`, `uvicorn`, `pydantic`.

## Expected Outcome
By the end of this season, we should be able to start the application, send a message via an API/WebSocket to the Thalamus, see it normalized into an event on the bus, and passed (as a dummy response) back out through the Brainstem.

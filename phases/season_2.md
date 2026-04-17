# Season 2 — Memory Architecture and Identity Manager

## Overview
This season implements the persistent state of the sentient being. We will build out the dual-storage memory system (structured and semantic) and the multi-layered Persona Manager.

## Key Objectives
1. **Memory Architecture**:
   - Set up SQLite + FTS5 for structured memories and metadata (`data/memory.db`).
   - Set up ChromaDB for semantic vectors (`data/chroma/`).
   - Implement the 4 memory types: Episodic, Semantic, Procedural (Skills), Emotional.
   - Build the Logic-based Memory Gatekeeper (deterministic, no LLM in write path) to handle deduplication and thresholds.
2. **Persona & Identity Manager**:
   - Implement the Three-Layer Identity model:
     - Layer 1: Constitutional Core (immutable, loaded from `config/identity/`).
     - Layer 2: Developmental (evolves).
     - Layer 3: Dynamic State (current mood/energy).
   - Establish the maturity tracking states (Nascent, Forming, Developing, Mature).

## Implementation Details
- **Libraries**: `sqlite3`, `chromadb`, `sentence-transformers`, `pyyaml`.
- **Integration**: The Identity manager needs to expose its state to the Event Bus so the Cognitive Core (Season 3) can use it for context assembly.

## Expected Outcome
The system can store and retrieve memories via semantic similarity and exact text search. The Identity Manager can load a Constitutional Core from YAML and maintain its dynamic state in memory.

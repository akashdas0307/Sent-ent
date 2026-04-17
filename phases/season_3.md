# Season 3 — Prajñā Pipeline and World Model

## Overview
This is the core reasoning phase. We will implement the continuous cognition engine that processes inputs, dreams during idle time, and critically reviews its own thoughts.

## Key Objectives
1. **Pre-Temporal-Occipital-Checkpost**:
   - Entity recognition, intent classification, source tagging.
2. **Queue Zone**:
   - Implement the idle mode (30s window accumulation) and active mode logic.
3. **Temporal-Limbic-Processor (TLP)**:
   - Combine memory retrieval, context assembly, and significance weighting.
4. **Frontal Processor (Cognitive Core)**:
   - Implement the 7-step reasoning loop (Intake → Associative → Options → Planning → Review → Execute → Reflect).
   - Implement structured internal monologue (MONOLOGUE / ASSESSMENT / DECISIONS / REFLECTION).
   - Implement Context State Manager (Letta-inspired save/restore).
   - Setup Continuous Cognition (Daydreaming) using random seeds.
5. **Supplementary-World-View (World Model)**:
   - Implement the 5-dimension review process (Feasibility / Consequence / Ethics / Consistency / Reality Grounding).
   - Establish the veto loop (max 3 cycles) to check Cognitive Core decisions.

## Implementation Details
- **LLM Usage**: Use Ollama as the provider. Note that Cognitive Core and World Model should ideally request different underlying models via Ollama to ensure architectural diversity (e.g., Claude Opus equivalent vs Gemma/Qwen equivalent).

## Expected Outcome
A complete input-to-thought pipeline. Inputs from the Event Bus are routed through the Queue, enriched by the TLP, reasoned over by the Cognitive Core, and reviewed by the World Model before decisions are published to the Event Bus.

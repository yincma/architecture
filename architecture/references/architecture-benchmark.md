### 2.5 Architecture Comparison & Benchmark Workflow

When a user requests comparing multiple architecture approaches (triggered by keywords like "compare", "benchmark", "evaluate", "pros and cons", "trade-offs", or "which is better"), follow this workflow:

**Step 1: Clarify Requirements & Identify Candidate Architectures**
- Parse the user's description to understand the system requirements (scale, budget, team size, performance needs, etc.)
- Propose 3 distinct architecture approaches. Common combinations include:
  - Monolithic / Microservices / Serverless
  - Self-hosted / Managed services / Hybrid
  - Synchronous / Event-driven / CQRS
  - Single-region / Multi-region / Edge-based
- Confirm the 3 candidates with the user before proceeding

**Step 2: Generate Architecture Diagrams**
- Generate one `.drawio` file per architecture approach
- File naming: `{project}-option-a-{style}.drawio`, `{project}-option-b-{style}.drawio`, `{project}-option-c-{style}.drawio`
- Each diagram must follow all XML compliance rules from Section 3
- Use consistent component naming across diagrams for easy comparison

**Step 3: Generate Benchmark Report**
- Output a Markdown file named `{project}-architecture-benchmark.md`
- The report must include:

```markdown
# Architecture Benchmark: {Project Name}

## Overview
Brief description of the system requirements and constraints.

## Candidate Architectures

### Option A: {Architecture Name}
- **Diagram**: `{filename}.drawio`
- **Summary**: 1-2 sentence description

### Option B: {Architecture Name}
- **Diagram**: `{filename}.drawio`
- **Summary**: 1-2 sentence description

### Option C: {Architecture Name}
- **Diagram**: `{filename}.drawio`
- **Summary**: 1-2 sentence description

## Comparison Matrix

| Dimension          | Option A | Option B | Option C |
|--------------------|----------|----------|----------|
| Development Cost   | ⭐⭐⭐⭐⭐  | ⭐⭐⭐      | ⭐⭐⭐⭐    |
| Operational Cost   | ⭐⭐⭐⭐    | ⭐⭐        | ⭐⭐⭐⭐⭐  |
| Scalability        | ⭐⭐       | ⭐⭐⭐⭐⭐  | ⭐⭐⭐⭐⭐  |
| Performance        | ⭐⭐⭐⭐    | ⭐⭐⭐⭐    | ⭐⭐⭐      |
| Ops Complexity     | ⭐⭐⭐⭐⭐  | ⭐⭐        | ⭐⭐⭐⭐    |
| Team Skill Req.    | ⭐⭐⭐⭐⭐  | ⭐⭐        | ⭐⭐⭐      |
| Time to Market     | ⭐⭐⭐⭐⭐  | ⭐⭐        | ⭐⭐⭐⭐    |
| Fault Isolation    | ⭐⭐       | ⭐⭐⭐⭐⭐  | ⭐⭐⭐⭐    |

> ⭐ scale: ⭐ = poor, ⭐⭐⭐ = average, ⭐⭐⭐⭐⭐ = excellent

## Detailed Analysis

### Development Cost
{Explain why each option scores as it does}

### Operational Cost
{Explain ongoing infrastructure and maintenance costs for each option}

### Scalability
{Explain scaling characteristics of each option}

### Performance
{Explain latency and throughput under normal load}

### Ops Complexity
{Explain deployment, monitoring, debugging difficulty}

### Team Skill Requirements
{Explain expertise needed to build and maintain}

### Time to Market
{Explain speed from design to production}

### Fault Isolation
{Explain blast radius when a component fails}

## Recommendation
Based on the requirements, **Option X** is recommended because...

### When to Choose Each Option
- **Option A**: Best when {conditions}
- **Option B**: Best when {conditions}
- **Option C**: Best when {conditions}
```

**Step 4: Evaluation Dimensions**
- Development Cost, Operational Cost, Scalability, Performance, Ops Complexity, Team Skill Requirements, Time to Market, Fault Isolation
- Score each dimension on a 1-5 star scale with justification

**Step 5: Output All Files**
- Write all 3 `.drawio` files and 1 `.md` benchmark file

# ai-writer-multitasker
A simple illustration AI multi task agent demo for my students. This Porject is for demostration purposes only. <br>

# What this Project Teaches
This project teaches:
[x] Prompt chaining
[x] Workflow orchestration
[x] Modular AI design
[x] Separation of concerns
[x] Real-world GenAI application architecture

# Workflow Architecture
```
User Input
    ↓
Step 1: Generate Outline
    ↓
Step 2: Expand Draft
    ↓
Step 3: Improve Style
    ↓
Step 4: Proofread
    ↓
Final Output
```

# Why Multi-Step Workflows?
A single prompt often produces:
- Weak structure
- Repetition
- Missing details
- Inconsistent tone

Breaking the task into stages gives much better results.

This mimics how human writers work:
[x] Plan
[x] Draft
[x] Edit
[x] Proofread

# Features Improvement Ideas
1. **Narrow down to Email writer assistant**
[x] Stage 1
- Determine intent
    - Sales
    - Support
    - Marketing
    - Follow-up

[x] Stage 2
- Draft Email structure
    - subject
    - Greeting
    - Body
    - Call-to-Action

[x] Stage 3
- Draft full email

[x] Stage 4
- Optimize tone

[x] Stage 5
- Proofread

2. **Blog Writer**
- **Workflow**
```
Topic
  ↓
Keyword Research
  ↓
Outline
  ↓
Introduction
  ↓
Body Sections
  ↓
Conclusion
  ↓
SEO Optimization
  ↓
Final Article
```

3. **Multi-agent Style**
```
Research Agent
      ↓
Outline Agent
      ↓
Writing Agent
      ↓
Editor Agent
      ↓
Proofreader Agent
```

# ⚠️ Caution
In practice and for a production level project, the design is **NOT** advisible
because it can be expensive and slow due to multiple API calls.

**For a single article:**<br>
The API is called four (4) times
1. Outline
2. Draft
3. Tone rewrite
4. Proofread

There are multiple problems associated with this including 
1. Increase latency
2. Increase token usage
3. Increase API cost

In practice a single well-constructed prompt could generate the final article directly.<br>
Using prompting techniques such as chain of thought or step back prompting<br> we could achieve better output.

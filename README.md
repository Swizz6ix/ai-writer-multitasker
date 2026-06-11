# ai-writer-multitasker
A simple illustration AI multi task agent demo for my students <br>
This Porject is for demostration purposes only <br>

In practice and for a production level project, the design is not<br> 
advisible because it make multiple API calls which can be expensive and slow.

**For a single article:**
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

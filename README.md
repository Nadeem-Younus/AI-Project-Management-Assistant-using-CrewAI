# AI-Project-Management-Assistant-using-CrewAI
This system helps plan software projects by breaking them into:
- Requirements analysis
- Project planning
- Risk analysis
- Resource estimation
- Executive reporting

Tools Used:
- CrewAI
- OpenAI GPT-4o-mini
- Langfuse (optional / partial working fine)

Agents:
- Requirements Agent
- Planning Agent
- Risk Agent
- Resource Agent
- Report Agent

Workflow Explanation: 
- User Input → Requirements Agent → Planning Agent → Risk Agent → Resource Agent → Report Agent → Final Output

How to run: 
- pip install -r requirements.txt
- python app.py

Example Input: 
- Build an AI-based project management tool for startups. Budget: $50,000. Timeline: 3 months. Team: 5 people

Output:
- Structured project plan
- Risks
- Resource allocation
- Executive summary

Challenges Faced:
- CrewAI version compatibility
- Task validation (expected_output required)
- Tool integration issues
- Langfuse version mismatch



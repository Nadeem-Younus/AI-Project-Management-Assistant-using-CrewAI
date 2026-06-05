from crewai import Agent, LLM

from tools.search_tool import project_template
from tools.custom_tool import effort_calculator
from tools.api_tool import current_date

llm = LLM(
    model="openai/gpt-4o-mini",
    temperature=0.3
)

requirements_agent = Agent(
    role="Requirements Analyst",
    goal="Extract project requirements",
    backstory="Senior business analyst specialized in requirement gathering.",
    llm=llm,
    verbose=True,
    memory=True
)

planning_agent = Agent(
    role="Project Planner",
    goal="Create project plan and milestones",
    backstory="Expert project manager with experience in WBS design.",
    llm=llm,
    tools=[project_template, current_date],
    verbose=True,
    memory=True
)

risk_agent = Agent(
    role="Risk Analyst",
    goal="Identify risks and mitigation strategies",
    backstory="Expert in project risk management and analysis.",
    llm=llm,
    verbose=True
)

resource_agent = Agent(
    role="Resource Estimator",
    goal="Estimate effort and staffing",
    backstory="Expert in resource planning and estimation.",
    llm=llm,
    tools=[effort_calculator],
    verbose=True
)

report_agent = Agent(
    role="Report Writer",
    goal="Generate final executive report",
    backstory="PMO expert in writing structured executive reports.",
    llm=llm,
    verbose=True
)
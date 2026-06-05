from crewai import Task
from agents import (
    requirements_agent,
    planning_agent,
    risk_agent,
    resource_agent,
    report_agent
)

requirements_task = Task(
    description="""
    Analyze the project description:
    {project}

    Extract:
    - objectives
    - timeline
    - budget
    - deliverables

    If any information is not explicitly provided,
    write 'Not Provided'.

    If budget is not provided, estimate a reasonable budget and clearly label it as 'Estimated Budget'.

    If timeline is not provided, estimate a reasonable timeline and clearly label it as 'Estimated Timeline'.

    Analyze the provided team. If additional roles are recommended, clearly separate them from the user-provided team. Label them as recommendations.
    """,
    expected_output="""
    Structured requirements document with all available information.
    """,
    agent=requirements_agent
)

planning_task = Task(
    description="Create project plan and WBS",
    expected_output="Project plan with milestones and phases",
    agent=planning_agent,
    context=[requirements_task]
)

risk_task = Task(
    description="Identify risks and mitigation strategies",
    expected_output="Risk register with risks and mitigations",
    agent=risk_agent,
    context=[requirements_task, planning_task]
)

resource_task = Task(
    description="Estimate resources and effort",
    expected_output="Resource allocation and effort estimation",
    agent=resource_agent,
    context=[requirements_task, planning_task]
)

report_task = Task(
    description="Generate final executive report",
    expected_output="Complete markdown executive report",
    agent=report_agent,
    context=[requirements_task, planning_task, risk_task, resource_task],

    output_file="outputs/project_report.md"
)
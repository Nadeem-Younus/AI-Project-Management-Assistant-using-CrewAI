from dotenv import load_dotenv
from crew import project_crew
from fallback.fallback_handler import handle_error

load_dotenv()

def run_project(user_input):

    try:
        result = project_crew.kickoff(
            inputs={"project": user_input}
        )

        # Save output to file
        with open("outputs/project_report.md", "w", encoding="utf-8") as f:
            f.write(str(result))

        return str(result)

    except Exception as e:
        return handle_error(e, "Crew Execution")


if __name__ == "__main__":

    print("Enter project description. For example, Build a cloud-based E-commerce platform with AI recommendation engine, budget $20000, engineers 4.\n")
    user_input = input("Please Enter project description: ")

    output = run_project(user_input)

    print("\n===== FINAL OUTPUT =====\n")
    print(output)

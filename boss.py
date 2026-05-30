import statistics as st
import os

# --- UTILITY FUNCTIONS ---

def get_number_only(prompt="Enter a number: "):
    """Safely gets a numerical input from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")

def get_option(options):
    """Displays a menu and returns a valid option index."""
    print("\n--- Main Menu ---")
    for i, opt in enumerate(options):
        print(f"[{i}] - {opt}")
    
    while True:
        choice = get_number_only("\nSelect an option: ")
        if 0 <= choice < len(options):
            return choice
        print(f"⚠️ Please choose a number between 0 and {len(options)-1}")

def get_result_category(average):
    """Categorizes the student based on their average score."""
    if average < 50: return "Fail"
    if average < 70: return "Pass"
    if average < 90: return "Good"
    return "Excellent"

def get_weakest_subject(math, english, programming):
    """Identifies the subject with the lowest score."""
    if math == 100 and english == 100 and programming == 100:
        return "None"
    
    subjects = {"Math": math, "English": english, "Programming": programming}
    # Find the key with the minimum value
    return min(subjects, key=subjects.get)

def no_data_message():
    print("\n❗ No student data available. Please add students first.")

# --- MAIN PROGRAM ---

def main():
    students_data = []
    
    while True:
        menu_items = ["Add Student", "Display Class Report", "Delete Student", "Save to File", "Exit"]
        option = get_option(menu_items)

        if option == 0:  # ADD STUDENT
            name = input("Student Name: ").strip().title()
            math = get_number_only("Enter Math score: ")
            english = get_number_only("Enter English score: ")
            prog = get_number_only("Enter Programming score: ")

            rate = st.mean([math, english, prog])
            result = get_result_category(rate)
            weakest = get_weakest_subject(math, english, prog)

            students_data.append({
                "name": name, "math": math, "english": english,
                "programming": prog, "rate": rate, 
                "result": result, "weakest_subject": weakest
            })
            print(f"✅ {name} added successfully!")

        elif option == 1:  # DISPLAY DATA
            if not students_data:
                no_data_message()
                continue
            
            print("\n" + "="*95)
            template = "| %-20s | M: %-3d | E: %-3d | P: %-3d | Avg: %-6.2f | Status: %-10s | Weakest: %-10s |"
            for s in students_data:
                print(template % (s["name"], s["math"], s["english"], s["programming"], s["rate"], s["result"], s["weakest_subject"]))
            print("="*95)

        elif option == 2:  # DELETE STUDENT
            if not students_data:
                no_data_message()
                continue
            
            name_to_delete = input("Enter the name of the student to delete: ").strip().title()
            # Efficiently filter the list
            initial_count = len(students_data)
            students_data = [s for s in students_data if s["name"] != name_to_delete]
            
            if len(students_data) < initial_count:
                print(f"🗑️ Student '{name_to_delete}' has been removed.")
            else:
                print(f"❌ Student '{name_to_delete}' not found.")

        elif option == 3:  # SAVE TO FILE
            if not students_data:
                no_data_message()
                continue
            
            with open("students_report.txt", "w") as f:
                template = "Name: %-20s | Average: %-6.2f | Status: %-10s\n"
                for s in students_data:
                    f.write(template % (s["name"], s["rate"], s["result"]))
            print("💾 Report saved to 'students_report.txt'")

        elif option == 4:  # EXIT
            print("Exiting... Goodbye!")
            break

if __name__ == "__main__":
    main()

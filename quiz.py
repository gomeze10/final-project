
def generate_training_plan(age, prior_training, training_goal, breed_type) -> list:

    plan = []

    print("\n--- Training Plan ---")

    if age < 6:
        plan.append("Keep sessions short (5-10 minutes). Focus on basic commands.")
    else:
        plan.append("Longer sessions are okay. Reinforce consistency.")

    if prior_training == "yes":
        plan.append("Build on previously learned commands.")
    else:
        plan.append("Start with basic obedience like sit, stay, and recall.")


    if training_goal == "tricks":
        plan.append("Focus on fun tricks like shake, roll over, and spin.")
    elif training_goal == "behavior":
        plan.append("Focus on good manners like leash walking and no jumping.")
    else:
        plan.append("Balance obedience training with fun tricks.")

    if breed_type == "herding":
        plan.append("Provide mental challenges and structured tasks.")
    elif breed_type == "working":
        plan.append("Include physical activity and task-based training.")
    elif breed_type == "toy":
        plan.append("Use gentle training and lots of positive reinforcement.")
    elif breed_type == "sporting":
        plan.append("Use active games and reward-based training.")

    return plan

if __name__ == '__main__':

    print("Welcome to the Dog Training Assistant!")

    age = int(input("What is the age of the puppy (in months)? "))

    prior_training = input("Has the dog had prior training? (yes/no): ")

    training_goal = input("What is the training goal? (tricks / behavior / both): ")

    breed_type = input("What type of breed is it? (herding / working / toy / sporting): ")

    print("\nThank you! Generating your training plan...")
    print(generate_training_plan(age, prior_training, training_goal, breed_type))

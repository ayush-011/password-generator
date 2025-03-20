class VotingSystem:
    def __init__(self):
        self.candidates = {"Candidate A": 0, "Candidate B": 0, "Candidate C": 0}
        self.voters = set()

    def check_eligibility(self, age, voter_id):
        if age < 18:
            print("You are not eligible to vote.")
            return False
        if voter_id in self.voters:
            print("You have already voted.")
            return False
        return True

    def cast_vote(self, voter_id, age, candidate):
        if not self.check_eligibility(age, voter_id):
            return
        
        if candidate in self.candidates:
            self.candidates[candidate] += 1
            self.voters.add(voter_id)
            print("Vote cast successfully!")
        else:
            print("Invalid candidate selection.")
    
    def display_results(self):
        print("\nVoting Results:")
        for candidate, votes in self.candidates.items():
            print(f"{candidate}: {votes} votes")
        winner = max(self.candidates, key=self.candidates.get)
        print(f"\nWinner: {winner}")

if __name__ == "__main__":
    voting_system = VotingSystem()
    
    while True:
        print("\n--- Voting System ---")
        print("1. Vote")
        print("2. Show Results")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            voter_id = input("Enter your Voter ID: ")
            age = int(input("Enter your age: "))
            print("Candidates: Candidate A, Candidate B, Candidate C")
            candidate = input("Enter the candidate you want to vote for: ")
            voting_system.cast_vote(voter_id, age, candidate)
        
        elif choice == "2":
            voting_system.display_results()
        
        elif choice == "3":
            print("Exiting the voting system. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

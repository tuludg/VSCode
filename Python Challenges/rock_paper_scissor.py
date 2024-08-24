print("...rock...")
print("...paper...")
print("...scissors...")

player1 = input("(enter Player 1's choice): ")
player2 = input("(enter Player 2's choice): ")

print("SHOOT!")

if player1 == "rock" and player2 == "paper":
    print(f"Player1 choice: {player1} and player2 choice: {player2}")
    print("Player2 wins")
elif player1 == "rock" and player2 == "scissors":
     print(f"Player1 choice: {player1} and player2 choice: {player2}")
     print("Player1 wins")
elif player1 == "paper" and player2=="rock":
         print(f"Player1 choice: {player1} and player2 choice: {player2}")
         print("player1 wins")
elif player1 == "scissors" and player2 == "rock":
             print(f"Player1 choice: {player1} and player2 choice: {player2}")
             print("Players2 wins")
elif player1 == "scissors" and player2 == "paper":
             print(f"Player1 choice: {player1} and player2 choice: {player2}")
             print("Player1 wins")
elif player1 == "paper" and player2 == "scissors":
                 print(f"Player1 choice: {player1} and player2 choice: {player2}")
                 print("player2 wins")

    
else:
    print(f"Player1 choice: {player1} and player2 choice: {player2}")
    print("its a draw")



    


    

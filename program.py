print("Welcome to my program! Hope you Enjoy!!")
while 1==1:
	try:
		crocs = int(input("Pls enter a number between 1 and 4:"))
		match crocs:
			case 1 | 2 | 3 | 4:
				crocs=str(crocs)
				print("Good, You chose option "+crocs+". question "+crocs+" is:")
				match crocs:
					case '1':
						answer=int(input("What is red in colour? \n\t\t\t\t\t\t1.red amongus(if u choose this option, that means u r sus) \n\t\t\t\t\t\t2.button\nYour Answer?: "))
						if answer==1:
							print("\nCorrect!(u r still sus)")
						else:
							print("\nIncorrect \\/['-']\\/")
						cntq=input("\n\n\n\nDo you want to continue (y/n)?")
						if cntq=='y':
							continue
					case '2':
						answer=int(input("what is infinity minus one?? \n\t\t\t\t\t\t1.something less than infinity  \n\t\t\t\t\t\t2.minus infinity  \n\t\t\t\t\t\t3.still infinity\nYour Answer?: "))
						if answer==3:
							print("\nCorrect!(u r still sus)")
						else:
							print("\nIncorrect \\/['-']\\/")
						cntq=input("\n\n\n\nDo you want to continue (y/n)?")
						if cntq=='y':
							continue

					case '3':
						answer=int(input("What is the latest Marvel Avengers Movie that is released?? \n\t\t\t\t\t\t1.Avengers End Game  \n\t\t\t\t\t\t2.Avengers Infinity Wars \n\t\t\t\t\t\t3.Thunderbolts\nYour Answer?: "))
						if answer==3:
							print("\nCorrect!(u r still sus)")
						else:
							print("\nIncorrect \\/['-']\\/")
						cntq=input("\n\n\n\nDo you want to continue (y/n)?")
						if cntq=='y':
							continue

					case '4':
						answer=int(input("In A Minecraft Movie, what food does Steve make in the village?? \n\t\t\t\t\t\t1.Steve's Lava Chicken \n\t\t\t\t\t\t2. pumpkin pie \n\t\t\t\t\t\t3.bake AcookieGod \nYour Answer?: "))
						if answer==1:
							print("\nCorrect!(u r still sus)")
						else:
							print("\nIncorrect \\/['-']\\/")
						cntq=input("\n\n\n\nDo you want to continue (y/n)?")
						if cntq=='y':
							continue
	
				break
			case _:
				print("\n"+str(crocs)+" is an invalid option; Try again!")
	except:
		print("try again")
		continue

print("Have a Nice day!")
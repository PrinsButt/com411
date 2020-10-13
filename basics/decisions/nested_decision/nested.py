def run():
  print("Please enter cover type (hard or soft)")
  cover_type = input()

  if (cover_type.lower() == "soft"):
    print("Is it perfect bound (yes/no)?")
    response = input()

    if (response.lower() == "yes"):
      print("Soft cover, perfect bound books are very popular!")
    elif (response.lower() == "no"):
      print("Soft covers with coils or stitches are great for short books")
    else:
      print("Not sure what you mean")

  else:
    print("Books with hard covers can be more expensive!") 
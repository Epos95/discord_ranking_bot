set shell := ["cmd.exe", "/c"] # Comment this if not using windows 

alias r := run

# This will fix the code (black python)
fix:
    python -m black src

# Run the bot
run:
    cd src & python main.py
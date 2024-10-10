#!/usr/bin/env python3

import sys
import textwrap
import random

def generate_fake_quote():
    """
    Generates a random fake quote from a politician by selecting one element
    from each of four predefined parts.

    Returns:
        str: A constructed fake quote.
    """
    
    # 1st Part: Introductory Phrases
    intro_phrases = [
        "We have to remember that",
        "I will always say:",
        "You can be sure that when I'm in charge",
        "It's imperative to understand that",
        "Let me make it clear:",
        "We must acknowledge that",
        "I firmly believe that",
        "Rest assured,",
        "It's time to recognize that",
        "Make no mistake,"
    ]
    
    # 2nd Part: Policy Statements
    policy_statements = [
        "lowering the taxes for the filthy rich",
        "making filthy rich people even richer",
        "increasing the income of the wealthy elite",
        "helping billionaires expand their empires",
        "reducing regulations on large corporations",
        "promoting tax breaks for big businesses",
        "enhancing subsidies for multinational companies",
        "encouraging investment by the financial sector",
        "cutting funding for social programs",
        "deregulating industries to boost profits"
    ]
    
    # 3rd Part: Rationale
    rationales = [
        "will return as a golden rain on the rest of society",
        "will cheer up the poorer segments of the population",
        "will stimulate economic growth nationwide",
        "will create a ripple effect benefiting all citizens",
        "will ensure prosperity spreads across the nation",
        "will lead to widespread financial well-being",
        "will result in increased job opportunities for everyone",
        "will foster a thriving and robust economy",
        "will pave the way for unprecedented national success",
        "will guarantee a brighter future for all"
    ]
    
    # 4th Part: Metaphorical Conclusions
    metaphors = [
        "as the tide rises all boats.",
        "because karma will return to us.",
        "just like a snowball rolling down a hill gathers more snow.",
        "similar to how planting seeds leads to a bountiful harvest.",
        "much like how the sun rises each morning without fail.",
        "as gravity keeps the planets in orbit.",
        "because a rising tide lifts all ships.",
        "just as the roots support the tallest trees.",
        "much like how a spark ignites a blazing fire.",
        "as the wind carries the seeds to new fertile grounds.",
        "just like the rain that waters the crops.",
        "much like how the moon controls the tides.",
    ]
    
    # Randomly select one element from each part
    intro = random.choice(intro_phrases)
    policy = random.choice(policy_statements)
    rationale = random.choice(rationales)
    metaphor = random.choice(metaphors)
    
    # Construct the full quote
    quote = f"{intro} {policy}, {rationale} {metaphor}"
    
    return quote

def generate_signature():
    """
    Generates a random signature consisting of a closing phrase and a fake name.

    Returns:
        tuple: A tuple containing two strings representing the signature lines.
    """
    
    import random
    from datetime import datetime, timedelta

    def random_date_between(start_date: datetime, end_date: datetime):
        """
        Generates a random datetime between two datetime objects.
        
        Args:
            start_date (datetime): The start of the date range.
            end_date (datetime): The end of the date range.
            
        Returns:
            datetime: A randomly selected datetime between start_date and end_date.
            
        Raises:
            ValueError: If start_date is after end_date.
        """
        if start_date > end_date:
            raise ValueError("start_date must be earlier than or equal to end_date.")
        
        # Calculate the time difference between the two dates
        delta = end_date - start_date
        random_seconds = random.randint(0, int(delta.total_seconds()))        
        random_date = start_date + timedelta(seconds=random_seconds)        
        return random_date

    date = random_date_between(datetime(2015, 1, 1), datetime.now()).strftime('%Y-%m-%d')
    
    names = [
        "Bordeaux, Combatant Day",
        "Paris, National Assembly",
        "Brussels, EU Plenary",
        "Lille, Town Hall",
        "Berlin, Bundestag",
        "Strasbourg, Council of Europe",
        "New York, United Nations Council of Human Rights",
        "Moscow, Diner with Putin",
    ]
    
    signature_line2 = random.choice(names)
    
    return f"Emmanuel Moocron, {date}", signature_line2

def print_cowsay(message, spacing=5):
    """
    Prints the given message in a speech bubble to the right of the cow ASCII art,
    abutting the cow by a specified number of spaces.

    Args:
        message (str): The message to display.
        spacing (int, optional): Number of spaces between the cow and the speech bubble. Defaults to 5.
    """
    # Define the cow ASCII art as a list of lines
    cow = [
        "        ^__^         |",
        "        (oo)\\_______/    /",
        "        (__)/       )_ _/",
        "            ||----w |   \\",
        "            ||     ||    \\"
    ]
    
    # Calculate maximum cow width
    max_cow_width = max(len(line) for line in cow)
    
    # Wrap the message to a maximum width
    max_width = 40
    # Split the message into lines based on existing newlines
    message_lines = message.split('\n')
    wrapped = []
    for line in message_lines:
        wrapped += textwrap.wrap(line, width=max_width) or ['']
    
    # Determine the width of the speech bubble
    max_len = max(len(line) for line in wrapped)
    bubble_width = max_len + 2  # for "< " and " >" or borders
    
    # Create the speech bubble lines
    if len(wrapped) == 1:
        bubble_lines = [
            f" {'-' * bubble_width}",
            f"< {wrapped[0]} >",
            f" {'-' * bubble_width}"
        ]
    else:
        bubble_lines = [f"/{'-' * bubble_width}\\"]
        for i, line in enumerate(wrapped):
            if i == 0:
                bubble_lines.append(f"/ {line.ljust(max_len)} |")
            elif i == len(wrapped) -1:
                bubble_lines.append(f" {line.ljust(max_len)} /")
            else:
                bubble_lines.append(f" {line.ljust(max_len)} |")
        bubble_lines.append(f"\\{'-' * bubble_width}/")
    
    # Calculate total height
    cow_height = len(cow)
    bubble_height = len(bubble_lines)
    total_height = max(cow_height, bubble_height)
    
    # Pad the cow and bubble lists to have the same number of lines
    if bubble_height < total_height:
        pad_top = (total_height - bubble_height) // 2
        bubble_lines = [' ' * (bubble_width + 2)] * pad_top + bubble_lines
        bubble_lines += [' ' * (bubble_width + 2)] * (total_height - len(bubble_lines))
    elif cow_height < total_height:
        pad_top = (total_height - cow_height) // 2
        cow = [' ' * max_cow_width] * pad_top + cow
        cow += [' ' * max_cow_width] * (total_height - len(cow))
    
    # Combine and print the lines
    for i in range(total_height):
        cow_part = cow[i] if i < len(cow) else ' ' * max_cow_width
        bubble_part = bubble_lines[i] if i < len(bubble_lines) else ' ' * (bubble_width + 2)
        # Ensure the speech bubble starts 'spacing' spaces after the cow
        print(cow_part.ljust(max_cow_width) + ' ' * spacing + bubble_part)

def main():
    """
    Main function to generate and display a fake political quote using cowsay,
    including a signature within the speech bubble.
    """
    # Generate a fake quote
    quote = generate_fake_quote()
    
    # Generate signature lines
    signature_line1, signature_line2 = generate_signature()
    
    # Combine quote and signature into a single message
    message = f"{quote}\n{signature_line1}\n{signature_line2}"
    
    # Define the spacing between cow and speech bubble
    spacing = 1  # Adjust this value to move the speech bubble closer or further
    
    # Print the message using cowsay
    print_cowsay(message, spacing)

if __name__ == "__main__":
    main()

"""
Synthetic dataset generator for Autonomous Bus public opinion sentiment analysis.
Generates 1000+ realistic opinions across positive, negative, and neutral sentiments.
"""

import pandas as pd
import random
import os

random.seed(42)

POSITIVE_TEMPLATES = [
    # Safety / technology trust
    "Self-driving buses could actually be safer than human drivers, fewer accidents caused by fatigue or distraction",
    "autonomous buses would eliminate drunk driving incidents on public transit routes",
    "the AI in these buses reacts faster than any human ever could, thats a win for safety",
    "I trust the technology tbh, computers dont get tired or distracted like human drivers do",
    "after seeing the test runs, im actually impressed with how well the autonomous bus handles traffic",
    "these buses have 360 degree sensors, way better awareness than a human driver",
    "self driving buses have driven millions of miles with fewer accidents per mile than human drivers",
    "the safety record of autonomous vehicles keeps improving every year, exciting stuff",
    "if planes can fly on autopilot why cant buses drive themselves? im all for it",
    "AV buses dont text and drive or fall asleep at the wheel, sign me up",
    "watched a demo of the autonomous bus handling an emergency brake, impressive reaction time",
    "the redundant safety systems in these buses make them incredibly reliable",
    # Convenience
    "imagine never waiting for a late bus again because the driver overslept, autonomous buses would run on perfect schedules",
    "self-driving buses running 24/7 would be a game changer for night shift workers",
    "autonomous buses could serve rural routes that arent profitable enough for traditional bus companies",
    "no more dealing with grumpy bus drivers lol, autonomous buses sound great",
    "these buses could optimize routes in real time based on passenger demand, so much more efficient",
    "public transit with autonomous buses would be so much more reliable and predictable",
    "love that autonomous buses could provide more frequent service without extra labor costs",
    "the convenience of on-demand autonomous bus service would transform how we commute",
    "finally public transit that actually runs on time, bring on the robot buses!",
    "autonomous buses + app integration = knowing exactly when ur ride arrives, every time",
    # Environment
    "electric autonomous buses would massively reduce carbon emissions in cities",
    "self driving electric buses are the future of green urban transport",
    "if autonomous buses get more people to ditch their cars, thats a huge environmental win",
    "the efficiency of autonomous driving means less fuel waste and lower emissions per passenger",
    "autonomous buses could reduce the number of cars on the road significantly, better air quality for everyone",
    "love that most autonomous bus projects are fully electric, good for the planet",
    "fewer cars + electric autonomous buses = cleaner cities, cant wait",
    "the environmental benefits alone make autonomous buses worth pursuing",
    "self-driving buses optimizing routes means less unnecessary driving and lower carbon footprint",
    "autonomous electric buses are probably the single best thing we can do for urban air quality",
    # Cost
    "autonomous buses would save taxpayers money in the long run by reducing operating costs",
    "cheaper public transit fares thanks to no driver salaries? yes please",
    "the long term cost savings of autonomous buses could fund better transit infrastructure",
    "cities spending less on bus drivers means more money for improving routes and stops",
    "autonomous buses make public transit financially sustainable even in smaller cities",
    "the ROI on autonomous bus fleets is looking really promising based on pilot programs",
    # Disability access / elderly
    "autonomous buses with proper accessibility features could be life changing for wheelchair users",
    "as someone with a disability, reliable autonomous bus service would give me so much more independence",
    "my grandmother cant drive anymore, autonomous buses would help seniors stay mobile and independent",
    "love that autonomous buses are being designed with universal accessibility from the start",
    "elderly people in rural areas desperately need autonomous bus services to get to appointments",
    "the accessibility potential of autonomous buses is underrated, could transform disabled peoples lives",
    # General positive
    "honestly excited about autonomous buses, the future of public transit looks bright",
    "autonomous buses are inevitable and I think thats a good thing for society",
    "the technology is ready, lets deploy autonomous buses and improve everyones commute",
    "every pilot program ive read about shows autonomous buses performing well, time to scale up",
    "cant believe how far autonomous bus tech has come, were living in the future",
    "fully support autonomous buses, innovation in public transit is long overdue",
    "the benefits of self driving buses far outweigh the risks imo",
    "autonomous buses will make cities more livable and accessible for everyone",
    "so ready for autonomous buses tbh, public transit needs this upgrade",
    "the data from autonomous bus trials is very encouraging, optimistic about widespread adoption",
]

NEGATIVE_TEMPLATES = [
    # Safety fears
    "no way im getting on a bus with no driver, what happens when the computer crashes??",
    "self driving buses are terrifying, technology fails all the time",
    "I dont trust a computer to drive a 40 foot bus through city traffic, period",
    "what happens when the autonomous bus encounters a situation it wasnt programmed for? people die thats what",
    "remember when that self driving uber killed a pedestrian? now imagine that with a full bus of passengers",
    "autonomous buses in snow and ice? recipe for disaster, the sensors cant handle bad weather",
    "hackers could take control of autonomous buses, this is a massive security risk",
    "the technology isnt ready, testing autonomous buses on public roads with real passengers is reckless",
    "who is liable when an autonomous bus causes an accident? nobody has answered this properly",
    "software bugs in your phone are annoying, software bugs in your bus could be fatal",
    "autonomous buses cant read hand gestures from traffic cops or construction workers, dangerous",
    "what if the bus malfunctions in the middle of a highway with 50 passengers? terrifying thought",
    "self driving bus sensors failed in rain during a test, and we want these on public roads??",
    "no driver means no one to handle medical emergencies on the bus, terrible idea",
    "autonomous buses will inevitably have accidents, and when they do the consequences will be severe",
    # Job loss
    "autonomous buses will put thousands of bus drivers out of work, devastating for working families",
    "great so we're replacing hardworking bus drivers with robots, late stage capitalism at its finest",
    "my dad has been a bus driver for 25 years, autonomous buses would destroy his livelihood",
    "the push for autonomous buses is just corporations trying to eliminate labor costs at workers expense",
    "bus drivers support their families with these jobs, autonomous buses will cause mass unemployment",
    "who cares about efficiency when real people lose their jobs to machines",
    "autonomous buses are a threat to transit worker unions and everything they've fought for",
    "replacing drivers with AI is morally wrong, people need jobs not more automation",
    "the human cost of autonomous buses is being completely ignored by tech enthusiasts",
    "sure autonomous buses save money, by firing thousands of workers, how progressive",
    "another industry destroyed by automation, bus drivers deserve better than this",
    "we should be creating jobs not eliminating them, autonomous buses are a step backward",
    # Technology distrust
    "my phone cant even get directions right half the time and you want me to trust a self driving bus?",
    "have you seen how often computers crash? now put 50 peoples lives in that computers hands",
    "the tech industry overpromises and underdelivers constantly, autonomous buses will be no different",
    "autonomous bus companies are rushing to market before the tech is truly ready, dangerous",
    "AI isnt intelligent, its pattern matching. roads are too unpredictable for pattern matching",
    "silicon valley thinks they can solve everything with AI, public transit isnt a tech problem",
    "the autonomous bus hype is just venture capitalists trying to cash in, not genuine progress",
    "how can we trust autonomous buses when even tesla's autopilot keeps causing accidents",
    "self driving technology has been '5 years away' for 20 years now, im skeptical",
    # Cost concerns
    "autonomous buses cost millions each, taxpayers will foot the bill for experimental tech",
    "the maintenance costs for autonomous bus sensors and computers are astronomical",
    "cities cant even maintain regular buses properly, how will they handle autonomous fleet maintenance",
    "the infrastructure changes needed for autonomous buses will cost billions, money we dont have",
    "pilot programs look cheap but scaling autonomous buses citywide will be prohibitively expensive",
    # Elderly / accessibility concerns (negative framing)
    "elderly passengers wont be able to figure out how to use autonomous buses without a driver to help",
    "who helps disabled passengers board when theres no driver? autonomous buses ignore accessibility",
    "my blind neighbor relies on the bus driver for help, autonomous buses would strand people like him",
    "seniors are already confused by technology, taking away the human driver is cruel",
    "autonomous buses assume everyone is tech savvy, what about elderly passengers who arent",
    # General negative
    "autonomous buses are a terrible idea and no amount of marketing will change my mind",
    "hard pass on self driving buses, I'll walk before I get on one",
    "we have real problems in public transit to solve before wasting money on autonomous buses",
    "the whole autonomous bus thing feels like a solution looking for a problem",
    "nope nope nope, not getting on a bus driven by a computer, ever",
    "autonomous buses are just another way tech bros are trying to disrupt something that works fine",
    "call me old fashioned but I want a human being driving my bus",
    "the risks of autonomous buses far outweigh any supposed benefits",
]

NEUTRAL_TEMPLATES = [
    # Balanced / questioning
    "autonomous buses seem interesting but I need to see more data before forming an opinion",
    "there are valid arguments both for and against autonomous buses, its not black and white",
    "I think autonomous buses could work in some contexts but not everywhere",
    "the technology has potential but the regulatory framework isnt ready yet",
    "autonomous buses might work on dedicated routes but mixed traffic is a different challenge",
    "im neither for nor against autonomous buses, I just want to see proper testing first",
    "the concept is fine but implementation will determine whether autonomous buses succeed or fail",
    "autonomous buses are an interesting experiment, lets see how the pilot programs go",
    "I can see both the benefits and risks of autonomous buses, reserving judgment for now",
    "whether autonomous buses succeed depends entirely on how the transition is managed",
    "autonomous buses in controlled environments like airports make sense, city streets less so",
    "the debate around autonomous buses has valid points on both sides",
    "I'd consider riding an autonomous bus after seeing it operate successfully for a few years",
    "autonomous buses will probably be fine for simple routes, complex urban navigation is another story",
    # Informational
    "several cities are currently testing autonomous bus pilots, results are mixed so far",
    "the autonomous bus market is expected to grow significantly in the next decade",
    "regulations for autonomous buses vary widely between countries and even states",
    "autonomous bus technology uses lidar, cameras, and radar to navigate",
    "most autonomous bus pilots currently operate at low speeds on fixed routes",
    "the first autonomous bus services are likely to supplement rather than replace existing transit",
    "autonomous buses are being tested in cities like Helsinki, Singapore, and Las Vegas",
    "the transition to autonomous buses will likely be gradual, not overnight",
    "current autonomous bus prototypes can handle most normal driving situations",
    "insurance and liability questions around autonomous buses are still being worked out",
    # Conditional
    "I'd support autonomous buses if they can prove theyre safer than human driven ones",
    "autonomous buses are fine as long as there are proper safety protocols in place",
    "Id ride one if it had a backup human operator on board at least initially",
    "autonomous buses could work if they start with simple suburban routes first",
    "the key question is whether autonomous buses can handle edge cases reliably",
    "I think we need both human drivers and autonomous buses for different route types",
    "autonomous buses might reduce costs but the savings should go to improving service not profits",
    "if the data shows autonomous buses are safer I'll support them, but the data needs to be solid",
    "autonomous buses in dedicated lanes could work well, mixed traffic is the real test",
    "I want to see at least 5 years of incident-free operation before I'm convinced",
    "would support autonomous buses with proper job retraining programs for displaced drivers",
]

# Augmentation: slang, typos, abbreviations, style variations
def augment_text(text):
    """Apply random realistic variations to make text more natural."""
    modifications = []

    # Random typo injection (10% chance per word for some words)
    if random.random() < 0.15:
        typo_map = {
            "the": random.choice(["teh", "the", "th"]),
            "that": "taht",
            "with": "wiht",
            "have": "ahve",
            "because": "becuase",
            "their": random.choice(["thier", "there"]),
            "would": "woudl",
            "could": "coudl",
            "about": "aobut",
            "people": "poeple",
            "autonomous": random.choice(["autonomus", "autonmous", "autonomous"]),
        }
        words = text.split()
        for i, w in enumerate(words):
            if w.lower() in typo_map and random.random() < 0.3:
                words[i] = typo_map[w.lower()]
                break
        text = " ".join(words)

    # Random abbreviation (15% chance)
    if random.random() < 0.15:
        abbrev_map = {
            "to be honest": "tbh",
            "in my opinion": "imo",
            "in my humble opinion": "imho",
            "to be fair": "tbf",
            "as far as I know": "afaik",
            "I dont know": "idk",
            "right now": "rn",
            "because": "cuz",
            "though": "tho",
            "people": "ppl",
            "probably": "prolly",
            "definitely": "def",
            "without": "w/o",
            "something": "smth",
        }
        for phrase, abbr in abbrev_map.items():
            if phrase in text.lower():
                text = text.replace(phrase, abbr, 1)
                break

    # Random emoji addition (20% chance)
    if random.random() < 0.20:
        emojis_pos = ["👍", "🙌", "💚", "✅", "🚌", "🔥", "👏"]
        emojis_neg = ["😡", "👎", "🙄", "😤", "💀", "🤦", "❌"]
        emojis_neutral = ["🤔", "🧐", "📊", "💭", "🔍"]
        text = text + " " + random.choice(emojis_pos + emojis_neg + emojis_neutral)

    # Random capitalization emphasis (10% chance)
    if random.random() < 0.10:
        words = text.split()
        if len(words) > 3:
            idx = random.randint(0, len(words) - 1)
            words[idx] = words[idx].upper()
            text = " ".join(words)

    # Random hashtag addition (10% chance)
    if random.random() < 0.10:
        hashtags = [
            "#autonomousvehicles", "#selfdriving", "#futureoftransit",
            "#publictransit", "#driverless", "#AVbus", "#smartcity",
            "#transportation", "#AI", "#technology"
        ]
        text = text + " " + random.choice(hashtags)

    # Randomly strip punctuation at end (make it casual)
    if random.random() < 0.3 and text.endswith((".", ",")):
        text = text[:-1]

    return text


def add_prefix(text, source):
    """Add source-appropriate prefix occasionally."""
    if source == "twitter" and random.random() < 0.15:
        prefixes = [
            "Hot take: ", "Unpopular opinion: ", "Thread: ", "PSA: ",
            "Breaking: ", "Honestly, ", "RT if you agree: ",
        ]
        text = random.choice(prefixes) + text
    elif source == "reddit" and random.random() < 0.15:
        prefixes = [
            "Am I the only one who thinks ", "Serious question: ",
            "CMV: ", "ELI5: why do people think ",
            "Genuine question about ", "DAE think ",
        ]
        text = random.choice(prefixes) + text.lower()
    elif source == "survey" and random.random() < 0.15:
        prefixes = [
            "I believe that ", "In my experience, ",
            "From my perspective, ", "I feel strongly that ",
            "I think ", "My opinion is that ",
        ]
        text = random.choice(prefixes) + text.lower()
    return text


def generate_dataset(n=1200):
    """Generate n synthetic opinions with sentiment labels."""
    data = []
    sources = ["twitter", "reddit", "survey"]

    # Distribution: 40% positive, 35% negative, 25% neutral
    n_positive = int(n * 0.40)
    n_negative = int(n * 0.35)
    n_neutral = n - n_positive - n_negative

    for _ in range(n_positive):
        text = random.choice(POSITIVE_TEMPLATES)
        source = random.choice(sources)
        text = add_prefix(augment_text(text), source)
        data.append({"text": text, "sentiment": "positive", "source": source})

    for _ in range(n_negative):
        text = random.choice(NEGATIVE_TEMPLATES)
        source = random.choice(sources)
        text = add_prefix(augment_text(text), source)
        data.append({"text": text, "sentiment": "negative", "source": source})

    for _ in range(n_neutral):
        text = random.choice(NEUTRAL_TEMPLATES)
        source = random.choice(sources)
        text = add_prefix(augment_text(text), source)
        data.append({"text": text, "sentiment": "neutral", "source": source})

    random.shuffle(data)
    return pd.DataFrame(data)


def main():
    os.makedirs("data", exist_ok=True)
    df = generate_dataset(1200)
    df.to_csv("data/opinions.csv", index=False)
    print(f"Generated {len(df)} opinions")
    print(f"Distribution:\n{df['sentiment'].value_counts()}")
    print(f"Sources:\n{df['source'].value_counts()}")
    print(f"Saved to data/opinions.csv")


if __name__ == "__main__":
    main()

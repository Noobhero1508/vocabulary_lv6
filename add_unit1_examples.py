import re, traceback

unit1_examples = {
    "Application for Employment": "He filled out an application for employment to get a job at the bank.",
    "Province": "She lives in a rural province in the north.",
    "State": "Each state has its own laws.",
    "Position": "I am applying for a management position.",
    "Sought": "They sought help from the local police.",
    "Postal": "Please write down your postal code.",
    "If so": "Are you coming? If so, I will buy a ticket for you.",
    "Seek": "Many people seek better opportunities in the city.",
    "Previous": "My previous job was very stressful.",
    "Precedent": "This decision sets a new precedent for similar cases.",
    "Attach": "Please attach a recent photo to your form.",
    "Separate": "Keep the raw meat separate from vegetables.",
    "End up + Ving": "We got lost and ended up walking for hours.",
    "Mile": "The beach is a mile away from here.",
    "Radius": "There are three schools within a one-mile radius.",
    "Competitive": "The job market is very competitive right now.",
    "Institute": "He studies technology at the science institute.",
    "Demand": "There is a high demand for skilled workers.",
    "Certificate": "You will get a certificate after finishing the course.",
    "Prestige": "The university has a lot of prestige.",
    "Apparently = Obvious": "Apparently, it is going to rain this afternoon.",
    "Outstanding": "She received an award for her outstanding performance.",
    "Bet": "I bet he will be late again.",
    "It’s just waiting and seeing": "We don’t know what will happen; it's just waiting and seeing.",
    "That might be a little overkill?": "Buying ten pizzas for three people might be a little overkill.",
    "I did’t want to take any chances": "I brought an umbrella because I didn't want to take any chances.",
    "I've got my heart set on": "I've got my heart set on entering that college.",
    "Aaren’t + N + six of one, half a dozen of the other": "Should we take the bus or walk? It's six of one, half a dozen of the other.",
    "Run of the mill = Ordinary": "It wasn't a special restaurant; just a run-of-the-mill place.",
    "All in all = Generally = My conclusion is….": "All in all, it was a very successful trip.",
    "I'll keep my fingers crossed for you": "Good luck with your exam today, I'll keep my fingers crossed for you.",
    "Ethics": "The class discusses medical ethics and rules.",
    "Period": "You must finish the test in a one-hour period.",
    "Gymnast": "The gymnast performed a perfect jump.",
    "Gymnastics": "She has been practicing gymnastics since she was five.",
    "World-class": "They stayed at a world-class resort in Hawaii.",
    "Prizes": "There are many great prizes for the winners.",
    "Honor": "It is an honor to meet the president.",
    "Dismounting": "The gymnast injured her knee while dismounting.",
    "Medal": "He won a gold medal in the race.",
    "Renowned": "The city is renowned for its beautiful museums.",
    "Intensity": "The storm hit the coast with great intensity.",
    "Practice": "You need more practice to improve your English.",
    "Athlete": "An athlete trains for many hours every day.",
    "Actress": "She won an award for best actress.",
    "Heritage": "We are proud of our rich cultural heritage.",
    "Diverse": "The city has a very diverse population.",
    "Pride": "He takes great pride in his work.",
    "Incorporate": "We need to incorporate new ideas into the project.",
    "Indigenous": "The kangaroo is indigenous to Australia.",
    "Adopt": "They decided to adopt a rescue dog.",
    "Migrate": "Many birds migrate south for the winter.",
    "Court": "The players ran onto the basketball court.",
    "Grass": "The grass in the park is so green.",
    "Glasses": "He needs a new pair of reading glasses.",
    "Career": "She wants to start a career in medicine.",
    "Course": "I signed up for a Spanish language course.",
    "Apply for": "Are you going to apply for the scholarship?",
    "Apply to": "He decided to apply to three different universities.",
    "Sign up for": "I want to sign up for yoga classes.",
    "Switch to": "He decided to switch to a cheaper phone plan.",
    "Be accepted to/ into/ by": "She was accepted into the medical school.",
    "Be rejected by": "His application was rejected by the company.",
    "Enroll in": "You must enroll in the class before Friday.",
    "Fulfill": "He works hard to fulfill his dreams.",
    "Lifelong": "They have been lifelong friends.",
    "Archaeologist": "The archaeologist found ancient bones in the cave.",
    "Graduate": "My sister will graduate from college next month.",
    "Ambitious": "The young lawyer is very ambitious.",
    "Put off": "Don't put off doing your homework.",
    "Purse": "She forgot her purse at the restaurant.",
    "The sky’s the limit for us": "With this new technology, the sky's the limit for us.",
    "Set a goal": "It is important to set a goal before starting.",
    "Work towards": "We all need to work towards a better future.",
    "Achievable": "Make sure your study plan is achievable.",
    "Breadwinner": "In many families, both parents act as breadwinners.",
    "Caregiver": "The nurse works as a caregiver for elderly patients.",
    "Spouse": "Your spouse can attend the dinner party with you.",
    "Observe": "Scientists observe animal behavior in the wild.",
    "Roles": "Men and women play different roles in society.",
    "Reversal": "There has been a complete reversal in his attitude.",
    "Resume": "Please send your resume to the email below.",
    "Advertised": "The position was advertised in the local newspaper.",
    "Candidate": "He is the best candidate for the job.",
    "Land": "He hopes to land a good job soon.",
    "Firm": "My uncle works for a large law firm.",
    "Dress right": "You should dress right for the interview.",
    "Aspect": "This is an important aspect of the whole problem.",
    "Disqualifier": "Being late to an interview is a major disqualifier.",
    "Major red flag": "His lack of experience was a major red flag.",
    "Provide": "The school will provide all necessary books.",
    "Airtight": "Make sure the container is completely airtight.",
    "Reassure": "I tried to reassure her that everything was fine.",
    "Be sure to stick with": "Be sure to stick with the original plan.",
    "Motivated": "He is a highly motivated student who always gets an A.",
    "Relevant": "Please only add relevant information to your report.",
    "Demonstrate": "The teacher will demonstrate how to use the equipment.",
    "Desperate": "They were desperate for food and water.",
    "Brag": "He likes to brag about his expensive car.",
    "Expect": "We expect the train to arrive on time.",
    "Colleagues": "I usually have lunch with my colleagues at work.",
    "Possess": "He possesses a rare artistic talent.",
    "Associate": "I associate rain with feeling sleepy.",
    "Assistant": "The manager's assistant organized the meeting.",
    "Salesclerk": "The salesclerk helped me find my size.",
    "Project": "Our science project won first prize."
}

def inject():
    try:
        with open('unit1.html', 'r', encoding='utf-8') as f:
            content = f.read()

        def replacer(match):
            full_obj = match.group(0)
            word = match.group(1)
            # Remove replacing backslashes so it matches directly since JSON might have escaped quotes
            word_clean = word.replace("\\'", "'")
            example = unit1_examples.get(word, unit1_examples.get(word_clean, ""))
            if example:
                return re.sub(r'phrase:\s*\"[^\"]*\"', f'phrase: "{example}"', full_obj)
            return full_obj

        new_content = re.sub(r'\{[^}]*word:\s*\"([^\"]+)\"[^}]*phrase:\s*\"([^\"]*)\"[^}]*\}', replacer, content)

        with open('unit1.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully updated unit1.html")
    except Exception as e:
        print("Error:", e)
        traceback.print_exc()

if __name__ == '__main__':
    inject()

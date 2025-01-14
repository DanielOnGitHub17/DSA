
"""
UNDERSTAND.
Spaces are mapped to spaces. UPPERCASE.

Two phrases from Both confisticated  No. 1 clear, No. 2 coded.
Perfect map from clear to coded.
    Alice -> Bob
    Bob -> Carol. ("really lucky") -> Different "mapping" from Alice to Bob

Finally, message from Carol (weak) -> Alice (By Persuasion/Cane)
    Carol -> Alice ==> Bob -> Carol first, Alice -> Bob second.

Input (what you have). 5 Parameters:
    1. First, clear, phrase from Alice to Bob
    2. Second, coded, phrase from Alice to Bob
    3. First, clear, phrase from Bob to Carol
    4. Second, coded, phrase from Bob to Carol
    5. Carol's coded message to Alice

Question: Decode Carol's message (fifth input).

Output:
    Clear text.

End UNDERSTAND

ALGORITHM:
Taking note of every UNDERSTAND detail.
5 inputs: clear_alice_bob, coded_alice_bob,
          clear_bob_carol, coded_bob_carol,
          coded_carol_alice

1 output: clear_carol_alice

Structure to use: Python Dictionary.
Key step: Creating a map from coded_name1_name2 to clear_name1_name2

Note: The mappings are perfect, so no need to really check for duplicates.
    It might help to, though, might end the execution faster.
Steps:

    1. Create a mapping from coded_alice_bob to clear_alice_bob:
        alice_bob = new python dictionary.
        for each corresponding character (coded => clear) in coded_alice_bob and clear_alice_bob:
            alice_bob[coded] = clear

    2. Create mapping from coded_bob_carol to clear_bob_carol:
        bob_carol = new python dictionary.
        for each corresponding in (coded => clear) in both messages:
            bob_carol[coded] = clear.
    
    Now you have all code to text mappings. Time to crack Carol's code.

    3. Create array having length same as Carol's coded message.
        let n be the length of coded_carol_alice
        message_builder = "" (empty string) repeated length(coded_carol_alice) times.
        Have an index tracker i for adding the clear text to the Message Builder
        for each character (coded) in coded_carol_alice:
            first set variable "clear" to decoding from bob to carol
            => clear = bob_carol[coded]
            then from alice to bob
            => clear = alice_bob[coded]
            
            `clear` is now a decoded character.
            If the coded was 'space', it remains unchanged
            
            Now, place `clear` in the correct position in `message_builder`
            => message_builder of index `i` => clear

            Go to the next index.
            => i -> i + 1
        
        Array, `message_builder`, created

    4.  Join the Message Builder.
        `message_builder` is now an array having the complete message.
        Join `message_builder` to get the coded message.

        clear_carol_alice = joined `message_builder`
        
    5.  Output the Message Builder.
        "return" `message_builder`

Code: Python Function with 5 string input and 1 string output
"""

def carolled(clear_alice_bob: str, coded_alice_bob: str,
          clear_bob_carol: str, coded_bob_carol: str,
          coded_carol_alice: str) -> str:
    alice_bob = {}  # New dict.
    for coded, clear in zip(coded_alice_bob, clear_alice_bob):
        alice_bob[coded] = clear

    bob_carol = {}
    for coded, clear in zip(coded_bob_carol, clear_bob_carol):
        bob_carol[coded] = clear

    i = 0
    message_builder = [""] * len(coded_carol_alice)
    for coded in coded_carol_alice:
        clear = bob_carol[coded]
        clear = alice_bob[coded]

        message_builder[i] = clear
        i += 1

    coded_carol_alice = "".join(message_builder)
    return coded_carol_alice


"""
You might be wondering why I made a message builder
   instead of adding the decoded characters to a string

Simple. It's more efficient.

"""

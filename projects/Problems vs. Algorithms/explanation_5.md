# Problem 5: Autocomplete with Tries

To solve this problem I implemented a Trie, the solution is divided into many parts: ​insert word​,
find ​and ​finding​ ​suffixes.

## Time and Space Complexity

**Insert word**

**Time → O(n)**, because we loop through a list of characters and when we finish we set a flag to true.

**Space → O(n)**, because we assign the characters in a word to multiple nodes.

**Find**

**Time → O(n)**, because we loop a word character per character. Space → O(1), because find returns a single node each time is called.

**Find suffix**

**Time → O(n)**, because it depends on the depth of the Trie.

**Space → O(n x m)**, because the suffixes function runtime will expand with the number of inputs but also with the length of the inputs. Being n the number of inputs and m the average of the length of the word or input.
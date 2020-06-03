# Problem 7: Request Routing in a Web Server with a Trie

To solve this problem I did a Trie implementation and the solution got divided into ​insert​ and lookup​ parts.

#Time Space Complexity

**insert path**

**Time → O(n)**, because we loop through a list of segments from a url path that has been split. 

**Space → O(n)**, because we store a segment in each node, depending on the number of segments once the url path has been split.

**lookup path**

**Time → O(n)**, because we loop through a list of segments from a url path that has been split.
 
**Space → O(1)**, because we just return the path’s handler

# thesis-grammar
An object-oriented design of a context-free grammar to model natural language.

Three files comprise this project. Grammar.py designs a Grammar class that has the ability to parse through a grammar file, apply a given rule set to its data, and generate a subsequent output based on those rules.

For example, this could be the beginning of a grammar file for an English sentence:
<sentence> ::= <noun_phrase> <verb>
<noun_phrase> ::= <proper_noun>
<noun_phrase> ::= <article> <noun>
<noun_phrase> ::= <article> <adjective> <noun>
<article> ::= THE
<article> ::= A
<noun> ::= COW
<noun> ::= FOX
<adjective> ::= BROWN
<adjective> ::= LAZY
<verb> ::= JUMPS
<proper_noun> ::= ZAK

According to my design, the Grammar class cycles through a grammar file that contains all possible elements of hundreds of different thesis statements for a freshman Humanities 110 paper, generating in its output a successful argument about ancient lit.

To test, open thesis.grm, Grammar.py, and thesis.py, and then execute thesis.py in your text editor.

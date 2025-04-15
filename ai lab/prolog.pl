% Factorial Implementations

% Recursive Factorial
factorial_recursive(0, 1) :- !.
factorial_recursive(N, Result) :-
    N > 0,
    N1 is N - 1,
    factorial_recursive(N1, SubResult),
    Result is N * SubResult.

% Tail Recursive Factorial (more efficient)
factorial_tail(N, Result) :-
    factorial_tail_helper(N, 1, Result).

factorial_tail_helper(0, Acc, Acc) :- !.
factorial_tail_helper(N, Acc, Result) :-
    N > 0,
    NewAcc is Acc * N,
    N1 is N - 1,
    factorial_tail_helper(N1, NewAcc, Result).

% Fibonacci Implementations

% Recursive Fibonacci (less efficient)
fibonacci_recursive(0, 0) :- !.
fibonacci_recursive(1, 1) :- !.
fibonacci_recursive(N, Result) :-
    N > 1,
    N1 is N - 1,
    N2 is N - 2,
    fibonacci_recursive(N1, Result1),
    fibonacci_recursive(N2, Result2),
    Result is Result1 + Result2.

% Tail Recursive Fibonacci (more efficient)
fibonacci_tail(N, Result) :-
    fibonacci_tail_helper(N, 0, 1, Result).

fibonacci_tail_helper(0, A, _, A) :- !.
fibonacci_tail_helper(1, _, B, B) :- !.
fibonacci_tail_helper(N, A, B, Result) :-
    N > 1,
    N1 is N - 1,
    NextA is B,
    NextB is A + B,
    fibonacci_tail_helper(N1, NextA, NextB, Result).

% Demonstration Predicates
demo_factorial :-
    write('Factorial Demonstrations:'), nl,
    write('Recursive Factorial:'), nl,
    factorial_recursive(5, RecFact),
    write('Factorial of 5: '), write(RecFact), nl,
    
    write('Tail Recursive Factorial:'), nl,
    factorial_tail(5, TailFact),
    write('Factorial of 5: '), write(TailFact), nl.

demo_fibonacci :-
    write('Fibonacci Demonstrations:'), nl,
    write('Recursive Fibonacci:'), nl,
    fibonacci_recursive(7, RecFib),
    write('7th Fibonacci: '), write(RecFib), nl,
    
    write('Tail Recursive Fibonacci:'), nl,
    fibonacci_tail(7, TailFib),
    write('7th Fibonacci: '), write(TailFib), nl.

% Main demonstration predicate
demo :-
    demo_factorial,
    nl,
    demo_fibonacci.
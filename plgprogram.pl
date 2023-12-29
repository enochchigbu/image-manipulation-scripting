% Reverse list rule
reverse_list([], []).
reverse_list([Head|Tail], Reversed) :-
    reverse_list(Tail, ReversedTail),
    append(ReversedTail, [Head], Reversed).

main :-
    % Step 1: Read input
    read(InputList),

    % Call the reverse_list rule
    reverse_list(InputList, ReversedList),

    % Write output
    write(ReversedList).

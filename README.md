# dontmissme
Python-written software that tries to simplify student's life by implementing a very famous study technique called "Active Recall".

To implement the spaced-repetition algorithm, SM2 has been implemented in this script, which has this kind of difficulty-rating:
    5: perfect response.
    4: correct response after a hesitation.
    3: correct response recalled with serious difficulty.
    2: incorrect response; where the correct one seemed easy to recall.
    1: incorrect response; the correct one remembered.
    0: complete blackout.
    Easiness: The easiness factor, a multipler that affects the size of the interval, determine by the quality of the recall.
    Interval: The gap/space between your next review.
    Repetitions: The count of correct response (quality >= 3) you have in a row.

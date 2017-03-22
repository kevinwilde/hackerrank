#lang racket

(define (answer x y p)
  (cond [(or (or (empty? x) (empty? y))
             (not (equal? (first x) (first y))))
         (list x y (flatten p))]
        [else
         (answer (rest x) (rest y) (cons p (list (first x))))]))

(define ans (answer (string->list (read-line)) (string->list (read-line)) empty))
(printf "~a ~a\n"
        (length (list-ref ans 2))
        (list->string (list-ref ans 2)))
(printf "~a ~a\n"
        (length (list-ref ans 0))
        (list->string (list-ref ans 0)))
(printf "~a ~a\n"
        (length (list-ref ans 1))
        (list->string (list-ref ans 1)))

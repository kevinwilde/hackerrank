#lang lazy
(require racket/string)

(define (read-list)
  (let ([lst (read-line)])
    (map string->number (string-split lst))))
    
(define lst (read-list))
(define A (first lst))
(define B (list-ref lst 1))
(define N (list-ref lst 2))

(define fib
  (cons A (cons B 
                (map + 
                     fib
                     (map (lambda (x) (expt x 2)) (rest fib))))))

(define ans (list-ref (!! (take N fib)) (- N 1)))

(printf "~a\n" ans)
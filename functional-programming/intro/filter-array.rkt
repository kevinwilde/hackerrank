#lang racket

(define x (read))

(define (read-list)
  (let ([x (read)]) 
    (if (eof-object? x)
        (list)
        (cons x (read-list)))))
(define lst (read-list))

(define (ans lst)
  (cond [(empty? lst) lst]
        [(< (first lst) x) (cons (first lst) (ans (rest lst)))]
        [else (ans (rest lst))]))

(define (print-list lst)
  (cond [(not (empty? lst)) (begin (printf "~s\n" (first lst))
                                   (print-list (rest lst)))]))

(print-list (ans lst))